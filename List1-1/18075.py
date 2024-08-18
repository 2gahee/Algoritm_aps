import sys
sys.stdin = open('input.txt')

T=int(input())
for tc in range(1,T+1):
    N=int(input())
    N_arr=list(map(int,input().split()))
    # print(N_arr)
    # i는 기준값, j는 i기준으로 오른쪽에 있는 배열들을 모두 순회하며 i보다 높거나 같은값이 있을 때마다 1씩 빼줌
    max_h=float('-inf')
    for i in range(N):
        res= N - i -1 # 나올수 있는 최댓값
        for j in range(i+1,N):  #i는 기준값, j는 i기준으로 오른쪽에 있는 배열들을 모두 순회
            if N_arr[i] <= N_arr[j]:
                res -= 1
        if res > max_h:
            max_h = res

    print(f'#{tc} {max_h}')
