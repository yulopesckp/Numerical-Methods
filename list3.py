import numpy as np
import matplotlib.pyplot as plt
from scipy import linalg


def func1(x,y):
    return y*(x**3-1.5)

def fc(x):
    return np.exp((x**4)/4 - 1.5*x)


def first_order(func, fc, y0, yf, x0, b, n):
    
    h = (b-x0)/(n)
    y = np.zeros(n)
    y[0] = y0
    y[-1] = yf
    A = np.zeros((n, n))
    A[0, 0] = 1
    x = np.linspace(x0, b, n)

    for i in range(1, n-1):
        A[i, i+1] = 1
        A[i, i] = -1
        y[i] = 2*h*func(x[i], y[i])
    
    A[-1, -1] = 1
    f = linalg.solve(A, y)
    v = np.linspace(x0, b, 1000)
    h = fc(v)
    plt.plot(v, h, 'g', label = "Solução analítica")
    plt.style.use('dark_background')
    plt.xlabel("x")
    plt.ylabel("y")
    plt.plot(x, f, 'bo--', label = "Método de Diferenças finitas para " + str(n) + " pontos.")
    plt.legend(loc = "upper center")
    plt.grid()
    plt.show()
    return None



if __name__ == '__main__':
    t1 = 10
    
    for i in range(3):
        first_order(func1, fc, 0, 2.75, 0, 2, t1)
        t1 = 10*t1
    
