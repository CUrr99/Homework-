num1 = int(input('Введите время в часах:'))
if 5 <= num1 <= 11:
    print('Утро')
elif 12 <= num1 <= 17:
    print('День')
elif 18 <= num1 <= 22:
    print('Вечер')
elif 0 <= num1 <= 4 or num1 == 23:   
    print('Ночь')
else:
    print('Ошибĸа, неверно введенное время')
