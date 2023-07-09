# Создайте в переменной data список значений разных типов перечислив их через
# запятую внутри квадратных скобок. Для каждого элемента в цикле выведите:
# ✔ порядковый номер начиная с единицы
# ✔ значение
# ✔ адрес в памяти
# ✔ размер в памяти
# ✔ хэш объекта
# ✔ результат проверки на целое число только если он положительный
# ✔ результат проверки на строку только если он положительный
# Добавьте в список повторяющиеся элементы и сравните на результаты.

import sys

data = [1, 45, 'text', 2.12, False, False, 'text']
for i, item in enumerate(data, start=1):
    adress: int = id(item)
    syze_of_item: int = sys.getsizeof(item)
    hesh_of_item: int = hash(item)
    result: str = ''
    # if isinstance(item, int):
    if type(item) == int:
        result: str = ', This is number'
    elif isinstance(item, str):
        result: str = ', This is string'
    print(f'Номер: {i}, значение: {item}, адрес в памяти: {adress},'
          f' размер памяти: {syze_of_item}, хэш: {hesh_of_item} {result}')
