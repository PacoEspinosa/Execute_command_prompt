# -*- coding: utf-8 -*-
"""
Created on Mon Sep 30 23:21:29 2019

@author: fespinosa
"""

import subprocess
MyOut = subprocess.Popen(['ls', '-l', '.'], 
            stdout=subprocess.PIPE, 
            stderr=subprocess.STDOUT)
stdout,stderr = MyOut.communicate()
print(stdout)
print(stderr)