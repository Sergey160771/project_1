# Пользователь вводит число от 1 до 999. Используя операции с числами
# сообщите что введено: цифра, двузначное число или трёхзначное число.
# Для цифры верните её квадрат, например 5 - 25
# Для двузначного числа произведение цифр, например 30 - 0
# Для трёхзначного числа его зеркальное отображение, например 520 - 25
# Если число не из диапазона, запросите новое число
# Откажитесь от магических чисел
# В коде должны быть один input и один print

input_num = 0
FIRST_NUM = 0
SECOND_NUM = 0
THIRD_NUM = 0
result = 0

START_DIGIT = 1
END_HUNDREDS = 999
END_DIGIT = 9
START_HUNDREDS = 100

while not (START_DIGIT <= input_num <= END_HUNDREDS):
    input_num = int(input("Ведите число: "))

if input_num <= END_DIGIT:
    FIRST_NUM = input_num
    result = FIRST_NUM ** 2

elif START_DIGIT < input_num < START_HUNDREDS:
    SECOND_NUM = input_num
    result = (SECOND_NUM // 10) * (SECOND_NUM % 10)

else:
    FIRST_NUM = input_num // 100
    SECOND_NUM = input_num // 10 % 10
    THIRD_NUM = input_num % 10
    result = THIRD_NUM * 100 + SECOND_NUM * 10 + FIRST_NUM

print(result)
