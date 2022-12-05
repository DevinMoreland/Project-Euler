"""
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
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