import sys
sys.stdin=open('sample_input (2).txt')

T=int(input())
for tc in range(1, T+1):
    N, M= map(int, input().split())
    lst= list(map(int, input().split()))
    min_sum=0
    max_sum=0
    res=0
    # print(N, M)
    # print(*lst)
    #버블 정렬을 활용해 오름차순 정리후 앞에서부터 M개 더하면 최솟값 뒤에서 부터M개 더하면 최댓값
    #내가 원래 쓰던대로 for문 한번만 쓰면 전체가 정렬되지 않고 1번만 정렬되어 제일 큰수만 뒤로 가있고 앞에는 정렬이 안되어있음.
    # 버블 정렬 써줘야 오름차순으로 정리됨.
    for i in range(N):
        for j in range(N-i-1):   #버블정렬은 1회차 끝나면 뒤에 큰 숫자 정렬됨, 이제 고려할 필요x
            if lst[j]>lst[j+1]:  #Range index에러 안나려고 N-i-1 (정렬된 원소 i제외하고 -1해줌)
                lst[j], lst[j+1] = lst[j+1], lst[j]
    # print(lst)
    for i in lst[0:M]: # 리스트의 처음부터 M개의 원소를 더하는 부분
        min_sum += i
    # print(min_sum)

    for i in lst[-M:]: # 리스트의 뒤에서부터 M개의 원소를 더하는 부분
        max_sum += i
    # print(max_sum)
    res= max_sum - min_sum

    print(f'#{tc} {res}')

