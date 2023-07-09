# ✔ Напишите программу, которая получает целое число и возвращает
# его двоичное, восьмеричное строковое представление.
# ✔ Функции bin и oct используйте для проверки своего
# результата, а не для решения.
# Дополнительно:
# ✔ Попробуйте избежать дублирования кода
# в преобразованиях к разным системам счисления
# ✔ Избегайте магических чисел
# ✔ Добавьте аннотацию типов где это возможно

BINARE_DIVIDER = 2
OCT_DIVIDER = 8


def get_number_from_user() -> tuple[int, int]:
    info = input('Please enter a number divider. Use space between them: ')
    r, d = info.split()
    return int(r), int(d)


def converter(patient: int, divider: int):
    r: str = ''
    while patient > 0:
        r = str(patient % divider) + r
        patient //= divider
    return r


patient, divider = get_number_from_user()
if isinstance(patient, int) and divider in (BINARE_DIVIDER, OCT_DIVIDER):
    print(converter(patient, divider))
else:
    print('Sth went wrong.Try .')
print(bin(patient))
print(oct(patient))
print(hex(patient))
