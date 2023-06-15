from collections import deque

n,k=map(int,input().split())
max = 100001
array=[0]*max

def bfs():
    q=deque([n])
    while q:
        now_pos = q.popleft()
        if now_pos ==k:  # now_pos 가 목표치에 도달했을때 거리 반환
            return array[now_pos]
        for next_pos in (now_pos -1, now_pos+1, now_pos*2):
            if 0<= next_pos < max and not array[next_pos]: #next_pos가 0보다크고 max보다 작을  때
                array[next_pos] = array[now_pos]+1
                q.append(next_pos) 


print(bfs())
                