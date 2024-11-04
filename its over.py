from fnmatch import fnmatch
from math import factorial


def function(calc):
    """ Функция, принимающая строку от пользователя и возвращающая ответ """
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
    
    case_dct = {'одного': 1, 'двух': 2, 'трех': 3, 'четырех': 4, 'пяти': 5,
           'шести': 6, 'семи': 7, 'восьми': 8, 'девяти': 9, 'десяти': 10,
           'одиннадцати': 11, 'двенадцати': 12, 'тринадцати': 13,
           'четырнадцати': 14, 'пятнадцати': 15}
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
    if 'размещений' in calc or 'перестановок' in calc or 'сочетаний' in calc:
        arg = 0
        if fnmatch(calc, 'размещений из * по *'):
            calc = calc.replace('размещений из ', '')
            calc = calc.split(' по ')
            if calc[0] in case_dct and calc[1] in dct:
                num1 = case_dct[calc[0]]
                num2 = dct[calc[1]]
                if num1 > num2:
                    result = factorial(num1) // factorial(num1 - num2)
                    arg = 1
                else:
                    print('Ошибка ввода')
            else:
                print('Ошибка ввода')

        elif fnmatch(calc, 'сочетаний из * по *'):
            calc = calc.replace('сочетаний из ', '')
            calc = calc.split(' по ')
            if calc[0] in case_dct and calc[1] in dct:
                num1 = case_dct[calc[0]]
                num2 = dct[calc[1]]
                if num1 > num2:
                    result = factorial(num1) // (factorial(num1 - num2) *
                                                   factorial(num2))
                    arg = 1
                else:
                    print('Ошибка ввода')
            else:
                print('Ошибка ввода')
 
        elif fnmatch(calc, 'перестановка * чисел'):
            calc = calc.replace('перестановка ', '')
            calc = calc.replace(' чисел', '')
            if calc in case_dct:
                num = case_dct[calc]
                result = factorial(num)
                arg = 1
            else:
                print('Ошибка ввода')
        else:
            print('Ошибка ввода')

        if arg == 1:
            if result in list_num:
                print(list_letter[list_num.index(result)])
                
    else:
        for indx in range(len(calc)):
            if indx == calc.find(' умножить на ', indx):
                op_list.append([' умножить на ',
                                calc.find(' умножить на ', indx)])
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
            
        if '' in calc:
            print('Ошибка ввода')
            return True
        for indx in range(len(calc)):
            if len(calc[indx]) == calc[indx].count(' '):
                print('Ошибка ввода')
                return True 
        for indx in range(len(calc)):
            if calc[indx] in list_letter[0:100] + list_letter[10000:10099]:
                calc[indx] = list_num[list_letter.index(calc[indx])]
            else:
                print('Ошибка ввода')
                return True
            
        result = 0    
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
                    
        if result in list_num:
            print(list_letter[list_num.index(result)])
        else:
            print('Ошибка ввода') 
               

function(input('Введите выражение: '))
input('Введите Enter для выхода')
