import sys
input = sys.stdin.readline

a,b,c = map(int,input().split())
counter = dict()


for i in range(1,a+1):
    for j in range(1,b+1):
        for k in range(1,c+1):
            sum = i +j +k
            if sum not in counter:
                counter[sum] =1
            else:
                counter[sum]  +=1
            
max_count =0
answer=0
for(key,value) in counter.items():
    if max_count <value:
        max_count =value
        answer =key
    elif max_count ==value:
        answer=min(answer,key)
    
print(answer)