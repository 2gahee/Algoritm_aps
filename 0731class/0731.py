# N = int(input)
# arr = [list(map(int, input().split()))for _ in range(N)] # 2차원 배열 (일반적인 순회에서는 _ 많이 씀)


# 0으로 채워진 상태로 배열 준비하는 법
arr1 = [0] * 3  # 1차원 3칸짜리 배열
arr2 = [[0] * 3 for _ in range(2)]   # 2차원(=2행짜리)(0으로 채워진 1차원배열을 반복해서 생성)
# print(arr1)
# print(*arr1)  # 언팩해서 출력

# for i in range(2):
#     print(arr2[i])

# for i in range(2): #2행
#     for j in range(3): #3열
#         print(arr2[i][j], end=' ')  #총 6개의 원소 나옴
#         print() #한줄씩 띄어쓰기
#arr2[][]: 원소에 접근
#arr2[0]:한 행에 접근 한 줄 가져옴/ 0번행가져옴
#arr2[*0]:한 행에 접근 한 줄 가져오는데 언팩해서0 가져옴/ 한줄을 가져왔기에 언팩가능

#배열순회
# n*m 배열의 n*m개의 모든 원소를 빠짐없이 조사하는 방법
# i는 행
# j는 열
#행우선순회: 행을 먼저 결정하고 행을 우선해서 순회


max_v=o #최댓값 구하기 위한 초기화(음수가 포함되어 있을때는 0으로 초기화하면 안됨,  문제에 맞는 적절한 ㅈ초깃값 렂어)
for i in range(n):  #행
    S=0 #한 행의 합을 구해 max_v와 비교 #한 행이 결정되고 나면 일단 초기화
    for j in range(m):  #열    # 결정된 한 행의 열에 접근
        f(array[i][j])
        S += A[i][j] # 원소의 합
       #행의 합 중 최댓값(결과적으로 2차원 모든 원소에 접근해야함)
        if max_v <s:
            # 이런식으로 작성
print(max_v)





#열 우선 순회: 열을 먼저
for j in range(m):  #행
    for i in range(n):  #열
        f(array[i][j])
        S +=A[i][j] # 원소의 합
        #행의 합 중 최댓값(결과적으로 2차원 모든 원소에 접근해야함)
 print(max_v)


#low 행 가로로, 1차원 한 줄
#column 열 세로


arr = [[1,2,3], [4,5,6]] # 2행 3열   //1행 123 2행456
print(len(arr)) #차원
print(len(arr[0])) #0행의 원소개수 즉 열 수


for i in range(n):  #행
    S=0 #한 행의 합을 구해 max_v와 비교 #한 행이 결정되고 나면 일단 초기화
    for j in range(m):  #열    # 결정된 한 행의 열에 접근
        f(array[i][j])
        f(array[j][i])  #행열 둘다...


##델타를 이요한 2차 배열 탐색




