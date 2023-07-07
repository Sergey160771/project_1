# Программа загадывает число от 0 до 1000. Необходимо угадать число за 10 попыток. Программа
# должна подсказывать «больше» или «меньше» после каждой попытки. Для генерации случайного
# числа используйте код:
# from random import randint
# num = randint(LOWER_LIMIT, UPPER_LIMIT)

from random import randint

LOWER_LIMIT = 0
UPPER_LIMIT = 1000
COUNT_TRY = 10

RAND_NUMBER = randint(LOWER_LIMIT, UPPER_LIMIT)
print(RAND_NUMBER)
for i in range(COUNT_TRY):
    number = int(input(f'Увас {COUNT_TRY - i} попыток, Введи число от 0 до 1000: '))
    if number == RAND_NUMBER:
        print(f'Ва угодали c {i + 1} попыток. Вы молодец!')
        break
    elif number < RAND_NUMBER:
        print(f'Ваше число {number} МЕНЬШЕ загаданного')
    else:
        print(f'Ваше число {number} БОЛЬШЕ загаданного')
else:
    print('К сожалению вы проиграли')
