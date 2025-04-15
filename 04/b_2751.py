import sys

input = sys.stdin.readline

N = int(input())
numbers = set()

for _ in range(N):
    num = int(input())
    numbers.add(num)

numbers = sorted(numbers)

for n in numbers:
    print(n)