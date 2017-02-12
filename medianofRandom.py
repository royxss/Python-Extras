# -*- coding: utf-8 -*-
"""
Created on Thu Feb  9 11:15:56 2017

@author: SROY
"""
import numpy as np   
a = np.random.randint(20, size=(1, 20))
a = np.ndarray.tolist(a)
a = a[0]
a.sort()

print(a)
print("input K value: ")
k = int(input().strip()) #create sublist K inclusive to find median of the new list
# sublist all numbers <=6
# this will cause problems when 6 has dups
# as it will give the first index only and skip the rest

b = a[::-1] #reverse a
b = b[b.index(k):]  #find index now. this will find the last value
# slice from the last index to first
# then sort
b.sort()
print(b)  # perfect sublist created

# Median
if len(b)%2 != 0:
    ind = ((len(b) + 1)/2)-1
    print("median = ", b[int(ind)])

if len(b)%2 == 0:    
    ind1 = (len(b)/2)-1
    ind2 = (len(b)/2)
    print("median = ", (b[int(ind1)] + b[int(ind2)])/2)