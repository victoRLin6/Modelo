import math

def potencia(x,n):
 exponente=1
 for i in range(0,n):
   exponente=exponente*x
 return exponente


def distancia(x1,x2,y1,y2):
  c1=x1-x2
  c2=y1-y2
  return math.sqrt(potencia(c1,2))+(potencia(c2,2))


x1=int(input("x1="))
y1=int(input("y1="))
x2=int(input("x2="))
y2=int(input("y2="))

print(distancia(x1,y1,x2,y2))



