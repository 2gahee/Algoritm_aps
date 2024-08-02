import sys
sys.stdin = open("sample_input (5).txt", "r")


T= int(input())
for tc in range(1,T+1):
    N=int(input())
    num_list=list(map(int, input().split()))

    result_list = [0]*len(num_list)

    for i in range(0,len(num_list)-1): #주어진 구간중 기준위치 정함
        min_idx=i #기준위치를 일단 최솟값으로 할당
        for j in range(i+1,len(num_list)-1): # 기준값 즉 시작값 제외한 나머지 원소에서 추출
            if num_list[i]>num_list[j]:
                min_idx=j
        num_list[i], num_list[min_idx] = num_list[min_idx], num_list[i]  # 구간의 최솟값을

        Orem_list = num_list

    # print(Orem_list)

    for i in range(0, len(num_list)-1):
        max_idx=i
        for j in range(i+1, len(num_list)):
            if num_list[i]<num_list[j]:
                max_idx=j
        num_list[i], num_list[max_idx] = num_list[max_idx], num_list[i]

        Naerim_list = num_list

    print(Naerim_list)










