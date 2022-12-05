"""
Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.


How many such routes are there through a 20×20 grid?
"""
import time

t=time.time()
n=0
row=[]
for i in range(20):
    row.append(i+2)
updaterow=row

for i in range(19):
    while n!=20:
        if n==0:
            updaterow[0]=row[0]+1
        else:
            updaterow[n]=row[n]+updaterow[n-1]
        n+=1
    row=updaterow
    n=0
print(row[19])
print(time.time()-t)