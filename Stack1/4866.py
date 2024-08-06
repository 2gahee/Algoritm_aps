import sys
sys.stdin = open('sample_input (1).txt','r')



T=int(input())
for tc in range(1,T+1):
    N=input()
    # print(N)
    # 1.왼족 괄호의 개수와 오른쪽 괄호의 개수가 같아야 한다.
    # 2.같은 괄호에서 왼쪽 괄호는 오른쪽 괄호보다 먼저 나와야 한다.
    # 3.괄호 사이에는 포함 관계만 존재한다.
    stack=[]
    char1='('
    char2=')'
    char3='{'
    char4='}'
    char5='['
    char6=']'
    stack_count=[]
    stack_count1 = 0
    stack_count2 = 0
    stack_count3 = 0
    stack_count4 = 0
    stack_count5 = 0
    stack_count6 = 0
    # print('{} {}'.
    for char in N:
        if char==char1 or char==char2 or char==char3 or char==char4 or char==char5 or char==char6:
           stack.append(char)


    # for char in stack:
    #      if char==char1:
    #          stack_count1 += 1
    #
    #      if char==char2:
    #          stack_count2+=1
    #
    #      if char==char3:
    #          stack_count3+=1
    #
    #      if char==char4:
    #          stack_count4+=1
    #
    #      if char==char5:
    #          stack_count5+=1
    #
    #      if char==char6:
    #          stack_count6+=1
    #
    # stack_count.append(stack_count1)
    # stack_count.append(stack_count2)
    # stack_count.append(stack_count3)
    # stack_count.append(stack_count4)
    # stack_count.append(stack_count5)
    # stack_count.append(stack_count6)

    # print(stack_count)
    #

    if stack_count[0]==stack_count[1] and stack_count[2]==stack_count[3] and stack_count[4]==stack_count[5]
         ans=1
    else:
         ans=0

    print(f'#{tc} {ans}')
