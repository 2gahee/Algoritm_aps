#2001 파리퇴치
import sys
sys.stdin=open('input (9).txt')

T=int(input())
for tc in range(1,T+1):
    N, M = map(int,input().split())# 전체 배열(N_arr)과 파리채 배열(M_arr)의 크기를 입력받는다.
    N_arr= [list(map(int, input().split()))for _ in range(N)] #전체 배열 리스트

    M_arr = [[0]*M for _ in range(M)] #파리채 리스트
    # print(N,M)
    # print(N_arr)
    # print(M_arr)


    max_sum = float('-inf')
# 파리채배열의 0,0을 기준으로 잡고, 전체배열에서 파리채배열의 기준이 갈 수 있는 범위를 순회
    # 파리채 배열의 상단 왼쪽이 전체 배열에서 위치할 수 있는 범위를 순회
    for i in range(0, N-M+1):
        for j in range(0,N-M+1):
            # 현재 위치(i, j)에서 파리채 배열을 놓았을 때의 모기 수를 계산한다.

            M_sum = 0
            for k in range(M):
                for h in range(M):
                    # 현재 위치(i+k, j+h)에서 모기 수를 더한다
                    M_sum += N_arr[i+k][j+h]   # M_arr이 아닌 N_arr의 값을 써야함
 #N_arr[i + k][j + h]는 현재 파리채 배열의 위치에서 모기 수를 접근합니다.
                    # i와 j는 파리채의 상단 왼쪽 좌표, k와 h는 파리채 배열 내에서의 상대적 좌표

                    if M_sum > max_sum:
                        max_sum = M_sum

    print(f'#{tc} {max_sum}')