import numpy as np
import matplotlib.pyplot as plt
import time


def M(n):
    
    A = np.zeros((n, n))
    A[0, 0] = 1
    
    for i in range(1, n-1):
        A[i, i-1] = -1
        A[i, i+1]= 1
        
    A[-1,-1] = 1
    
    return A

    
def first_order(func, fc, M, y0, yf, x0, b, n):
    
    if (n%2) == 1:
        n = n+1
    
    h = (b-x0)/(n)
    B = np.zeros(n)
    y = np.zeros(n)
    B[0] = y0
    B[-1] = yf
    A = np.zeros((n, n))
    x = np.linspace(x0, b, n)
    A = M(n)
    
    for j in range(10*n):
            
        for i in range(1, n-1):
            B[i] = 2*h*func(x[i],y[i])
            
        f = np.linalg.solve(A, B)
        y = f
    
    f = np.matmul(np.linalg.inv(A), B)
    v = np.linspace(x0, b, 1000)
    h = fc(v)
    plt.plot(v, h, 'r', label = "Solução analítica")
    plt.style.use('dark_background')
    plt.xlabel("x")
    plt.ylabel("y")
    plt.plot(x, f, 'bo--', label = "Método de Diferenças finitas para " + str(n) + " pontos.")
    plt.legend(loc = "upper center")
    plt.grid()
    plt.show()
    
    return None


def main():
    t1 = 10
    
    func1 = lambda x, y : y*(x**3-1.5)
    fc = lambda x : np.exp((x**4)/4 - 1.5*x)
    
    for i in range(3):
        
        inicio = time.time()
        first_order(func1, fc, M, 1, 2.72, 0, 2, t1)
        fim = time.time()
        print("Para " + str(t1) + " iterações, " + " t = " + str(fim - inicio) + " segundos.")
        t1 *= 10
    

if __name__ == '__main__':
    main()
