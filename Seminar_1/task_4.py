# Нарисовать в консоли ёлку спросив
# у пользователя количество рядов.

WHITESPACE = " "
ASTERISK = "*"
number_rows = int(input('Сколько рядов в ёлке ?: '))
for i in range(1, number_rows + 1):
    print(WHITESPACE * (number_rows - i), ASTERISK * (2 * i - 1))