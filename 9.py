"""
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a^2 + b^2 = c^2
For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""
a=1
b=2
c=3
sum=0
product=1
print("working...")
while True:
    while True:
        
        while True:
            sum=a+b+c
            if sum==1000:
                if a**2+b**2==c**2:
                    product=a*b*c
                    break
            if sum>1000:
                break
            c+=1
            
        if sum==1000 and a**2+b**2==c**2:
            break
        if b>1000:
            break
        b+=1
        c=b+1
    if sum==1000 and a**2+b**2==c**2:
        break
    a+=1
    b=a+1
    c=a+2
print(a,b,c,sum,product)