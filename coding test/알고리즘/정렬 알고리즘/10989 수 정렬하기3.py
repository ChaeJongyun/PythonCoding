import sys

n = int(sys.stdin.readline())

array = [0] *10001  

for i in range(n):
    data =int(sys.stdin.readline())
    array[data] +=1
    
for i in range(10001):
    if array[i] !=0:
        for j in range(array[i]):
            print(i)
            
            
# O(n)을 사용해야만 풀 수 있고 입력값이 많으므로 import sys가 필수
