# Лабораторная работа №9

## Задание 
Сложность:  Rare
* Решите задачу своего варианта.
* Оформите отчёт в README.md. Отчёт должен содержать:
* Условия задач
* Описание проделанной работы
* Скриншоты результатов
* Ссылки на используемые материалы

### Вариант 4

* Генератор, создающий все возможные уникальные комбинации элементов из нескольких последовательностей.

### Код:

```py
import itertools

def generate_combinations(*args):
    for combination in itertools.product(*args):
                yield combination
seq1 = [1, 2, 3]
seq2 = ['a', 'b', 'c', 'd']
seq3 = ('x','y')
combinations = generate_combinations(seq1,seq2, seq3)
for combo in combinations:
    print(combo)
```

### Результат:
![1](https://github.com/user-attachments/assets/46855538-3869-4a2a-8d54-1d5254899be8)
![2](https://github.com/user-attachments/assets/051f0dab-0c06-4b6a-aa77-c390999269da)
![3](https://github.com/user-attachments/assets/7e91a621-ed33-4757-ab33-4fa7d20cab74)

# Ссылки на источники:
1. https://www.geeksforgeeks.org/generators-in-python/?ysclid=m4zu7cyf3t143309374
2. https://stackabuse.com/python-generators/
3. https://realpython.com/introduction-to-python-generators/





