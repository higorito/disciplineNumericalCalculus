from math import e
import numpy as np

def f(x):
    
 #aqui vou escolher qual função do exercicio pq nao consegui usar o eval
    
 # return  np.log(x)
 # return  e**x
 # return  np.cos(x)
 # return  x**2 +2*x +1
 # return  (e**(2-x**2))*(x+1)**2
 # return  x**3 +3*x -1
 # return  x**2 +np.sin(x)
 # return  e**x -x**2 -10
 # return  np.sqrt(x) -np.cos(x)
  return  x-3 -x**-x


 
def bissecao(a, b, tol, n):
    xa = float('nan')
    for i in range(n):

        x = (a + b) / 2
        fx = f(x)
         
        sinal = f(a) * fx
        
        error=abs((x-xa)/max(x, 1))
         
        xa = x
        
        print('It. {i:3d}:'.format(i=i), 'a={a:+.6f},'.format(a=a),
         'b={b:+.6f},'.format(b=b), 'error={e:+.6f},'.format(e=error),
         'x={x:+.6f},'.format(x=x), 'f(x)={fx:+.6f},'.format(fx=fx),
         'sinal={s:+.6f}'.format(s=sinal))
        if (fx == 0) or (error < tol):

            print('Raiz aproximada encontrada: {r:+.6f}'.format(r=x))
             
            break
        
        if sinal > 0:
        
            a = x
        else:
         
            b = x
        
        
bissecao(2, 4, 0.0001, 20)


#RESPOSTAS 
#TODAS UTILIZEI 20 INTERAÇÕES E 10**-5  MUDOU-SE OS INTERVALOS NA FUNÇÃO BISSECAO
#a) ln x, intervalo [0; 2]
#Raiz aproximada encontrada: +1.000000

#b) e**x intervalo {1,2}
#Raiz aproximada encontrada: +1.999878

#c) np.cos(x) intervalo {1,2}
#Raiz aproximada encontrada: +1.570679

#d) x**2 +2*x +1 intervalo {-2,0}
#Raiz aproximada encontrada: +1.999878

#e) (e**(2-x**2))*(x+1)**2 intervalo {-2,-0.5}
#Raiz aproximada encontrada: -0.500092

#f) x**3 +3*x -1 intervalo {-5,5}
#Raiz aproximada encontrada: +0.322189

#g) x**2 +np.sin(x) intervalo {-2,-0.5}
#Raiz aproximada encontrada: -0.876740

#h) **x -x**2 -10 {-10,5}
#Raiz aproximada encontrada: +2.918777

#i) np.sqrt(x) -np.cos(x) intervalo {0,2}
#Raiz aproximada encontrada: +0.641663

#j) x-3 -x**-x intervalo {2,4}
#Raiz aproximada encontrada: +3.034424