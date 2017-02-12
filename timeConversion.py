# -*- coding: utf-8 -*-
"""
Created on Fri Feb 10 00:56:03 2017

@author: SROY
"""

#!/bin/python3

import sys


time = input().strip()
h,m,s = time.split(':')

if (s[2] == 'P') and (int(h) != 12):
    hr = 12 + int(h)
if (s[2] == 'A') and (int(h) != 12):
    hr = h
if (s[2] == 'A') and (int(h) == 12):
    hr = '00'
if (s[2] == 'P') and (int(h) == 12):
    hr = h    
print(str(hr) + ':' + m + ':' + s[:2]) 