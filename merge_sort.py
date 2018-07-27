def merge_sort(a):
    if len(a) > 1:
        middle = int(len(a)/2)
        l = merge_sort(a[:middle])
        r = merge_sort(a[middle:])
        return f_merge(l, r)
    else:
        return a

def f_merge(left, right):
    result = []
    while len(left) > 0 and len(right) > 0:
        if left[0] <= right[0]:
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
