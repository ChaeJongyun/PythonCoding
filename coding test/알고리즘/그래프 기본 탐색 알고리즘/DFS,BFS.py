from collections import deque

def dfs(v):
    print(v, end=' ')
    visited[v]=True # 방문한 것은 True값 즉 1로 바꿔줌
    for i in adj[v]: #인접한 노드를 살펴봄
        if not(visited[i]): #만약에 방문한 적이 없다면 (있으면 넘어감)
            dfs(i) #재귀함수 실행

def bfs(v):
    q = deque([v]) # deque을 활용함
    visited[v]=True
    while q: # q가 빌때까지 반복함
        v=q.popleft()
        print(v, end=' ')
        for i in adj[v]:
            if not(visited[v]):
                visited[v]=True
           
n,m,v=map(int,input().split())
adj=[[] for _ in range(n+1)]

for _ in range(m):
    x,y = map(int,input().split())
    adj[x].append(y)
    adj[y].append(x)

for i in range(1,n+1):
    adj[i].sort()

visited=[False]*(n+1)
dfs(v)
print() #한 줄 띄어쓰기
visited=[False]*(n+1) # visited 리스트 초기화를 위해서 한번 더 써준 것
bfs(v)
          
            
            