# -*- coding: utf-8 -*-
"""
Created on Thu Feb  9 10:54:18 2017

@author: SROY
"""

#!/bin/python3

import sys


n = int(input().strip())
a = []
for a_i in range(n):
    a_t = [int(a_temp) for a_temp in input().strip().split(' ')]
    a.append(a_t)

a_diag = []
for i in range(n):
    a_diag.append(a[i][i])
sum_a_diag = sum(a_diag)  

b = a[::-1]
a_rev_diag = []
for i in range(n):
    a_rev_diag.append(b[i][i])
sum_a_rev_diag = sum(a_rev_diag)

print(abs(sum_a_diag - sum_a_rev_diag))