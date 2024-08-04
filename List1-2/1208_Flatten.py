import sys
sys.stdin = open('input (6).txt')

for tc in range(1,11):
    N = int(input())  # 834 #617
    arr = list(map(int, input().split()))
        # 최대값, 최소값 위치 찾기
    for i in range(len(arr)):
         for j in range(len(arr)-i-1):
             if arr[j]>arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                new_list = arr
                max_value = new_list[-1]
                min_value = new_list[0]


    for _ in range(N):
        for i in range(len(new_list)):
            if new_list[i] >max_value:
                max_value = new_list[i]
                max_value -= 1
            if new_list[i] < min_value:
                min_value = new_list[i]
                min_value += 1



    print(f'#{tc} {max_value-min_value}')











