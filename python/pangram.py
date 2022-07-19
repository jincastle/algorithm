# 팬그램 은 알파벳의 모든 문자를 포함하는 문자열입니다 . 
# 주어진 문장이 영어 알파벳의 팬그램인지 판단합니다. 대소문자를 무시합니다. pangram또는 not pangram적절하게 반환합니다 .
# 팬그램 = 모든 알파벳 문자 사용해서 만든 언어
# 
from string import ascii_lowercase
 
def pangrams(s):
    # Write your code here
    s1 = list(s.lower())
    a = list(ascii_lowercase)
    for i in s1:
        if i in a:
            a.remove(i)
    if len(a) ==0:
        return "pangram"
    else:
        return "not pangram"