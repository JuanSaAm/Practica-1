
m3 = []
m4 = []
m5 = []

print('\n\t\t\t---Este programa nos ayuda a calcular el promedio de tres materias---')
n = int(input('\t\t\t---Que semestres quieres promediar?(Solo 3, 4 o 5 semestre)\n\t\t\t---'))  #Guardar un dato dado por el usuario en un int

if n == 3:      #if simple
    print('\t\t\t---Escogiste el Tercer semestre---')
    m3.append(int(input('\t\t\t--Que calificacion sacaste en la materia 1:  ')))
    m3.append(int(input('\t\t\t--Que calificacion sacaste en la materia 2:  ')))
    m3.append(int(input('\t\t\t--Que calificacion sacaste en la materia 3:  ')))    #Guardar datos dado por el usuario en una lista
    M = (m3[0] + m3[1] + m3[2])/3

    if M < 0:   #if dentro de un if
        print('\t\t\t--Valores invalidos')

    elif M <= 69:   #metodos elif
        print('\t\t\t--Tu Promedio es: ', M, 'REPROBASTE')

    elif M >= 70 and M <= 100:  #condicionales
        print('\t\t\t--Tu Promedio es: ', round(M,0), 'APROBASTE')

    else:   #metodo else
        print('\t\t\t--Valores invalidos')

elif n == 4:
    print('\t\t\t---Escogiste el Cuarto semestre---')
    m4.append(int(input('\t\t\t--Que calificacion sacaste en la materia 1:  ')))
    m4.append(int(input('\t\t\t--Que calificacion sacaste en la materia 2:  ')))
    m4.append(int(input('\t\t\t--Que calificacion sacaste en la materia 3:  ')))
    M = (m4[0] + m4[1] + m4[2])/3

    if M < 0:
        print('\t\t\t--Valores invalidos')

    elif M <= 69:
        print('\t\t\t--Tu Promedio es: ', M, 'REPROBASTE')

    elif M >= 70 and M <= 100:
        print('\t\t\t--Tu Promedio es: ', round(M,0), 'APROBASTE')

    else:
        print('\t\t\t--Valores invalidos')

elif n == 5:
    print('\t\t\t---Escogiste el Quinto semestre---')
    m5.append(int(input('\t\t\t--Que calificacion sacaste en la materia 1:  ')))
    m5.append(int(input('\t\t\t--Que calificacion sacaste en la materia 2:  ')))
    m5.append(int(input('\t\t\t--Que calificacion sacaste en la materia 3:  ')))
    M = (m5[0] + m5[1] + m5[2])/3

    if M < 0:
        print('\t\t\t--Valores invalidos')

    elif M <= 69:
        print('\t\t\t--Tu Promedio es: ', M, 'REPROBASTE')

    elif M >= 70 and M <= 100:
        print('\t\t\t--Tu Promedio es: ', round(M,0), 'APROBASTE')

    else:
        print('\t\t\t--Valores invalidos')

else:
    print('\t\t\t---Valor no valido---')