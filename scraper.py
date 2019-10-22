#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 20 12:17:05 2019

@authors: mbs76 & mnavalon 
"""

import requests
from bs4 import BeautifulSoup
import sys

"""
<<<<<<< HEAD
page = requests.get("http://www.lme.com")
soup = BeautifulSoup(page.content)
#print(soup.prettify())


=======
<<<<<<< HEAD

"""

def storeURL(str):
    page = requests.get(str)
    soup = BeautifulSoup(page.content)
    tag = soup.table
    head_tag = tag.thead
    print("Fecha: ", head_tag.get_text().strip())
    body_tag = tag.tbody
  
    trs = body_tag.findAll('tr')
    
    for tr in trs:
        producto = tr.findAll('th')
        print("Producto: ", producto[0].get_text().strip())
        cantidad = tr.findAll('td')
        print("Cantidad: ",  cantidad[0].get_text().strip())
        


storeURL("https://www.lme.com")



