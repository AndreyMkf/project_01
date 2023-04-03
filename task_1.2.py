# Задача 1.2.

# Пункт A. 
# Приведем плейлист песен в виде списка списков
# Список my_favorite_songs содержит список названий и длительности каждого трека
# Выведите общее время звучания трех случайных песен в формате
# Три песни звучат ХХХ минут

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

# Пункт B. 
# Есть словарь песен 
# Распечатайте общее время звучания трех случайных песен
# Вывод: Три песни звучат ХХХ минут.

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

# Дополнительно для пунктов A и B
# Пункт C.
# Сгенерируйте случайные песни с помощью модуля random
# import random

# Дополнительно 
# Пункт D.
# Переведите минуты и секунды в формат времени. Используйте модуль datetime 


# Сделано

  Пункт A:

import random

songs = random.sample(my_favorite_songs, 3)
total_time = sum(song[1] for song in songs)
print(f"Три песни звучат {total_time:.0f} минут")


Пункт B:

import random

songs = random.sample(list(my_favorite_songs_dict.items()), 3)
total_time = sum(song[1] for song in songs)
print(f"Три песни звучат {total_time:.0f} минут")


Пункт C:

import random

song_names = ['Song 1', 'Song 2', 'Song 3', 'Song 4', 'Song 5', 'Song 6']
songs = [(name, random.randint(180, 360)) for name in song_names]

Пункт D:

import datetime

total_time = datetime.timedelta(seconds=int(total_time * 60))
print(f"Три песни звучат {total_time}")

# Все отлично) я сделал немного иначе
from datetime import timedelta
from math import modf
from random import sample


total_time = timedelta()

for song in sample(my_favorite_songs, 3):
    s, m = modf(song[1])
    total_time += timedelta(minutes=int(m), seconds=int(s * 100))

print(f'Три песни звучат {total_time} минут')
