number = int(input('Введите день недели числом:'))
if 1 <= number <= 5:
    print('Будний день')
else:
    if 6 <= number <= 7:
        print('Выходной день')
        
