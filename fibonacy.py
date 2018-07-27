def bad_fib(n):
    if n <= 1:
        return n
    return bad_fib(n-1)+bad_fib(n-2)

def best_fib(n):
    if n <= 1:
        return n
    fib = [0,1]+[0]*(n-1)
    for i in range(2,n+1):
        fib[i]=fib[i-1]+fib[i-2]
    return fib[n]

F = [None] * 10001

def good_fib(n):
    assert(n >= 0 and n <10000)
    if F[n] is not None:
        if n<= 1:
            F[n]=n
        else:
            F[n]=good_fib(n-1)+ good_fib(n-1)
    return F[n]

f1=bad_fib(10)
f2=good_fib(10)
f3=best_fib(10)

print(f2)


