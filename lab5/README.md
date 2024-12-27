# Лабораторная работа №5

## Задание 
1) Создайте в каталоге для данной ЛР в своём репозитории виртуальное окружение и установите в него ```matplotlib``` и ```numpy```. Создайте файл ```requirements.txt```.
2) Откройте книгу [1] и выполните уроки 1-3. Первый урок можно начинать со стр. 8.
3) Выберите одну из неразрывных функции своего варианта из лабораторной работы №2, постройте график этой функции и касательную к ней. Добавьте на график заголовок, подписи осей, легенду, сетку, а также аннотацию к точке касания.
4) Добавьте в корень своего репозитория файл .gitignore отсюда, перед тем как делать очередной коммит.
5) Оформите отчёт в README.md. Отчёт должен содержать:
- графики, построенные во время выполнения уроков из книги
- объяснения процесса решения и график по заданию 4
6) Склонируйте этот репозиторий НЕ в ваш репозиторий, а рядом. Изучите использование этого инструмента и создайте pdf-версию своего отчёта из README.md. Добавьте её в репозиторий.



## Уроки
### Урок 1.2
``` python
import matplotlib.pyplot as plt

plt.plot([1,2,3,4,5],[1,2,3,4,5])
plt.show()
```
![1 y](https://github.com/user-attachments/assets/b43c4990-6d4a-4852-8f5c-d80e590d2a6c)

### Урок 1.3

``` python
import matplotlib.pyplot as plt
import numpy as np

# Независимая (x) и зависимая (y) переменные
x = np.linspace(0, 10, 50)
y = x
# Построение графика
plt.title('Линейная зависимость y = x') # заголовок
plt.xlabel('x') # ось абсцисс
plt.ylabel('y') # ось ординат
plt.grid()      
# включение отображение сетки
plt.plot(x, y)  # построение графика
plt.show()
```
![2 y](https://github.com/user-attachments/assets/b3365714-5660-4585-b2ad-1b7fe030183f)

### Урок 1.4
``` python
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0,10,50)
y1 = x #линейная зависимость
y2 = [i**2 for i in x] #квадратичная зависимость

plt.title('Зависимость: y1 = x, y2 = x^2') #заголовок
plt.xlabel('x') # ось абсцисс
plt.ylabel('y1, y2') # ось ординат   
plt.grid() # включение отображение сетки
plt.plot(x, y1, x, y2) # построение графика
plt.show()
```
![3 y](https://github.com/user-attachments/assets/15de4177-353f-48e8-878d-20dc743f5995)

### Урок 1.5
``` python
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0,10,50)
y1 = x #линейная зависимость
y2 = [i**2 for i in x] #квадратичная зависимость

plt.figure(figsize=(9, 9)) #построение графика
plt.subplot(2, 1, 1)
plt.plot(x, y1) #построение графика            
plt.title('Зависимости: y1 = x, y2 = x^2') #заголовок
plt.ylabel('y1', fontsize=14) #ось ординат
plt.grid(True) #ось ординат    

plt.subplot(2, 1, 2)
plt.plot(x, y2) #gостроение графика         
plt.xlabel('x', fontsize=14) #ось абсцисс   
plt.ylabel('y2', fontsize=14) #ось ординат  
plt.grid(True) #включение отображение сетки                 

plt.show()
```
![4 y](https://github.com/user-attachments/assets/8aec0c86-af09-48ca-b550-bf52ff42ee7d)


### Урок 1.6
``` python
import matplotlib.pyplot as plt

fruits = ['apple', 'peach', 'orange', 'bannana', 'melon'] #название фруктов
counts = [34, 25, 43, 31, 17] #количество фруктов
plt.bar(fruits, counts) #построение вертикальной столбчатой диаграммы
plt.title('Fruits!') #заголовок
plt.xlabel('Fruit') #ось абцисс
plt.ylabel('Count') #ось ординат
plt.show()
```
![5 y](https://github.com/user-attachments/assets/1bc58565-0c93-4efe-b0b8-a5e32374f40d)

### Урок 2.1 и 2.2
``` python
import matplotlib.pyplot as plt

x = [1, 5, 10, 15, 20]
y = [1, 7, 3, 5, 11]
plt.plot(x, y, label = 'steel price') #по оси ординат (ось y), а по оси абсцисс (ось x) будут отложены индексы элементов массива
plt.xlabel('Day', fontsize=15, color='blue')
plt.title('График', fontsize=17)
plt.ylabel('Price', fontsize=15, color='blue')
plt.legend()
plt.grid(True)
plt.text(15, 4, 'grow up!')
plt.show()
```
![6 y](https://github.com/user-attachments/assets/65b48d14-b2b8-4d21-a584-aa4215b20b23)

### Урок 2.3
``` python
import matplotlib.pyplot as plt

x = [1, 5, 10, 15, 20]
y = [1, 7, 3, 5, 11]
plt.plot(x, y, '--r')
plt.show()
```
![7 y](https://github.com/user-attachments/assets/db4c7d98-0bf9-4649-97de-43e21ef8c50d)

### Урок 2.4
``` python
import matplotlib.pyplot as plt

x = [1, 5, 10, 15, 20]
y1 = [1, 7, 3, 5, 11]
y2 = [i*1.2 + 1 for i in y1]
y3 = [i*1.2 + 1 for i in y2]
y4 = [i*1.2 + 1 for i in y3]
# Настройка размеров подложки
plt.figure(figsize=(12, 7))
plt.subplot(2, 2, 1)
plt.plot(x, y1, '-')
plt.subplot(2, 2, 2)
plt.plot(x, y2, '--')
plt.subplot(2, 2, 3)
plt.plot(x, y3, '-.')
plt.subplot(2, 2, 4)
plt.plot(x, y4, ':')
plt.show()
```
![8 y](https://github.com/user-attachments/assets/7d549b9d-76ff-4528-b37c-ae4aa1bd3a95)

### Урок 2.5
``` python
import matplotlib.pyplot as plt

x = [1, 5, 10, 15, 20]
y1 = [1, 7, 3, 5, 11]
y2 = [i*1.2 + 1 for i in y1]
y3 = [i*1.2 + 1 for i in y2]
y4 = [i*1.2 + 1 for i in y3]
plt.plot(x, y1, '-', x, y2, '--', x, y3, '-.', x, y4, ':')
plt.show()
```

![9 y](https://github.com/user-attachments/assets/df582d17-7180-40f8-8cbe-7a75d6d2b4d7)

### Урок 3.1
``` python
import matplotlib.pyplot as plt

locs = ['best', 'upper right', 'upper left', 'lower left',
'lower right', 'right', 'center left', 'center right',
'lower center', 'upper center', 'center']
x = [1, 5, 10, 15, 20]
y1 = [1, 7, 3, 5, 11]
y2 = [4, 3, 1, 8, 12]
plt.figure(figsize=(12, 12))
for i in range(3):
    for j in range(4):
        if i*4+j < 11:
           plt.subplot(3, 4, i*4+j+1)
           plt.title(locs[i*4+j])
           plt.plot(x, y1, 'o-r', label='line 1')
           plt.plot(x, y2, 'o-.g', label='line 2')
           plt.legend(loc=locs[i*4+j])
        else:
            break
plt.show()
```
![10 y](https://github.com/user-attachments/assets/d5128e58-48a4-4dd6-a3d0-9a9bfa756acb)

## Задание варианта
```python
import math
import matplotlib.pyplot as plt
import numpy as np

def f(x):
    return math.exp(-x - 1/2)

x = np.linspace(1, 4, 100)

y = [f(i) for i in x]

w = 2.3

plt.plot(x, y, label="e^(-x-1/2)")

def df(x):
    return -math.exp(-x - 1/2)

tangent_slope = df(w)

tangent = [f(w) + tangent_slope*(i - w) for i in x]

plt.plot(x, tangent, label="kasatelnaya x=2.3")
plt.plot(w, f(w), "ro")

plt.xlabel('x')
plt.ylabel('y')
plt.legend()

plt.show()
```

![gr](https://github.com/user-attachments/assets/38539215-b3cc-4b6d-9646-245d99dcfc66)






















































































