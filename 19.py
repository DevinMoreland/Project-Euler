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