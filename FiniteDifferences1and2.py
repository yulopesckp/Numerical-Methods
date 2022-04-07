import numpy as np
import matplotlib.pyplot as plt
from scipy import linalg

def func1(x,y):
    return 10*(x-1)

def first_order(func, y0, yf, x0, b, n):
    #n =  round((b-x0)/h) + 1
    h = (b-x0)/(n-1)
    y = np.zeros(n)
    y[0] = y0
    m = np.zeros((n, n))
    m[0, 0] = 1
    x = np.linspace(x0, b, n)

    for i in range(1, n-1):
        m[i, i+1] = 1
        m[i, i] = -1
        y[i] = h*func(x[i], y[i])
    
    m[-1, -1] = 1
    y[-1] = yf
    f = linalg.solve(m, y)
    
    print(f)
    print(x)
    #print(y)
    
    plt.style.use('dark_background')
    plt.xlabel("x")
    plt.ylabel("y")
    plt.plot(x, f, 'bo--')
    plt.grid()
    plt.show()
    print(np.dot(m, y) == f)
    return None


first_order(func1, 5, 1, 0, 1, 11)
