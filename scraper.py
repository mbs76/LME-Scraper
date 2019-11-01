#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 20 12:17:05 2019

@authors: mbs76 & mnavalon 
"""

import requests
from bs4 import BeautifulSoup
import csv
import os


def storeURL(str):
    
    page = requests.get(str)
    
    if page.status_code == 200:
    
        soup = BeautifulSoup(page.content, "lxml")
    
        tag = soup.table
        head_tag = tag.thead
        body_tag = tag.tbody
            
        data = []
        separador = head_tag.get_text().find(":")
        moneda = head_tag.get_text()[0:separador].strip()
        fecha = head_tag.get_text()[separador + 1:].strip()
  
        trs = body_tag.findAll('tr')
    
        for tr in trs:
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


storeURL("https://www.lme.com")




