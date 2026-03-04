# 1 ВАРИАНТ
# 1. Задание:
Функция для подсчёта числа элементов в списках, включая вложенные списки
# Результаты вычислений:
```python
def f(x):
    total = 0
    for i in x:
        total+=1
        if isinstance(i, list):
            total += f(i)
    return total
print (f([1, 2, [3, 4, [5]]]))
print(k)    
```
<img width="28" height="35" alt="image" src="https://github.com/user-attachments/assets/da316ad9-c1c2-4d54-9c25-fd676865d169" />




1.Реализован полный перебор всех 5-буквенных комбинаций с помощью ```product```<br>
2.Получено итоговое число допустимых кодов <br>

# 2. Задание:
Функция для расчёта \( x_i = \frac{(i-1)x_{i-1}}{3} + \frac{(i-2)x_{i-2}}{4} \). \( x_1 = 1, x_2 = -\frac{1}{8} \).
# Результаты вычислений:
```python
def f(n):
    if n == 1:
        return 1
    if n == 2:
        return -1/8
    x_pred = 1  
    x_pos = -1/8     
    for i in range(3,n+1):
        x = ((i-1)*x_pos)/3 + ((i - 2) * x_pred)/4
        x_pred=x_pos
        x_pos=x
    return x_pos
print(f(3))
```
<img width="315" height="42" alt="image" src="https://github.com/user-attachments/assets/fa71fe8a-3d28-4239-9f56-9a7d00ed529e" />




1.Число переведено в двоичную систему функцией ```bin```<br>
2.Из двоичной записи удалён префикс ```0b```<br>
3.Получено итоговое число единиц в двоичном представлении<br>



# Список использованных источников:
1. [Itertools в Python](https://habr.com/ru/companies/otus/articles/529356/)
2. [Пример отчёта в Markdown](https://github.com/still-coding/report_demo?tab=readme-ov-file)
