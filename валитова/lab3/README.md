# Лабораторная работа №3

## Задание

Сложность: Rare
1. Напишите программу по своему варианту.
2. Оформите отчёт в README.md. Отчёт должен содержать:
2.1 Задание
2.2 Описание проделанной работы
2.3 Скриншоты результатов
2.4 Ссылки на используемые материалы


### Задание. Вариант №4.
`
Максимально эффективно по используемой памяти сформировать массив из элементов, встречающихся в обоих массивах A и B.
`

### 2. Код
```c
#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main() {
    int sizeA, sizeB;
    srand(time(0));

    printf("enter size A: ");
    scanf("%d", &sizeA);
    printf("enter size B: ");
    scanf("%d", &sizeB);

    int arrA[sizeA];
    int arrB[sizeB];
    
    printf("array A:\n");
    for (int i = 0; i < sizeA; i++) {
        arrA[i] = rand() % 10;
        printf("%5d", arrA[i]);
    }
    printf("\n");

    printf("array B:\n");
    for (int i = 0; i < sizeB; i++) {
        arrB[i] = rand() % 10; 
        printf("%5d", arrB[i]);
    }
    printf("\n");
    int s = 0;
    printf("\narray C:\n");
    for (int i = 0; i < sizeA; i++) {
        for (int j = 0; j < sizeB; j++) {
            if (arrA[i] == arrB[j]) {
                s++;
                printf("%d ", arrA[i]);
                }
                }
    }
    printf("s = %d\n ", s);
    int arrC[s];
    int k = 0;
    printf("\narray C:\n");
    for (int i = 0; i < sizeA; i++) {
        for (int j = 0; j < sizeB; j++) {
            if (arrA[i] == arrB[j]) {
                arrC[k++] = arrA[i];
                printf("%5d", arrC[k-1]);
                }   
        }
    }

    printf("k = %d\n ", k);
    for (int i = 0; i < s; i++) {
        printf("%5d", arrC[i]);  
    }
    printf("\n");
    return 0;
}
```

## Результат:


