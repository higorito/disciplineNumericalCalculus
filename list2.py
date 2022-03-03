# -*- coding: utf-8 -*-
"""
Created on Mon Jan 31 17:22:31 2022

@author: higor
"""

import numpy as np
import matplotlib.pyplot as pyplot
from math import e


def eval_f(fx, x):
    return eval(fx)

def plotar(fx, a, b):
    xx=np.linspace(a, b)
    pyplot.plot(xx, eval_f(fx, xx))
    pyplot.grid()
    pyplot.show()
    
func = input("Qual a função? ")

a= float(input("Intervalo inicio: "))
b= float(input("Intervalo final: "))

plotar(func, a, b)

#RESPOSTAS LISTA 2
#letra A)  Intervalos respectivamente nas linhas  - np.log(x)
#{100, -50}  
#{50, -10}
#{10, 0}    todos tem so uma raiz, mas aqui vê mais claramente

#letra b)  Intervalos respectivamente nas linhas  - e**x
#{100, -100} 
#{50, -50} 
#{5, -5} 

#letra c)  Intervalos respectivamente nas linhas  - np.cos(x)
#{100, -100} 
#{10, -10} 
#{0, -2} 

#letra d)  Intervalos respectivamente nas linhas  - x**2 +2*x +1
#{100, -100} 
#{15, -15} 
#{1, -5}
#{-1.5, -0.5}
#{-1.11, 0.99}


#letra e)  Intervalos respectivamente nas linhas  - (e**(2-x**2))*(x+1)**2
#{100, -100} 
#{0, 15} 
#{3, 3.5}  //nunca vai encontrar

#letra f)  Intervalos respectivamente nas linhas  - x**3 +3*x -1
#{100, -100} 
#{10, -10} 
#{1, -1} 

#letra g)  Intervalos respectivamente nas linhas  - x**2 +np.sin(x)
#{100, -100} 
#{20, -20} 
#{0.2, -0.5} 

#letra h)  Intervalos respectivamente nas linhas  - e**x -x**2 -10
#{100, -100} 
#{0, 5}

#letra i)  Intervalos respectivamente nas linhas  - np.sqrt(x) -np.cos(x)
#{100, -100} 
#{2000, -2000} 
#{100000, 10000}     Nao tem 

#letra j)  Intervalos respectivamente nas linhas  - x-3 -x**-x
#{100, -100} 
#{0, 20}
#{0, 5}

