# Задача 1.2.
# Пункт A.
# Приведем плейлист песен в виде списка списков
# Список my_favorite_songs содержит список названий и длительности каждого трека
# Выведите общее время звучания трех случайных песен в формате
# Три песни звучат ХХХ минут
# my_favorite_songs = [ ['Waste a Moment', 3.03], ['New Salvation', 4.02], ['Staying' Alive', 3.40], ['Out of Touch', 3.03], ['A Sorta Fairytale', 5.28], ['Easy', 4.15], ['Beautiful Day', 4.04], ['Nowhere to Run', 2.58], ['In This World', 4.02], ]

# Пункт B.
# Есть словарь песен
# Распечатайте общее время звучания трех случайных песен
# Вывод: Три песни звучат ХХХ минут.
# my_favorite_songs_dict = { 'Waste a Moment': 3.03, 'New Salvation': 4.02, 'Staying' Alive': 3.40, 'Out of Touch': 3.03, 'A Sorta Fairytale': 5.28, 'Easy': 4.15, 'Beautiful Day': 4.04, 'Nowhere to Run': 2.58, 'In This World': 4.02, }

# Дополнительно для пунктов A и B
# Пункт C.
# Сгенерируйте случайные песни с помощью модуля random
# import random
# Дополнительно
# Пункт D.
# Переведите минуты и секунды в формат времени. Используйте модуль datetime

my_favorite_songs = [
    ['Waste a Moment', 3.03],
    ['New Salvation', 4.02],
    ['Staying\' Alive', 3.40],
    ['Out of Touch', 3.03],
    ['A Sorta Fairytale', 5.28],
    ['Easy', 4.15],
    ['Beautiful Day', 4.04],
    ['Nowhere to Run', 2.58],
    ['In This World', 4.02],
]
print(len(my_favorite_songs))

import random
random.choice(my_favorite_songs)
# print(random.choice(my_favorite_songs))
a = random.choice(my_favorite_songs)
b = random.choice(my_favorite_songs)
c = random.choice(my_favorite_songs)

print(a)
print(b)
print(c)

my_favorite_songs = [
    ['Waste a Moment', 3.03],
    ['New Salvation', 4.02],
    ['Staying\' Alive', 3.40],
    ['Out of Touch', 3.03],
    ['A Sorta Fairytale', 5.28],
    ['Easy', 4.15],
    ['Beautiful Day', 4.04],
    ['Nowhere to Run', 2.58],
    ['In This World', 4.02],
]
import random
random.choice(my_favorite_songs)
# print(random.choice(my_favorite_songs))
a = random.choice(my_favorite_songs)
b = random.choice(my_favorite_songs)
c = random.choice(my_favorite_songs)
sum_my_favorite_songs = 0
sum_my_favorite_songs += a [1]
sum_my_favorite_songs += b [1]
sum_my_favorite_songs += c [1]

print('Три песни звучат', round(sum_my_favorite_songs, 2), 'минут')