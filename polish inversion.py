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
    calc = calc.replace(' умножить на минус ', ' умножить на ******')
    calc = calc.replace(' плюс минус ', ' плюс ******')
    calc = calc.replace(' минус минус ', ' минус ******')
    op_list = []
    arg_type = 1
    if calc.find(' плюс ') == 0:
        arg_type = 0
    if calc.find(' минус ') == 0:
        arg_type = 0
    if calc.find(' умножить на ') == 0:
        arg_type = 0
    for indx in range(len(calc)):
        if indx == calc.find(' умножить на ', indx):
            op_list.append([' умножить на ', calc.find(' умножить на ', indx)])
        elif indx == calc.find(' плюс ', indx):
            op_list.append([' плюс ', calc.find(' плюс ', indx)])
        elif indx == calc.find(' минус ', indx):
            op_list.append([' минус ', calc.find(' минус ', indx)])
    op_list = sorted(op_list, key = lambda x: x[1])

    for indx in range(len(op_list)):
        calc = calc.replace(op_list[indx][0], '?', 1)
        opers.append(op_list[indx][0])
        
    calc = calc.split('?')
    for indx in range(len(calc)):
        calc[indx] = calc[indx].replace('******', 'минус ')

    for indx in range(len(calc)):
        minus = 0
        count = 0
        argument = 1
        if calc[0] == '' or len(str(calc[0])) == str(calc[0]).count(' '):
            argument = 0
        calc[indx] = calc[indx].split()
        for num in calc[indx]:
            if num in dct:
                count += dct[num]
            elif calc[indx].index(num) == 0 and num == 'минус':
                minus = 1
            else:
                argument = 0
                print('Ошибка ввода')
                return True
        if argument == 1 and minus == 0:
            calc[indx] = count
        elif argument == 1 and minus == 1:
            calc[indx] = int('-' + str(count))
    for num in calc:
        if type(num) != int:
            arg_type = 0
            break
    if arg_type == 1:
        for num in calc:
            if abs(num) > 99:
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
            for indx in range(len(pieces)):
                if indx < len(pieces) - 1 and pieces[indx] == 10:
                    pieces[indx] += pieces[indx + 1]
                    pieces[indx + 1] = '?'
            while '?' in pieces:
                pieces.remove('?')
                    
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
