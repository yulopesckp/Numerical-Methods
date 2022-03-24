import numpy as np 
import matplotlib.pyplot as plt 



def func1(x, y):
    return y*x**3 - 1.5*y



def func2(x, y):
    return (1+4*x)*np.sqrt(y)



def func3(x,y):
    return x**2 - 2*y



def Runge_Kutta2(y, y0, x0, b, h1, h2, var, ex):
    n1 = round((b-x0)/h1)+1
    x1 = np.zeros(n1)
    f1 = np.zeros(n1)
    x1[0] = x0
    f1[0] = y0
    
    
    for i in range(1,n1):
        x1[i] = x0 + i*h1
        k1 = y(x1[i-1], f1[i-1])
        k2 = y(x1[i-1]+h1,  f1[i-1]+h1*k1)
        f1[i] = f1[i-1] + (h1/2)*(k1+k2)
        
        
    n2 = round((b-x0)/h2)+1
    x2 = np.zeros(n2)
    f2 = np.zeros(n2)
    x2[0] = x0
    f2[0] = y0
    
    
    for i in range(1,n2):
        x2[i] = x0 + i*h2
        k1 = y(x2[i-1], f2[i-1])
        k2 = y(x2[i-1]+h2,  f2[i-1]+h2*k1)
        f2[i] = f2[i-1] + (h2/2)*(k1+k2)
    
    
    plt.style.use('dark_background')
    plt.xlabel(var)
    plt.ylabel("y")
    plt.plot(x1, f1, 'bo--', markersize = 11, 
             label = 'Método de Runge-Kutta 2 para h = ' + str(h1) + '.')
    plt.plot(x2, f2, 'ro--',
             label = 'Método de Runge-Kutta 2 para h = ' + str(h2) + '.')
    plt.legend(loc = "upper center")
    plt.title(ex)
    plt.grid()
    plt.show()
    
    
    return None



def Runge_Kutta4(y, y0, x0, b, h1, h2, var, ex):
    n1 = round((b-x0)/h1)+1
    x1 = np.zeros(n1)
    f1 = np.zeros(n1)
    x1[0] = x0
    f1[0] = y0
    
    
    for i in range(1,n1):
        x1[i] = x0 + i*h1
        k1 = h1*y(x1[i-1], f1[i-1])
        k2 = h1*y(x1[i-1]+h1/2,  f1[i-1]+k1/2)
        k3 = h1*y(x1[i-1]+(h1/2), f1[i-1]+(k2/2))
        k4 = h1*y(x1[i-1]+(h1), f1[i-1]+k3)
        f1[i] = f1[i-1] + (1/6)*(k1+(2*k2)+(2*k3)+k4)
        
        
    n2 = round((b-x0)/h2)+1
    x2 = np.zeros(n2)
    f2 = np.zeros(n2)
    x2[0] = x0
    f2[0] = y0
    
    
    for i in range(1,n2):
        x2[i] = x0 + i*h2
        k1 = h2*y(x2[i-1], f2[i-1])
        k2 = h2*y(x2[i-1]+h2/2,  f2[i-1]+k1/2)
        k3 = h2*y(x2[i-1]+(h2/2), f2[i-1]+(k2/2))
        k4 = h2*y(x2[i-1]+(h2), f2[i-1]+k3)
        f2[i] = f2[i-1] + (1/6)*(k1+(2*k2)+(2*k3)+k4)
    
    
    plt.style.use('dark_background')
    plt.xlabel(var)
    plt.ylabel("y")
    plt.plot(x1, f1, 'bo--', markersize = 11, 
             label = 'Método de Runge-Kutta 4 para h = ' + str(h1) + '.')
    plt.plot(x2, f2, 'ro--', 
             label = 'Método de Runge-Kutta 4 para h = ' + str(h2) + '.')
    plt.legend(loc = "upper center")
    plt.title(ex)
    plt.grid()
    plt.show()
    
    return None



if __name__ == '__main__' :

    n1 = 0.5
    n2 = 0.25
    var1 = "x"
    var2 = "t"
    ex1 = "Exercício 1"
    ex2 = "Exercício 2"
    ex3 = "Exercício 3"
    Runge_Kutta2(func1, 1, 0, 2, n1, n2, var2, ex1 + " Runge Kutta 2")
    Runge_Kutta4(func1, 1, 0, 2, n1, n2, var2, ex1 + " Runge Kutta 4")
    Runge_Kutta2(func2, 1, 0, 1, n1, n2, var1, ex2 + " Runge Kutta 2")
    Runge_Kutta4(func2, 1, 0, 1, n1, n2, var1, ex2 + " Runge Kutta 4")
    Runge_Kutta2(func3, 1, 0, 2, n1, n2, var2, ex3 + " Runge Kutta 2")
    Runge_Kutta4(func3, 1, 0, 2, n1, n2, var2, ex3 + " Runge Kutta 4")
