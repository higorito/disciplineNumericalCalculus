import numpy as np
from math import e

def f(x):
 # return np.log(x)
 # return  e**x
 # return  np.cos(x)
 # return  x**2 +2*x +1
 # return  (e**(2-x**2))*(x+1)**2
 # return  x**3 +3*x -1
 # return  x**2 +np.sin(x)
 # return  e**x -x**2 -10
 # return  np.sqrt(x) -np.cos(x)
  return  x-3 -x**-x

def gx1(x):
 return x - 0.05 * f(x)

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
     

pontoFixo(2, 4, 10**-5, 300)

#RESPOSTAS
#A) #Raiz aproximada encontrada por ponto fixo: +1.000188
#No intervalo a = +0.100000
#No intervalo b = +3.000000
# 161  iterações

#B) Não tem raiz, nao importa a interação

#C) #Raiz aproximada encontrada por ponto fixo: -1.570615
#No intervalo a = +1.000000
#No intervalo b = +2.000000
# 250  iterações

#D) #Raiz aproximada encontrada por ponto fixo: -1.000000
#No intervalo a = -2.000000
#No intervalo b = +0.000000
# 1  iterações

#E) #Raiz aproximada encontrada por ponto fixo: -3.516057
#No intervalo a = -2.000000
#No intervalo b = -0.500000
# 17340  iterações

#F) #Raiz aproximada encontrada por ponto fixo: +0.322136
#No intervalo a = -5.000000
#No intervalo b = +5.000000
# 49  iterações

#G) aqui quando se usa o intervalo como -0.5 da erro e quando usa 0.5 da esse resultado:
    #Raiz aproximada encontrada por ponto fixo: -0.000187
    #No intervalo a = -2.000000
    #No intervalo b = +0.500000
    # 197  iterações
    
#H) #Raiz aproximada encontrada por ponto fixo: +2.918819
#No intervalo a = -10.000000
#No intervalo b = +5.000000
# 22  iterações

#I) #Raiz aproximada encontrada por ponto fixo: +0.641860
#No intervalo a = +0.000000
#No intervalo b = +2.000000
# 123  iterações

#J) #Raiz aproximada encontrada por ponto fixo: +3.033927
#No intervalo a = +2.000000
#No intervalo b = +4.000000
# 76  iterações