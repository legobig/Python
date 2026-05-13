from functools import wraps
def r(func=None, times=1, a1=None, a2=None):
    def decorator(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            results = []
            for i in range(times):
                if a1 is not None and a2 is not None:
                    results.append(f(a1, a2))
                else:
                    results.append(f(*args, **kwargs))
            return results
        return wrapper
    if callable(func):
        return decorator(func)
    else:
        return decorator
@r(times=10, a1=4, a2=3)
def add(a, b):
    return a + b
print(add())

@r
def add(a, b):
    return a + b
print(add(4, 3))
