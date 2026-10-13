def add(n):
    if n<=100:
        return 0
    if n%2==0:
        return n+add(n-1)
    else:
        return add(n-1)
print(add(1000))