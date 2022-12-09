'''
Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.
'''
#%%
import numpy as np

def divisorSum(n):
    y = np.array([])
    for i in range(1,n):
        if n%i== 0:
            y=np.append(y,i)
    return(y.sum())

def hasAmicable(n):
    x=int(divisorSum(n))
    y=int(divisorSum(x))
    if y==n and n!=x:
        return(x,y)

n=10000
array = np.array([])
for i in range(1,n):
    x=np.array([hasAmicable(i)])
    x = [i for i in x if i is not None]
    if x!=[]:
        array=np.append(array,hasAmicable(i))
array=set(array)
print(int(sum(array)))
# %%
