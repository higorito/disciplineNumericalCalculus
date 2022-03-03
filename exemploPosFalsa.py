# -*- coding: utf-8 -*-
"""
Created on Fri Feb 18 15:07:44 2022

@author: higor
"""

def f(x):
  return x**3 - 9*x**2 + 22*x - 15


 
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

            print('Raiz aproximada encontrada por pos falsa: {r:+.6f}'.format(r=x))
            print('No intervalo a = {v:+.6f}'.format(v=a))
            print('No intervalo b = {n:+.6f}'.format(n=b))
            print(i,' iterações')
            break
        
        if sinal > 0:
        
            a = x
        else:
         
            b = x
        
        
posFalsa(2, 3, 0.02, 20)