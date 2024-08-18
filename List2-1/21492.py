#색칠하기
import sys
sys.stdin=open('sample_input (4).txt')

T=int(input())
for tc in range(1, T+1):
    N=int(input())
    arr=[[0]*10 for _ in range(10)]
    count=0
    for i in range(N):
        x1, y1, x2, y2, color= map(int, input().split())
        # print(x1, y1, x2, y2, color)
        # 주어진 배열들 돌면서 color값 넣기 혹은 color값 더하기
        # color가 1이면 빨강 / 2이면 파랑/3이면 빨+파 파+빨/ 같은색인 영역은 겹치치않는다는 정보가 있으므로 가능
        for i in range(x1,x2+1):
            for j in range(y1, y2+1):
                arr[i][j]+=color
                if arr[i][j]==3:
                    count+=1

    print(f'#{tc}', count)






