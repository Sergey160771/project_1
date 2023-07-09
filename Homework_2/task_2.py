# Напишите программу, которая принимает две строки
# вида “a/b” — дробь с числителем и знаменателем.
# Программа должна возвращать сумму
# и *произведение дробей. Для проверки своего
# кода используйте модуль fractions.

import fractions

number: str = input(f'Введите две дроби вида a/b через пробел: ')
fraction_1, fraction_2 = number.split()
numerator_1, denominator_1 = map(int, fraction_1.split('/'))
numerator_2, denominator_2 = map(int, fraction_2.split('/'))

sum_fractions: str = f'{(numerator_1 * denominator_2) + (numerator_2 * denominator_1)}/' \
                f'{denominator_1 * denominator_2}'
product_fractions: str = f'{(numerator_1 * numerator_2)}/{denominator_1 * denominator_2}'
print(fractions.Fraction(sum_fractions), fractions.Fraction(product_fractions))

print(fractions.Fraction(fraction_1) + fractions.Fraction(fraction_2),
      fractions.Fraction(fraction_1) * fractions.Fraction(fraction_2))




