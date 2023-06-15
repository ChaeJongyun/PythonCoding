def check(x):
    for i in range(x):
        if column[x] == column[i]:
            return False
        if abs(column[x]-column[i])== x-i:
            return False
    return True


def dfs(x):
    global result
    if x==n:
        result+=1
    else:
        for i in range(n):
            column[x]=i
            if check(x):
                dfs(x+1)
                

n =int(input())
column=[0]*n
result=0
dfs(0)
print(result)



                
                 