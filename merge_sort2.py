
def merge_sort(A):
    if len(A) > 1:
        middle = int(len(A)/2)
        print('q = ', middle)
        left = merge_sort(A[:middle])
        right = merge_sort(A[middle:]
        x = f_merge(left, right)
        return x
    else:
        return A

def f_merge(left, right):
    result = []
    while len(left) > 0 and len(right) > 0:
        if left[0] <= right[0]
            result.append(left[0])
            left = left[1:]
        else:
            result.append(right[0])
            right = right[1:]
    if len(left) > 0:
        result += left
    if len(right) > 0:
        result += right
    return result
'''
Необходимо:
Разработать алгоритм функции Merge(A,p,q,r) на любом удобном вам языке, с использованием дополнительной памяти или без нее, как вам будет быстрее или удобнее в реализации.
'''

def main():
    '''Функция сортирующая массив элементов A:'''
    print('Пример массива:')
    a = [5,2,4,6,1,3,2,6]
    print(a)
    print('Примера запуска:')
    b = merge_sort(a)
    print('Примера запуска:')
    print(b)



if __name__ == '__main__':
    main()
