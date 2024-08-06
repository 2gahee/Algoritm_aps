import sys
sys.stdin = open('sample_input (1).txt','r')

T=int(input())
for tc in range(1,T+1):
    N=input()
    # 1.왼족 괄호의 개수와 오른쪽 괄호의 개수가 같아야 한다.
    # 2.같은 괄호에서 왼쪽 괄호는 오른쪽 괄호보다 먼저 나와야 한다.
    # 3.괄호 사이에는 포함 관계만 존재한다.
    stack=[]

    for char in N:
        if char=='(' or char=='{' or char=='}' or char==')':
           stack.append(char)

        # print(stack)
        b_stack=[]
        for char in stack:

            if char=='(' or char=='{':
                b_stack.append(char)

            elif len(b_stack)==0:  #처음에 }가 들어왔을 때
                ans= 0
                break

            else:
                if char==')' and b_stack[-1]=='(':
                    b_stack.pop()
                else:
                    ans=0
                if char=='}' and b_stack[-1]=='{':
                    b_stack.pop()
                else:
                    ans=0


    # print(b_stack)
    if b_stack:
        ans=0
    else:
        ans=1
    print(f'#{tc} {ans}')