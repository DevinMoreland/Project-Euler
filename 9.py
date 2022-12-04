# -*- coding: utf-8 -*-
"""
Created on Sat May 27 14:47:54 2017

@author: Atrocity
"""
a=1
b=2
c=3
sum=0
product=1
print("working...")
while True:
    while True:
        
        while True:
            sum=a+b+c
            if sum==1000:
                if a**2+b**2==c**2:
                    product=a*b*c
                    break
            if sum>1000:
                break
            c+=1
            
        if sum==1000 and a**2+b**2==c**2:
            break
        if b>1000:
            break
        b+=1
        c=b+1
    if sum==1000 and a**2+b**2==c**2:
        break
    a+=1
    b=a+1
    c=a+2
print(a,b,c,sum,product)