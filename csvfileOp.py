# -*- coding: utf-8 -*-
"""
Created on Mon Oct 24 21:51:40 2016

@author: SROY
"""

#runfile('C:/Users/SROY/Documents/CodeBase/PythonWorkspace/csvfileOp.py', wdir='C:/Users/SROY/Documents/CodeBase/PythonWorkspace')

def showcsvcontent(filename):
    import csv
    with open(filename,'r', encoding = 'utf-8') as file:
            r = csv.reader(file)
            for row in r:
                print(row)
    file.close()    