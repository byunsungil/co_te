# 15829

# ord : ASCII 코드 함수, ord('a')


import sys

input = sys.stdin.readline

L = int(input())
word = input().strip()

def H(word):
    r = 31
    result = 0
    M = 1234567891
    for i in range(L):
        num = ord(word[i]) - ord('a') + 1 # 알파벳 숫자
        result = (result + num * r ** i) % M
    return result

print(H(word))

    