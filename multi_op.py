from fnmatch import fnmatch


def function(calc):
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
    list_num = []
    
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

    for num in list_letter[1:]:
        list_letter.append('минус' + ' ' + num)

    for num in range(0, 10000):
        list_num.append(num)

    for num in list_num[1:]:
        list_num.append(int('-' + str(num)))
        
    opers = []
    while (calc.count(' плюс ') + calc.count(' минус ') +
           calc.count(' умножить на ')) > 0:
        temp = []
        if ' плюс ' in calc:
            temp.append([calc.index(' плюс '), ' плюс '])
        if ' минус ' in calc:
            temp.append([calc.index(' минус '), ' минус '])
        if ' умножить на ' in calc:
            temp.append([calc.index(' умножить на '), ' умножить на '])
        temp = sorted(temp, key=lambda x: x[0])
        while len(temp) > 0:
            opers.append(temp[0][1])
            calc = calc.replace(temp[0][1], '.', 1)
            temp = temp[1:]
    result = 0
    calc = calc.split('.')
    for indx in range(len(calc)):
        if indx == 0 and calc[indx] in list_letter[0:100]:
            result += list_num[list_letter.index(calc[indx])]
        elif calc[indx] in list_letter[0:100] and indx > 0:
            if opers[indx - 1] == ' плюс ':
                result += list_num[list_letter.index(calc[indx])]
            elif opers[indx - 1] == ' минус ':
                result -= list_num[list_letter.index(calc[indx])]
            elif opers[indx - 1] == ' умножить на ':
                result *= list_num[list_letter.index(calc[indx])]
    if result in list_num:
        result = list_letter[list_num.index(result)]
    print(result)

    
function(input('Введите выражение: '))
input('Введите Enter для выхода')
