# Caesar Cipher
# 아스키코드 이용
# 암호화 사용
# 카이사르 암호


def caesarCipher(s, k):
    # Write your code here
    result = str()
    for i in range(len(s)):
        a = s[i]
        if (a.islower()):  # 소문자
            result += chr((ord(a) + k - 97) % 26 + 97)
        elif (a.isupper()):  # 대문자
            result += chr((ord(a) + k-65) % 26 + 65)
      # Encrypt lowercase characters in plain text
        else:  # 특수문자
            result += a
    return result


# def caesarCipher(s, k):
#     k = k% 26
#     result:str = '';
#     temp:str = '';
#     for i in s:
#         temp = chr(ord(i) + k)
#         if i <= 'Z' and i >= 'A':
#             if temp > 'Z':
#                 result += chr(ord(temp) - 26)
#             else:
#                 result += temp
#         elif i <= 'z' and i >= 'a':
#             if temp > 'z':
#                 result += chr(ord(temp) - 26)
#             else:
#                 result += temp
#         else:
#             result += i
#             continue
#     return result
