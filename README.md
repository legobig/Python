# 1. Задание:
Есть словарь координат городов
sites = {
    'Moscow': (550, 370),
    'London': (510, 510),
    'Paris': (480, 480),
}
Составим словарь словарей расстояний между ними
# Результаты вычислений:
```python
sites = {
    'Moscow': (550, 370),
    'London': (510, 510),
    'Paris': (480, 480),
}

distances = {}

for city1 in sites:
    for city2 in sites:
        x1,y1=sites[city1]
        x2,y2=sites[city2]
        dist = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
        distances[city1,city2]= round(dist, 2)
print(distances)
```
<img width="1671" height="1550" alt="image" src="https://github.com/user-attachments/assets/33387592-b69f-49ed-82ad-db5d2600c67d" />


1.Реализован алгоритм вычисления евклидова расстояния между всеми парами городов
2.Выполнено округление результатов для удобства восприятия
3.Получен словарь, содержащий полную матрицу расстояний

# 2. Задание:
Есть значение радиуса круга
radius = 42
Выведите на консоль значение прощади этого круга с точностю до 4-х знаков после запятой
Далее, пусть есть координаты точки
point_1 = (23, 34)
Если точка point лежит внутри того самого круга [центр в начале координат (0, 0), radius = 42],
то выведите на консоль True, Или False, если точка лежит вовне круга.
Аналогично для другой точки
point_2 = (30, 30)

# Результаты вычислений:
```python
from math import*
radius=42
pi=3.1415926
S=radius**2*pi
print(round(S,4))
point_1 = (23, 34)
distance_1=sqrt(point_1[0]**2+point_1[1]**2)
print(distance_1 <= radius)
point_2 = (30, 30)
distance_2=sqrt(point_2[0]**2+point_2[1]**2)
print(distance_2 <= radius)
```
Площадь круга вычислена корректно с заданной точностью
Для проверки принадлежности точки кругу корректнее использовать сравнение квадратов расстояний: x² + y² ≤ R², чтобы избежать погрешностей при извлечении корня

# 3. Задание:
Расставьте знаки операций "плюс", "минус", "умножение" и скобки
между числами "1 2 3 4 5" так, что бы получилось число "25".
Использовать нужно только указанные знаки операций, но не обязательно все перечесленные.
Порядок чисел нужно сохранить.

# Результаты вычислений:
Путём подбора было найдено выражение:
```python
result =1*(2+3)+4*5
print(result)
```
# 4. Задание:
Есть строка с перечислением фильмов
my_favorite_movies = 'Терминатор, Пятый элемент, Аватар, Чужие, Назад в будущее'
Выведите на консоль с помощью индексации строки, последовательно:
#первый фильм
#последний
#второй
#второй с конца

# Результаты вычислений:
```python
my_favorite_movies = 'Терминатор, Пятый элемент, Аватар, Чужие, Назад в будущее'
print(my_favorite_movies[:10])

print(my_favorite_movies[-15:])

print(my_favorite_movies[12:25])

print(my_favorite_movies[-22:-17])
```
1.В данном задании индексы подобраны вручную на основе фиксированной структуры строки
2.При работе с реальными данными, где позиции могут меняться, предпочтительнее использовать методы split(), find() или регулярные выражения

# 5. Задание:
Создайте списки:
моя семья
список списков приблизителного роста членов вашей семьи
Выведите на консоль рост отца в формате
Выведите на консоль общий рост вашей семьи как сумму ростов всех членов

# Результаты вычислений:
```python
my_family = ['папа', 'мама', 'брат', 'бабушка']

my_family_height = [
    ['папа', 180],
    ['мама', 165],
    ['сестра', 170],
    ['бабушка', 160],
]

print('Рост отца - ',my_family_height[0][1],'см')
height = 0
for person in my_family_height:
    height += person[1]
print('Общий рост моей семьи -',height,'см')
```
1.Освоены базовые операции со вложенными списками
2.Реализован перебор элементов списка с накоплением суммы

