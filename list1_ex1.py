# 3
# 5
# 477162 658880 751280 927930 297191
# 5
# 565469 851600 460874 148692 111090
# 10
# 784386 279993 982220 996285 614710 992232 195265 359810 919192 158175
#
# 1 630739
# 2 740510
# 3 838110
T = int(input())  #테스트케이스 개수
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    max_v = arr[0]
    for i in (1, N):
        if max_v < arr[i]:
            max_v = arr[i]
    min_v = arr[0]
    for i in (1, N):
        if min_v > arr[i]:
            min_v = arr[i]

result = (max_v - min_v)
print(result)