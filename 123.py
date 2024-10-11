from fnmatch import fnmatch


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


def function():
    while True:
        calc = input('Введите арифметическую операцию: ')
        if fnmatch(calc, '* плюс *'):
            calc = calc.split(' плюс ')
            if (calc[0] in list_letter[0:100] + list_letter[10000:10099]
                    and calc[1] in list_letter[0:100] +
                    list_letter[10000:10099]):
                result = (list_num[list_letter.index(calc[0])] +
                          list_num[list_letter.index(calc[1])])
                result = list_letter[list_num.index(result)]
                print(result)
                break
        elif fnmatch(calc, '* умножить на *'):
            calc = calc.split(' умножить на ')
            if (calc[0] in list_letter[0:100] + list_letter[10000:10099]
                    and calc[1] in list_letter[0:100] +
                    list_letter[10000:10099]):
                result = (list_num[list_letter.index(calc[0])] *
                          list_num[list_letter.index(calc[1])])
                result = list_letter[list_num.index(result)]
                print(result)
                break
        elif fnmatch(calc, '* минус *'):
            calc = calc.split(' минус ', 1)
            if (calc[0] in list_letter[0:100] + list_letter[10000:10099]
                    and calc[1] in list_letter[0:100] +
                    list_letter[10000:10099]):
                result = (list_num[list_letter.index(calc[0])] -
                          list_num[list_letter.index(calc[1])])
                result = list_letter[list_num.index(result)]
                print(result)
                break
        elif fnmatch(calc, '* разделить на *'):
            calc = calc.split(' разделить на ', 1)
            if (calc[0] in list_letter[0:100] + list_letter[10000:10099]
                    and calc[1] in list_letter[0:100] +
                    list_letter[10000:10099]):
                result = (list_num[list_letter.index(calc[0])] /
                          list_num[list_letter.index(calc[1])])
                result = round(result, 3)
                res_split = str(result).split('.')
                result = (list_letter[list_num.index(int(res_split[0]))] +
                          ' и ' +
                          list_letter[list_num.index(int(res_split[1]))])
                print(result)
                break
        else:
            print('Ошибка при вводе операции')

function()
input('Введите Enter для выхода')
