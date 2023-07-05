# Треугольник существует только тогда, когда сумма любых двух его сторон больше третьей.
# Дано a, b, c - стороны предполагаемого треугольника.
# Требуется сравнить длину каждого отрезка-стороны с суммой двух других.
# Если хотя бы в одном случае отрезок окажется больше суммы двух других,
# то треугольника с такими сторонами не существует.
# Отдельно сообщить является ли треугольник разносторонним, равнобедренным или равносторонним.

TEXT = "Ведите сторону треугольника "
TEXT_EXIST = "Треугольник не существует"

side_a = float(input(TEXT + "a: "))
side_b = float(input(TEXT + "b: "))
side_c = float(input(TEXT + "c: "))

sum_a_b = side_a + side_b
sum_a_c = side_a + side_c
sum_b_c = side_b + side_c

if sum_a_b > 0 and sum_a_c > 0 and sum_b_c > 0:
    if sum_a_b < side_c or sum_a_c < side_b or sum_b_c < side_a:
        print(TEXT_EXIST)
    else:
        if side_a == side_b and side_b == side_c and side_a == side_c:
          print("Треугольник равносторонний")
        elif side_a == side_b or side_b == side_c or side_a == side_c:
            print("Треугольник равнобедренный")
        else:
            print("Треугольник разносторонний")
else:
    print(TEXT_EXIST)
