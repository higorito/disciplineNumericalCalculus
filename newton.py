# -*- coding: utf-8 -*-
"""
Created on Wed Feb 23 15:47:55 2022

@author: higor
"""

import numpy as np
from math import e


def eval_f(fx, x):
    return eval(fx)

def eval_derivada(dx, x):
    return eval(dx)
 
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
      
        
        
f = input('Informe a função: ')
d= input('Informe a derivada: ')
a = float(input('Informe o início do intervalo: '))
b = float(input('Informe o fim do intervalo: '))
t = float(input('Informe a tolerância: '))
n = int(input('Informe o número de iterações: '))


newton(f,d, a, b, t, n)