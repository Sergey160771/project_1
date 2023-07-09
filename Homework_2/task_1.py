# ✔ Напишите программу, которая получает целое
# число и возвращает его шестнадцатеричное
# строковое представление. Функцию hex
# используйте для проверки своего результата.

DIVIDER = 16
conversion_table = {0: '0', 1: '1', 2: '2', 3: '3', 4: '4',
                    5: '5', 6: '6', 7: '7',
                    8: '8', 9: '9', 10: 'A', 11: 'B', 12: 'C',
                    13: 'D', 14: 'E', 15: 'F'}

number = int(input('Введите число в деситичной системе исчисления: '))

print(hex(number))

hexadecimal = ''
while number > 0:
    remainder = number % DIVIDER
    hexadecimal = conversion_table[remainder] + hexadecimal
    number //= DIVIDER
print(hexadecimal)

