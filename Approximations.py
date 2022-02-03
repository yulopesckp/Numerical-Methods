import numpy as np 
from scipy import random
import time


def f(x):
    return 


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
        print("Não se pode calcular o valor.")
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


n = 100000
a = 0
b = 9


print("1° método, por Soma de Riemann: " + str(Riemann_Int(a,b,f,n)) + ", para n = " + str(n) + " de precisão")
print("2° método, por Trapézio: " + str(Trap_Int(a,b,f,n)) + ", para n = " + str(n) + " de precisão")
print("3° método, pela Regra de Simpson: " + str(Simpson_Rule(a,b,f,n)) + ", para n = " + str(n) + "  precisão")
print("4° método, pelo método de Monte Carlo: " + str(MonteCarlo(a,b,f,n)) + ", para n = " + str(n) + "  precisão")
print("5° método, pelo método de Monte Carlo com a média das respostas: " + str(MonteCarlo2(a,b,f,n)))
print("Pelo método das secantes, a raíz da equação é: " + str(secant(a,b,f,n)))