def gcd1(a,b):
    '''
    Returns the 
    '''
    while b != 0:
        remainder = a % b
        a, b = b, remainder
    return a

def gcd2(a,b):
    if a == b:
        return a
    elif a > b:
        return gcd2(a-b,b)
    else:
        return gcd2(a,b-a)

def gdc3(a,b):
    if b == 0:
        return a
    else:
        return gdc3(b,a%b)

c = gcd1(4851,3003)
print(c)
c = gcd2(4851,3003)
print(c)
c = gdc3(4851,3003)
print(c)
