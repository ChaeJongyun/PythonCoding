n =int(input())

arr=[]
arr[0]=0
arr[1]=1
result=0
for i in range(2,n+1):
     arr[i] = arr[i-2]+arr[-1]
     result= result +arr[i]
     
     
print(result)