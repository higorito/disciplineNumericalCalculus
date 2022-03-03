# -*- coding: utf-8 -*-
"""
Created on Mon Feb 28 11:08:08 2022

@author: higor
"""

import numpy as np   #aqui modulos para equações
from math import e

import matplotlib.pyplot as pyplot   #aqui para plotar


def eval_f(fx, x):           #essa função é para receber a equação e depois retornar em ralação a x quando necesssario
    return eval(fx)

def eval_derivada(dx, x):
    return eval(dx)

def plotar(fx, a, b):                 #função para plotar o grafico, recebendo a função e os intervalos
    xx=np.linspace(a, b)
    pyplot.plot(xx, eval_f(fx, xx))
    pyplot.grid()
    pyplot.show()
    
    
def bissecao(f, a, b, t, n):
   xa = float("nan")
   for i in range(n):
     x = (a + b) / 2
     fx = eval_f(f, x)
     sinal = eval_f(f, a) * fx
     error=abs((x-xa)/max(x, 1))
     xant = x
     print("Iteração {i:3d}: a={a:+.6f}, ".format(i=i+1, a=a) +
     "b={b:+.6f}, x={x:+.6f}, ".format(b=b, x=x) +
     "f(x)={fx:+.6f}, error={e:+.6f}, ".format(fx=fx, e=error) +
     "sinal={s:+.6f}".format(x=x, fx=fx, s=sinal))
     if (fx == 0) or (error < t):
         print("Raiz aproximada encontrada: {r:+5.6f}".format(r=x))
         print('#No intervalo a = {v:+.6f}'.format(v=a))
         print('#No intervalo b = {n:+.6f}'.format(n=b))
         print('#',i+1,' iterações')
     break
     if sinal > 0:
         a = x
     else:
         b = x
def f(x):
    return eval_f(func, x)    
    
def posFalsa(a, b, tol, n):
    xa = float('nan')
    for i in range(n):

        x = (a*f(b)-b*f(a))/(f(b)-f(a))
        
        
        fx = f(x)
         
        sinal = f(a) * fx
        
        error=abs((x-xa)/max(x, 1))
         
        xa = x
        
        print('It. {i:3d}:'.format(i=i), 'a={a:+.6f},'.format(a=a),
         'b={b:+.6f},'.format(b=b), 'error={e:+.6f},'.format(e=error),
         'x={x:+.6f},'.format(x=x), 'f(x)={fx:+.6f},'.format(fx=fx),
         'sinal={s:+.6f}'.format(s=sinal))
        if (fx == 0) or (error < tol):

            print('#Raiz aproximada encontrada por pos falsa: {r:+.6f}'.format(r=x))
            print('#No intervalo a = {v:+.6f}'.format(v=a))
            print('#No intervalo b = {n:+.6f}'.format(n=b))
            print('#',i,' iterações')
            break
        
        if sinal > 0:
        
            a = x
        else:
         
            b = x
def gx1(x):
 return x - 0.05 * eval_f(func, x)

def pontoFixo(a, b, tol, n):

    x=(a+b)/2
    xa = float('nan')
    
    
    for i in range(n):
     gx=gx1(x); xa=x; x=gx1(x)
     error=abs((x-xa)/max(x, 1))
     
     print('------Rodada:',i+1,'-------')
     print('gx ',gx)
     print('xa ',xa)
     print('x ',x)
     print('-------------------------')
     
     if (gx == 0) or (error < tol):
         print('#Raiz aproximada encontrada por ponto fixo: {r:+.6f}'.format(r=x))
         print('#No intervalo a = {v:+.6f}'.format(v=a))
         print('#No intervalo b = {n:+.6f}'.format(n=b))
         print('#',i+1,' iterações')
         break
         
def newton(f,d, a, b, tol, n):
    xa = float('nan')
    x=a
    for i in range(n):
        
        xa=x
        
        x=x- ((eval_f(f, x)))/(eval_derivada(d, x))
        
        
        error=abs((x-xa)/max(x, 1))
         
       
        
        print('It. {i:3d}:'.format(i=i+1), 'a={a:+.6f},'.format(a=a),
        'b={b:+.6f},'.format(b=b), 'error={e:+.6f},'.format(e=error),
        'x={x:+.6f},'.format(x=x))
        if (x == 0) or (error < tol):

            print('#Raiz aproximada encontrada por bisseçao: {r:+.6f}'.format(r=x))
            print('#No intervalo a = {v:+.6f}'.format(v=a))
            print('#No intervalo b = {n:+.6f}'.format(n=b))
            print('#',i+1,' iterações')
            break
         
def secante(f,d, a, b, t, n):
    
    x=a
    xa=b
    for i in range(n):
        
        error=abs((x-xa)/max(x, 1))
        
        
        xaa= x-((eval_f(f, x))*((x-xa)/(eval_f(f, x)-eval_derivada(d, x))))
        
        xa=x
        x=xaa
        print('x:',x,' xa:',xa,' xaa:',xaa)

        print('It. {i:3d}:'.format(i=i+1), 'a={a:+.6f},'.format(a=a),
        'b={b:+.6f},'.format(b=b), 'error={e:+.6f},'.format(e=error),
        'x={x:+.6f},'.format(x=x))
        if (x == 0) or (error < t):

            print('#Raiz aproximada encontrada por secante: {r:+.6f}'.format(r=x))
            print('#No intervalo a = {v:+.6f}'.format(v=a))
            print('#No intervalo b = {n:+.6f}'.format(n=b))
            print('#',i+1,' iterações')
            break
     
          
   
#inicio do programa
print('Tolerancia e interações constantes, respectivamente 10**-5 e 100 ')
func = input("Qual a função? ")
res = 's'
while res =='s':
    
    a= float(input("Intervalo inicio: "))
    b= float(input("Intervalo final: "))
    plotar(func, a, b)
    res= input('Deseja mudar o intervalo?[s/n] ')  

print('1- Calcular Raiz por bissecao. ') 
print('2- Calcular Raiz por posição falsa. ')   
print('3- Calcular Raiz por ponto fixo. ')   
print('4- Calcular Raiz por newton-raphson. ')   
print('5- Calcular Raiz por secantes. ')  
op=int(input('Qual a opção desejada?'))
if op == 1:
    bissecao(func, a, b, 0.0001, 100)
elif op== 2:
    posFalsa(a, b, 0.0001, 100)
elif op == 3:
    pontoFixo(a, b, 0.0001, 100)
elif  op== 4:
    d= input('Informe a derivada: ')
    newton(func, d, a, b, 0.0001, 100)
elif op == 5:
    d= input('Informe a derivada: ')
    secante(func, d, a, b, 0.0001, 100)
else:
    print ("Opção INVALIDA")
        


