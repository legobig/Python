def r(times):
    def decorator(func):
        def wrapper(a1,a2):
            results = []
            for i in range(times):
                results.append(func(a1,a2))
            return results
        return wrapper
    return decorator
@r(10)
def make_add(a, b):
    
    def add():
        return a + b
    return add

print(make_add(4,3))


