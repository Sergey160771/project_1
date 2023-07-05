# Напишите программу, которая запрашивает год и проверяет его на високосность.
# Распишите все возможные проверки в цепочке elif
# Откажитесь от магических чисел
# Обязательно учтите год ввода Григорианского календаря
# В коде должны быть один input и один print

year = int(input("Введите год: "))
GRIGORIAN_YEAR = 1582
YEAR_YES = "{} Високосный год"
YEAR_NO = "{} Не високосный год"
IS_GRIGORIAN = "{} год не в Григорианском календоре"
MULTI_400 = 400
MULTI_4 = 4
MULTI_100 = 100
result = ""

if year <= GRIGORIAN_YEAR:
    result = IS_GRIGORIAN.format(year)
elif year % MULTI_4 == 0 and year % MULTI_100 != 0 or year % MULTI_400 == 0:
    result = YEAR_YES.format(year)
else:
    result = YEAR_NO.format(year)
print(result)
