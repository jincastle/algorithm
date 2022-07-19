# 배열안에 같은 숫자 찾기
# n은 배열 개수
# ar은 배열
# n=9, ar = [10, 20, 20, 10, 10, 30, 50, 10, 20] 일때 2개를 한짝으로 묶은 개수
# 3이 나와야한다

def sockMerchant(n, ar):
    # Write your code here
    count = 0
    l = list(set(ar))
    for i in range(len(l)):
            count +=ar.count(l[i])//2
    return count  


#다른 방법 인터넷
def sockMerchant(n, ar):
    pears = 0
    color = set()
    for i in range(len(ar)):
        if ar[i] not in color:
            color.add(ar[i])
        else:
            pears += 1 
            color.remove(ar[i])
    return pears


def sockMerchant(n, ar):
    countOfSocks = []
    for sock in set(ar):
        countOfSocks.append(ar.count(sock)) 
    return sum([i//2 for i in countOfSocks])


def sockMerchant(n, ar):

    ############## step 1 ################################
    # 초기 dic 설정
    dic = {}
    for i in ar:
        # dic에 i라는 key가 있으면 value에 1을 더해줌
        try :
            dic[i]=dic[i]+1
        # dic에 i라는 key가 없으면 만들어주고 value에 1을 넣어줌
        except :
            dic[i]=1
        # print(dic) # debug
    ############## step 2 ################################
    # pair 개수
    a = 0
    for j in dic:
        # dic의 key가 양말 색 / value가 색의 개수
        # 각 양말 색의 개수를 2로 나눠 몫을 가져와 합한다.
        a = a+dic[j]//2  # value//2 : 몫 , value%%2 : 나머지
        
    return a