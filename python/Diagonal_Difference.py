# 정사각 행렬이 주어지면 대각선의 합 사이의 절대 차이를 계산합니다.

# 예를 들어, 정방 행렬아래에 나와 있습니다.
# 1 2 3
# 4 5 6
# 9 8 9  
# 왼쪽에서 오른쪽 대각선 다합한거 15. 오른쪽에서 왼쪽 대각선 다합한거 17. 그들의 절대적인 차이는. 15-17 = 2

# 1차시도
def diagonalDifference(arr):
    a=0
    b=0
    for i in range(len(arr)):
        a +=arr[i][i]
    for j in range(len(arr)):
        b +=arr[j][-(j-1)]

# 2차 시도 하나의 for문으로 변경

def diagonalDifference(arr):
    # Write your code here
    a=0
    b=0
    for i in range(len(arr)):
        a += arr[i][i]
        b += arr[i][-(i+1)]
    answer = abs(a-b)
    return answer

2

