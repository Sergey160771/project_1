# ✔ Самостоятельно сохраните в переменной строку текста.
# ✔ Создайте из строки словарь, где ключ — буква, а значение — код буквы.
# ✔ Напишите преобразование в одну строку.

s: str = input('Ведите строку текста: ')
dict_from_string = {l: ord(l) for l in s}
print(dict_from_string)
