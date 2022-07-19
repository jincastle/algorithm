# 희소배열
# 입력 문자열 모음과 쿼리 문자열 모음이 있습니다. 각 쿼리 문자열에 대해 입력 문자열 목록에서 발생하는 횟수를 결정합니다. 결과의 배열을 반환합니다.


# 있다'의 사례,의 '' 그리고의 ''. 각 쿼리에 대해 반환 배열에 요소를 추가합니다..

# 기능 설명

# 아래 편집기에서 matchingStrings 기능을 완료하십시오 . 이 함수는 문자열에서 각 쿼리 문자열 의 발생 빈도를 나타내는 정수 배열을 반환해야 합니다 .

# matchingStrings에는 다음 매개변수가 있습니다.

# string strings[n] - 검색할 문자열 배열
# 문자열 쿼리[q] - 쿼리 문자열의 배열
# 보고

# int[q]: 각 쿼리에 대한 결과 배열
# 입력 형식

# 첫 번째 줄은 및 정수를 포함합니다., 의 크기.
# 각각의 다음줄에는 문자열이 포함됩니다..
# 다음 줄에는 다음이 포함됩니다., 의 크기.
# 각각의 다음줄에는 문자열이 포함됩니다..

## 1차로 했는데 속도 문제 발생

# def matchingStrings(strings, queries):
#     # Write your code here
#     a = 0
#     for i in range(len(queries)):
#         for j in range(len(strings)):
#             if queries[i] == strings[j]:
#                 a+=1
#         print(a)
#         a=0


## 2차 시도 속도 문제 발생
# def matchingStrings(strings, queries):
#     # Write your code here
#     for i in queries:
#         print(strings.count(i))

##  3차 시도
##     results = list(0 for i in range(len(queries)))
## 이게 리스트형 변수를 선언할 때 바로 크기를 지정하고 싶을 때 사용하는 코드인데 가장 빠르네 
## 알기 쉽게 말하면 리스트 개수만큼 [0,0,0....] 이렇게 생긴다고 생각하면됨 여기에 for 문돌아갈때 마다 하나씩 증가만 추가하면 됨
def matchingStrings(strings, queries):
    # Write your code here
    results = list(0 for i in range(len(queries)))
    
    for i in range(len(queries)):
        count = 0
        for j in range(len(strings)):
            if queries[i] == strings[j]:
                count += 1
        results[i] = count
    return results