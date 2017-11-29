print("casilla1")
x=int(input())
y=int(input())
print("casilla2")
x1=int(input())
y2=int(input())


if((x+y)%2==0)and((x1+y2)%2==0):
  print("Mismo color negro")
elif ((x+y)%2!=0)and((x1+y2)%2!=0):
  print("Mismo color blanco")
else:
  if((x+y)%2==0)and((x1+y2)%2!=0):
    print("Distinto color: primero negro segundo blanco")
  else:
    print("Distinto color: Primero blanco segundo negro")
  
  

