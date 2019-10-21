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
    #print(soup.prettify())
    tag = soup.table
    head_tag = tag.thead
    print("Fecha: ", head_tag.get_text().strip())
    body_tag = tag.tbody
    
    #print(body_tag.get_text())
  
    trs = body_tag.findAll('tr')
    
    for tr in trs:
    #for row in body_tag.findAll('tr'):
        producto = tr.text
        print("Producto: ", producto)
        cantidad = tr.findAll('td')
        print("Cantidad: ",  cantidad[0].get_text().strip())
        
"""
    for sibling  in body_tag.next_siblings:
            print(head_tag.get_text())    
            print(repr(sibling))
    
"""

storeURL("https://www.lme.com")



