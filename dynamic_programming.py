def trajectory(n):
    k = [0,1]+[0]*n
    for i in range(2,n+2):
        k[i]=k[i-2]+k[i-1]
    return k[n]

def count_trajectories(n, allowed:list):
    k = [0,1,int(allowed[2])]+[0]*(n-3)
    for i in range(3,n+1):
        if allowed[i]:
            k[i]=k[i-3]+k[i-2]+k[i-1]
    return k[n]

def count_min_coast(n, price:list):
    C = [float('-inf')],price[1],price[1]+price[2]+[0]*(n-2)
    for i in range(3,n+1):
        C[i]=price[i]+min(C[i-1],C[i-2])
    return C[n]

def lcs(A,B):
    '''
    
    '''
    F = [[0]*(len(B)+1) for i in range(len(A)+1)]
    for i in range(1,len(A)+1):
        for j in range(1,len(B)+1):
            if A[i-1]==B[j-1]:
                F[i][j] = 1 + F[i-1][j-1]
            else:
                F[i][j] = min(F[i-1][j],F[i][j-1])
    return F[-1][-1]

def gis(A):
    '''
    Находит наибольшую возрастающую подпоследовательность
    '''
    F = [0]*(len(A)+1)
    for i in range(1,len(A)+1):
        m = 0
        for j in range(0,i):
            if A[i-1] > A[j-1] and F[j] > m:
                m = F[j]
        F[i] = m + 1
    return F[len(A)]

'''Задача о рюкзаке'''

def backpack(m,v):
    M = len(m)
    N = len(v)
    F=[[0] * (N+1) for i in range(M=1)]
    for i in range(1,N+1):
        for k in range(1,M+1):
            if m[i] <= k:
                F[k][i]=max(F[k][i-1],v[i]+F[k-m[i][i-1])
            else:
                F[k][i] +F[k][i-1]
    return F[M][N]


def equal(A,B):
    if len(A) != len(B):
        return False
    for i in range(len(A)):
        if A[i] != B[i]:
            return False
    return True

def levenstein(A, B):
    '''
    Returns the Levenstein's distance between strings A and B.
    '''
    F = [[i+j if i*j==0 else 0 for j in range(len(B)+1)] for i in range(len(A)+1)]
    for i in range(1,len(A)+1):
        for j in range(1, len(B)+1):
            if A[i-1] == B[j-1]:
                F[i][j] = F[i-1][j-1]
            else:
                F[i][j] = 1+ min(F[i-1][j],F[i][j-1],F[i-1][j-1])
    return F[len(A)][len(B)]

A = 'молоко'
B = 'колокол'

lev = levenstein(A, B)

def search_substring(s,sub):
    ss = []
    for i in range(0,len(s)-len(sub)):
        si = s[i:i+len(sub)]
        print(si, ' ', sub)
        if equal(si,sub):
            ss.append(i)
            print(i)
    return ss

s = 'abcbabacabaccbab'
sub = 'ab'

ss = search_substring(s,sub)            
print(ss)
'''
def kmp(s,sub):
    ss = ss + '@' + s
'''
