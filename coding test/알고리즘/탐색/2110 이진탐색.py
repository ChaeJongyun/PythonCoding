n,c = list(map(int,input().split()))

array=[]
for i in range(n):
    array.append(int(input()))
array=sorted(array)

start =array[1]-array[0]
end = array[-1]-array[0]
result =0

while (start <=end): #중요
    mid=(start+end)//2 #mid 는 gap을 의미
    value=array[0]
    count=1
    for i in range(1,len(array)):
        if array[i] >= value +mid:
            value =array[i]
            count+=1
        if count <=c:
            start =mid+1
            result = mid
        else :
            end =mid-1
             
print(result ) 