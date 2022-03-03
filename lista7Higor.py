import numpy as np
from math import e


def eval_f(fx, x):
    return eval(fx)

def eval_derivada(dx, x):
    return eval(dx)
 
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
      
        
        
f = input('Informe a função: ')
d= input('Informe a derivada: ')
a = float(input('Informe o início do intervalo: '))
b = float(input('Informe o fim do intervalo: '))
t = float(input('Informe a tolerância: '))
n = int(input('Informe o número de iterações: '))


secante(f,d, a, b, t, n)

#RESPOSTAS
#A)#Raiz aproximada encontrada por secante: +0.381711
#No intervalo a = +0.100000
#No intervalo b = +2.000000
# 9  iterações

#B) Nao tem raiz


#C) #Raiz aproximada encontrada por secante: +1.340837
#No intervalo a = +1.000000
#No intervalo b = +2.000000
# 7  iterações

#D) #Raiz aproximada encontrada por secante: -1.414211
#No intervalo a = -2.000000
#No intervalo b = +0.000000
# 7  iterações

#E) #Raiz aproximada encontrada por secante: -3.847586
#No intervalo a = -2.000000
#No intervalo b = -0.500000
# 8  iterações

#F) #Raiz aproximada encontrada por secante: -11.158264
#No intervalo a = -5.000000
#No intervalo b = +5.000000
# 65  iterações

#G) #Raiz aproximada encontrada por secante: -1.403476
#No intervalo a = -2.000000
#No intervalo b = -0.500000
# 11  iterações

#H) #Raiz aproximada encontrada por secante: +2.069575
#No intervalo a = -10.000000
#No intervalo b = +5.000000
# 24  iterações

#I) Nao consegui achar... mas deu esse resultado abaixo 
#Raiz aproximada encontrada por secante: +0.000000
#No intervalo a = +0.000000
#No intervalo b = +2.000000
# 1  iterações

#J) #Raiz aproximada encontrada por secante: +2.917595
#No intervalo a = +2.000000
#No intervalo b = +4.000000
# 6  iterações