import sys
sys.stdin=open('input (4).txt')

for tc in range(1,11):
    res = 0
    N = int(input())  # 리스트원소개수
    arr = list(input())  # input받아오는 리스트
    stack = []
    lst = []  # 후위표기법으로 전환한거 담은 리스트
    # icp = {'+': 1, '*': 2}  # 연산자 우선순위
    # 연산자는 스택에 넣음

    for i in range(N):
        if arr[i].isdigit():  # 숫자인 경우, lst에 저장
            lst.append(int(arr[i]))


        else:  # 연산자인 경우
            if arr[i] == '+' and len(stack) == 0:  # 스택 비어있고, + 일 때 stack에 + 추가
                stack.append(arr[i])

            elif len(stack) != 0 and arr[i] == '+':  # 스택이 비어있지 않고, +일때,
                while len(stack)!=0:  #스택이 0이 될때까지 stack에 있는 거 다빼놓고 +를 스택에 넣음
                    lst.append(stack.pop())
                stack.append(arr[i])

            # elif arr[i] == '*':
            #     stack.append(arr[i])
            elif arr[i] == '*'and len(stack) == 0:  # 스택 비어있고, * 일 때 stack에 * 추가
                stack.append(arr[i])
            elif len(stack) != 0 and arr[i] == '*':  # 스택이 비어있지 않고, *일때,
                while len(stack) != 0 and stack[-1]=='*':  #stack에 있는 *은 빼고    *를 스택에 넣음
                    lst.append(stack.pop())
                stack.append(arr[i])

    while len(stack)!=0:     # for문 다 돌았는데 stack에 남아있는 것들 다 빼서 lst에 추가
        lst.append(stack.pop())

    print(*lst)



    # 후위표기법으로 바꾼거 최종 계산하기
    # 숫자(피연산자)를 스택에 넣기
    # 연산자 나오면 피연산자2개를 스택에서 pop하고 연산결과를 다시 스택에 push(pop두번)
    # 수식이 끝나면, 마지막으로 스택을 pop하여 출력

    for i in range(len(lst)):
        if lst[i] == '*':
            a = stack.pop()
            b = stack.pop()
            c = b * a
            stack.append(c)

        elif lst[i] == '+':
            a = stack.pop()
            b = stack.pop()
            c = b + a
            stack.append(c)

        else: #숫자일 경우 스택에 추가
            stack.append(lst[i])
    res = stack.pop()  # 다돌고 맨마지막 스택 빼옴

    print(f'#{tc}', res)







