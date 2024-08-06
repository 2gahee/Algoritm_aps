# 스택 : 후입 선출
# 빈스택, stack = [1, 2, 3, 4, 5]
# 후입 ---> append(), 선출 ---> pop()
# 재귀 + used 가지치기(백트래킹) + 자료구조 그래프(완전탐색 중 하나) ---> DFS(깊이우선탐색)

# append() : 시간복잡도가 O(1), pop() : 시간복잡도가 O(1)
# lst = [1, 2, 3]
# lst.append(4)
# lst == [1, 2, 3, 4]

# 큐 : 선입선출 , append(), pop(0) <--- 시간이 오래걸린다 : 시간복잡도가 O(N)
# lst = [1, 2, 3] # 기존에 있던 원소들의 인덱스가 바꼈을 까요?
# lst.pop(0)
# lst == [2, 3]
# pop(0)를 쓰지 않는다 왜? 시간복잡도가 높으니까
# deque 모듈 ---> pop(0) 대신 popleft() ----> 덱을 만들어야한다 덱에서 제거 ---> 시간복잡도가 O(1)
# ---> BFS에서는 deque 모듈

# 괄호 검사
# 언제 append() ?
# 언제 pop() ?
# append <--- 스택에 추가 : 여는 괄호면, 짝이 맞지 않을 때
# stack을 이용해서 만약 stack 비어 있지 않으면 result = 0
# pop() <--- 스택에서 제거 : 빈 스택이 아니다 and 닫는 괄호 and 짝이 맞을 때
# 코드의 마지막에서 stack이 비어있다면 result = 1

'''
for tc in range(1, int(input()) + 1):
    code = input()
    stack = [] # 빈스택 초기화
    for i in code:
        # 1. 여는 괄호면 스택에 추가
        if i == '{' or i == '(':
            stack.append(i)
        # 2. 닫는괄호(중괄호), 짝이 맞는다, 빈스택이 아니다
        elif stack and i == '}' and stack[-1] == '{':
            stack.pop()
        # 3. 닫는괄호(소괄호), 짝이 맞는다, 빈스택이 아니다
        elif stack and i == ')' and stack[-1] == '(':
            stack.pop()
        # 4. 짝이 맞지 않을 때
        elif i == '}' or i ==')':
            stack.append(i)

    if stack:
        result = 0
    else:
        result = 1

    print(f'#{tc} {result}')
    '''
'''
def check(code):
    stack = []
    opening = '{('
    closing = '})'
    pairs = {'}' : '{',
             ')' : '('}
'''