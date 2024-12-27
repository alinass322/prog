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
plt.title('График 4 вариант')
plt.legend()

plt.show()