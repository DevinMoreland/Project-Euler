listofnumbers=[]
n=0
while n<=999:
    if n%3==0 or n%5==0:
        listofnumbers.append(n)
    n+=1
print((listofnumbers))
print(sum(listofnumbers))
