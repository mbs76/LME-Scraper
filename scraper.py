#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 20 12:17:05 2019

@authors: mbs76 & mnavalon 
"""

import requests
from bs4 import BeautifulSoup
import sys


<<<<<<< HEAD
page = requests.get("http://www.lme.com")
soup = BeautifulSoup(page.content)
#print(soup.prettify())


=======

def storeURL(str):
    page = requests.get(str)
    soup = BeautifulSoup(page.content)
    #print(soup.prettify())
    tag = soup.table
    head_tag = tag.thead
    #print(head_tag.get_text())
    body_tag = tag.tbody.tr
   
    for sibling  in body_tag.next_siblings:
            print(head_tag.get_text())    
            print(repr(sibling)) 
    
storeURL("https://www.lme.com")
#>>>>>>> 484022ac7588645fc51384c8cec429ec0aac831c