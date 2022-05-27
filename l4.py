import matplotlib
import numpy as np
import matplotlib.pyplot as plt
import time as time
from tabulate import tabulate
import pandas as pd

def solution(Ts, Ti, Te, Td, a, L, n, s, Tempo):
    

    dx = L/n
    dy = dx
    dt = s/(a*(1/dx**2 + 1/dy**2))
    x = np.linspace(0, L, n)
    y = x
    T = np.ones((n,n))*Ti
    
    for i in range(0, n-2):
        T[i+1, 0] = Te
        T[i+1, n-1] = Td
        T[0, i+1] = Ti
        T[n-1, i+1] = Ts
    
    t = 0
    
    while t <= Tempo:
        To = T
        
        for i in range(1, n-1):
            
            for j in range(1, n-1):
                T[i,j]=To[i,j]+dt*a*(((To[i-1,j]-2*To[i,j]+
                                       To[i+1,j])/dx**2)+((To[i,j-1]-2*To[i,j]+To[i,j+1])/dy**2))
        
        t += dt
    
    plt.style.use('dark_background')
    plt.figure(dpi = 1200)
    ax = matplotlib.pyplot.contourf(x, y, T, 9)
    plt.colorbar()
    plt.clabel(ax, inline = True, colors = "black")
    plt.xlabel("x(m)")
    plt.ylabel("y(m)")
    plt.title("Distribuição de temperatutra na chapa para " + str(n) + " pontos, s = " + str(s) + " e " r'$\alpha$' + " = " + str(a))
    plt.show()
    
    if n<=11:
    
        table = pd.DataFrame(T)
        table = table.reindex(index=table.index[::-1])
        print(table)
        print(tabulate(table, tablefmt = 'latex'))

    return None


def main():

    Ts, Ti, Te, Td = 100, 20, 30, 30
    a = 0.0155
    L = 1
    s = 1/20
    n = 6
    Tempo = 20
    start = time.time()
    solution(Ts, Ti, Te, Td, a, L, n, s, Tempo)
    stop = time.time()
    print("Para n = " + str(n) + " e " + "s " + "= " + str(a) + ", o tempo de cálculo é: " + str(stop - start) + " segundos.")
    
    n = 11
    start = time.time()
    solution(Ts, Ti, Te, Td, a, L, n, s, Tempo)
    stop = time.time()
    print("Para n = " + str(n) + " e " + "s " + "= " + str(a) + ", o tempo de cálculo é: " + str(stop - start) + " segundos.")
    
    s = 0.5
    start = time.time()
    solution(Ts, Ti, Te, Td, a, L, n, s, Tempo)
    stop = time.time()
    print("Para n = " + str(n) + " e " + "s " + "= " + str(s) + ", o tempo de cálculo é: " + str(stop - start) + " segundos.")
    
    n = 31
    start = time.time()
    solution(Ts, Ti, Te, Td, a, L, n, s, Tempo)
    stop = time.time()
    print("Para n = " + str(n) + " e " +  "s " + "= " + str(s) + ", o tempo de cálculo é: " + str(stop - start) + " segundos.")
    
if __name__ == '__main__':
    main()
   
