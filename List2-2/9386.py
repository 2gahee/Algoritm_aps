import sys
sys.stdin=open('input1.txt')

T=int(input())
for tc in range(1,T+1):
    N=int(input())
    N_arr = list(map(int,input()))
    # print(N_arr)

    count=0
    count_list=[]
    max_count=float('-inf')
    for i in range(len(N_arr)):
        if N_arr[i]==1:
            count+=1
        if N_arr[i]==0:
            count_list.append(count)
            count=0

        if count > max_count:
            max_count = count


    print(f'#{tc} {max_count}')