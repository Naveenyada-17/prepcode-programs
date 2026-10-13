def fibo(n):
    if n <= 14:
        return 15

    return n + fibo(n-1)

print(fibo(25))