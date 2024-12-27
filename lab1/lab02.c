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
