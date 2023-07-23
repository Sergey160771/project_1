# ✔ Создайте вручную кортеж содержащий элементы разных типов.
# ✔ Получите из него словарь списков, где:
# ключ — тип элемента,
# значение — список элементов данного типа.

some_turtle = (2, -6.4, 'stping', False, 645, None, 345.2, 0.0034, '83', True)
some_dict = {}

for val in some_turtle:
    if type(val) in some_dict.keys():
        some_dict[type(val)].append(val)
    else:
        some_dict[type(val)] = [val]

print(some_dict)
