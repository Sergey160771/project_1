# Дан список повторяющихся элементов. Вернуть список
# с дублирующимися элементами. В результирующем списке
# не должно быть дубликатов.

some_list = [1, 3, 1, 3, 6, 7, 8, 5, 8, 1, 6, 5, 5, 7, 9]
new_list = []
for item in some_list:
    if some_list.count(item) > 1:
        new_list.append(item)
print(set(new_list))
