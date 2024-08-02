import sys
sys.stdin = open('input (3).txt', 'r')

T=int(input())
for tc in range(1,T+1):
    N=list(input())
    # print(N)
    reverse_N=N[::-1]
    if reverse_N == N:
        res=1
    else:
        res=0

    print(f'#{tc} {res}')
