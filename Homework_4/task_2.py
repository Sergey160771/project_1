# Напишите функцию принимающую на вход только ключевые
# параметры и возвращающую словарь, где ключ — значение
# переданного аргумента, а значение — имя аргумента. Если
# ключ не хешируем, используйте его строковое представление.


def kwargs_to_dict(**kwargs):
    result = dict()
    for key, value in kwargs.items():
        if isinstance(value, (list, dict, set)):
            value = str(value)
        result[value] = key
    return result


print(kwargs_to_dict(num1=[1, 2, 3], str2='hello', bool3=False, list4=1234, set5={'a', 'b', 'c'}))
