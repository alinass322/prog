# Лабораторная работа №2

## Задания для самостоятельного выполнения
### Сложность: Rare

### 1. Напишите программу по варианту, используя оператор цикла while (нечётные варианты) или do while (чётные варианты).
### 2. Напишите программу, используя оператор цикла for.
### 3. Постройте график с использованием gnuplot.
### 4. Составьте блок-схемы.
### 5. Оформите отчёт в README.md. Отчёт должен содержать:
* 5.1 Задание
* 5.2 Описание проделанной работы
* 5.3 Скриншоты результатов
* 5.4 Блок-схемы
* 5.5 График функции
* 5.6 Ссылки на используемые материалы

## Ход работы
 ## Вариант - 4

$$ f(n) =
 \begin{cases}
 \sqrt{x+1} - \sqrt{x} - \frac{1}{2}, & \quad 0 \leq x \leq 1; \\
e^{-x-\frac{1}{x}}, & \quad 1 < x \leq 2.
\end{cases}
$$

 ### 1. Напишите программу по варианту, используя оператор цикла do while.
 ```c
#include <stdio.h>
#include <math.h>

int main() {
    double x = 0.0, y;
    double eps;
    double h;
    scanf("%lf", &h);
    eps = h / 2.0;
    printf("x\t\ty\n");

    do {
        if (x >= 0.0 && x <= 1.0 + eps) {
            y = sqrt(x + 1) - sqrt(x) - 0.5;
        } else if (x > 1.0 + eps && x <= 2.0 + eps) {
            y = exp(-x - 1 / x);
        } else {
            y = 0.0;
        }

        printf("%f\t%f\n", x, y);
        x = x + h;
    } while (x >= 0.0 && x <= 2.0 + eps);

    return 0;
}
 ```
 ### 2. Напишите программу, используя оператор цикла for.
```c
#include <stdio.h>
#include <math.h>

int main() {
    double x, y;
    double eps;
    double h;
    scanf("%lf", &h);
    eps = h / 2.0;

    printf("x\t\t\ty\n");

    for (x = 0.0; x <= 2.0 + eps; x += h) {
        if (x >= 0.0 && x <= 1.0 + eps) {
            y = sqrt(x + 1) - sqrt(x) - 0.5;
        } else if (x > 1.0 + eps && x <= 2.0 + eps) {
            y = exp(-x - 1 / x);
        } else {
            y = 0.0;
        }

        printf("%.6f\t%.6f\n", x, y);
    }

    return 0;
}
 ```
### Результат

![1 ph](https://github.com/user-attachments/assets/0d75e3bb-24fe-43f4-9bd2-d7d282f5e4e8)

### 3. Постройте график с использованием gnuplot.

![2 ph](https://github.com/user-attachments/assets/e75718a4-545e-4699-acf4-63f49bf2c66d)


#### Блок-схема для оператора цикла do while:

![w ph](https://github.com/user-attachments/assets/25ff9b55-544f-47c4-9d76-3c4ab0fd7e50)


#### Блок-схема для оператора цикла for:

![f ph](https://github.com/user-attachments/assets/12ebec4e-5541-4dce-9b93-7eaa0dd14823)


### Источники:

1. https://en.wikibooks.org/wiki/LaTeX/Mathematics
2. https://programforyou.ru/block-diagram-redactor
















