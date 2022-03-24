import numpy as np 
import matplotlib.pyplot as plt 



def func1(x, y):
    return y*x**3 - 1.5*y



def y1(x):
    return np.exp((1/4)*x**4 - 1.5*x)



def func2(x, y):
    return (1+4*x)*np.sqrt(y)



def y2(x):
    return ((1/2)*x + x**2 + 1)**2



def func3(x,y):
    return x**2 - 2*y



def Euler_Method(func, y, y0, x0, b, h, var):

    
    n = round(b/h)+1
    x = np.zeros(n)
    f = np.zeros(n)
    x[0] = x0
    f[0] = y0

    
    for i in range(1,n):
        x[i] = x0 + i*h
        f[i] = f[i-1] + h*(func(x[i-1],f[i-1]))


    plt.style.use('dark_background')
    plt.xlabel(var)
    plt.ylabel("y")
    plt.plot(x, f, 'bo--', label = 'Método de Euler para ' + str(n) + ' passos.')
    x1 = np.linspace(x0, b, 1000)
    y1 = y(x1)
    plt.plot(x1, y1, 'r', label = 'Solução Analítica')
    plt.legend(loc = "upper left")
    plt.grid()
    plt.show()
    
    return None


def Euler_Method2(y, f, y0, x0, b, h1, h2, var):
    n1 = round(b/h1)
    x1 = np.zeros(n1)
    f1 = np.zeros(n1)
    x1[0] = x0
    f1[0] = y0
    
    
    for i in range(1,n1):
        x1[i] = x0 + i*h1
        f1[i] = f1[i-1] + h1*(y(x1[i-1],f1[i-1]))
    
    
    n2 = round(b/h2)
    x2 = np.zeros(n2)
    f2 = np.zeros(n2)
    x2[0] = x0
    f2[0] = y0
    
    
    for i in range(1,n2):
        x2[i] = x0 + i*h2
        f2[i] = f2[i-1] + h2*(y(x2[i-1], f2[i-1]))
    
    plt.style.use('dark_background')
    plt.xlabel(var)
    plt.ylabel("y")
    plt.plot(x1, f1, 'bo--', markersize = 11, label = 'Método de Euler para ' + str(n1) + ' passos.')
    plt.plot(x2, f2, 'ro--', label = 'Método de Euler para ' + str(n2) + ' passos.')
    plt.legend(loc = "upper center")
    plt.grid()
    plt.show()



if __name__ == '__main__':

    n1 = 0.5
    n2 = 0.25
    var1 = "x"
    var2 = "t"
    Euler_Method(func1, y1, 1, 0, 2 , n1, var2)
    Euler_Method(func1, y1, 1, 0, 2 , n2, var2)
    Euler_Method(func2, y2, 1, 0, 1 , n1, var1)
    Euler_Method(func2, y2, 1, 0, 1 , n2, var1)
    Euler_Method2(func3, 1, 0, 2, n1, n2, var2)
