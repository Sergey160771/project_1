# ✔ Создайте функцию-генератор.
# ✔ Функция генерирует N простых чисел,
# начиная с числа 2.
# ✔ Для проверки числа на простоту используйте
# правило: «число является простым, если делится
# нацело только на единицу и на себя».

def get_primes_from_2_to_N(n: int):
    count: int = 2
    while 1 < count <= n:
        is_prime: bool = True
        for i in range(2, count // 2 + 1):
            if count % i == 0:
                count += 1
                is_prime = False
                break
        if is_prime:
            yield count
            count += 1


for n in get_primes_from_2_to_N(29):
    print(n, end=" ")

