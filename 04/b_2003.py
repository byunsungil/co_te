# 2003

# 문제
# N개의 수로 된 수열 A[1], A[2], …, A[N] 이 있다. 이 수열의 i번째 수부터 j번째 수까지의 합 A[i] + A[i+1] + … + A[j-1] + A[j]가 M이 되는 경우의 수를 구하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 N(1 ≤ N ≤ 10,000), M(1 ≤ M ≤ 300,000,000)이 주어진다. 다음 줄에는 A[1], A[2], …, A[N]이 공백으로 분리되어 주어진다. 각각의 A[x]는 30,000을 넘지 않는 자연수이다.

# 출력
# 첫째 줄에 경우의 수를 출력한다.

import sys

input = sys.stdin.readline

N, M = map(int,input().split()) # 수열 길이, 합
su = list(map(int,input().split())) # 길이가 N인 수열 입력
count = 0 # 경우의 수 셈
# 연속된 구간의 합이 M이 되야 함
nsum = 0 # 현재 합산 된거
start, end = 0, 0

while True:
    if nsum > M:  
        nsum -= su[start]   # 현재 합이 M 보다 크기 때문에 시작구간을 오른쪽으로 한칸 이동함
        start += 1
    elif end == N:          # 끝 구간이 수열의 길이와 같아지니까 종료
        break
    else:
        nsum += su[end]     # 현재 합이 M 보다 작기 때문에 끝 구간을 오른쪽으로 한칸 이동
        end += 1

    if nsum == M:           # 맞으면 경우의수 + 1
        count += 1


print(count)


