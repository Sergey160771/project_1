# ✔ Напишите программу, которая выводит
# на экран числа от 1 до 100.
# ✔ При этом вместо чисел, кратных трем,
# программа должна выводить слово «Fizz»
# ✔ Вместо чисел, кратных пяти — слово «Buzz».
# ✔ Если число кратно и 3, и 5, то программа
# должна выводить слово «FizzBuzz».
# ✔ *Превратите решение в генераторное выражение.

for n in range(1,101):
    a = None
    if n % 3 == 0 and n % 5 == 0:
        a = 'FizzBuzz'

    elif n % 3 == 0:
        a = 'Fizz'
    elif n % 5 == 0:
        a = 'Buzz'
    else:
        a = n
    print(a, end=' ')
