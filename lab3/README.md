# 1 ВАРИАНТ
# 1. Задание:
Функция для подсчёта числа элементов в списках, включая вложенные списки
# Результаты вычислений:
Рекурсия
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
Без рекурсии
```python
def f(n):
    total = 0
    s = [n]

    while s:
        current = s.pop()
        for i in current:
            total += 1
            if isinstance(i, list):
                s.append(i)
    return total
print (f([1, 2, [3, 4, [5]]]))
```
<img width="28" height="35" alt="image" src="https://github.com/user-attachments/assets/da316ad9-c1c2-4d54-9c25-fd676865d169" />




1.Рекурсивная функция содержит - двойной подсчет списков<br>
2.Стек эффективно имитирует рекурсию, но без риска переполнения <br>

# 2. Задание:
Функция для расчёта \( x_i = \frac{(i-1)x_{i-1}}{3} + \frac{(i-2)x_{i-2}}{4} \). \( x_1 = 1, x_2 = -\frac{1}{8} \).
# Результаты вычислений:
Рекурсия
```python
def f(n):
    total = 0
    s = [n]

    while s:
        current = s.pop()
        for i in current:
            total += 1
            if isinstance(i, list):
                s.append(i)
    return total
print (f([1, 2, [3, 4, [5]]]))
```

Без рекурсии
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
1. [Рекурсии в Python](https://proglib.io/p/samouchitel-po-python-dlya-nachinayushchih-chast-13-rekursivnye-funkcii-2023-01-23)
2. [Функция isinstance () в Python](https://thecode.media/funkciya-isinstance-v-python/)
