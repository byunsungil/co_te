# 2108

# 수를 처리하는 것은 통계학에서 상당히 중요한 일이다. 통계학에서 N개의 수를 대표하는 기본 통계값에는 다음과 같은 것들이 있다. 단, N은 홀수라고 가정하자.

# 산술평균 : N개의 수들의 합을 N으로 나눈 값
# 중앙값 : N개의 수들을 증가하는 순서로 나열했을 경우 그 중앙에 위치하는 값
# 최빈값 : N개의 수들 중 가장 많이 나타나는 값
# 범위 : N개의 수들 중 최댓값과 최솟값의 차이
# N개의 수가 주어졌을 때, 네 가지 기본 통계값을 구하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 수의 개수 N(1 ≤ N ≤ 500,000)이 주어진다. 단, N은 홀수이다. 그 다음 N개의 줄에는 정수들이 주어진다. 입력되는 정수의 절댓값은 4,000을 넘지 않는다.

# 출력
# 첫째 줄에는 산술평균을 출력한다. 소수점 이하 첫째 자리에서 반올림한 값을 출력한다.

# 둘째 줄에는 중앙값을 출력한다.

# 셋째 줄에는 최빈값을 출력한다. 여러 개 있을 때에는 최빈값 중 두 번째로 작은 값을 출력한다.

# 넷째 줄에는 범위를 출력한다.


import sys

input = sys.stdin.readline

N = int(input())

number = []

for _ in range(N):
    num = int(input())
    number.append(num) 

def mean(number):
    r1 = int(round(sum(number)/N,0)) # round() 함수는 소수점 첫째 자리에서 반올림
    return r1

def median(number):
    number.sort()
    m = len(number) // 2
    r2 = number[m]
    return r2

def mode(number):
    count = {} # 빈 딕셔너리 생성 
    for i in number: # number 리스트에서 하나씩씩
        if i in count: 
            count[i] += 1 # i가 count에 있으면 키:i 값을 1 증가 중복되면 증가함
        else:
            count[i] = 1 # i가 count에 없으면 키:i 값을  하나만 있으면 1임
    max_count = max(count.values()) # count의 값 중에서 최댓값을 구함
    mode_list = [] # 최빈값을 저장할 리스트 생성
    for key, value in count.items():
        if value == max_count:
            mode_list.append(key)
    mode_list.sort()
    if len(mode_list) > 1:  # 최빈값이 여러 개일 경우
        r4 = mode_list[1]   # 두 번째로 작은 값을 출력
    else:
        r4 = mode_list[0]  # 최빈값이 하나일 경우 제일 작은 값을 출력
    return r4



def range(number):
    r3 = max(number) - min(number)
    return r3

print(mean(number))
print(median(number))
print(mode(number))
print(range(number))