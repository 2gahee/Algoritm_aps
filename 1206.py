for tc in range(1, 11):
    N = int(input('N입력'))
    arr = list(map(int, input().split()))

    for i in range(0, N):
        new_list = arr[i: i+5] `
        # BubbleSort (new_list를 버블정렬)
        for j in range(i+4, i-1, -1):  # 범위의 끝 위치
            for h in range(0, j):   # 비교할 왼쪽 원소
                if new_list[h] > new_list[h+1]:
                    new_list[h], new_list[h+1] = new_list[h+1], new_list[h]
                    print(new_list)


        # if (arr[i]-arr[i-1] > 0) & (arr[i]-arr[i-2] > 0) & (arr[i]-arr[i+1] > 0) & (arr[i]-arr[i+2] > 0) :




    # print(f'#{tc} ')