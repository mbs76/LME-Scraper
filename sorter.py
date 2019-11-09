#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 20 12:17:05 2019

@authors: mbs76 & mnavalon 
"""
import os
import csv
import pandas as pd

# Definimos los elementos de cada categoría de metales mediante conjuntos
# Los nombres son los utilizados por la London Metals Exchange 'LME'

ferrous_metals = set(["LME Steel Rebar", "LME Steel Scrap"])
non_ferreous_metals = set(["LME Aluminium", "LME Copper", "LME Zinc", "LME Nickel", "LME Tin", "LME Lead", "LME Aluminium Alloy", "LME NASAAC"])
minor_metals = set(["LME Cobalt"])
precious_metals = set(["LME Gold", "LME Silver", "LME Platinum", "LME Palladium"])


# Función que clasifica cada metal y genera un nuevo fichero csv con el campo 
# de la categoría a la que pertenece

def sorter(file_csv):
    
    # Leemos el fichero csv que debe tener 4 columnas denominadas 
    # Date, Product, Currency,Value
    dataset = pd.read_csv(file_csv, sep=',')
    
    with open("lme_sorter.csv", "w") as f:
        
        writer = csv.writer(f)
        
        if os.stat('lme_sorter.csv').st_size == 0:
            # Si el fichero no existe lo creamos insertando la cabecera
            writer.writerow(["Date", "Product", "Currency", "Value", "Type"])
        
        for row in dataset.itertuples():
            if row.Product in ferrous_metals: 
                tipo = "Ferrous metals"
            elif row.Product in non_ferreous_metals: 
                tipo = "Non ferrous metals"
            elif row.Product in minor_metals: 
                tipo = "Minor metals" 
            elif row.Product in precious_metals: 
                tipo = "Precious metals" 
            else:
                tipo = "NaN" # No se encuentra en ninguno de los conjuntos
            
            # Creamos la fila con el metal categorizado
            writer.writerow([row.Date,row.Product,row.Currency,row.Value,tipo])           

# Llamamos a la función clasificadora con el fichero csv que contiene el dataset
sorter("lme.csv")
