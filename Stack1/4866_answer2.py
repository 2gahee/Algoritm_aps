T = int(input())
for tc in range(1, T + 1):
    N = input()
    stack = []

    # 괄호를 처리하는 부분
    for char in N:
        if char in '({':
            stack.append(char)
        elif char in ')}':
            # 스택이 비어있는 경우
            if not stack:
                ans = 0
                break
            # 괄호 짝 맞추기
            if (char == ')' and stack[-1] == '(') or (char == '}' and stack[-1] == '{'):
                stack.pop()
            else:
                ans = 0
                break
    else:
        # 반복문이 정상적으로 끝났을 때
        if stack:
            ans = 0
        else:
            ans = 1

    print(f'#{tc} {ans}')