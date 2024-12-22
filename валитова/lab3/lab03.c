#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <limits.h>

int main() {
    int sizeA, sizeB;
    printf("Enter size A: ");
    scanf("%d", &sizeA);

    printf("Enter size B: ");
    scanf("%d", &sizeB);

    int *arrA = (int *)malloc(sizeA * sizeof(int));  
    int *arrB = (int *)malloc(sizeB * sizeof(int)); 

    printf("Array A:\n");
    for (int i = 0; i < sizeA; i++) {
        scanf("%d", &arrA[i]); 
    printf("\n");

    printf("Array B:\n");
    for (int i = 0; i < sizeB; i++) {
        scanf("%d", &arrB[i]); 
    }
    printf("\n");

    int maxSize = sizeA > sizeB ? sizeA : sizeB; 
    int *arrC = (int *)malloc(maxSize * sizeof(int));  

    int sizeC = 0; 

    for (int i = 0; i < sizeA; i++) {
        bool isDuplicate = false; 

        for (int j = 0; j < sizeC; j++) {
            if (arrA[i] == arrC[j]) {
                isDuplicate = true;
                break;
            }
        }

        if (isDuplicate) {
            continue; 
        }

        for (int j = 0; j < sizeB; j++) {
            if (arrA[i] == arrB[j]) {
                arrC[sizeC] = arrA[i];
                sizeC++;
                break;
            }
        }
    }

    printf("Array C (Common Elements):\n");
    for (int i = 0; i < sizeC; i++) {
        printf("%d ", arrC[i]);
    }
    printf("\n");

    free(arrA); 
    free(arrB); 
    free(arrC); 

    return 0;
}