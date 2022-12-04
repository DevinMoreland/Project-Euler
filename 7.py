# -*- coding: utf-8 -*-
"""
Created on Wed May 24 18:50:05 2017

@author: Atrocity
"""


#==============================================================================
# n=2
# i=n-1
# count=0
# limit=10001
# while True:
#     
#     while True:
#         if i==1:
#             count+=1
#             break
#         
#         if n%i==0:
#             break
#         
#         i-=1
#         
#     if count==limit:
#         break
#     else:
#         n+=1
#         i=n-1
#     print(count)
# print(n)
#==============================================================================
import time
start=time.time() 
n=2
i=2
count=0
limit=10001
while True:
    
    while True:
        if i>(n**.5):
            if n!=4:
                count+=1
                break
        
        if n%i==0:
            break
            print(n,"hi")
        i+=1
        
    if count==limit:
        break
    else:
        n+=1
        i=2
    print(count)
print(n)
print(time.time()-start)
           