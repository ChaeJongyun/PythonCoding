import sys
input = sys.stdin.readline

a,b,c =map(int,input().split())

arr = [0] * int(a+b+c+1)
result=0

for i in range(1,a+1):
    for j in range(1,b+1):
        for k in range(1,c+1):
            result = i+j+k
            arr[result] +=1
           
 
                       
print(arr.index(max(arr)))