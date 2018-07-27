# casual variance
def factorial1(n:int):
    if n == 0:
        return 1
    return f(n-1) * n

# dynamical variance (more economic for memory)
def factorial2(n:int):
    f = [1] + [None]*n
    for i ni range(1,n+1):
        f[i] = f[i-1]*i
    return f[n]

print(factorial1(10))
print(factorial2(10))