# 6. Задание:
Есть список животных в зоопарке
zoo = ['lion', 'kangaroo', 'elephant', 'monkey', ]
посадите медведя (bear) между львом и кенгуру и выведите список на консоль
добавьте птиц из списка birds в последние клетки зоопарка
birds = ['rooster', 'ostrich', 'lark', ] и выведите список на консоль
уберите слона и выведите список на консоль
выведите на консоль в какой клетке сидит лев и жаворонок 

# Результаты вычислений:
```python
zoo = ['lion', 'kangaroo', 'elephant', 'monkey', ]
zoo.insert(1, 'bear')
print(zoo)
birds = ['rooster', 'ostrich', 'lark', ]
zoo.extend(birds)
print(zoo)
zoo.remove('elephant')
print(zoo)
lion_index = zoo.index('lion') + 1
lark_index = zoo.index('lark') + 1
print('Лев-',lion_index)
print('Жаворонок-',lark_index)
```
1.Освоены основные методы работы со списками: insert(), extend(), remove(), index()

# 7. Задание:
Есть список песен группы Depeche Mode со временем звучания с точностью до долей минут
Точность указывается в функции round(a, b)
где a, это число которое надо округлить, а b количество знаков после запятой
более подробно про функцию round смотрите в документации
violator_songs_list = [
    ['World in My Eyes', 4.86],
    ['Sweetest Perfection', 4.43],
    ['Personal Jesus', 4.56],
    ['Halo', 4.9],
    ['Waiting for the Night', 6.07],
    ['Enjoy the Silence', 4.20],
    ['Policy of Truth', 4.76],
    ['Blue Dress', 4.29],
    ['Clean', 5.83],
]
распечатайте общее время звучания трех песен: 'Halo', 'Enjoy the Silence' и 'Clean' в формате

# Результаты вычислений:
```python
violator_songs_list = [
    ['World in My Eyes', 4.86],
    ['Sweetest Perfection', 4.43],
    ['Personal Jesus', 4.56],
    ['Halo', 4.9],
    ['Waiting for the Night', 6.07],
    ['Enjoy the Silence', 4.20],
    ['Policy of Truth', 4.76],
    ['Blue Dress', 4.29],
    ['Clean', 5.83],
]
halo= violator_songs_list[3][1]
enjoy= violator_songs_list[5][1]
clean= violator_songs_list[8][1]

total = halo + enjoy + clean
total_time= round(total, 2)

print('Три песни звучат',total_time,'минут')
violator_songs_dict = {
    'World in My Eyes': 4.76,
    'Sweetest Perfection': 4.43,
    'Personal Jesus': 4.56,
    'Halo': 4.30,
    'Waiting for the Night': 6.07,
    'Enjoy the Silence': 4.6,
    'Policy of Truth': 4.88,
    'Blue Dress': 4.18,
    'Clean': 5.68,
}
sweetest= violator_songs_dict['Sweetest Perfection']
policy= violator_songs_dict['Policy of Truth']
blue= violator_songs_dict['Blue Dress']
total = sweetest + policy + blue
total_time= round(total, 2)
print('А другие три песни звучат',total_time,'минут')
```
1.Освоены два способа хранения данных: списки и словари
2.Преимущества словарей при работе с именованными данными — код становится более понятным и устойчивым к изменениям порядка элементов

# 8. Задание:
Есть зашифрованное сообщение
secret_message = [
    'квевтфпп6щ3стмзалтнмаршгб5длгуча',
    'дьсеы6лц2бане4т64ь4б3ущея6втщл6б',
    'т3пплвце1н3и2кд4лы12чф1ап3бкычаь',
    'ьд5фму3ежородт9г686буиимыкучшсал',
    'бсц59мегщ2лятьаьгенедыв9фк9ехб1а',]
Нужно его расшифровать и вывести на консоль в удобочитаемом виде.
Ключ к расшифровке:
первое слово - 4-я буква
второе слово - буквы с 10 по 13, включительно
третье слово - буквы с 6 по 15, включительно, через одну
четвертое слово - буквы с 8 по 13, включительно, в обратном порядке
пятое слово - буквы с 17 по 21, включительно, в обратном порядке

