# -*- coding: utf-8 -*-
"""
Created on Thu Feb  9 10:51:45 2017

@author: SROY
"""

#!/bin/python3

import sys


n = int(input().strip())
for i in range(n):
    j=0;k=0
    for j in range(n-i-1):
        sys.stdout.write(' ')
    for k in range(i+1):
        sys.stdout.write('#')
    sys.stdout.write('\n') 