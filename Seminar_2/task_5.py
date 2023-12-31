# Напишите программу, которая решает
# квадратные уравнения даже если
# дискриминант отрицательный.
# ✔ Используйте комплексные числа
# для извлечения квадратного корня.

a, b, c = map(int, input('ведите коэффиценты квадратного уравнения: ').split())
d = b ** 2 - 4 * a * c
if d > 0:
    x_1 = (- b - d ** 0.5)/(2 * a)
    x_2 = (- b + d ** 0.5) / (2 * a)
    result: str = f'Уравнение имеет 2 корня: {x_1}, {x_2} '
elif d == 0:
    x = - b / (2 * a)
    result: str = f'Уравнение имеет 1 корень: {x} '
else:
    d = complex(d, 0)
    x_1 = (- b - d ** 0.5) / (2 * a)
    x_2 = (- b + d ** 0.5) / (2 * a)
    result: str = f'Уравнение имеет комплексных 2 корня: {x_1}, {x_2}'

print(result)
