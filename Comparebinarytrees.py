# -*- coding: utf-8 -*-
"""
Created on Tue Nov  9 19:13:14 2016

@author: SROY
This program creates two binary trees and checks if the both trees
have similar structure or not

"""
#runfile('C:/Users/SROY/Documents/CodeBase/PythonWorkspace/ADOComparebinarytrees.py', wdir='C:/Users/SROY/Documents/CodeBase/PythonWorkspace')

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
     

def printTree(tree):
        if tree != None:
            printTree(tree.left)
            print(tree.data)
            printTree(tree.right) 
            
def TreeCompare(t1, t2):

    if t1 is None and t2 is None:
        return True
 
    if t1 is not None and t2 is not None:
        return ((t1.data == t2.data) and
        TreeCompare(t1.left, t2.left)and
        TreeCompare(t1.right, t2.right))
     
    return False 
           
#Create Tree 1 
root1 = Node(1)
root1.left = Node(2)
root1.right = Node(3)
root1.left.left = Node(4)
root1.left.right = Node(5)

#Create Tree 2
root2 = Node(1) 
root2.left = Node(2)
root2.right = Node(3)
root2.left.left = Node(4)
root2.left.right = Node(5)

print('Print Tree 1:\n')
printTree(root1)
print('Print Tree 2:\n')
printTree(root2)

print('Tree Comparison Result: ') 
if TreeCompare(root1, root2):
    print ('Trees are identical')
else:
    print ('Trees are not identical')