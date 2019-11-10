#!/usr/bin/env python3
# -*- coding: utf-8 -*-

## Created on Sun Oct 20 12:17:05 2019
## @authors: mbs76 & mnavalon 


import requests
from bs4 import BeautifulSoup
import csv
import os
from tkinter import filedialog


### -------------------------------------------------------------------------
### Función que descarga de los precios de los metales 
### -------------------------------------------------------------------------

### Esta función debería integrarse en un web crawler
### que automatizase la recogida diara

def storeURL(str):
    
    page = requests.get(str)
    
    if page.status_code == 200:
        
        # Creamos el arbol con todo el documento html
        soup = BeautifulSoup(page.content, "lxml")
    
        tag = soup.table
        head_tag = tag.thead
        body_tag = tag.tbody
            
        data = []
        # separamos la moneda de la fecha identificando la posición de los (:)
        separador = head_tag.get_text().find(":")
        moneda = head_tag.get_text()[0:separador].strip()
        fecha = head_tag.get_text()[separador + 1:].strip()
  
        trs = body_tag.findAll('tr')
    
        for tr in trs:
            # Eliminamos los caracteres que no forman parte del nombre (*)
            metal = tr.th.get_text().replace("*","").strip()
            valor = tr.td.get_text().strip()
            print("Fecha: {0}\nProducto: {1}\nMoneda: {2}\nCantidad: {3}\n".format(fecha, metal, moneda, valor))
            data.append((fecha,metal,moneda,valor))
            
        with open("lme.csv", "a") as f:
            writer = csv.writer(f)
            if os.stat('lme.csv').st_size == 0:
                writer.writerow(["Date", "Product", "Currency", "Value"])
            for fecha,metal,moneda,valor in data:
                writer.writerow([fecha,metal,moneda,valor])           
     
    else:
        print ("Error code {}".format(page.status_code))

### -------------------------------------------------------------------------
### Procedimiento que descarga la imagen de la url pasada como parámetro
### -------------------------------------------------------------------------

def load_requests(source_url):
    
    image = requests.get(source_url, stream = True)
    
    if image.status_code == 200:
        
        # Elegimos como nombre de la imagen la última parte de la url
        name = source_url.split('/')[-1]
        path = directory + "/" + name
        print(path)
        # Abrimos el fichero para escritura en modo binario
        with open(path, "wb") as output:
            for chunk in image:
                output.write(chunk)
    
    else:
        print ("Error code {}".format(image.status_code))


### -------------------------------------------------------------------------
### Función que captura de todas las imágenes de la url indicada
### -------------------------------------------------------------------------

def storeImages(url):

    page = requests.get(url)
     
    if page.status_code == 200:
        
        # Creamos el arbol con todo el documento html
        soup = BeautifulSoup(page.content, "lxml")
        
        # Buscamos todas las imágenes
        for img in soup.findAll('img'):
            image = (img.get('src'))
            image = image[0:image.find('?')]
            # Descargamos la imagen
            load_requests("https://www.lme.com"+image)
    else:
        print ("Error code {}".format(page.status_code))


storeURL("https://www.lme.com")

# Variable global que indica el directorio donde se van a grabar las imágenes
# Tenemos una forma de solicitarlo al usuario pero ha dado un error en uno de
# de los sistemas operativos donde se ha probado y hemos preferido mantener la
# versión estable en la que se indica el directorio directamente en el código
# directory = filedialog.askdirectory(initialdir=os.getcwd(),title='Directorio para la descarga de imágenes')
 
directory = "/Users/marianavalon/Documents/GitHub/LME-Scraper/Pictures" 

storeImages("https://www.lme.com/Metals")





