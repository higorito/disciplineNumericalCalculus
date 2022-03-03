# -*- coding: utf-8 -*-
"""
Created on Fri Feb 18 15:15:49 2022

@author: higor
"""
import numpy as np
from math import e

def f(x):
   #aqui vou escolher qual função do exercicio pq nao consegui usar o eval
      
    return  np.log(x)
   # return  e**x
   # return  np.cos(x)
   # return  x**2 +2*x +1
   # return  (e**(2-x**2))*(x+1)**2
   # return  x**3 +3*x -1
   # return  x**2 +np.sin(x)
   # return  e**x -x**2 -10
   # return  np.sqrt(x) -np.cos(x)
   # return  x-3 -x**-x


 
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
        
        
posFalsa(0.1, 3, 10**-5, 20000)

#RESPOSTAS
#a) Raiz aproximada encontrada por pos falsa: +1.000015
#No intervalo a = +0.100000
#No intervalo b = +1.000025
#22  iterações   Tive que aumentar o numero de iterações para achar
#
#b) Não foi possivel achar raiz, não importando o numero de iterações

#c) Raiz aproximada encontrada por pos falsa: +1.570796
#No intervalo a = +1.570796
#No intervalo b = +1.574628
#4  iterações

#d) Foi necessario aumentar as iterações 
#Raiz aproximada encontrada por pos falsa: -0.996137
#No intervalo a = -0.996127
#No intervalo b = +0.500000
# 388  iterações

#e) Não tem raiz em 20 interações foi necessario aumentar para 20000
#Raiz aproximada encontrada por pos falsa: -4.083888
#No intervalo a = -4.083878
#No intervalo b = -0.500000
# 14492  iterações

#f) Aumentei denovo as iterações
#Raiz aproximada encontrada por pos falsa: +0.322368
#No intervalo a = -8.000000
#No intervalo b = +0.322378
# 149  iterações

#g) #Raiz aproximada encontrada por pos falsa: +0.000015
#No intervalo a = +0.000022
#No intervalo b = +3.000000
# 28  iterações

#h) #Raiz aproximada encontrada por pos falsa: +2.918613
#No intervalo a = +2.918587
#No intervalo b = +6.000000
# 109  iterações

#i) #Raiz aproximada encontrada por pos falsa: +0.641714
#No intervalo a = +0.641713
#No intervalo b = +1.416173
# 6  iterações

#j) #Raiz aproximada encontrada por pos falsa: +3.034452
#No intervalo a = +0.000000
#No intervalo b = +3.034470
# 7  iterações

