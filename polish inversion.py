from fnmatch import fnmatch


def function(calc):
    dct = {'ноль': 0, 'один': 1, 'два': 2, 'три': 3, 'четыре': 4, 'пять': 5,
           'шесть': 6, 'семь': 7, 'восемь': 8, 'девять': 9, 'десять': 10,
           'одиннадцать': 11, 'двенадцать': 12, 'тринадцать': 13,
           'четырнадцать': 14, 'пятнадцать': 15, 'шестнадцать': 16,
           'семнадцать': 17, 'восемнадцать': 18, 'девятнадцать': 19,
           'двадцать': 20, 'тридцать': 30, 'сорок': 40, 'пятьдесят': 50,
           'шестьдесят': 60, 'семьдесят': 70, 'восемьдесят': 80,
           'девяносто': 90, 'сто': 100, 'двести': 200, 'триста': 300,
           'четыреста': 400, 'пятьсот': 500, 'шестьсот': 600,'семьсот': 700,
           'восемьсот': 800, 'девятьсот': 900, 'тысяча': 1000,
           'две тысячи': 2000, 'три тысячи': 3000, 'четыре тысячи': 4000,
           'пять тысяч': 5000, 'шесть тысяч': 6000, 'семь тысяч': 7000,
           'восемь тысяч': 8000, 'девять тысяч': 9000}
    
    case_dct = {'одного': 1, 'двух': 2, 'трех': 3, 'четырех': 4, 'пяти': 5,
           'шести': 6, 'семи': 7, 'восьми': 8, 'девяти': 9, 'десяти': 10,
           'одиннадцати': 11, 'двенадцати': 12, 'тринадцати': 13,
           'четырнадцати': 14, 'пятнадцати': 15}
                
    opers = []
    temp = []
    while ' умножить на ' in calc:
        temp.append([calc.index(' умножить на '), ' умножить на '])
        calc = calc.replace('умножить на ', '', 1)
    while ' плюс ' in calc:
        temp.append([calc.index(' плюс '), ' плюс '])
        calc = calc.replace('плюс ', '', 1)
    while ' минус ' in calc:
        temp.append([calc.index(' минус '), ' минус '])
        calc = calc.replace('минус ', '', 1)
    temp = sorted(temp, key=lambda x: x[0])
    for oper in temp:
        opers.append(oper[1])
        
    calc = calc.split()
    for indx in range(len(calc)):
        calc[indx] = calc[indx].split(' ')
        count = 0
        argument = 1
        for num in calc[indx]:
            if num in dct:
                count += dct[num]
            else:
                argument = 0
                print('Ощибка ввода')
                break
        if argument == 1:
            calc[indx] = count
            
    arg_type = 1
    for num in calc:
        if type(num) != int:
            arg_type = 0
            break
    if arg_type == 1:
        for num in calc:
            if num > 99:
                arg_type = 0
                break
    result = 0
    if arg_type == 1:
        while ' умножить на ' in opers:
            indx = opers.index(' умножить на ')
            opers.pop(indx)
            calc[indx: indx + 2] = [calc[indx] * calc[indx + 1]]
        for indx in range(len(calc)):
            if indx == 0:
                result += calc[indx]
            elif indx > 0:
                if opers[indx - 1] == ' плюс ':
                    result += calc[indx]
                elif opers[indx - 1] == ' минус ':
                    result -= calc[indx]
        output = ''
        pieces = []
        if str(result)[0] == '-':
            output += 'минус '
            result = abs(result)
        if result < 10000:
            for step in range(len(str(result))):
                pieces.append(result % int('1' + '0' * (step + 1)))
                result -= result % int('1' + '0' * (step + 1))
            for _ in range(pieces.count(0)):
                pieces.remove(0)
            pieces = pieces[:: -1]
            for num in pieces:
                    for key in dct:
                        if num == dct[key]:
                            output += key + ' '
            output = output.strip()
            print(output)
        else:
            print('Ошибка ввода')
    else:
        print('ошибка ввода')


function(input('Введите выражение: '))
input('Введите Enter для выхода')
