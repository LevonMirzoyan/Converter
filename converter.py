def converter(num):
    assert (0 <= num) # аварийно завершим т.к отрицательные числа не допустимы
    digit = {
            0: 'ноль', 1: 'один', 2: 'два', 3: 'три', 4: 'четыре', 5: 'пять',
            6: 'шесть', 7: 'семь', 8: 'восемь', 9: 'девять', 10: 'десять',
            11: 'одиннадцать', 12: 'двенадцать', 13: 'тринадцать', 14: 'четырнадцать',
            15: 'пятнадцать', 16: 'шестнадцать', 17: 'семнадцать', 18: 'восемнадцать',
            19: 'девятнадцать', 20: 'двадцать',
            30: 'тридцать', 40: 'сорок', 50: 'пятьдесят', 60: 'шестьдесят',
            70: 'семьдесят', 80: 'восемьдесят', 90: 'девяносто'
            }
    hundred  = [100, 'сто', 'сот']
    thousand = [1000, 'тысяча', 'тысяч,']
    million =  [1000000, 'миллион', 'миллионов,']
    billion =  [1000000000, 'миллиард', 'миллиардов,']
    trillion = [1000000000000, 'триллион', 'триллионов,']
    if num < 20:
        return digit[num]
    if num < 100:
        div, mod = divmod(num, 10) # частное и остаток
        return digit[num] if mod == 0 else digit[div * 10] + ' ' + digit[mod]
    else:
        if num < thousand[0]:
            divider, view1, view2 = hundred
        elif num < million[0]:
            divider, view1, view2 = thousand
        elif num < billion[0]:
            divider, view1, view2 = million
        elif num < trillion[0]:
            divider, view1, view2 = billion
        else:
            divider, view1, view2 = trillion
        div, mod = divmod(num, divider) # частное и остаток
        if mod == 0:
            return '{} {}'.format(converter(div), view1)
        else:
            return '{} {} {}'.format(converter(div), view2, converter(mod))


print (converter(int(input("Введите неотрицательное число: "))))
