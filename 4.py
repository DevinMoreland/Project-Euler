# -*- coding: utf-8 -*-
"""
Created on Sat May 20 17:36:44 2017

@author: Atrocity
"""

import math
list=[]
def palindrome(value):
    if str(value)==str(value)[::-1]:
        return True
    else:
        return False
i=999
j=999    
while i>0:
    while j>0:
        if palindrome(i*j)==True:
            list.append(i*j)
        j-=1
    j=i
    i-=1
    

print(max(list))