# Вручную создайте список с целыми числами, которые
# повторяются. Получите новый список, который содержит
# уникальные (без повтора) элементы исходного списка.
# ✔ *Подготовьте два решения, короткое и длинное, которое
# не использует другие коллекции помимо списков.

some_list = [1, 3, 1, 3, 6, 7, 8, 5, 8]
new_list = []
for value in some_list:
    if value not in new_list:
        new_list.append(value)
print(new_list)

some_set = set(some_list)
print(list(some_set))

some_f_set = frozenset(some_list)
print(some_f_set)