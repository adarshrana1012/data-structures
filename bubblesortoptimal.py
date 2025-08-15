import time
start_time = time.perf_counter()
n = int(input("Enter the size: "))
l = []
print("Enter elements:")
for _ in range(n):
    v = int(input())
    l.append(v)
c = 0  
s = 0   
for i in range(n-1, 0, -1):
    f = False 
    for j in range(i):
        c += 1
        if l[j] > l[j+1]:
            l[j], l[j+1] = l[j+1], l[j]
            s += 1
            f = True 
    if not f:
        break 
print("Sorted list:", l)
print("No. of swapping:", s)
print("No. of comparison:", c)
end_time = time.perf_counter()
print("Runtime:", end_time - start_time, "seconds")
