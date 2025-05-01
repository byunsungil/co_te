# 2775

T = int(input())  # 테스트 케이스 수 입력

for _ in range(T):
    k = int(input())  # 층수 입력
    n = int(input())  # 호수 입력

    # 0층의 각 호에 대한 초기화
    floor = [i for i in range(1, n + 1)]

    # 1층부터 k층까지 계산
    for _ in range(k):
        for i in range(1, n):
            floor[i] += floor[i - 1]

    print(floor[-1])