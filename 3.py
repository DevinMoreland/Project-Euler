# -*- coding: utf-8 -*-
"""
Created on Wed May 17 19:18:47 2017

@author: Atrocity
"""

n=20
i=2
while n%i!=0:
    i+=1
newnumber=n/i
i=2
while True:
    if newnumber%i==0 and i<newnumber:
        newnumber=newnumber/i
    if i>=newnumber:
        break
    i+=1
print(newnumber)