# Результаты вычислений:
```python
secret_message = [
    'квевтфпп6щ3стмзалтнмаршгб5длгуча',
    'дьсеы6лц2бане4т64ь4б3ущея6втщл6б',
    'т3пплвце1н3и2кд4лы12чф1ап3бкычаь',
    'ьд5фму3ежородт9г686буиимыкучшсал',
    'бсц59мегщ2лятьаьгенедыв9фк9ехб1а',
]
w1 = secret_message[0][3]
w2 = secret_message[1][9:13]
w3 = secret_message[2][5:15:2]
w4 = secret_message[3][7:13][::-1]
w5 = secret_message[4][16:21][::-1]
result = f"{w1} {w2} {w3} {w4} {w5}"
print(result)
```
1.Освоены различные приёмы работы со срезами строк

# 9. Задание:
В саду сорвали цветы
garden = ('ромашка', 'роза', 'одуванчик', 'ромашка', 'гладиолус', 'подсолнух', 'роза', )
на лугу сорвали цветы
meadow = ('клевер', 'одуванчик', 'ромашка', 'клевер', 'мак', 'одуванчик', 'ромашка', )
создайте множество цветов, произрастающих в саду и на лугу
garden_set =
meadow_set =
выведите на консоль все виды цветов
#выведите на консоль те, которые растут и там и там
выведите на консоль те, которые растут в саду, но не растут на лугу
выведите на консоль те, которые растут на лугу, но не растут в саду

# Результаты вычислений:
```python
garden = ('ромашка', 'роза', 'одуванчик', 'ромашка', 'гладиолус', 'подсолнух', 'роза', )
meadow = ('клевер', 'одуванчик', 'ромашка', 'клевер', 'мак', 'одуванчик', 'ромашка', )
garden_set = set(garden)
meadow_set = set(meadow)
print("Все виды цветов:", garden_set | meadow_set)

print("Цветы, которые растут и в саду, и на лугу:", garden_set & meadow_set)


print("Цветы, которые растут только в саду:", garden_set - meadow_set)


print("Цветы, которые растут только на лугу:", meadow_set - garden_set)
```
1.Освоены основные операции над множествами


# 10. Задание:
Есть словарь магазинов с распродажами
shops = {
    'ашан':
        [
            {'name': 'печенье', 'price': 10.99},
            {'name': 'конфеты', 'price': 34.99},
            {'name': 'карамель', 'price': 45.99},
            {'name': 'пирожное', 'price': 67.99}
        ],
    'пятерочка':
        [
            {'name': 'печенье', 'price': 9.99},
            {'name': 'конфеты', 'price': 32.99},
            {'name': 'карамель', 'price': 46.99},
            {'name': 'пирожное', 'price': 59.99}
        ],
    'магнит':
        [
            {'name': 'печенье', 'price': 11.99},
            {'name': 'конфеты', 'price': 30.99},
            {'name': 'карамель', 'price': 41.99},
            {'name': 'пирожное', 'price': 62.99}
        ],
}
Создайте словарь цен на продкты следующего вида

# Результаты вычислений:
```python
shops = {
    'ашан':
        [
            {'name': 'печенье', 'price': 10.99},
            {'name': 'конфеты', 'price': 34.99},
            {'name': 'карамель', 'price': 45.99},
            {'name': 'пирожное', 'price': 67.99}
        ],
    'пятерочка':
        [
            {'name': 'печенье', 'price': 9.99},
            {'name': 'конфеты', 'price': 32.99},
            {'name': 'карамель', 'price': 46.99},
            {'name': 'пирожное', 'price': 59.99}
        ],
    'магнит':
        [
            {'name': 'печенье', 'price': 11.99},
            {'name': 'конфеты', 'price': 30.99},
            {'name': 'карамель', 'price': 41.99},
            {'name': 'пирожное', 'price': 62.99}
        ],
}
sweets = {
    'печенье': [
        {'shop': 'пятерочка', 'price': 9.99},
        {'shop': 'ашан', 'price': 10.99},
    ],
    'конфеты': [
        {'shop': 'магнит', 'price': 30.99},
        {'shop': 'пятерочка', 'price': 32.99},
    ],
    'карамель': [
        {'shop': 'магнит', 'price': 41.99},
        {'shop': 'ашан', 'price': 45.99},
    ],
    'пирожное': [
        {'shop': 'пятерочка', 'price': 59.99},
        {'shop': 'магнит', 'price': 62.99},
    ],
}

print(sweets)
```
1.Реализован алгоритм, корректно обрабатывающий все продукты из всех магазинов
2.Полученная структура позволяет легко анализировать цены на конкретные продукты в разных магазинах

