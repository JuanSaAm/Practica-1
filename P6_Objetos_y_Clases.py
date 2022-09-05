#Declarar bibliotecas
import math

#Declarar clases
class Usuario():
    def __init__(self, name,pin)        #propiedades __init__
        self.name=name
        self.pin=pin

    def singin(self):
        print('hola' + self.name + 'bienveniado')

    def singout(self):
        print('adios' + self.name)
class Usuario_VIP(Usuario):     #Clase con herencia
    pass

#funciones sueltas
def colores(**args):
    print('El color', args[1], 'es mi favorito.', 'El color', args[0], 'tampoco está mal.')

perimetro = lambda radio: round(math.pi*radio*2)    #funcion lambda

#Main

Usuariox=Usuario('Jose', '3294') #crear objeto
Usuarioy=Usuario_VIP('Mario', '2011')

colores("verde","Rojo") #ejecucion de funcione

print (perimetro(2))

Usuariox.singin() #Usar funciones dentro de clases
Usuariox.singin()