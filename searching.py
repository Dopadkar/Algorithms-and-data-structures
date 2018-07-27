def left_boundery(A, key):
    '''
    A is sorted.
    '''
    left = -1
    right = len(A)
    while right-left>1:
        middle = (left+right)//2
        if A[middle] < key:
            left = middle
        else:
            right = middle
    return left

def right_boundery(A, key):
    '''
    A is sorted.
    '''
    left = -1
    right = len(A)
    while right-left>1:
        middle = (left+right)//2
        if A[middle] <= key:
            left = middle
        else:
            right = middle
    return right

def binaru_search(A,key):
    left = left_boundery(A, key)
    right = right_boundery(A, key)
    if right - left <= 1:
        return
    return left, right


    
    
