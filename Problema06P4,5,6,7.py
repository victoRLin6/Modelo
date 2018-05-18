m=1
x=0
y=0
g=0
while True:
  
  n=int(input('Da un número:'))
  
  if n < g:
    g = g
  else:
    g = n
  if n==0:
   
    break
  
  x+=1
  y=y+n
print('Cantidad de numeros:'+str(x))
print('Suma numeros:'+str(y))

m=y/(x)
print('Media:'+ str(m))
print('Mas grande:'+ str(g))