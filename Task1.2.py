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

# Пункт А
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
sum_sound_time = 0
sum_sound_time += my_favorite_songs[2][1]
sum_sound_time += my_favorite_songs[4][1]
sum_sound_time += my_favorite_songs[7][1]
print('Три песни звучат', round(sum_sound_time, 2), 'минут')

# Пункт В
my_favorite_songs_dict = {
    'Waste a Moment': 3.03,
    'New Salvation': 4.02,
    'Staying\' Alive': 3.40,
    'Out of Touch': 3.03,
    'A Sorta Fairytale': 5.28,
    'Easy': 4.15,
    'Beautiful Day': 4.04,
    'Nowhere to Run': 2.58,
    'In This World': 4.02,
}

sum_sound_time = 0
sum_sound_time += my_favorite_songs_dict['Waste a Moment']
sum_sound_time += my_favorite_songs_dict['A Sorta Fairytale']
sum_sound_time += my_favorite_songs_dict['In This World']

print('Три песни звучат', round(sum_sound_time, 2), 'минут')

# Пункт С
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

# Пункт D
import random
import datetime

my_favorite_songs = [
    ['Waste a Moment', 3.03],
    ['New Salvation', 4.02],
    ['Staying Alive', 3.40],
    ['Out of Touch', 3.03],
    ['A Sorta Fairytale', 5.28],
    ['Easy', 4.15],
    ['Beautiful Day', 4.04],
    ['Nowhere to Run', 2.58],
    ['In This World', 4.02],
]

# Выбираем 3 случайные песни
random_songs = random.sample(my_favorite_songs, 3)

# Вычисляем общее время звучания с помощью переменной x
total_x = sum(song[1] for song in random_songs)

# Преобразуем общее время звучания в объект timedelta
x = datetime.timedelta(minutes=int(total_x), seconds=int((total_x % 1) * 60))

print("Три песни", "звучат", str(x))
