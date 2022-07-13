# 두개의 순열 조합

# 기능 설명

# 아래 편집기에서 twoArrays 함수를 완성 하세요. YES또는 문자열을 반환해야 합니다 NO.

# twoArrays에는 다음 매개변수가 있습니다.

# int k: 정수
# int A[n]: 정수 배열
# int B[n]: 정수 배열

def twoArrays(k, A, B):
    # Write your code here
    A.sort(reverse=True)
    B.sort()
    for i in range(len(A)):
        if (A[i] + B[i] < k):
            return "NO"

    return "YES"
