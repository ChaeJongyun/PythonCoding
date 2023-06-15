t=int(input())
array=[]
for _ in range(t):
    width,height,n=map(int,input().split())
    for i in range(n):
        
        x,y=map(int,input().split())
        array.append((x,y))
        
print(array)