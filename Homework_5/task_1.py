# Напишите функцию, которая принимает на вход строку —
# абсолютный путь до файла. Функция возвращает кортеж из трёх
# элементов: путь, имя файла, расширение файла.

file = 'D:\\Обучение програмированию\\Программа разработчик\\Погружение в Python\\project_1\Homework_5\\task_1.py'


def parsing_path_file(file: str) -> tuple[str, str, str]:
    *path, file = file.split('\\')
    *file_name, file_extension = file.split('.')
    return '\\'.join(path), '.'.join(file_name), file_extension


print(parsing_path_file(file))
