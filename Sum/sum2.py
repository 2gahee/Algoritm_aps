import sys

sys.stdin = open('input.txt', 'r')

for tc in range(1, 11):
    T = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]
    max_sum = 0
    dia1_sum = 0
    dia2_sum = 0
    for r in range(100):
        row_sum = 0
        column_sum = 0
        for c in range(100):
            row_sum += arr[r][c]
            column_sum += arr[c][r]
            if max_sum < row_sum:
                max_sum = row_sum
            if max_sum < column_sum:
                max_sum = column_sum

            if r == c:
                dia1_sum += arr[r][c]
                if dia1_sum > max_sum:
                    max_sum = dia1_sum

            if r == (99 - c):
                dia2_sum += arr[r][c]
                if dia2_sum > max_sum:
                    max_sum = dia2_sum

    print(f'#{tc} {max_sum}')
