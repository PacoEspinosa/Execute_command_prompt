#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 18 00:03:54 2019

@author: francisco
"""

import datetime

a = datetime.datetime.today()
numdays = 100
datelist= []
for x in range(0,numdays):
    datelist.append((a-datetime.timedelta(days=x)).strftime("%Y-%m-%d"))
    
print(datelist)
