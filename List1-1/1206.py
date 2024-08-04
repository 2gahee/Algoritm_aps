import sys
sys.stdin = open('sample_input (1).txt')


####i제외한 4개 건물 중 가장 큰 건물을 4개모두를 비교하는 if문을 써서 뽀아내고 최종적으로 i와 비교
for tc in range(1, 11):
    N = int(input())
    arr = list(map(int, input().split()))
    total=0

    # print(arr)
    for i in range(2,N-2): #i기준으로 양옆 2개의 건물 비교해야하므로 2~N-2
        high_building = arr[i-1]  #if문 이용해  i기준으로 양옆 2개의 건물들 중 제일 큰 건물 찾아냄
        if arr[i-2]> high_building: #일단 i제외한 주변4개 건물중 아무거나 high_building변수에 담기
           high_building = arr[i-2]  #i제외한 주변4개 건물 모두 비교해줌
        if arr[i+1]>high_building:
            high_building = arr[i+1]
        if arr[i+2]>high_building:
            high_building=arr[i+2]  #i제외한 주변4개 건물 모두 비교후 가장 큰 걸 담아놓음

        if high_building< arr[i]: #i기준으로 양옆 2개의 건물들 중 제일 큰 건물이 i보다 작을경우
            total+= arr[i]-high_building

    print(f'#{tc} {total}')
