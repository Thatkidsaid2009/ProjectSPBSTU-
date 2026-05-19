from math import ceil
def view_vocabulary(dictionar):
    i = 10
    pages = list(range(0,ceil(len(dictionar)/10)+1))
    pages = [str(x) for x in pages]
    while True:
        print(f'СТРАНИЦА {i//10}')
        print('-'*10)
        page = list(dictionar.items())[i-10:i]
        for const in page:
            print(' ', const[0], const[1])
        req = str(input(f' 1-{ceil(len(dictionar)/10)}. Номер страницы \n 0. Выйти в меню: \n {'-'*10}\n  '))
        if req.isalpha() == True or req not in pages:
            while True:
                req = str(input(f' Ошибка ввода! \n 1-{ceil(len(dictionar)/10)}. Номер страницы \n 0. Выйти в меню: \n {'-'*10}\n  '))
                if req.isdigit() == True and req in pages:
                    break
        req = int(req)
        if req == 0:
            break
        else:
            i = req*10
view_vocabulary()