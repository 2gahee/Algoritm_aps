import sys
from pprint import pprint
sys.stdin=open('input (2).txt')

memo=[]
ls=[]
T=int(input())
for tc in range(1,T+1):
    ls.append(int(input()))
n=max(ls)

for i in range(n):
    arr = [0] * (i+1)
    arr[0] = 1
    for j in range(1, i+1):
        if i == j:
            arr[j] = 1
        else: arr[j] = memo[i - 1][j - 1] + memo[i - 1][j]
    memo.append(arr)


#
# for line in memo:
#      print(*line)

# for line in memo:
#      for ele in line:
#          print(ele, end=' ')
#      print()


for i in range(len(ls)):
     N = ls[i]
     print(f'#{i+1}')
     for j in range(N):
         print(*memo[j])








