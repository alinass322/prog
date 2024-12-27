# Лабораторная работа №8
## Задание 

1. Решите обе задачи своего варианта.
2. Примените декоратор к замыканию.
3. Оформите отчёт в README.md. Отчёт должен содержать:
- Условия задач
- Описание проделанной работы
- Скриншоты результатов
- Ссылки на используемые материалы


### Вариант 4
* Замыкание, отбирающее только уникальные значения из переданных.
* Декоратор, который будет ограничивать количество вызовов функций.

### Код замыкания:

```py
def unique_values_closure():
    unique_values = set()

    def inner(*args):
        nonlocal unique_values
        unique_values.update(args)
        return list(unique_values)

    return inner
#пример
unique_values = unique_values_closure()
print(unique_values(1, 2, 3, 2, 4, 5, 3, 6))
print(unique_values(5, 6, 7, 8, 1, 2, 3, 4))
```
### Результат:


### Код декоратора:

```py
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
```
### Результат:



### Декоратор к замыканию:

```py
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
                return "Максимальное количество вызовов превышено!"
        return wrapper
    return decorator
    
def unique_values_closure():
    unique_values = set()
    @limit_calls(1)

    def inner(*args):
        nonlocal unique_values
        unique_values.update(args)
        return list(unique_values)

    return inner
unique_values = unique_values_closure()
print(unique_values(1, 2, 3, 2, 4, 5, 3, 6))
print(unique_values(5, 6, 7, 8, 1, 2, 3, 4))


``` 
### Результат:

