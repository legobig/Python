# 1. Задание:
Есть словарь координат городов
sites = {<br>
    'Moscow': (550, 370),<br>
    'London': (510, 510),<br>
    'Paris': (480, 480),<br>
}<br><br>
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
<img width="1662" height="37" alt="image" src="https://github.com/user-attachments/assets/13411959-897d-4069-8421-894b2dee85c3" />

1.Реализован алгоритм вычисления евклидова расстояния между всеми парами городов<br>
2.Выполнено округление результатов для удобства восприятия <br>
3.Получен словарь, содержащий полную матрицу расстояний <br>
