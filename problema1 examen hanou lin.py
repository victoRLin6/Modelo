cadena=input("Di una cadena")
s=cadena.find("t")
k=cadena.rfind("t")
print((cadena[:s])+(cadena[k+1:]))
