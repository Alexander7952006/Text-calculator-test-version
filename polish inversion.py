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
