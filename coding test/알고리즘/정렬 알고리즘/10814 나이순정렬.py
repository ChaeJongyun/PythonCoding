n = int(input())
arr1=[]


for i in range(n):
    a,b = input().split()
    arr1.append((int(a),b))
    

arr1=sorted(arr1,key=lambda x:x[0])

# for i in arr1:
  # print(i[0],i[1])
for i in arr1:
    print(*i)
