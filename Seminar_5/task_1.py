# ✔ Пользователь вводит строку из четырёх
# или более целых чисел, разделённых символом “/”.
# Сформируйте словарь, где:
# ✔второе и третье число являются ключами.
# ✔первое число является значением для первого ключа.
# ✔четвертое и все возможные последующие числа
# хранятся в кортеже как значения второго ключа.

s: str = input('Enter datas: ')
value_1, key_1, key_2, *value_2 = s.split('/')
dict_res = {int(key_1): int(value_1), int(key_2): tuple(map(int, value_2))}
print(dict_res)

