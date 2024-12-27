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