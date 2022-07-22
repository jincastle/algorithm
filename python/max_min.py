# n개의 값을 가진 배열 arr에서 k개만큼 값을 선택했을 때 Max(arr) - Min(arr) 값이 가장 작은 경우의 값을 출력하는 문제이다.

# 배열을 정렬한 후에 각 배열간의 차이를 구한 배열을 만들고, Queue처럼 한칸씩 움직이며 Min값을 체크하는 식으로 구현하였다.
def maxMin(k, arr):
    arr.sort()
    diff = []
    unfairness = 0
    min = sys.maxsize

    for i in range(len(arr)-1):
        diff.append(arr[i+1] - arr[i])

    for i in range(k-1):
        unfairness += diff[i]

    min = unfairness

    for i in range(k-1, len(diff)):
        unfairness -= diff[i-(k-1)]
        unfairness += diff[i]

        if min > unfairness:
            min = unfairness

    return min
