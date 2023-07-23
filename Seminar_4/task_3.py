# ✔ Функция получает на вход строку из двух чисел через пробел.
# ✔ Сформируйте словарь, где ключом будет
# символ из Unicode, а значением — целое число.
# ✔ Диапазон пар ключ-значение от наименьшего из введённых
# пользователем чисел до наибольшего включительно.


def get_dict_unicode_chars(str_nums: str) -> dict[str: int]:
    num_1, num_2 = map(int, str_nums.split())
    unicode_chars_dict = {}
    for i in range(min(num_1, num_2), max(num_1, num_2) + 1):
        unicode_chars_dict[chr(i)] = i
    return unicode_chars_dict


input_str = input('Ведите два числа через пробел: ')
print(get_dict_unicode_chars(input_str))
