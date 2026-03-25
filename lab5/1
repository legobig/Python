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
    
