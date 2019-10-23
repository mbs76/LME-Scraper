#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 20 12:17:05 2019

@authors: mbs76 & mnavalon 
"""

import requests
from bs4 import BeautifulSoup
import sys
import os


def storeURL(str):
    
    page = requests.get(str)
    soup = BeautifulSoup(page.content)
    
    tag = soup.table
    head_tag = tag.thead
    body_tag = tag.tbody
    
    separador = head_tag.get_text().find(":")
    moneda = head_tag.get_text()[0:separador].strip()
    fecha = head_tag.get_text()[separador + 1:].strip()
    
    f = open("lme.csv", "a")
    if os.stat('lme.csv').st_size == 0:
        f.write("Date, Product, Currency, Value\n")
  
    trs = body_tag.findAll('tr')
    
    for tr in trs:
        linea = ""
        print("Fecha: " + fecha)
        linea = fecha
        producto = tr.findAll('th')
        print("Producto: ", producto[0].get_text().strip())
        linea += ", " + producto[0].get_text().strip()
        linea += ", " + moneda
        cantidad = tr.findAll('td')
        print("Cantidad: ",  cantidad[0].get_text().strip())
        linea += ', "' + cantidad[0].get_text().strip() + '"\n'
        print(linea)
        f.write(linea)
    
    f.close()


storeURL("https://www.lme.com")




