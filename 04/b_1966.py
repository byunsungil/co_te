# 1966

# N = int(input()) # 문서의 개수

# for _ in range(N):
#     d,q = map(int, input().split()) # 문서의 개수, 찾고 싶은 문서가 있는 index
#     r = list(map(int,input().split())) # 중요도

# # q에 있는 문서가 몇번째로 출력되는가?
# result = 0 # 몇번째 카운트용
# findnum = r[q] # 찾는 수의 중요도 초기화

# for i in range(len(r)):
#     if r[i] < max(r):
#         r.append(r[i])# 리스트 맨 마지막에 추가
#         r.pop(0) # 제거
#     if r[i] == max(r):
#         r.pop() # 출력하니까 제거
#         result += 1
#     if findnum == max(r):
#         print(result)


# 1966

# 1966

N = int(input())  # 테스트 케이스 수
outputs = []      # 결과 저장 리스트

for _ in range(N):
    d, q = map(int, input().split())  # 문서 수, 궁금한 문서 위치
    r = list(map(int, input().split()))  # 중요도 리스트

    r = [(i, val) for i, val in enumerate(r)]  # (인덱스, 중요도)
    result = 0

    while r:
        if any(r[0][1] < x[1] for x in r[1:]):
            r.append(r.pop(0))
        else:
            result += 1
            if r[0][0] == q:
                outputs.append(result)
                break
            r.pop(0)  # 내 문서 아니면 제거

# 출력은 마지막에 한 번에
for out in outputs:
    print(out)

