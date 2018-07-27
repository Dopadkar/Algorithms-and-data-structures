def matreshka(n):
    if n == 1:
        print("Матрешечка")
    else:
        print(n, '-я матрешка (верх)')
        matreshka(n-1)
        print(n, '-я матрешка (низ)')

matreshka(5)
