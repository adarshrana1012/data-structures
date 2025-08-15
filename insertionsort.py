import time
start_time = time.time()
n=int(input("enter size"))
l=list(range(n, 0, -1))
#for i in range (0,n):
    #v=int(input())
    #l.append(v)
c=0
s=0
for i in range (1,n):
    temp=l[i]
    j=i-1
    while j >= 0:
        c += 1 
        if l[j] > temp:
            l[j + 1] = l[j]
            s += 1
            j -= 1
        else:
            break
    l[j + 1] = temp
print(l)
end_time = time.time()
print("no of shifts",s)
print("no.of comparison",c)
print("Runtime:", end_time - start_time, "seconds")