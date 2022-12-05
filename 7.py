'''
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
'''
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
           