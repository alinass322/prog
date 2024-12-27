import functools

def limit_calls(max_calls):
    def decorator(func):
        calls = 0
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            nonlocal calls
            if calls < max_calls:
                calls += 1
                return func(*args, **kwargs)
            else:
                return "Максимальное количество вызовов превышено"
        return wrapper
    return decorator

@limit_calls(3)
def limited_function():
    print("Функция была вызвана")
#пример
limited_function()  
limited_function()  
limited_function() 
limited_function()  