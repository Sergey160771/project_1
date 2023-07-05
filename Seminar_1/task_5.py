# Выведите в консоль таблицу умножения от 2х2 до 9х10 как на школьной тетрадке.

for i in range(2, 11):
    print()
    for j in range(2, 6):
        print(j, '*', i, '=', j * i, '   ', end=' ')
print()
for i in range(2, 11):
    print()
    for j in range(6, 10):
        print(j, '*', i, '=', j * i, '   ', end=' ')
