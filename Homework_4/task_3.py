# Возьмите задачу о банкомате из семинара 2. Разбейте её
# на отдельные операции — функции. Дополнительно сохраняйте
# все операции поступления и снятия средств в список.

from datetime import datetime

summa: float = 0
MIN_SUM = 50
MAX_SUM = 5000000
COMMISSION = 0.015
BONUS = 0.03
TAX = 0.10
count = 0
MIN_COMMISSION = 30
MAX_COMMISSION = 600
TEXT = 'Сумма на счёте '


def replenish(cash: float):  # Пополнение
    global summa
    global count
    summa += cash
    count += 1
    if count % 3 == 0:
        summa = summa + BONUS * summa
        print(f'Начислен процент {BONUS * summa} {TEXT} {summa}')


def take(cash: float):  # Снятие
    global summa
    global count
    summa -= cash
    count += 1
    if cash * COMMISSION < MIN_COMMISSION:
        summa -= MIN_COMMISSION
        print(f'Списан процен за снятие {MIN_COMMISSION} ')
    elif cash * COMMISSION > MAX_COMMISSION:
        summa -= MAX_COMMISSION
        print(f'Списан процен за снятие {MAX_COMMISSION} ')
    else:
        summa -= cash * COMMISSION
        print(f'Списан процен за снятие {cash * COMMISSION} ')
    if count % 3 == 0:
        summa = summa + BONUS * summa
        print(f'Начислен процент {BONUS * summa} ')
    print(f'{TEXT} {summa}')


def coming_out():  # Выход
    print("Мы будем рады видетеь Вас в следующий раз!")
    exit()


def check_multiplicity():  # Проверка кратности
    while True:
        cash = int(input(f'Введите сумму кратную {MIN_SUM} '))
        if cash % MIN_SUM == 0:
            return cash


operation_log = []

while True:
    action: str = input('Введите действие: 1 - снять, 2 - внести, 3 - история операций, 0 - выйти: ')
    if action == '1':
        if summa > MAX_SUM:
            summa = summa - summa * TAX
            print(f'Списан налог на богатых {summa * TAX} {TEXT} {summa}')
        cash = check_multiplicity()
        if cash < summa:
            take(cash)
            operation_log.append([str(datetime.today()), -1 * cash])

        else:
            print(f'У Вас не хватает денег. {TEXT} {summa}')

    elif action == '2':
        cash = check_multiplicity()
        replenish(cash)
        if summa > MAX_SUM:
            summa = summa - summa * TAX
            print(f'Списан налог на богатых {summa * TAX} {TEXT} {summa}')
        print(f'{TEXT} {summa}')
        operation_log.append([str(datetime.today()), cash])
    elif action == '0':
        coming_out()
    elif action == '3':
        print(operation_log)
