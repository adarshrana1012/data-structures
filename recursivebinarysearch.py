import time
start_time = time.time()
def binary(l, t, x, y):
    if x > y:
        return -1  
    mid = (x + y) // 2
    if l[mid] < t:
        return binary(l, t, mid + 1, y)
    elif l[mid] > t:
        return binary(l, t, x, mid - 1)
    else:
        return mid+1 
n = int(input("Enter the size: "))
l=list(range(1, n+1))
print(l)
#print("Enter the elements")
#for i in range(n):
 #   v = int(input())
  #  l.append(v)
t = int(input("Enter the target element to search: "))
#l.sort()
r= binary(l, t, 0, n-1)
if r!= -1:
    print(f"Element found at index {r}")
else:
    print("Element not found.")
end_time = time.time()

print("Runtime:", end_time - start_time, "seconds")
