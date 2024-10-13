from fnmatch import fnmatch


def function():
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
    while True:
        calc = input('Введите арифметическую операцию: ')
        copy = calc
        if (fnmatch(calc, '* плюс *') or fnmatch(calc, '* умножить на *') or
            fnmatch(calc, '* минус *')):
            if ' плюс ' in calc:
                calc = calc.split(' плюс ')
                oper = 'плюс'
            if ' умножить на ' in calc:
                calc = calc.split(' умножить на ')
                oper = 'умножение'
            if ' минус ' in calc:
                calc = calc.split(' минус ', 1)
                oper = 'минус'
            if (calc[0] in list_letter[0:100] + list_letter[10000:10099]
                    and calc[1] in list_letter[0:100] +
                    list_letter[10000:10099]):
                if oper == 'плюс':
                    result = (list_num[list_letter.index(calc[0])] +
                          list_num[list_letter.index(calc[1])])
                    result = list_letter[list_num.index(result)]
                    print(result)
                    break
                elif oper == 'умножение':
                    result = (list_num[list_letter.index(calc[0])] *
                          list_num[list_letter.index(calc[1])])
                    result = list_letter[list_num.index(result)]
                    print(result)
                    break
                elif oper == 'минус':
                    result = (list_num[list_letter.index(calc[0])] -
                          list_num[list_letter.index(calc[1])])
                    result = list_letter[list_num.index(result)]
                    print(result)
                    break
            else:
                if (copy.count('умножить на') > 1 or copy.count('плюс') > 1
                    or 'минус плюс' in copy or 'минус умножить на' in copy or
                    copy.find('минус минус') == 0 or copy.find('плюс') == 0 or
                    copy.find('умножить на') == 0 or copy.find(' ') == 0 or
                    'плюс умножить на' in copy or 'умножить на плюс' in copy):
                    print('Неправильная последовательность чисел и операций')
                    continue
                else:    
                    print('Неправильная запись числа')
                    continue
        else:
            print('Неправильная последовательность чисел и операций')
            continue

                
function()
input('Введите Enter для выхода')
