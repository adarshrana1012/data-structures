import random
import time
start_time = time.time()
n=int(input("enter the size"))
l =[]
i=0
for i in range (n):
      v=int(input())
      l.append(v)
c=0
s=0
for i in range (n-1):
    min=i
    j=i+1
    for j in range (i+1,n):
      c=c+1
      if(l[min]>l[j]):
         min=j
    temp = l[i]
    l[i] = l[min]
    s=s+1
    l[min]=temp
print("no. of comparison:-",c)
print("no. of swapping:-",s)


end_time = time.time()

print("Runtime:", end_time - start_time, "seconds")


