# ESte programa es una calculadora que opera dos numeros ingresados por el usuario 

A=float(input("Por favor ingrese el primer numero: "))
B=float(input("Por favor ingrese el segundo numero: "))

operador=(input("Que operacion desea hacer con estos numeros? Seleccione +,-,/,*: "))

if (operador!="+") and (operador!="-") and (operador!="*"):
 suma=A/B
 print("EL resultado de la"+" "+operador+" "+"es igual a"+" "+str(suma)) 
 
if operador=="-":
 resta=A-B
 print("EL resultado de la",operador,"es igual a",str(resta)) 
if operador=="/":
 division=A/B
 print("EL resultado de la",operador,"es igual a",str(division)) 
if operador=="*":
 multiplicacion=A*B
 print("EL resultado de la",operador,"es igual a",str(multiplicacion)) 
 
#print(type(operador))
#print(type(A))
#print(type(B))