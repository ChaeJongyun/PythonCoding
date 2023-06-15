test_case = int(input())

for _ in range(test_case):
    left_stack=[]
    right_stack=[]
    data = input()
    for i in data:
        if i  == '-':
            if left_stack: # left_stack이 안비어있다면
                left_stack.pop()
        elif i =='<':
            if left_stack:
                right_stack.append(left_stack.pop())
        elif i == '>':
            if right_stack:
                left_stack.append(right_stack.pop())
        else:
            left_stack.append(i)
            
    left_stack.extend(reversed(right_stack))
    print(''.join(left_stack))  # join은 리스트로 된 문자열을 한줄로 합치는 역할
                                #['b','a','s','d','f',] -> basdf
    
# N의 범위가 20: O(n!), O(2^n) 브루트포스 , 전탐색 : 모든 경우의 수를 세는방법

    #N의 범위가 500: 시간 복잡도가 O(N³) 알고리즘을 설계하면 문제를 풀 수 있다.
            # 플로이드 와샬 알고리즘 : 

# N의 범위가 2,000: 시간 복잡도가 O(N²) 알고리즘을 설계하면 문제를 풀 수 있다.
#벨만 포드 알고리즘 

# N의 범위가 100,000: 시간 복잡도가 O(NlogN),O(N) 알고리즘을 설계하면 문제를 풀 수 있다.
#동적프로그래밍, 이분탐색, 다익스트라 알고리즘, 유니언 파인드, 세그먼트 트리, 투 포인터 

# N의 범위가 10,000,000: 시간 복잡도가 O(logN) 알고리즘을 설계하면 문제를 풀 수 있다
# 유클리드 호제법.