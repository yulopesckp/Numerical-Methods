import numpy as np 
from scipy import random
import time
#import matplotlib.pyplot as plt 



def f(x):
    return x**2 + 2*x*(x+1)



def func(x, y):
    return x+y



def Riemann_Int(a,b,f,n):
    
    if a==b:
        return None
    
    if n == 0:
         n = 1
         
    #y = np.zeros(n+1)
    diff = b-a
    base = diff/n
    x = a
    s= 0
    i = 0
    
    while x <= b:
        #y[i] = f(x)
        s += f(x)
        x = x+base
        i=i+1
    #s = np.sum(y)
    s = s*base
    #print(i)
    return s



def Trap_Int(a,b,f,n):
    
    if a==b:
        return None
    
    if n == 0:
         n = 1
         
    #y = []
    diff = b-a
    base = diff/n
    x = a
    i=1
    sum1 = f(a) + f(b)
    sum1 = sum1/2
    x = x+base
    s =0
     
    while x < b:
        #y.append(f(x))
        s += f(x)
        x = x+base
        i+=1
        
    
    #y = np.array(y)
    #s = np.sum(y)
    s = s*base
    #print(i)
    return s



def Simpson_Rule(a,b,f,n):
    
    if a==b:
        return None
    
    if n == 0:
        n=1
    
    n = 2*n
    y = []
    diff = b - a
    dx = diff/n
    s1 = f(a) + f(b)
    x = a+dx
    i = 1
    s = f(a) + f(b)
    
    while x < b:
        
        if i % 2 == 0:
            y.append(2*f(x))
            
            
        else:
            y.append(4*f(x))
            

        i += 1
        x += dx
    
    y = np.array(y)
    s = (np.sum(y) + s1)*(dx/3)
    return s



def MonteCarlo(a,b,f,n):
    
    if a==b:
        return None
    
    xrand = random.uniform(a,b,n)
    s = 0
    diff = b-a
    dx = diff/n
    
    for i in range(n):
        s += f(xrand[i])
    
    return s*dx



def MonteCarlo2(a,b,f,n):
    
    if a==b:
        return None
    
    if n > 15000:
        n = 15000
   #return "n > 10000 é um valor muito grande para o cálculo"
        
        
    elif n == 0:
        n = 1
        
    start = time.time()
    A = []
    diff = b-a
    dx = diff/n
    for i in range(n):
        xrand = random.uniform(a,b,n)
        s = 0
        
        for i in range(n):
            s += f(xrand[i])
    
        s = s*dx
        A.append(s)
    
    
    s = np.array(s)
    s = np.sum(s)/np.size(s)
    end = time.time()
    print("Tempo de execução: " + str(end - start))
    
    return s



def secant(a,b,f,n):
    
    an = a
    bn = b
    
    if (f(a)*f(b)) >= 0:
        print("Não se pode concluir a existência de raiz.")
        return None
    
    for i in range(1,n+1):
        mn = an - f(an)*(bn - an)/(f(bn) - f(an))
        
        if f(an)*f(mn) < 0:
            an = an
            bn = mn
        
        elif f(bn)*f(mn) < 0:
            an = mn
            bn = bn
        
        elif f(mn) == 0:
            print("Solução: " + str(mn))
            return mn
        
        else:
            print("Método das Secantes falha.")
            return None
    
    return an - f(an)*(bn - an)/(f(bn) - f(an))



def LeylandNumber_firstkind(x,y):
    if (x == 0 and y == 0) or (x <= 0 and y <= 0) or (x >= y):
        print("Both x and y must be different, bigger than zero and x >= y.")
        return None
    
    else:
        L = x**y + y**x
    
    return L



def LeylandNumber_secondkind(x,y):
    if (x == 0 and y == 0) or (x <= 0 and y <= 0) or (x >= y):
        print("Both x and y must be different, bigger than zero and x >= y.")
        return None
    
    else:
        L = x**y - y**x
    
    return L



def Euler_Method(func, y0, x0, b, n):
    
    h = (b - x0)/n
    
    x = x0
    yi = y0 + h*func(x,y0)
    #print("Para a iteração " + str(0) + ", resulta em "+ str(yi))
    xi = x0+h
    
    for i in range(1,n):
        xi = xi + h
        yi = yi + h*(func(xi,yi))
        #print("Para a iteração " + str(i+1) + ", resulta em "+ str(yi))
    
    
    
    return yi



def Adam_Method(func, y0, x0, b, n):
    
    n+=3
    h = (b-x0)/n
    x = np.zeros(n+1)
    x[0] = x0
    
    for i in range(1,n+1):
        x[i] = x0+i*h
        
    
    y = np.zeros(len(x))
    
    y[0] = y0
    
    
    y[1] = y[0] + h*func(x[0], y[0])
    
    for i in range(2,n):
        y[i] = y[i-1] + (3/2)*h*func(x[i-1],y[i-1]) -(1/2)*h*func(x[i-2], y[i-2])
        #print("Para a iteração " + str(i-2) + ", resulta em "+ str(y[i]))
    
    return y[i]



def Runge_Kutta4(func, y0, x0, b, n):
    h = (b - x0)/n
    x = x0
    y = y0
    i = 0
    for i in range(n):
        k1 = h*func(x,y)
        k2 = h*func(x+(h/2),  y+(h/2))
        k3 = h*func(x+(h/2), y+(k2/2))
        k4 = h*func(x+(h), y+k3)
         
        y = y + (1/6)*(k1+(2*k2)+(2*k3)+k4)
        x += h
        
    return y



##Test##
if __name__ == '__main__':
    ##################################
    ##parte para integração numérica##
    n0 = 1000
    a = 0
    b = 1
    ##############################################

    ##############################################
    ##Parte para resolução de EDOs numericamente##
    n1 = 1000
    a1 = 0
    b1 = 1
    ##############################################

    E = Euler_Method(func, 1, 0, b1, n1)
    A = Adam_Method(func, 1, 0, b1, n1)
    RK4 = Runge_Kutta4(func, 1, 0, b1, n1)

    s = 2*(np.exp(1)-1)

    print("1° método, por Soma de Riemann: " + str(Riemann_Int(a,b,f,n0)) + ", para n = " + str(n0) + " de precisão")
    print("2° método, por Trapézio: " + str(Trap_Int(a,b,f,n0)) + ", para n = " + str(n0) + " de precisão")
    print("3° método, pela Regra de Simpson: " + str(Simpson_Rule(a,b,f,n0)) + ", para n = " + str(n0) + "  precisão")
    print("4° método, pelo método de Monte Carlo: " + str(MonteCarlo(a,b,f,n0)) + ", para n = " + str(n0) + "  precisão")
    #print("5° método, pelo método de Monte Carlo com a média das respostas: " + str(MonteCarlo2(a,b,f,n0)))
    #print("Pelo método das secantes, a raíz da equação é: " + str(secant(a,b,f,n0)))

    name = ["Euler", "Adam", "Runge-Kutta de 4° ordem"]
    sn = [E, A, RK4]

    for i in range(len(name)):
        print("A diferença no método de " + name[i] + ", valendo " + str(sn[i]) + ", é de " + str(abs(sn[i] - s)) + ", com " + str(n1) + " iterações.")
