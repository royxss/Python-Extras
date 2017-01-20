# -*- coding: utf-8 -*-
"""
Created on Sat Oct 22 11:02:08 2016

@author: SROY
"""

#runfile('C:/Users/SROY/Documents/CodeBase/PythonWorkspace/hashing.py', wdir='C:/Users/SROY/Documents/CodeBase/PythonWorkspace')

def bitwise_op(init_val, shift):
    a=init_val
    y=shift
    print("Single left Y shift value : ", a<<y)
    print("Double left Y shift value : ", a<<(y+1))
    
def hashfunc(str):
    import hashlib
    h=hashlib.md5(str.encode('utf-8')).hexdigest()
    print("The hash of input string : ", h)

#%%    
def hashfile(filename):
    import hashlib
    h=hashlib.md5()
    
    with open(filename,'rb') as file:
        rd=0
        #while rd != b'':
        while True:
            print('Value of rd = ',rd,'  Line : ',file.readline())
            rd=file.readline()
            h.update(rd)
            if not rd: break
        
    hval=h.hexdigest()                
    print("The hash of file : ", hval)
    
    file.close()
            
    