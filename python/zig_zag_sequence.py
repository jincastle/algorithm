# 주어진 배열고유한 정수인 경우 배열 요소를 치환하여 배열을 지그재그 시퀀스로 변환합니다. 첫 번째 경우 시퀀스를 지그재그 시퀀스라고 합니다.시퀀스의 요소는 오름차순이며 마지막요소는 내림차순이며, 여기서. 
# 주어진 배열에서 사전식으로 가장 작은 지그재그 시퀀스 를 찾아야 합니다 .
# a = [2,3,5,1,4]
# [1,4,5,3,2]


def findZigZagSequence(a, n):
    a.sort()
    mid = int(n / 2)
    a[mid], a[n-1] = a[n-1], a[mid]

    st = mid + 1
    ed = n - 2
    while(st <= ed):
        a[st], a[ed] = a[ed], a[st]
        st = st + 1
        ed = ed - 1

    for i in range (n):
        if i == n-1:
            print(a[i])
        else:
            print(a[i], end = ' ')
    return

test_cases = int(input())
for cs in range (test_cases):
    n = int(input())
    a = list(map(int, input().split()))
    findZigZagSequence(a, n)
