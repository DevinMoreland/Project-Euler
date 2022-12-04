# -*- coding: utf-8 -*-
"""
Created on Thu Jun  1 20:34:15 2017
 
@author: Atrocity
"""
sequence=1
length=500
trianglenumber=0
numlist=[]
n=1
while True:
    for i in range(0,sequence+1):
        trianglenumber=i+trianglenumber
    while True:
        if n>trianglenumber**.5:
            setlist=set(numlist)
            break
        if trianglenumber%n==0:
            numlist.append(n)
            numlist.append(trianglenumber/n)
        n+=1
    if len(numlist)>=length:
        break
    numlist=[]
    trianglenumber=0
    n=1
    sequence+=1
print(trianglenumber)
print(setlist)
print(numlist)
print(15%2)