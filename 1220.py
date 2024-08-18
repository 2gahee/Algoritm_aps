#1220 Magnetic
import sys
sys.stdin=open('input (9).txt')
#파란색(2)를 찾은 후 이전값(pre)가 빨간색(1)이면 교착상태
for tc in range(1,11):
    N=int(input())
    arr=[list(map(int,input().split()))for _ in range(N)]
    # print(arr)
    res=0
    #열을 탐색해야하므로 전치행렬로 바꿔서 행 탐색
    arr_t=list(zip(*arr)) #전치행렬로 바꿈(전치행렬에서의 행이 기존행열의 열임)
    for lst in arr_t: #행단위로 처리
        pre=0 #직전값
        for n in lst:
            if n==1 or n==2: #0일때는 볼 필요 없음
                if n==2 and pre==1:  #교착
                    res+=1
                pre=n

    print(f'#{tc}', res)