#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 15 08:15:58 2019

@author: francisco
"""

import os

#path = os.getcwd()
path = 'C:\\Users\\fespinosa\\Documents\\Trabajo\\DWH\\Datos\\2020\\202009' 
#path.replace('/','//')
files = []

for r, d, f in os.walk(path):
    for file in f:
        files.append(file)

for f in files:
    print(f)
