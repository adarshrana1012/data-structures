import time
start_time = time.perf_counter()
n=int(input("enter the size"))
l=[]
for i in range(n):
    v=int(input())
    l.append(v)
c=0
s=0
for i in range (n-1,0,-1):
    for j in range (i):
     c=c+1
     if(l[j]>l[j+1]):
        l[j],l[j+1]=l[j+1],l[j]
        s=s+1
print("no.of swapping",s)
print("no.of comparison",c)
end_time = time.perf_counter()

print("Runtime:", end_time - start_time, "seconds")