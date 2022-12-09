'''
The sum of the squares of the first ten natural numbers is,

The square of the sum of the first ten natural numbers is,

Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is .

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
'''
#%%
def sumofsquares(x):
    sum=0
    for i in range(x+1):
        sum = sum+i**2
    return(sum)
def squareofsums(x):
    square=0
    for i in range(x+1):
        square+=i
    return(square**2)
y=100
print(squareofsums(y)-sumofsquares(y))
