import numpy as np
import matplotlib.pyplot as plt
#from scipy import linalg


def func1(x, y):
    return y*(x**3-1.5)



def f_anal(x):
    return np.exp((x**4)/4 - 1.5*x)



def first_order(func, f_anal, y0, yf, x0, b, n):
    
    
    h = (b-x0)/(n)
    h /= 2
    y = np.zeros(n)
    y[0] = y0
    y[-1] = yf
    A = np.zeros((n, n))
    x = np.linspace(x0, b, n)
    A[0, 0] = (2*h*(x[0]**3-1.5)+1)
    A[0, 1] = -1


    for i in range(1, n-1):

        
        A[i, i] = (2*h*(x[i]**3-1.5)+1)
        A[i, i+1] = -1
        
        
    A[-1, -1] = (2*h*(x[-1]**3-1.5)+1)
    print("A: " + str(A))
    print("y: " + str(y))
    f = np.matmul(np.linalg.inv(A), y)
    print("f: " + str(f))
    v = np.linspace(x0, b, 1000)
    h = f_anal(v)
    plt.style.use('dark_background')
    plt.xlabel("x")
    plt.ylabel("y")
    plt.plot(x, f, 'bo--', label = "Método de Diferenças Finitas para " + str(n) + " pontos.")
    plt.plot(v, h, 'r', label = "Solução analítica")
    plt.legend(loc = "upper center")
    plt.grid()
    plt.show()
    return None



def main():
    
    t = 10
    
    for i in range(3):
        first_order(func1, f_anal, 1, 2.72, 0, 2, t)
        t *= 10



if __name__ == '__main__':
    main()
