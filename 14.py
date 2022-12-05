"""
The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
"""
import time
start=time.time()
i=1
j=999999
numlist=[]
updatelist=[]
max=0
while True:
  while True:
    numlist.append(i)
    if i==1:
      break
    if i%2==0:
      i=i/2
    else:
      i=i*3+1
  if len(numlist)>len(updatelist):
    updatelist=numlist
    max=j
  j-=1
  i=j
  numlist=[]
  if j==1:
    break
print(updatelist)
print(max)
totaltime=time.time()-start
print(totaltime)