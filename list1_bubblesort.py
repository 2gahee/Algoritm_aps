N=6
arr=[7,2,5,3,4,1]

for i in range (N-1, 0, -1):
    for j in range(i):
        if arr[j] > arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]  #왼쪽 원소가 더 크면 교환
print(*arr)