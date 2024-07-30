# 3
# 5
# 477162 658880 751280 927930 297191
# 5
# 565469 851600 460874 148692 111090
# 10
# 784386 279993 982220 996285 614710 992232 195265 359810 919192 158175

T = int(input())

for testcase in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))

    Max_v = arr[0]
    for i in range(1, N):
        if Max_v < arr[i]:
            Max_v = arr[i]

    Min_v = arr[0]
    for i in range(1, N):
        if Min_v > arr[i]:
            Min_v = arr[i]

    print(f'#{testcase} {Max_v - Min_v}')