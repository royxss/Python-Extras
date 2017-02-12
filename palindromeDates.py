# -*- coding: utf-8 -*-
"""
Created on Thu Feb  9 12:18:22 2017

@author: SROY
"""

import datetime


start = datetime.datetime.strptime("01-01-1000", "%d-%m-%Y")
end = datetime.datetime.strptime("01-01-2000", "%d-%m-%Y")

date_generated = []

for x in range(0, (end-start).days):
    ndt = start + datetime.timedelta(days=x)
    left = ndt.strftime('%m%d%Y')
    right = left[::-1]
    if left == right:
        date_generated.append(left)

print("Palindrome dates between range start and end: ")        
print(date_generated)        