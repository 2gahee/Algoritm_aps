# 파일에서 입력받기
# import sys
# sys.stdin = open('1208_input.txt','r')
# sys.stdout = open('1208_output.txt','w')

# 주어진 상자들을
# 정해진 횟수만큼 덤프하고
# 최고점과 최저점의 높이를 반환
# 총 테스트 케이스는 10개
for tc in range(1,11):
    N = int(input())
    boxes = list(map(int,input().split()))
    #입력을 받았으면 제대로 받았는지 확인하기
    # print(boxes)
    # 덤프의 횟수만큼 최대값 위치에서 -1, 최소값 위치에서 +1
    for _ in range(N):
        # 최대값, 최소값 위치 찾기
        max_index = 0
        min_index = 0
        # boxes 처음부터 끝까지 한 번씩 보기
        for i in range(100):
            # boxes[i] 현재 살펴보고 있는 box 높이
            # boxes[max_index] 여태까지 알고 있는 제일 높은 box 높이
            if boxes[i] > boxes[max_index]:
                max_index = i
            elif boxes[i] < boxes[min_index]:
                min_index = i
        # 최고높이 위치와 최저 높이 위치를 찾음!
        boxes[max_index] -= 1
        boxes[min_index] += 1

    max_index = 0
    min_index = 0

    # boxes 처음부터 끝까지 한 번씩 보기
    for i in range(100):
        # boxes[i] 현재 살펴보고 있는 box 높이
        # boxes[max_index] 여태까지 알고 있는 제일 높은 box 높이
        if boxes[i] > boxes[max_index]:
            max_index = i
        elif boxes[i] < boxes[min_index]:
            min_index = i

    print(f'#{tc} {boxes[max_index]-boxes[min_index]}')








