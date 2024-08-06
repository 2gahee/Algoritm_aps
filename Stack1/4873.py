T=int(input())
for tc in range(1,T+1):
    string = input()
    stack=[]


    for str in string:  # 문자열 순회
        if str not in stack:  #문자가 리스트에 없으면 추가
            stack.append(str)
        elif str in stack and str != stack[-1]: # 혹은 문자가 리스트에 있으나 바로 이전 문자랑 다르면 추가
            stack.append(str)
        elif str == stack[-1]: # 문자가 리스트내 바로 직전 문자와 같으면  넣지 않고, 직전 문자 반환
            stack.pop()

        total = 0
        for i in range(len(stack)):
            total += 1


    print(f'#{tc} {total}')
