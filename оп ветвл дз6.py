number = int(input("Введите целое число: "))

if number == 0:
    description = "ноль"
elif number > 0:
    if number % 2 == 0:
        description = "положительное четное число"
    else:
        description = "положительное нечетное число"
else:
    if number % 2 == 0:
        description = "отрицательное четное число"
    else:
        description = "отрицательное нечетное число"

print(description)
