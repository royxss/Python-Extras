#!/bin/python3

import sys


a0,a1,a2 = input().strip().split(' ')
a0,a1,a2 = [int(a0),int(a1),int(a2)]
b0,b1,b2 = input().strip().split(' ')
b0,b1,b2 = [int(b0),int(b1),int(b2)]
alice=[0]
bob=[0]

if a0 > b0:
    alice.append(1)
if a0 < b0:
    bob.append(1)    
if a1 > b1:
    alice.append(1)
if a1 < b1:
    bob.append(1)
if a2 > b2:
    alice.append(1)
if a2 < b2:
    bob.append(1)    

alice_sum = sum(alice)  
bob_sum = sum(bob)

sys.stdout.write(str(alice_sum))
sys.stdout.write(' ')
sys.stdout.write(str(bob_sum))