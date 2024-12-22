#include <stdio.h>
#include <stdlib.h>
#include <time.h>

void fill(int n, int a[]) {
    for (int i = 0; i < n; i++)
        a[i] = rand() % 11;
}

void findCommonElements(int n, int A[], int B[], int C[], int *sizeC) {
    *sizeC = 0;
    
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            if (A[i] == B[j]) {
                C[*sizeC] = A[i];
                (*sizeC)++;
                break;
            }
        }
    }
}

int main() {
    srand(time(NULL));
    int n;
    printf("size A and B: ");
    scanf("%d", &n);

    int A[n], B[n], C[n];
    
    printf("A:\n");
    fill(n, A);
    for (int i = 0; i < n; i++)
        printf("%5d", A[i]);
    printf("\n");

    printf("B:\n");
    fill(n, B);
    for (int i = 0; i < n; i++)
        printf("%5d", B[i]);
    printf("\n");

    int sizeC;
    findCommonElements(n, A, B, C, &sizeC);
    
    printf("C:\n");
    for (int i = 0; i < sizeC; i++) {
        printf("%5d", C[i]);
    }
    printf("\n");

    return 0;
}