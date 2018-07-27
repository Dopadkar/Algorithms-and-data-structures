def insert_sort(A):
    '''сортирует список A вставками'''
    n = len(A)
    for top in range(1,n):
        k = top
        while k > 0 and A[k-1] > A[k]:
            A[k], A[k-1] = A[k-1], A[k]
            k -= 1
    return A

def choice_sort(A):
    '''сортирует список A выбором'''
    n = len(A)
    for pos in range(0, n-1):
        for k in range(pos +1, n):
            if A[k] < A[pos]:
                A[pos], A[k] = A[k], A[pos]
    return A

def bubble_sort(A):
    '''сортирует список A методом пузырька'''
    n = len(A)
    for bypass in range(1, n):
        for k in range(0, n-bypass):
            if A[k] > A[k+1]:
                A[k+1], A[k] = A[k], A[k+1]
    return A

def count_sort(A):
    '''сортирует список A методом подсчёта'''
    n = len(A)
    F = [0]*10
    for i in range(n):
        F[A[i]] += 1
    B = A
    for i in F:
        B.append(i * F.index(i))
    return bubble_sort(A)

def merge(A:list,B:list):
    C = [0] * (len(A)+len(B))
    i = j = n = 0
    while i<len(A) and j<len(B):
        if A[i] < B[j]:
            C[n] = A[i]
            i += 1
            n += 1
        else:
            C[n] = B[j]
            j += 1
            n += 1
    while i<len(A):
        C[n] = A[i]
        i += 1
        n += 1
    while j<len(B):
        C[n] = B[j]
        j += 1
        n += 1
    return C

A = [1,6,8,5,4,8,2]
B = [2,6,4,7,9,5,3,8,10]

def merg_sort(A):
    if len(A) <= 1:
        return
    middle = len(A)//2
    L = [A[i] for i in range(0:middle)]
    R = [A[i] for i in range(middle:len(A))]
    merge_sort(L)
    merge_sort(R)
    C = merge(L,R)
    for i in range(len(A)):
        A[i]=C[i]

# Tony Hoar's sorting
def hoar_sort(A):
    if len(A) <= 1:
        return
    L = []
    M = []
    R = []
    barrier = = A[0]
    for x in A:
        if x < barrier:
            L.append(x)
        elif x > barrier:
            R.append(x)
        else:
            M.append(x)
    hoar_sort(L)
    hoar_sort(R)
    k = 0
    for x in L+M+R:
        A[k] = x
        k += 1
    
def check_sorted(A,ascending=True):
    '''
    Проверка отсортированности
    '''
    flag = True
    s = int(ascending)*2 - 1
    for i in range(0,n-1):
        if s*A[i] > s*A[i+1]:
            flag = False
            break
    return flag

def test_sort(sort_algoritm, A, A_ans):
    print('Test_case', sort_algoritm.__doc__)
    A_sorted = sort_algoritm(A)
    print(A_sorted, 'Test is ', 'Ok' if A_sorted == A_ans else 'Fail')

if __name__ == '__main__':
    A = [2,4,5,1,3]
    print('Unsorted arrey is ', A)
    A_ans = [1,2,3,4,5]
    print('Sorted arrey is ', A_ans)
    test_sort(insert_sort, A, A_ans)
    test_sort(choice_sort, A, A_ans)
    test_sort(bubble_sort, A, A_ans)
    test_sort(count_sort, A, A_ans)
