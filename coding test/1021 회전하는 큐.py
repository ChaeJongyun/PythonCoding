import sys
input = sys.stdin.readline
from collections import deque
n,m = map(int,input().split())
d = deque([i for i in range(1,n+1)])
targets = list(map(int,input().split()))
cnt = 0

for target in targets:
    while True:
        if d[0] == target:
            d.popleft()
            break
        else:
            if d.index(target) < len(d)/2:
                while d[0] != target:
                    d.append(d.popleft())
                    cnt +=1
            else:
                while d[0] != target:
                    d.appendleft(d.pop())
                    cnt +=1
                
                
print(cnt)