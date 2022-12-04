# -*- coding: utf-8 -*-
"""
Created on Mon May 29 18:57:19 2017

@author: Atrocity
"""

primeslist=[]
n=2
i=2

while True:
    while True:
        if i>n**.5:
            primeslist.append(n)
            break
        else:
            if n%i==0:
                break
            i+=2
    if n==2:
        n=1
    n+=2
    i=3
    if n>=2*10**6:
        break
print(sum(primeslist))