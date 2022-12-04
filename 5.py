# -*- coding: utf-8 -*-
"""
Created on Wed May 17 19:18:47 2017

@author: Atrocity
"""
'''
n=24
i=1

factor=n
while i*i<=n:
    if n%i==0:
        factor=i
    i+=1
    if (factor+1)==i:
        factor-=1
        while factor-1%n!=0:
            factor-=1
            
print(factor)'''

n=20
i=1
alist=[]
while True:
    while n%i!=0:
        i+=1
    newnumber=n/i
    i=1
    while True:
        if newnumber%i==0 and i<newnumber:
            newnumber=newnumber/i
        if i>=newnumber:
            break
        i+=1
    n-=1
    i=1
    alist.append(newnumber)
    if n==1:
        break
print(set(alist))
new=set(alist)
next=list(new)
product=1
for i in range(0,len(set(alist))):
    product=product*next[i]
print(product/4)
