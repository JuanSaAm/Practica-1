#P3-Listas y Tuplas

#Declaracion de listas y tuplas
l1 = []     #Lista vacia
l2 = [1, 10, 'Elemento 3', 12.14, 22]   #Las listas se declaran con corchetes []
l3 = ['d', 'w', 'x', 'f', 'z', 'h']
t = (1, 10, 12.14, 'Elemento 4', 22)    #Las listas se declaran con parentesis ()

#main
print("\t\t--Este programa compara listas y tuplas--\n", "\t\tLista 1: ", l1, "\n", "\t\tLista 2: ", l2, "\n\t\tLista 3: ", l3, "\n", "\t\tTupla: ", t)
print('\t\t-Las listas y las tuplas pueden guardar elementos\n\t\t la diferencia es que las listas pueden ser\n\t\t modificadas y las tuplas no.')
print("\t\t-Puedes llamar los elementos de las listas")
print("\t\t Segundo elemento de la lista:", l2[2])    #las listas empiezan a contar desde el 0
print("\t\t Elemento -1 de la lista:", l2[-1])        #Tambien puedes llamr a los elemntos en negativo
print('\t\t--Para modificar las listas podemos eliminar sus elemntos de 3 maneras')
del l2[1]   #Metodo del
print('\t\t -Metodo 1 : Eliminar el elemnto 1 de lista 2- ', l2)
l2.remove(1)#Metodo remove
print('\t\t -Metodo 2 : Eliminar el numero 1 de lista 2- ', l2)
a = l2.pop(-1)#Metodo pop
print('\t\t -Metodo 3 :Este metodo guarda el elemento eliminado en una variable,\n\t\t Eliminar el numero 1 de lista 2- ', l2, 'Variable nueva: ', a)
print('\t\t--Tambien podemos agregar elemntos a las listas con 2 metodos :')
l1.append(12) #metodo append
print('\t\t -Metodo 1 : Agregar el elemento 12 en lista1- ', l1)
l2.insert(1,'hola')#Metodo insert
print('\t\t -Metodo 2 :Este metodo podemos decidir en que lugar va a estar\n\t\t Eliminar el numero 1 de lista 2- ', l2)
print('\t\t--Tambien podemos ordenar los elemntos de las listas con 2 metodos :')
print('\t\t--Ordenar de manera temporal lista 3: ', sorted(l3))#metodo sorted
print('\t\t -despues lista 3: ', l3)
l3.sort()
print('\t\t--Ordenar de manera permanente lista 2: ', l3)#metodo sort
print('\t\t -despues lista 3: ', l3)
print('\t\t--funciones adicionales:')
print('\t\t -Contar la longitud de la lista 3: ', len(l3)) #metodo len
print('\t\t -covertir la lista 2 en tupla:', tuple(l2))
print('\t\t -covertir la tupla en una lista: ', list(t))