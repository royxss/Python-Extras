# -*- coding: utf-8 -*-
"""
Created on Fri Feb 10 01:35:15 2017

@author: SROY
"""

#!/bin/python3

import sys


n,k,q = input().strip().split(' ')
n,k,q = [int(n),int(k),int(q)]
a = [int(a_temp) for a_temp in input().strip().split(' ')]
b = a
k %= n
b = a[-k:] + a[:-k]

print ("Rotated K times")
print(b)
    
for i in range(q):
    m = int(input().strip())
    print(b[m])  