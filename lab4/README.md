# 1 ВАРИАНТ
# 1. Задание:
Замыкание-калькулятор, накапливающее результат и поддерживающее 4 арифметичесике операции:
```python
>>> calc = make_calc("*", initial=1)
>>> calc(5)
5
>>> calc(2)
10
```
# Результаты вычислений:
```python
import operator
def make_calc(op, i=0):
    ops = {"+": operator.add,"-": operator.sub,
           "*": operator.mul,"/": operator.truediv}

    result = i

    def calc(value):
        nonlocal result
        result = ops[op](result, value)
        return result

    return calc
c = make_calc("*", i=1)
print(c(5))
print(c(2))
print(c(5))  
```
<img width="41" height="91" alt="image" src="https://github.com/user-attachments/assets/514eb574-47d7-46b0-a6a8-5e530c45571c" />





1. Внутренняя функция calc сохраняет доступ к переменной result даже после завершения внешней функции make_calc<br>
2. Каждый вызов изменяет сохранённое значение <br>

# 2. Задание:
Декоратор, который будет запускать функцию указанное число раз с указанными параметрами и возвращать последвательность результатов.
# Результаты вычислений:
Рекурсия
```python
def r(times, a1,a2):
    def decorator(func):
        def wrapper():
            results = []
            for i in range(times):
                results.append(func(a1,a2))
            return results
        return wrapper
    return decorator
@r(10, 4, 3)
def add(a, b):
    return a + b
print(add())
```

<img width="492" height="41" alt="image" src="https://github.com/user-attachments/assets/f0daf3ce-a7e1-4cce-801a-e4f933a73034" />






1.Функция add() вызывается без аргументов, хотя исходная функция требует два параметра<br>
2.Все результаты сохраняются в список, даже если они одинаковые<br>



# Список использованных источников:
1. [Operator в Python](https://proglib.io/p/samouchitel-po-python-dlya-nachinayushchih-chast-13-rekursivnye-funkcii-2023-01-23)
2. [Декораторы в Python](https://tproger.ru/translations/demystifying-decorators-in-python)
