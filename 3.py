"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""

n=20
i=2
while n%i!=0:
    i+=1
newnumber=n/i
i=2
while True:
    if newnumber%i==0 and i<newnumber:
        newnumber=newnumber/i
    if i>=newnumber:
        break
    i+=1
print(newnumber)
