# 1 ВАРИАНТ
Генератор случайных чисел в заданном диапазоне. Не используйте готовые реализации ГПСЧ. Отфильтруйте вывод генератора, чтобы он не содержал чисел с числом делителей больше n.


# Результаты вычислений:
```python
def gen(seed):
    a = 1103515245
    c = 12345
    m = 2**32 
    while True:
        seed = (a * seed + c) % m
        yield seed
def count_del(n):
    count = 0
    for i in range(1,  n+ 1):
        if n % i == 0:
            count += 1
    return count



max_del = 6
g = gen(seed=10)
def us(x):
    return count_del(x) <= max_del

numbers = [(next(g) % 50) +1  for i in range(20)]  

result = list(filter(us, numbers))

print("Сгенерированные:", numbers)
print("После фильтрации:", result)

```
<img width="1514" height="74" alt="image" src="https://github.com/user-attachments/assets/62407969-6bf6-49d6-a1fa-a5bd83865f9f" />






1. Генератор ```gen``` является бесконечным, что позволяет получать неограниченное количество псевдослучайных чисел<br>
2. Функция ```count_del``` выполняет полный перебор делителей, что при больших значениях n может быть неэффективным, но в рамках диапазона 1–50 работает корректно <br>





# Список использованных источников:
1. [yield в Python](https://habr.com/ru/articles/132554/)
