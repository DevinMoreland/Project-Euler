# -*- coding: utf-8 -*-
'''
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
'''

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
