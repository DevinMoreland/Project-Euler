"""
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
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