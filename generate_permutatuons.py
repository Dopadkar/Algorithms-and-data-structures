def generate_permutatuons(N:int, M:int=-1, prefix=None):
    """ Генерирует перестановку N чисел в M позициях, начиная с префикса prefix"""
    M = N if M == -1 else M # по умолчанию N чисел в M позициях
    prefix = prefix or []
    if M == 0:
        print(*prefix, end=' ', sep="")
        return
    for number in range(1, N+1):
        if find(number, prefix):
            continue
        prefix.append(number)
        generate_permutatuons(N, M-1, prefix)
        prefix.pop()

def find(number, A):
    '''
    Ищет число x d 
    '''
    flag = False
    for x in A:
        if number == x:
            flag = True
            break
    return flag

generate_permutatuons(5)
