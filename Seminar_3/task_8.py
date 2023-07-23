# Три друга взяли вещи в поход. Сформируйте
# словарь, где ключ — имя друга, а значение —
# кортеж вещей. Ответьте на вопросы:
# ✔ Какие вещи взяли все три друга
# ✔ Какие вещи уникальны, есть только у одного друга
# ✔ Какие вещи есть у всех друзей кроме одного
# и имя того, у кого данная вещь отсутствует
# ✔ Для решения используйте операции
# с множествами. Код должен расширяться
# на любое большее количество друзей.

things_friends_dict = {'Алексей': ('кружка',  'чашка', 'полатка', 'вода'),
                       'Сергей': ('кружка', 'ложка', 'чашка', 'котелок', 'еда'),
                       'Иван': ('кружка', 'ложка',  'лодка', 'вода', 'еда'),
                       'Василий': ('кружка', 'ложка', 'чашка', 'монгал', 'шампура')}


things_from_all_friends = set(things_friends_dict[list(things_friends_dict.keys())[0]])
for key, value in things_friends_dict.items():
    things_from_all_friends = things_from_all_friends.intersection(value)
print(f'Вещи которые есть у всех друзей: {things_from_all_friends}')

unique_things = []
new_dict = dict()

for value in things_friends_dict.values():
    for item in value:
        item_value = new_dict.setdefault(item, 0)
        new_dict[item] += 1
for key, value in new_dict.items():
    if value == 1:
        unique_things.append(key)
print(f'Уникальны вещи, есть только у одного друга {unique_things}')
print(new_dict)

absent_things = []
absent_friends = dict()

for key, value in new_dict.items():
    if value == (len(things_friends_dict) - 1):
        absent_things.append(key)
for item in absent_things:
    for key, value in things_friends_dict.items():
        if item not in value:
            absent_friends[key] = item
print(f'Друзья и вещи, которых у них нет{absent_friends}')

