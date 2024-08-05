# 회문 : string == string[::-1]
def find_p(N, M, arr):
    for i in range(N): # 행순회
        for j in range(N - M + 1): # 회문의 길이가 M이기 때문
            # 가로 회문 : 시작점 j 부터 M 길이의 회문 슬라이싱
            h = arr[i][j:j+M]
            # 세로 회문
            # v = arr[j:j+M][i] # 틀린 슬라이싱
            v = [arr[k][i] for k in range(j, j+M)]
            # 회문인지 판별!!!
            if h == h[::-1]:
                return h
            if v == v[::-1]:
                return v


T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [list(input()) for _ in range(N)]
    # map(함수, iterable)
    # 우리가 원하는대로 데이터를 가공하기 위해서(함수를 적용해서)
    result = find_p(N, M, arr)
    print(f'#{tc}', ''.join(result))