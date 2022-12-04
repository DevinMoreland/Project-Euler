# -*- coding: utf-8 -*-
"""
Created on Sat Jun 10 16:12:53 2017

@author: Atrocity
"""

def numberinwords(n):
    digits=[]
    ones=["","one","two","three","four","five","six","seven","eight","nine"]
    tens=["","ten","twenty","thirty","fourty","fifty","sixty","seventy","eighty","ninety"]
    teens=["","ten","eleven","twelve","thirteen","fourteen","fifteen","sixteen","seventeen","eighteen","nineteen"]
    if len(str(n))==4:
        word="onethousand"
    elif len(str(n))==3:
        digits.append(0)
        digits.append(str(n)[0])
        digits.append(str(n)[1])
        digits.append(str(n)[2])
        word=ones[int(digits[1])]+"hundred"
        if int(digits[2])==1:
            word=word+"and"+teens[int(digits[3])+1]
        elif int(digits[2])!=1 and int(digits[2])!=0:
            word=word+"and"+tens[int(digits[2])]+ones[int(digits[3])]
        elif int(digits[3])!=0 and int(digits[2])==0:
            word=word+"and"+ones[int(digits[3])]
        elif int(digits[3])!=0:
            word=word+ones[int(digits[3])]
    elif len(str(n))==2:
        digits.append(0)
        digits.append(0)
        digits.append(str(n)[0])
        digits.append(str(n)[1])
        if int(digits[2])!=1:
            word=tens[int(digits[2])]+ones[int(digits[3])]
        else:
            word=teens[int(digits[3])+1]
    elif len(str(n))==1:
        digits.append(0)
        digits.append(0)
        digits.append(0)
        digits.append(str(n)[0]) 
        word=ones[int(digits[3])]
    return(word)

sum=0
list=[]
for i in range(1,1001):
    sum=sum+len(numberinwords(i))
    list.append(numberinwords(i))
print(sum)