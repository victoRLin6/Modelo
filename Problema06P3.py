x=int(input('Km que puedes correr'))
y=int(input("km que tiene que correr"))
dias=0
while x<y:
  i=x*0.1
  x=x+i
  dias+=1
print(dias)