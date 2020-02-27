import numpy as np
from matplotlib import pyplot as plt
import sympy as sy

# Created by Raviv Herrera #
# Newton Raphson method for one dimension function - Finding the root of a function #

x = sy.Symbol('X')
f = x ** 2
xx = np.linspace(-10, 10, 100)
yy = np.ndarray(xx.size, dtype=np.float64)
for i in range(xx.size):
    yy[i] = f.subs(x, xx[i])
plt.grid(True)
plt.axis([-10, 10, -10, 10])
plt.axvline()
plt.axhline()
plt.plot(xx, yy, color='r')
plt.pause(1)


def Newton_Raphson(epsilon, function, x0):
    x_next = 0
    Ei = 1
    x_current = x0
    while Ei > epsilon:
        x_next = x_current - (function.subs(x, x_current) / function.diff(x, 1).subs(x, x_current))
        Ei = np.abs(x_next - x_current)
        x_current = x_next
        print("x_next = {}".format(float(x_next)))
        #plt.plot(x_next, 0, ".", color='black')
        #plt.pause(1)
    plt.plot(x_next, 0, "*", color='y')
    print("root = {}".format(float(x_next)))
    return x_next


root = Newton_Raphson(0.0001, f, 4)
plt.show()
print(f"Function f(x) = {f}")
