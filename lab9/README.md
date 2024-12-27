# Лабораторная работа №3

## Задание

Сложность: Rare
    
 1. Напишите программу по своему варианту.
 2. Оформите отчёт в README.md. Отчёт должен содержать:
 2.1 Задание
 2.2 Описание проделанной работы
 2.3 Скриншоты результатов
 2.4 Ссылки на используемые материалы

## Этапы работы
### 1. Задание по Варианту №4
`
Максимально эффективно по используемой памяти сформировать массив из элементов, встречающихся в обоих массивах A и B.
`

### 2. Код


``` c
#include <stdio.h>
#include <stdlib.h>
#include <time.h>

void fill(int n, int a[]){
    for (int i=0; i<n; i++){
        a[i] = rand()%7+1;   
    }
}

void display(int n, int a[]){
    for (int i = 0; i < n; i++){
        printf("%4d", a[i]);
    }
    printf("\n");
}

int sravn(int n, int A[], int B[]){
    int sc=0,zap=0;
    for (int i=0; i<n; i++){
        for (int j=0; j<n; j++){
            if (A[i]==B[j]){
                for(int z=0; z<i; z++){
                    if(A[z]==A[i]){
                        zap+=1;
                    }
                } 
                for(int z=0; z<j; z++){
                    if(B[z]==B[j]){
                        zap+=1;
                    }
                }     
                if(zap>0){
                    zap=0;
                    break;
                } else 
                    sc+=1; 
            }
        }
    }
    return sc;
}

void newc(int n, int a[], int b[]){
    int C[sravn(n,a,b)],s=0,zap=0;
    printf("Kol. povtoreni %d\n",sravn(n,a,b));
    for (int i=0; i<n; i++){
        for (int j=0; j<n; j++){
            if (a[i]==b[j]){
                for(int z=0; z<i; z++){
                    if(a[z]==a[i]){
                        zap+=1;
                    }
                } 
                for(int z=0; z<j; z++){
                    if(b[z]==b[j]){
                        zap+=1;
                    }
                }     
                if(zap>0){
                    zap=0;
                    break;
                } else {
                    C[s]=a[i]; 
                    s+=1;
                }
            }
        }
    }
    printf("C:");
    display(sravn(n,a,b),C);
}

int main(){
    srand(time(NULL));
    int n;
    printf("Enter n: ");
    scanf("%d", &n);
    int A[n], B[n];
    fill(n,A);
    fill(n,B);
    printf("A:");
    display(n,A);
    printf("B:");
    display(n,B);
    newc(n,A,B);
    return 0;
}
```
#Результат: 
![1r](https://github.com/user-attachments/assets/40c15641-07da-4c3f-abd5-fd79c79c3c5e)

### Источники:
1. https://pythonist.ru/massiv-v-python/?ysclid=m56nfxgkft390163750
2. https://docs.python.org/3/tutorial/datastructures.html
3. https://pythoninfo.ru/osnovy/massivy-python











