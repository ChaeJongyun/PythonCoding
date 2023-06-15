n = int(input())
import heapq
arr=[]
h=[]
result =[]
result2=0

for i in range(n):
    a = int(input())
    heapq.heappush(arr,a)
for i in range(n-1):    
    one = heapq.heappop(arr)
    two = heapq.heappop(arr)
    result.append(one+ two)
    
    heapq.heappush(arr,one+two)
    
for i in range(n-1):
    result2 +=result[i]

print(result2)
    
       

    