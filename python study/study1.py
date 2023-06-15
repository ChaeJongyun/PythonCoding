

def dfs(v):
    visited[v] =True
    print(v, end=' ')
    for i in graph[v]: #현재 노드와 연결된 달느 노드를 재귀적으로 방문
         if not visited[i]:
            dfs(i)
         
graph=[
  [],
  [2,3,8],
  [1,7],
  [1,4,5],
  [3,5],
  [3,4],
  [7],
  [2,6,8],
  [1,7]
]

visited=[False] *9

dfs(1)