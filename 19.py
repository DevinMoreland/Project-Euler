'''
You are given the following information, but you may prefer to do some research for yourself.

1 Jan 1900 was a Monday.
Thirty days has September,
April, June and November.
All the rest have thirty-one,
Saving February alone,
Which has twenty-eight, rain or shine.
And on leap years, twenty-nine.
A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?
'''
import time
start=time.time()
calendardays=[31,28,31,30,31,30,31,31,30,31,30,31]
count=0
year=1901
days=0
while True:
  for i in range(0,12):
    days=calendardays[i]+days
    if i==2 and year%4==0 and year<2000:
      days+=1
    if days>36524:
      break
    if days%7==5:
      count+=1
    year+=1
  if days>36524:
    break
print(count,time.time()-start)