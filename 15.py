# -*- coding: utf-8 -*-
"""
Created on Thu Jun  8 19:41:48 2017

@author: Atrocity
"""
import time

t=time.time()
n=0
row=[]
for i in range(20):
    row.append(i+2)
updaterow=row

for i in range(19):
    while n!=20:
        if n==0:
            updaterow[0]=row[0]+1
        else:
            updaterow[n]=row[n]+updaterow[n-1]
        n+=1
    row=updaterow
    n=0
print(row[19])
print(time.time()-t)