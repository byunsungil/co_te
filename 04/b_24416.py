    # 24416

n = int(input())

def fibonacci(n):
    cnt = 0
    f = [0] * (n+1)
    f[1] = f[2] = 1
    for i in range(3, n+1):
        f[i] = f[i-1] + f[i-2]
        cnt += 1
    return f[n], cnt

fib_val, cnt = fibonacci(n)
print(fib_val, cnt)
