## 외로운 정수
# 하나를 제외한 모든 요소가 두 번 발생하는 정수 배열이 주어지면 고유한 요소를 찾습니다.

# 예시

# 독특한 요소는.

def lonelyinteger(a):
    # Write your code here
    l = set(a)
    for i in l:
        if a.count(i) ==1:
            return i

##인터넷 다른 방법
def lonelyinteger(a):
    result = 0
    for i in a:
        result = result ^ i
    return result
