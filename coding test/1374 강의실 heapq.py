import sys
input = sys.stdin.readline
import heapq

n = int(input())
lectures =[]
for i in range(n):
    id,start,end = map(int,input().split())
    heapq.heappush(lectures,(start,end))
    
print(heapq)