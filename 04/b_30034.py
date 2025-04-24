# 30034

import sys
input = sys.stdin.readline

sep = set()
bkl = set()

# 문자 구분자 입력
N = int(input())
for _ in range(N):
    sep.add(input().strip())

# 숫자 구분자 입력
M = int(input())
for _ in range(M):
    sep.add(input().strip())

# 병합자 입력
K = int(input())
for _ in range(K):
    bkl.add(input().strip())

# 최종 구분자: 병합자를 제거한 문자/숫자 구분자
sep_f = sep - bkl

# 문자열 입력
S = int(input())
stc = input().strip()

result = []
for ch in stc:
    if ch in sep_f or ch == ' ':  # 공백도 항상 구분자로 처리
        if result:
            print(''.join(result))
            result.clear()
    else:
        result.append(ch)

# 마지막 조각 출력
if result:
    print(''.join(result))
