#숫자를 정렬하자
import sys
sys.stdin=open('input (8).txt')

T=int(input())
for tc in range(1, T+1):
    N=int(input())
    lst=list(map(int, input().split()))
    # print(*lst)
    # 오름차순정렬 버블정렬이용
    #외부 루프: 전체 배열을 순회. 매 반복마다 가장 큰 원소가 배열의 끝으로 이동
    #내부 루프: 현재 패스에서 정렬되지 않은 부분의 원소들을 비교하고 교환
    #i는 패스(혹은 반복)의 수. 총 N번 반복. 이 때, 매번 반복할 때마다 하나씩 정렬된 부분이 배열의 끝쪽으로 이동
    #j는 현재 패스에서 비교할 인덱스, N - i - 1은 j의 범위를 결정

    for i in range(N): #외부 루프: 전체 배열을 순회. 매 반복마다 가장 큰 원소가 배열의 끝으로 이동
        for j in range(0,N-i-1): #배열끝에서 이미 정렬되 부분 제외하고 남은 부분 순회#j+1인덱스범위맞추기위해 -1
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1] ,lst[j]
    print(f'#{tc}', *lst)