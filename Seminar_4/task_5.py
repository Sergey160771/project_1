# ✔ Функция принимает на вход три списка одинаковой длины:
# ✔ имена str,
# ✔ ставка int,
# ✔ премия str с указанием процентов вида «10.25%».
# ✔ Вернуть словарь с именем в качестве ключа и суммой
# премии в качестве значения.
# ✔ Сумма рассчитывается как ставка умноженная на процент премии.

import decimal


def get_awards(names: list[str], salaries: list[int], awards: list[str]) -> dict[str:decimal.Decimal]:
    people_award = {}
    for name, salary, award in zip(names, salaries, awards):
        people_award[name] = salary * decimal.Decimal(award[:-1]) / 100
    return people_award


names = ['Петя', 'Вася', 'Ваня', 'Ирина']
salary = [10_000, 25_000, 14_000, 17_500]
award = ['9.5%', '7.85%', '12.33%', '16.66%']

print(get_awards(names, salary, award))
