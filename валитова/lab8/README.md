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
![й1](https://github.com/user-attachments/assets/f4c1c7be-957d-48b2-9236-cbe86b0d1ff0)

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
![й2](https://github.com/user-attachments/assets/503a01a2-e33d-47ea-8304-be2768379eca)

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
![й3](https://github.com/user-attachments/assets/68f02b5c-0941-474d-913c-99e0afa92a4f)

# Ссылки на источники: 
1. https://devpractice.ru/closures-in-python/?ysclid=m4zu473ojs530173051
2. https://www.geeksforgeeks.org/python-closures/?ysclid=m4zu4jyfao245740076
3. https://wiki.python.org/moin/PythonDecorators




