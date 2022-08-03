# 동적 배열
# 기능 설명

# 아래의 dynamicArray 함수를 완성 하세요.

# dynamicArray 에는 다음 매개변수가 있습니다.
# - int n: 초기화할 빈 배열의 수
# - 문자열 쿼리[q]: 공백으로 구분된 3개의 정수를 포함하는 쿼리 문자열
def dynamicArray(n, queries):
    # Write your code here
    answer = 0
    arr = [[] for i in range(n)]

    a = []

    for q in queries:
        if q[0] == 1:
            idx = (q[1] ^ answer) % n
            arr[idx].append(q[2])

        else:
            idx = (q[1] ^ answer) % n
            temp = q[2] % len(arr[idx])
            answer = arr[idx][temp]
            a.append(answer)
    return a
