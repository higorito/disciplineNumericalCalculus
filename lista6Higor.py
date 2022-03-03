# -*- coding: utf-8 -*-
"""
Created on Thu Feb 24 17:02:57 2022

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

            print('#Raiz aproximada encontrada por newton: {r:+.6f}'.format(r=x))
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

#RESPOSTAS
#A) TESTE DE CONVERGENCIA 
#1- é continua no intervalo 0.1,2
#2- a derivada nao é igual a zero no intervalo
#3- a segunda derivada nao muda de sinal no intervalo
#Raiz aproximada encontrada por newton: +1.000000
#No intervalo a = +0.100000
#No intervalo b = +2.000000
# 6  iterações

#B) TESTE DE CONVERGENCIA 
#1- é continua no intervalo 
#2- a derivada nao é igual a zero no intervalo
#3- a segunda derivada nao muda de sinal no intervalo
# Apesar de passar no teste de convergencia não foi possivel identificar a raiz

#C) TESTE DE CONVERGENCIA 
#1- é continua no intervalo 
#2- a derivada nao é igual a zero no intervalo
#3- a segunda derivada MUDA o sinal no intervalo
# mas mesmo assim irei aplicar o metodo
#Raiz aproximada encontrada por newton: +1.570796
#No intervalo a = +1.000000
#No intervalo b = +2.000000
# 4  iterações

#D) TESTE DE CONVERGENCIA 
#1- é continua no intervalo 
#2- a derivada nao é igual a zero no intervalo
#3- a segunda derivada nao muda o sinal no intervalo
#Raiz aproximada encontrada por newton: -1.000008
#No intervalo a = -2.000000
#No intervalo b = +0.000000
# 17  iterações

#E) TESTE DE CONVERGENCIA 
#1- é continua no intervalo 
#2- a derivada nao é igual a zero no intervalo
#3- a segunda derivada MUDA o sinal no intervalo
#mesmo assim eu rodei o algoritmo e não foi possivel achar raiz nos 20intervalos

#F) TESTE DE CONVERGENCIA 
#1- é continua no intervalo 
#2- a derivada nao é igual a zero no intervalo
#3- a segunda derivada MUDA o sinal no intervalo
#Mas vou testar mesmo assim 
#Raiz aproximada encontrada por newton: +0.322185
#No intervalo a = -5.000000
#No intervalo b = +5.000000
# 8  iterações

#G) TESTE DE CONVERGENCIA 
#1- é continua no intervalo 
#2- a derivada nao é igual a zero no intervalo
#3- a segunda derivada NAO muda o sinal no intervalo
#Raiz aproximada encontrada por newton: -0.876726
#No intervalo a = -2.000000
#No intervalo b = -0.500000
# 6  iterações

#H) TESTE DE CONVERGENCIA 
#1- é continua no intervalo 
#2- a derivada nao é igual a zero no intervalo
#3- a segunda derivada MUDA o sinal no intervalo
#Irei testar mesmo assim

#Raiz aproximada encontrada por newton: +2.918827
#No intervalo a = -10.000000
#No intervalo b = +5.000000
# 7  iterações

#I) TESTE DE CONVERGENCIA 
#1- é continua no intervalo 
#2- a derivada nao é igual a zero no intervalo
#3- a segunda derivada MUDA o sinal no intervalo
#Irei testar indiferente do teste
#Nao achou raiz

#J) TESTE DE CONVERGENCIA 
#1- é continua no intervalo 
#2- a derivada nao é igual a zero no intervalo
#3- a segunda derivada NAO muda o sinal no intervalo
#Raiz aproximada encontrada por newton: +3.034447
#No intervalo a = +2.000000
#No intervalo b = +4.000000
# 5  iterações