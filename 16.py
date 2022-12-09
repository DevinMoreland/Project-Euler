'''
2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2^1000?
'''
# %%
import numpy as np
def SumOfDigits(x):
    *x,=str(x)
    x=np.asarray(x)
    return(np.sum(x.astype(int)))

y=2**1000
print(SumOfDigits(y))


# %%
