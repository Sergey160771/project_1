# ✔ Продолжаем развивать задачу 2.
# ✔ Возьмите словарь, который вы получили.
# Сохраните его итераторатор.
# ✔ Далее выведите первые 5 пар ключ-значение,
# обращаясь к итератору, а не к словарю.

s: str = input('Ведите строку текста: ')
res_dict = {}
for l in s:
    res_dict[l] = ord(l)
print(res_dict)

NOW_MANY_PAIRS_NEEDED = 5

iter_from_dict = iter(res_dict.items())
for _ in range(NOW_MANY_PAIRS_NEEDED):
    print(next(iter_from_dict))


