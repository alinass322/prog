# Лабораторная работа №1
## Задания для самостоятельного выполнения
### Сложность:
### Rare
### 1.Разберите код программы из примера.
### 2.Составьте блок-схему алгоритма для своего варианта.
### 3.Напишите программу, решающую задачу по своему варианту.
### 4.Оформите отчёт в README.md. Отчёт должен содержать:
* Задание
* Описание проделанной работы
* Скриншоты результатов
* Блок-схему
* Ссылки на используемые материалы
## Ход работы:
### 1.Разобрать код программы из примера.
### 2.Составить блок-схему Алгоритма решения варианта №4

### 3.Написать программу, решающую задачу по своему варианту.
## Задача

### Код для решение данной задачи:
```c
#include <stdio.h>

int main() {
    float a1, a2, a3;
    
    printf("Enter a1 -> ");
    scanf("%f", &a1);
    
    printf("Enter a2 -> ");
    scanf("%f", &a2);
    
    printf("Enter a3 -> ");
    scanf("%f", &a3);

    float max_value;
    int max_number;

    if (a1 >= a2 && a1 >= a3) {
        max_value = a1;
        max_number = 1;
    } else if (a2 >= a1 && a2 >= a3) {
        max_value = a2;
        max_number = 2;
    } else {
        max_value = a3;
        max_number = 3;
    }

    if ((int)max_value % 2 == 0) {
    	
        float percentage = (max_value / (a1 + a2 + a3)) * 100;
        printf("(a%d) %.2f %.2f%% \n", max_number, max_value, percentage);
    } else {

        float min_value;

        if (a1 <= a2 && a1 <= a3) {
            min_value = a1;
        } else if (a2 <= a1 && a2 <= a3) {
            min_value = a2;
        } else {
            min_value = a3;
        }

        float difference = max_value - min_value;
        printf("(a%d) %.2f.\n", max_number, difference);
    }

    return 0;
}
```
## Результат работы программы для нечётного максимального значения 
