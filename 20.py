n=1
for i in range(1,101):
  n=n*i
x=str(n)
sum=0
for i in range(len(x)):
  sum+=int(x[i])
print(sum)