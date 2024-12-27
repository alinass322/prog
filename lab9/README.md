# Лабораторная работа №9

## Задание 

Сложность: Rare

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

