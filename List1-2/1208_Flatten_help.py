import sys
sys.stdin = open('input (6).txt')

for tc in range(1,11):
    N = int(input())
    arr=list(map(int, input().split()))
    # print(f'#{tc} {arr}')
    for _ in range(N):
        max_idx=0
        min_idx=0
        for i in range(len(arr)):
            if arr[i]>arr[max_idx]:
                max_idx=i
            elif arr[i]<arr[min_idx]:
                min_idx=i

        arr[max_idx]-=1
        arr[min_idx]+=1

    for i in range(len(arr)):
        if arr[i] > arr[max_idx]:
            max_idx = i
        elif arr[i] < arr[min_idx]:
            min_idx = i

    print(f'#{tc} {arr[max_idx] - arr[min_idx]}')