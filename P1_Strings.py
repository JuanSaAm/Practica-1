#!/usr/bin/env python 
#-*- coding: cp1252 -*-
#-*- coding: 850 -*-
#-*- coding: utf-8 -*-      #Lineas para poder imprimir acentos y caracteres especiales en la consola

#Declaracion de variables Strings
titulo = "\t\t\t---ejemplos de strings---\n\n"  #utilizar \t para tabular y \n para enter
up = "atención"
lo = "BuEnOs DíAs"
lo2 = "MINUSCULAS"
co = "'Comillas simples' dentro de un String"
co2 = '"Comillas dobles" dentro de Strings'     #Comillas en strings

#Imprimir Strings en la consola
print(titulo.title())   #Usar metodo title()
print("\t\t\tEste programa muestra la utilización de los Strings.\n")    #Imprimir Strings directamente
print("\t\t\t--" + up.upper() + "Es un metodo para poner todas en mayuculas." + "\n\t\t\t--" + lo.lower() + " y " + lo2.lower() + " Son ejemplos del metodo lower.\n")    #Concatenacion de variables strings
print("\t\t\t--Por ultimo: Esto es como se usan las comillas" + co + co2)
