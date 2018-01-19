a=int(input("Primer numero:"))
b=int(input("Segundo numero:"))
if(a<b):
  for i in range(a,b+1):
    print(i)
else:
  for x in range(a,b-1,-1):
    print(x)
    