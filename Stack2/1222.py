import sys
sys.stdin=open('input (2).txt')

for tc in range(1,11):
    res=0
    N=int(input()) #리스트원소개수
    arr= list(input())  #input받아오는 리스트
    stack=[]
    lst=[] #후위표기법으로 전환한거 담은 리스트
   ## 후위표기법으로 변환
    #연산자를 스택에 넣고
    #피연자는 후위표기법 리스트에 그냥 담음
    for i in range(len(arr)):
        if arr[i]=='+' and len(stack)==0:  #스택 비어있고, + 일 때 stack에 + 추가
           stack.append(arr[i])

        elif arr[i].isdigit():  # 숫자라면 lst에 저장
            lst.append(int(arr[i]))


        elif len(stack) != 0 and arr[i]=='+': #스택이 비어있지 않고, +일때, stack에서 빼서 lst에 추가하고 다시 stack에 추가
            lst.append(stack.pop())
            stack.append(arr[i])
    lst.append(stack.pop()) # #다 돌고 스택에 남은 + 빼와서 lst에 추가 맨마지막 +
    # print(stack) #스택 비어있는 지 확인
    # print(lst) #후위표기법으로 잘 바꼈는 지 확인

##후위표기법의 수식을 스택사용해 계산
#피연산자를 스택에 넣기
#연산자 나오면 피연산자2개를 스택에서 pop하고 연산결과를 다시 스택에 push(pop두번)
#수식이 끝나면, 마지막으로 스택을 pop하여 출력


    for i in range(len(lst)):
        if lst[i]=='+':
            a = stack.pop()
            b = stack.pop()
            c = a + b
            stack.append(c)
        else :
            stack.append(lst[i])
    res=stack.pop() #다돌고 맨마지막 스택 빼옴


    print(f'#{tc}', res)
