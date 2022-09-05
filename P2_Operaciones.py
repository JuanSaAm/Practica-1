#P2-Operadores

#Declaracion de variables numericas
n1 = 234        #variable int
n2 = 12.3445    #variable float
suma = 23 + 65
resta = 12-8
mul = 4*3       #Operaciones dentro de variables
div = 12/3
exp = 2**5      #Exponencial

#Imprimir variables numericas 
print("La forma incorrecta de declarar numeros en python es con '+': ", n1+n2+suma) #Concatenacion no se hace con +, porque los resultados se suman
print("La forma correcta de declarar numeros en python es con ',': ", n1,n2,suma)
print("Ruesultados de las variables:\n","suma: ",suma,"\n","resta: ",resta,"\n","multiplicacion: ",mul,"\n","divicion: ",div,"\n","exponencial: ",exp)
print("De esta manera se redondea un numero float",round(n2,2))
