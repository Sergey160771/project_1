import fractions
import math

number: str = input(f'Введите две дроби вида a/b через пробел: ')
fraction_1, fraction_2 = number.split()
numerator_1, denominator_1 = map(int, fraction_1.split('/'))
numerator_2, denominator_2 = map(int, fraction_2.split('/'))
sum_fractions_numerator: int = ((numerator_1 * denominator_2) + (numerator_2 * denominator_1))
sum_fractions_denominator: int = (denominator_1 * denominator_2)

nod_sum: int = math.gcd(sum_fractions_numerator,
                        sum_fractions_denominator)
sum_fractions_numerator: int = sum_fractions_numerator // nod_sum
sum_fractions_denominator: int = sum_fractions_denominator // nod_sum
product_fractions_numerator: int = numerator_1 * numerator_2
product_fractions_denominator: int = denominator_1 * denominator_2

nod_prod: int = math.gcd(product_fractions_numerator, product_fractions_denominator)
product_fractions_numerator: int = product_fractions_numerator // nod_prod
product_fractions_denominator: int = product_fractions_denominator // nod_prod

print(f'{sum_fractions_numerator}/{sum_fractions_denominator} '
      f'{product_fractions_numerator}/{product_fractions_denominator}')

print(fractions.Fraction(fraction_1) + fractions.Fraction(fraction_2),
      fractions.Fraction(fraction_1) * fractions.Fraction(fraction_2))
