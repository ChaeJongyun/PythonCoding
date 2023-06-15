import sys
input =sys.stdin.readline

n= int(input())
k=1
result=0
while n-k+1 !=0 :
    if k>n:
        k=1
    k +=1  
    n = n-k
    result +=1

print(result)