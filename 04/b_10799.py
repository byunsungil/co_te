# 10799

import sys

input = sys.stdin.readline

s = input().strip()
stack = []
result = 0

for i in range(len(s)):
    if s[i] == '(':
        stack.append('(')
    else:  # ')'
        stack.pop()
        if s[i-1] == '(':  # 레이저
            result += len(stack)
        else:  # 파이프 끝
            result += 1

print(result)



# 잘려진 조각 개수는 레이저 수 +1
# 레이저는 () 열리고 바로 닫힘
# '(' 스택에 저장하다가 '()'나오면 레이저 카운트 1
# 스택에 있는 '(' 는 파이프 ? ')' 닫히면 파이프 끝?
# 파이프가 끝날때 마다 파이프 안에 있는 레이저 수 카운트?
#  
# (((()(()()))(())())) (()())
#      --|--|--
#    -|---|--|--  -|-
#   --|---|--|-----|---|-
# ----|---|--|-----|---|--  --|--|--
# 24
# 3 4 2 6 6 3
