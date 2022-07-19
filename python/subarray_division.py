# 참조 https://chips556.medium.com/hackerrank-subarray-division-illustrated-solution-fe34d4c38b36

# 리스트 s가 주어진다
# 앞에서 부터 순서대로 m길이 만큼 잘라서 더한후 값이 d와 같으면 count를 1더해준다
# 그리고 최종적으로 count를 출력해준다

#1차 시도 실패
def birthday(s, d, m):
    count = 0
    for i in range(len(s)):
        if sum(s[i:m]) == d:
            count +=1
    return count

#2 차 수정
# 슬라이스 이동까지 생각을 못함
def birthday(s, d, m):
    count = 0
    for i in range(len(s)):
        if sum(s[i:i+m]) == d:
            count +=1
    return count








#다른 정답
def birthday(s, d, m):
    return sum([1 for i in range(len(s)-m+1) if sum(s[i:i+m])==d])

#다른정답
def birthday(s, d, m):
    ans = 0
    for i in range(n-m+1):
        if (sum(s[i:i+m]) == d):
            ans += 1
    return ans

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = list(map(int, input().rstrip().split()))

    first_multiple_input = input().rstrip().split()

    d = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    result = birthday(s, d, m)

    fptr.write(str(result) + '\n')

    fptr.close()