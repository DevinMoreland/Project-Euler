'''
A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of two abundant numbers is 24. By mathematical analysis, it can be shown that all integers greater than 28123 can be written as the sum of two abundant numbers. However, this upper limit cannot be reduced any further by analysis even though it is known that the greatest number that cannot be expressed as the sum of two abundant numbers is less than this limit.

Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.
'''
#%%
import numpy as np
import math

iLim = 1
uLim = 28123

def getDivisors(n):
    y = np.array([])
    for i in range(1,math.ceil(n/2)+1):
        if n%i== 0:
            y=np.append(y,i)
    return(y.astype(int))

def isAbundent(x):
    y = sum(getDivisors(x))
    if y > x:
        return(True)
    else:
        return(False)

def abundentList(x,y):
    z=np.array([])
    if x < y: 
        for i in range(x,y):
            if isAbundent(i)==True:
                z=np.append(z,i).astype(int)
        return(z)
    else:
        print("fail")
            
    result = [False] * (lim + 1)
    for i in range(len(y)):
        for j in range(i, len(y)):
            s = y[i] + y[j]
            if s > lim:
                break
            result[s] = True
            
allAbundent = abundentList(iLim,uLim)

for i in range(len(allAbundent)):
    for j in range(i, len(allAbundent)):
        s = allAbundent[i] + allAbundent[j]
        if s > uLim:
            break
        result[s] = True

print(sum(i for i, x in enumerate(result) if not x))
# %%
