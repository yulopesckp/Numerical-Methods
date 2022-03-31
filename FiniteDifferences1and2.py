import numpy as np
import matplotlib as plt

def func1(x,y):
    return 10*(x-1)

def first_order(func, y0, x0, b, h):
    n =  round((b-x0)/h) + 1
    x = np.zeros(n)
    x[0] = x0
    y = np.zeros(n)
    y[0] = y0
    m = np.zeros((n, n))
    m[0,0] = 1
    
    for i in range(1, n):
        for j in range(n):
            
            if i == j:
                m[i, j] = -1
                m[i, j+1] = 1
    
    for i in range(1, n):
        
        x[i] = x0 + i*h
        y[i] = h*func(x[i], y[i])
        
    f = np.linalg.solve(m, y)
    y[-1] = 
    print(f)
    print(x)
    print(y)
    
    plt.style.use('dark_background')
    plt.xlabel("x")
    plt.ylabel("y")
    plt.plot(x, f, 'bo--')
    plt.grid()
    plt.show()
    return None


first_order(func1, 0, 0, 5, 0.5)
