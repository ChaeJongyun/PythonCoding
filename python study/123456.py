from collections import deque
d = deque([(1,2),(3,4),(5,6)])
x,y = d.popleft()
print(x)