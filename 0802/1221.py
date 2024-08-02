import sys
sys.stdin = open('GNS_test_input.txt','r')

T=int(input())
for tc in range(1,T+1):
    testcase, str1 = map(str,input().split())   # 1 7041 #2 7778 를 받아옴
    alpha_list=['ZRO','ONE','TWO','THR','FOR','FIV','SIX','SVN','EGT','NIN']
    input_list=list(map(str, input().split()))  # 띄어쓰기 기준으로 하나씩 요소를 받아와서 리스크로 만듬


    # new_list는 숫자로 바꿔놓은 리스트
    for i in range(len(input_list)):  # 입력값을 순회해서 받고 alpha_list와 비교하여
        for j in range(len(alpha_list)): # 값이 같으면 해당값을 인덱스로 바꿈
            if input_list[i]==alpha_list[j]: # alpha_list의 인덱스가 해당 숫자와일치
                 input_list[i]=j  #alpha_list에 순서대로 넣어놨기에 인덱스가 곧 숫자
                 new_list=input_list
    # print(new_list)

    # new_list 숫자를 오름차순 정렬함
    for i in range(len(new_list)-1,0,-1):  #버블정렬을 이용한 오름차순정리
        for j in range(0,i):
            if new_list[j] > new_list[j+1]:
                new_list[j], new_list[j+1] = new_list[j+1], new_list[j]
    # print(new_list)

    # res_list는 오름차순 해놓은 숫자 new_list를 다시 영문으로 바꿈
    for i in range(len(new_list)):  #입력값을 순회해서 받고 alpha_list와 비교하여
        for j in range(len(alpha_list)): #값이 같으면 해당값을 인덱스로 바꿈
            if new_list[i]==j: # new_list가 alpha_list의 인덱스와 같으면
               new_list[i]=alpha_list[j]  #new_list에 alpha_list값 할당
               res_list=new_list
    print(testcase)
    print(*res_list) #리스트를 언팩해서 출력

    # for i in range(len(Num_list)):
    #     if Num_list[i]== 'ZRO':
    #         Num_list[i] = 0
    #     elif Num_list[i]== 'ONE':
    #         Num_list[i] = 1
    #     elif Num_list[i] == 'TWO':
    #         Num_list[i] = 2
    #     elif Num_list[i]== 'THR':
    #         Num_list[i] = 3
    #     elif Num_list[i]== 'FOR':
    #         Num_list[i] = 4
    #     elif Num_list[i] == 'FIV':
    #         Num_list[i] = 5
    #     elif Num_list[i] == 'SIX':
    #         Num_list[i] = 6
    #     elif Num_list[i] == 'SVN':
    #         Num_list[i] = 7
    #     elif Num_list[i] == 'EGT':
    #         Num_list[i] = 8
    #     elif Num_list[i] == 'NIN':
    #         Num_list[i] = 9

