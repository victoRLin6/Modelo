print("casilla1")
x=int(input())
y=int(input())
print("casilla2")
a=int(input())
b=int(input())
if(a==x+1)or(a==x-1):
  if(b==y):
    print ("si")
elif(b==y+1)or(b==y-1):
  if(a==x):
    print("si")
else:
  print("no")
  
  
  
    
    


  