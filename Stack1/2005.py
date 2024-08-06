def pascal(N):
    stack = [1] # 첫 번째 스택의 원소는 1로 초기화

    for row in range(N):
        print(*stack) # 현재 줄(행) 출력
        new_stack = [1] # 새로운 행 첫 번째 원소도 1로 초기화

        while len(stack) > 1:
            a = stack.pop() # stack 에서 제거
            b = stack[-1] # top요소는 stack에서 꺼내지는 않음
            new_stack.append(a + b) # 새로운 요소 계산 및 추가

        new_stack.append(1) # 마지막 요소도 1추가
        # code.....
        stack = new_stack # 새로운 스택 갱신

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    print(f'#{tc}')
    pascal(N)

