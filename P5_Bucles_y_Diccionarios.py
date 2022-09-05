#Declaracion de variables globales
N = 1
t1 = ('Nombre', 'telefono', 'celular')

#Declaracion de diccionarios
Per1 = {
    'Nombre': 'Juan',
    'telefono': '33XXXXX231',
    'celular': '30XXXXX956'
}

Per2 = {
    'Nombre': 'Maria',
    'telefono': '30XXXXX944',
    'celular': '31XXXXX336'
}

Per3 = {
    'Nombre': 'Pepe',
    'telefono': '34XXXXX456',
    'celular': '30XXXXX776'
}

Per4 = {
    'Nombre': 'Sofia',
    'telefono': '30XXXXX666',
    'celular': '30XXXXX616'
}

while N >= 0 :   #Bucle while
    print('\n\t\t\t---Este programa una agenda---', 
      '\n\t\t\t---Seleccione un numero para realizar una accion')
    N = int(input('\n\t\t\t0.- Mostrar\n\t\t\t1.- Agregar\n\t\t\t2.- Modificar\n\t\t\t3.- Eliminar\n\t\t\t4.- Salir\n\t\t\t--'))

    if N == 4: #if anidado
        print('\n\t\t\t--ADIOS--')
        break   #termina el ciclo

    elif N == 0:
        print('\n\t\t\t---SELECCIONASTE Mostrar---', 
          '\n\t\t\t--Todos los datos--')
        print('\t\t\t--Persona 1:')
        for y in Per1:      #ciclo for
            print('\t\t\t--', Per1[y])
        print('\t\t\t--Persona 2:')
        for y in Per2:
            print('\t\t\t--', Per2[y])
        print('\t\t\t--Persona 3:')
        for y in Per3:
            print('\t\t\t--', Per3[y])  #llamar todos los datos de un diccionario

    elif N == 1: 
        print('\n\t\t\t---SELECCIONASTE AGREGAR---', 
          '\n\t\t\t--Porfavor introdusca los datos--')
        t1 = dict.fromkeys(t1)      #combertir una tupla en diccionario
        t1['Nombre'] = str(input('\t\t\t--Nombre: '))
        t1['telefono'] = str(input('\t\t\t--Telefono: '))
        t1['celular'] = str(input('\t\t\t--Celular: ')) #agregar valores a los datos de la tupla
        print ('\t\t\t--Nuevo contacto: ', t1)
    elif N == 2:
        print('\n\t\t\t---SELECCIONASTE Modificar---', 
          '\n\t\t\t--Modificar--')
        a = int(input('\t\t\t-- Que quieres cambiar\n\t\t\t--1.-nombre\n\t\t\t--2.-telefono\n\t\t\t3.-celular\n\t\t\t'))
        print('\t\t\t--Se modifico--')
        if a == 1:
            b = 'Nombre'
            Per1[b] = str(input('\t\t\t--Nuevo valor: '))   #Cambiar dato de un diccionario
    
        elif a == 2:
           b = 'telefono'
           Per1[b] = str(input('\t\t\t--Nuevo valor: '))
        elif a == 3:
            b = 'celular'
            Per1[b] = str(input('\t\t\t--Nuevo valor: ')) 
    elif N == 3:
        print('\n\t\t\t---SELECCIONASTE Eliminar---', 
          '\n\t\t\t--Quieres eliminar todos los contactos?')
        a = int(input('\t\t\t--1.-Si\n\t\t\t--2.-No\n\t\t\t'))
        if a == 1:
            del Per1
            del Per2
            del Per3
            del Per4    #borrar diccionarios por completo
            print('\t\t\t---Registros borrados---')
        
    if N >= 5:
        print('\t\t\t---Valor no valido---')
        x = (input('\t\t\t--Introdusca 0 o mayor a cero para continuar ...'))
else:   #else en while
    print('\t\t\t---Valor no valido---')

