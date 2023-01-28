# 알고리즘

입력 받기

```python
a = input()
b = input().split()
A = int(input())

a, b = map(int, input().split()) # a=1 , b=2
a, b = input().split()
a = int(a)
b = int(b)
# 띄어쓰기로 나누어 입력값일때
# 1 2
a = list(map(int,input().split())) # a = [1,2]
# 줄바꿈으로 나누어 입력값일때
# 1
# 2
a = [int(input()) for _ in range(9)] # a = [1, 2]

```

입력값 개수가 정해져 있지 않을때

```python
while True:
    try:
        a,b = map(int, input().split())
        print(a+b)
    except:
        break
```

풀면서 많이 사용한 함수 또는 방법

```python
# 개수
{list}.count({해당값})

# 최대 최소
min = min({list})
max = max({list})

# 정렬
# 오름차순
{list}.sort()
# 내림차순
{list}.sort(reverse=True)
# 문자열 길이로 정열
{list}.sort(key=len)

# 문자열 뒤집기
string[::-1]

```
