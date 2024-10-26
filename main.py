def repeat(n):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(n):
                result = func(*args, **kwargs)
            return result

        return wrapper

    return decorator


def greet(name):
    print(f"Hello, {name}!")

x = repeat(3)
x(greet)("xx")


