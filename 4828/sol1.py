'''
input_arr : 입력 배열(0-k)
countung_arr: 카운팅 배열
k는 데이터의 개수가 아닌, 데이터의 원소 범위
'''

def counting_sort(arr, k):
    counting_arr = [0] * (k+1)  # 카운팅 배열 // k는 데이터의 원소범위

# 1. counting_arr 에  input_arr내 원소의 빈도수 담기
    for i in range(len(arr)):  # input_arr 만큼 순회 // input_arr의 원소 하나씩 꺼내기
        counting_arr[input_arr[i]] += 1  #counting_arr[0],counting_arr[4],


# 2. 누적 counting_arr 업데이트 -> 내 앞에 몇개?
    for i in range(1, len(counting_arr)):
        counting_arr[i] += counting_arr[i-1] # counting_arr[1] =+ counting_arr[0]

# 3. result_arr 초기화: 정렬된 결과
    result_arr = [-1] * len(arr)
    print(result_arr)

# 4. result_arr 에 정렬하기 (counting_arr 를 참조할 것이다.) [0 4 1 3 1 2 4 1]
    for i in arr:  # arr는 순회가능한 iterable한 객체 -> 컬렉션
        counting_arr[i] -= 1     # 0 4 1 3 .....: counting_arr의 해당 원소 값 하나 줄인다.
        result_arr[counting_arr[i]] = i  # result_arr에 counting_arr의 해당 요소를 넣느다.


input_arr = [0, 4, 1, 3, 1, 2, 4, 1] # 정렬할 target
print(counting_sort(input_arr, 5))