# Напишите код, который запрашивает число и сообщает является ли оно простым или составным.
# Используйте правило для проверки: “Число является простым,
# если делится нацело только на единицу и на себя”.
# Сделайте ограничение на ввод отрицательных чисел и чисел больше 100 тысяч.

MIN = 0
MAX = 100000
divider = 2
count = 0

number = int(input(f'Введите число от {MIN} до {MAX}: '))
if MIN <= number <= MAX:
    for i in range(divider, number - 1):
        if number % i == 0:
            count += 1
    if count <= 0:
        print("Число является простым")
    else:
        print("Число является составным")
else:
    print("Число не входит в диапазон")
