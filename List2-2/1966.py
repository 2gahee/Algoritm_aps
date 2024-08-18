import sys
sys.stdin=open('input (9).txt')

T=int(input())
for tc in range(1,T+1):
    N=int(input())
    lst=list(map(int, input().split()))
    # print(lst)

#버블정렬
#겉은 전체 순회, 안에서 끝배열 빼고 남은 부분 순회
    for i in range(len(lst)):
        for j in range(len(lst)-i-1):
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
    print(f'#{tc}', *lst)


