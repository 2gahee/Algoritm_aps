#삼성시의 버스노선
import sys
sys.stdin=open('s_input.txt')

T=int(input())
for tc in range(1,T+1):
    N=int(input()) #버스노선 개수
    N_arr=[list(map(int,input().split()))for _ in range(N)]# 각 버스노선의 정류장범위  [[1, 3], [2, 5]]
    P=int(input())#버스정류장 개수
    P_arr=[int(input())for _ in range(P)] # 각 버스 정류장 리스트
    # print(N)
    # print(N_arr)
    # print(P)
    # print(P_arr)
#구해야하는 거 : 각 정류장에 몇개의 버스노선이 다니는지
# 각 정류장에 다니는 버스노선 수를 센 리스트 만들기
#버스노선이 중복해서 다니는 정류장은 count+=1


#외부 루프 (for (start, end) in N_arr) 버스 노선의 범위를 순회하여 각 노선 범위 (start, end)를 처리합니다.
#내부 루프 (for i in range(P))는 각 버스 정류장 번호를 순회하여 P_arr[i]가 현재 버스 노선 범위에 포함되는지를 검사합니다.
#각 버스 정류장 번호가 현재 범위에 포함되면 count_lst에서 해당 인덱스의 값을 증가시킵니다.

    count_lst=[0]*P #각 정류장 개수만큼 리스트 만들어놓음


    for start, end in N_arr: #각 버스 노선의 범위에 대해
        for i in range(P): #각 버스 정류장에 대해
            stop=P_arr[i]

            if start <= stop <= end:   # 정류장이 현재 노선의 범위에 포함되면 카운트 증가
                count_lst[i]+=1




    print(f'#{tc}', *count_lst)

