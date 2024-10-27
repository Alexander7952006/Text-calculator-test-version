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
    
    list_letter = ['ноль', 'один', 'два', 'три', 'четыре', 'пять', 'шесть',
               'семь', 'восемь', 'девять', 'десять', 'одиннадцать',
               'двенадцать', 'тринадцать', 'четырнадцать', 'пятнадцать',
               'шестнадцать', 'семнадцать', 'восемнадцать', 'девятнадцать']
    
    list_ten = ['двадцать', 'тридцать', 'сорок', 'пятьдесят', 'шестьдесят',
                'семьдесят', 'восемьдесят', 'девяносто']
    
    list_hundred = ['сто', 'двести', 'триста', 'четыреста', 'пятьсот',
                    'шестьсот', 'семьсот', 'восемьсот', 'девятьсот']
    
    list_thousand = ['тысяча', 'две тысячи', 'три тысячи', 'четыре тысячи',
                     'пять тысяч', 'шесть тысяч', 'семь тысяч', 'восемь тысяч',
                     'девять тысяч']
    for ten in list_ten:
        for num in [''] + list_letter[1:10]:
            if num != '':
                list_letter.append(ten + ' ' + num)
            else:
                list_letter.append(ten + num)      
    for hundred in list_hundred:
        for ten in [''] + list_letter[1:100]:
            if ten != '':
                list_letter.append(hundred + ' ' + ten)
            else:
                list_letter.append(hundred + ten)
    for thousand in list_thousand:
        for hundred in [''] + list_letter[1:1000]:
            if hundred != '':
                list_letter.append(thousand + ' ' + hundred)
            else:
                list_letter.append(thousand + hundred)      
    opers = []
    calc = calc.replace(' умножить на минус ', ' умножить на ******')
    calc = calc.replace(' плюс минус ', ' плюс ******')
    calc = calc.replace(' минус минус ', ' минус ******')
    op_list = []
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
        if indx == 0 and calc[indx] == ' ':
            argument = 0
        else:
            argument = 1
        calc[indx] = calc[indx].split()
        for num in calc[indx]:
            if num in dct:
                count += dct[num]
            elif calc[indx].index(num) == 0 and num == 'минус':
                minus = 1
            else:
                argument = 0
                print('Ощибка ввода')
                break
        if argument == 1 and minus == 0:
            calc[indx] = count
        elif argument == 1 and minus == 1:
            calc[indx] = int('-' + str(count))
  
    arg_type = 1
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
        if str(result)[0] == '-':
            output += 'минус '
            result = abs(result)
        if result < 10000:
            for indx in range(len(list_letter)):
                if result == indx:
                    print(output + list_letter[indx])
        else:
            print('Ошибка ввода')
                    
    else:
        print('ошибка ввода')       

        
function(input('Введите выражение: '))
input('Введите Enter для выхода')
