# -*- coding: utf-8 -*-
"""
Created on Tue Oct 25 17:43:30 2016

@author: SROY
"""

#runfile('C:/Users/SROY/Documents/CodeBase/PythonWorkspace/matrices.py', wdir='C:/Users/SROY/Documents/CodeBase/PythonWorkspace')

import numpy as np

a= [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
b = np.matrix('1 2 3;4 5 6;7 8 9')
print('A = ',a)
print('Matrix B = ',b)


print('Transpose of B = ', np.transpose(b))
print('Inverse of B = ', np.transpose(b))
print('sum of diagonals of B = ', sum(np.diagonal(b)))

def mat_rot1():
    a_rot = np.rot90(np.matrix(a))
    print(a_rot)  
    
   

