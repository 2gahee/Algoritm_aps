#특별한 정렬
import sys
sys.stdin=open('sample_input (4).txt')
T=int(input())
for tc in range(1, T+1):
    N=int(input())
    arr=list(map(int,input().split()))
    new_arr=[]
    # print(arr)
    arr1=sorted(arr)
    # print(arr1)
    arr2=sorted(arr1, reverse=True)
    # print(arr2)
    for i in range(len(arr)//2):
         new_arr.append(arr2[i])
         new_arr.append(arr1[i])
         if len(new_arr)==10:
            break

    print(f'#{tc}', *new_arr)