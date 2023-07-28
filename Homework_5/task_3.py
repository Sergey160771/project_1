# Создайте функцию генератор чисел Фибоначчи (см. Википедию).

number_elements = int(input('Ведите необходимое количество элементов последовотельности Фибоначи: '))


def generating_fibo(number_elements: int):
    first_number = 0
    second_number = 1
    for _ in range(number_elements):
        yield first_number
        first_number, second_number = second_number, first_number + second_number


print(*generating_fibo(number_elements))
