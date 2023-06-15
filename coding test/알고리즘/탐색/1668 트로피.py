def ascending(array):
    now = array[0]
    result =1
    for i in range(1,n):
        if now < array[i]:
            result +=1
            now =array[i]   
    return result
   
array=[]
n= int(input())
for _ in range(n):
    array.append(int(input()))
    
print(ascending(array))
array.reverse()
print(ascending(array))