# 11. Задание:
Есть словарь кодов товаров

goods = {
    'Лампа': '12345',
    'Стол': '23456',
    'Диван': '34567',
    'Стул': '45678',
}

Есть словарь списков количества товаров на складе.

store = {
    '12345': [
        {'quantity': 27, 'price': 42},
    ],
    '23456': [
        {'quantity': 22, 'price': 510},
        {'quantity': 32, 'price': 520},
    ],
    '34567': [
        {'quantity': 2, 'price': 1200},
        {'quantity': 1, 'price': 1150},
    ],
    '45678': [
        {'quantity': 50, 'price': 100},
        {'quantity': 12, 'price': 95},
        {'quantity': 43, 'price': 97},
    ],
}

Рассчитать на какую сумму лежит каждого товара на складе
Вывести стоимость каждого вида товара на складе

# Результаты вычислений:
```python
goods = {
    'Лампа': '12345',
    'Стол': '23456',
    'Диван': '34567',
    'Стул': '45678',
}
store = {
    '12345': [
        {'quantity': 27, 'price': 42},
    ],
    '23456': [
        {'quantity': 22, 'price': 510},
        {'quantity': 32, 'price': 520},
    ],
    '34567': [
        {'quantity': 2, 'price': 1200},
        {'quantity': 1, 'price': 1150},
    ],
    '45678': [
        {'quantity': 50, 'price': 100},
        {'quantity': 12, 'price': 95},
        {'quantity': 43, 'price': 97},
    ],
}

lamp_code = goods['Лампа']
lamp_qty = store[lamp_code][0]['quantity']
lamp_price = store[lamp_code][0]['price']
lamp_cost = lamp_qty * lamp_price
print('Лампа - ',lamp_qty,' шт, стоимость ',lamp_cost,' руб')

table_code = goods['Стол']
table_qty1 = store[table_code][0]['quantity']
table_price1 = store[table_code][0]['price']
table_cost1 = table_qty1 * table_price1
table_qty2 = store[table_code][1]['quantity']
table_price2 = store[table_code][1]['price']
table_cost2 = table_qty2 * table_price2
table_qty = table_qty1 + table_qty2
table_cost = table_cost1 + table_cost2
print('Стол - ',table_qty,' шт, стоимость ',table_cost,' руб')

sofa_code = goods['Диван']
sofa_qty1 = store[sofa_code][0]['quantity']
sofa_price1 = store[sofa_code][0]['price']
sofa_cost1 = sofa_qty1 * sofa_price1
sofa_qty2 = store[sofa_code][1]['quantity']
sofa_price2 = store[sofa_code][1]['price']
sofa_cost2 = sofa_qty2 * sofa_price2
sofa_qty = sofa_qty1 + sofa_qty2
sofa_cost = sofa_cost1 + sofa_cost2
print('Диван - ',sofa_qty,' шт, стоимость ',sofa_cost,' руб')

chair_code = goods['Стул']
chair_qty1 = store[chair_code][0]['quantity']
chair_price1 = store[chair_code][0]['price']
chair_cost1 = chair_qty1 * chair_price1
chair_qty2 = store[chair_code][1]['quantity']
chair_price2 = store[chair_code][1]['price']
chair_cost2 = chair_qty2 * chair_price2
chair_qty3 = store[chair_code][2]['quantity']
chair_price3 = store[chair_code][2]['price']
chair_cost3 = chair_qty3 * chair_price3
chair_qty = chair_qty1 + chair_qty2 + chair_qty3
chair_cost = chair_cost1 + chair_cost2 + chair_cost3
print('Стул - ',chair_qty,' шт, стоимость ',chair_cost,' руб')
```
1.Освоены механизмы доступа к данным во вложенных структурах
2.Недостаток такой реализации - дубликация одной и той же логики

# Список использованных источников:
1. [Python](https://www.python.org/)
