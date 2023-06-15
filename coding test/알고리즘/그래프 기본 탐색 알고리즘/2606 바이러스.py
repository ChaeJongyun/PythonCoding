from collections import deque 


def bfs (v):
    global count
    q=deque([v])
  
    array[v]=True
    while q:
        v = q.popleft()
       
        for i in adj[v]:
            if not array[i]:
                array[i]=True
                count =count+1
                q.append(i)
    
    return count                



count =0
n = int(input())
m = int(input())
array=[False for _ in range(n+1)]
adj=[[] for _ in range(n+1)]
for i in range(1,m+1):
    x,y=map(int,input().split())
    adj[x].append(y)
    adj[y].append(x)
   
print(bfs(1))


