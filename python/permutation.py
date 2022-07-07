#문제설명
#길이가 n인 배열에 1부터 n까지 숫자가 중복 없이 한 번씩 들어 있는지를 확인하려고 합니다. 1부터 n까지 숫자가 중복 없이 한 번씩 들어 있는 경우 true를, 아닌 경우 false를 반환하도록 함수 solution을 완성해주세요.

#제한사항

#배열의 길이는 10만 이하입니다.
#배열의 원소는 10만 이하의 자연수입니다.

# 체크 방식 이용
def solution(arr):
    # 1에서 n까지 모든 수가 옳은 위치에 있는지 확인해줄 check 배열을 만듦. 0 없음. 1 있음
    check = [0 for i in range(100000)] # 배열의 최대 길이가 1부터 최대 10만

    for i in arr: # arr안의 숫자를 모두 순회 하며
        check[i - 1] += 1 # arr의 숫자에 맞는 인덱스에 1을 넣어줌

        for j in range(len(arr)):
            if (check[j] > 1 or check[j] == 0):
                return False

            return True

# 정렬 방식이
def solution(arr):
    arr.sort()
    for i in range(len(arr)):
        if(i + 1 != arr[i]):
            return False

        return True
