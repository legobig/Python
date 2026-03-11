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

