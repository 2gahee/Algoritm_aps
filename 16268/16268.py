import sys
sys.stdin = open('input1.txt','r')

##함수 없이 푼거
T=int(input())
for tc in range(1,T+1):
    N,M=map(int, input().split())
    arr = [list(map(int, input().split()))for _ in range(N)]
    max_sum=0

    di=[0, -1, 0, 1]
    dj=[1, 0, -1, 0]

    for i in range(N):
        for j in range(M):
            total = arr[i][j]
            for k in range(4):
                ni = i + di[k]
                nj = j + dj[k]
                if 0<= ni <N and 0<= nj <M:
                    total += arr[ni][nj]
                    if total > max_sum:
                        max_sum = total
    print(f'#{tc} {max_sum}')



# ##함수로 푼거
# T=int(input())
# for tc in range(1, T+1):
#     N, M= map(int,input().split())
#     arr= [list(map(int,input().split())) for _ in range(N)]
#     di=[0,1,0,-1]
#     dj=[1,0,-1,0]
#
#     def find_max_sum(N, M, arr):
#         max_sum = 0
#
#         di = [0, -1, 0, 1]
#         dj = [1, 0, -1, 0]
#
#         for i in range(N):
#             for j in range(M):
#                 total = arr[i][j]
#                 for k in range(4):
#                     ni = i + di[k]
#                     nj = j + dj[k]
#                     if 0 <= ni < N and 0 <= nj < M:
#                         total += arr[ni][nj]
#                         if total > max_sum:
#                             max_sum = total
#         return max_sum

#
#     print(find_max_sum(3,5,))