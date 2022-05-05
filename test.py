import numpy as np
import matplotlib.pyplot as plt



def func1(x,y):
    return y*(x**3-1.5)


def fc(x):
    return np.exp((x**4)/4 - 1.5*x)


def M(n):
    
    A = np.zeros((n, n))
    A[0, 0] = 1
    
    for i in range(1, n-1):
        A[i, i-1] = -1
        A[i, i+1]= 1
        
    A[-1,-1] = 1
    return A

    
    
def first_order(func, fc, M, y0, yf, x0, b, n):
    
    h = (b-x0)/(n)
    B = np.zeros(n)
    y = np.zeros(n)
    y[0] = y0
    y[-1] = yf
    A = np.zeros((n, n))
    x = np.linspace(x0, b, n)
    A = M(n)
    print(y)
    
    for j in range(2*n - 1):
            
        for i in range(1, n-1):
            B[i] = 2*h*func(x[i],y[i])
            print(B[i])
        
        f = np.linalg.solve(A, B)
        print(f)
        print(y)
        y = f
        print(y)
    
    f = np.linalg.solve(A, B)
    v = np.linspace(x0, b, 1000)
    h = fc(v)
    plt.plot(v, h, 'g', label = "Solução analítica")
    plt.style.use('dark_background')
    plt.xlabel("x")
    plt.ylabel("y")
    plt.plot(x, f, 'bo--', label = "Método de Diferenças finitas para " + str(n) + " pontos.")
    #plt.legend(loc = "upper center")
    plt.grid()
    plt.show()
    
    
    return None


def main():
    t1 = 5 
    
    for i in range(1):
        first_order(func1, fc, M, 1, 2.72, 0, 2, t1)
        #t1 *= 10


if __name__ == '__main__':
    main()
