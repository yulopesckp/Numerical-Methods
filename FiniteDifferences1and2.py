import numpy as np
import matplotlib.pyplot as plt
from scipy import linalg


def func1(x,y):
    return 10*(x-1)


def func2(x,y):
    return -9.8


def first_order(func, y0, yf, x0, b, n):

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
        y[i] = h*func(x[i], y[i])
    
    A[-1, -1] = 1
    f = linalg.solve(A, y)    
    plt.style.use('dark_background')
    plt.xlabel("x")
    plt.ylabel("y")
    plt.plot(x, f, 'bo--')
    plt.grid()
    plt.show()
    return None



def second_order(func, y0, yf, x0, b, n):
    
    h = (b-x0)/(n)
    y = np.zeros(n)
    y[0] = y0
    y[-1] = yf
    A = np.zeros((n, n))
    A[0, 0] = 1
    x = np.linspace(x0, b, n)

    for i in range(1, n-1):
        A[i, i+1] = 1
        A[i, i] = -2
        A[i,i-1] = 1
        y[i] = (h**2)*func(x[i], y[i])
    
    A[-1, -1] = 1
    f = linalg.solve(A, y)    
    plt.style.use('dark_background')
    plt.xlabel("x")
    plt.ylabel("y")
    plt.plot(x, f, 'bo--')
    plt.grid()
    plt.show()
    return None


if __name__ == '__main__':
    first_order(func1, 5, 0, 0, 1, 11)
    second_order(func2, 0, 50, 0, 5, 10)
