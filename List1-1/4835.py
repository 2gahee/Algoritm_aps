import sys
sys.stdin=open('sample_input (2).txt')

T=int(input())
for tc in range(1, T+1):
    N, M= map(int, input().split())
    lst= list(map(int, input().split()))
    min_sum=float('inf') #최솟값의 초깃값은 최대한 크게
    max_sum=float('-inf') #최댓값의 초깃값은 최대한 작게
    res=0 #결과값 tc돌때마다 초기화

    # 이웃한 M개의 수의 합을 계산
    for i in range(N-M+1):  #예시 i, i+1, i+2를 구하는데 인덱스범위에러안나려면 N-M+1# 각 i는 이웃한 M개의 원소를 포함할 수 있는 시작 인덱스로 즉 해당예시에서는 3
       current_sum = 0
       for j in range(M):
           current_sum+=lst[i+j]

       if min_sum > current_sum:
          min_sum = current_sum
       if max_sum < current_sum:
          max_sum = current_sum

    res = max_sum - min_sum

    print(f'#{tc} {res}')