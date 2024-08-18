# Baby-gin

import sys
sys.stdin=open('input10.txt')

T=int(input())
for tc in range(1,T+1):
    arr=list(map(int, input()))#띄어쓰기 아님 주의
    res=0
    count=[0]*12 #list index error방지를 위해12개로 설정
    for i in range(len(arr)):
        count[arr[i]] += 1


    for i in range(10):   #while을 써서 조건문이 만족하는 동안 무한 반복
        while count[i] >= 3:
            res += 1
            count[i] -= 3

        while count[i]>=1 and count[i+1]>=1 and count[i+2]>=1:
            res += 1
            count[i] -= 1
            count[i+1] -= 1
            count[i+2] -= 1

    if res >= 2:
        res=1
    else:
        res=0

    print(f'#{tc}', res)
