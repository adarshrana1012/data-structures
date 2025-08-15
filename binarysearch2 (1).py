import time
start_time=time.time()
n = int(input("Enter the size: "))
l=list(range(1, n+1))
#print(l)
#print("Enter the elements")
#for i in range(n):
 #   v = int(input())
  #  l.append(v)
s = int(input("Enter the target element to search: "))
#l.sort()
l.sort()  
x = 0
y = len(l) - 1
u=-1
while x <= y:
    mid = (x + y) // 2
    if l[mid] < s:
        x = mid + 1
    elif l[mid] > s:
         y = mid - 1
    else:
        u = mid
        break
        print("Binary Search")
if u != -1:
    print("Number found at position", u + 1)
else:
    print("Number not found")
end_time = time.time()

print("Runtime:", end_time - start_time, "seconds")