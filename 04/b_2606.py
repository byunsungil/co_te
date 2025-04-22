N = int(input())
c = int(input())

edges = []
for _ in range(c):
    a, b = map(int, input().split())
    edges.append([a, b])

infected = [1]

for _ in range(N):  # 최대 N번만 돌면 충분
    for a, b in edges:
        if a in infected and b not in infected:
            infected.append(b)
        elif b in infected and a not in infected:
            infected.append(a)

print(len(set(infected)) - 1)  # 1번 제외하고 출력
