# Напишите однострочный генератор словаря, который принимает
# на вход три списка одинаковой длины: имена str, ставка int,
# премия str с указанием процентов вида «10.25%». В результате
# получаем словарь с именем в качестве ключа и суммой
# премии в качестве значения. Сумма рассчитывается
# как ставка умноженная на процент премии

names = ['Ваня', 'Петя', 'Вася', 'Коля']
salarys = [30000, 25000, 28000, 35000]
awards = ['7.5%', '5.8%', '10.25%', '6.3%']
wages_dict ={names[i]: salarys[i] * float(awards[i][:-1])/100 for i in range(len(names))}
print(wages_dict)