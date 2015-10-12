#TAREA
#-----
#Fecha de Revisión: 12/10/2015
#-----

#Instrucciones:
#--------------
#1. Dado un intervalo de tiempo en minutos, calcular los días, horas y minutos correspondientes.

#2. ¿Qué es __main__ y cómo funciona?

#


chance = 0
minutos = 0
while chance < 6:
    time_min = int(input("Ingrese el tiempo en minutos: "))
    chance +=1
    if time_min / 60:
        minutos = 60 - time_min % 60
        dias = 24 - time_min % 24
        horas = 8 - time_min % 8
        print(minutos)
        print(dias)
        print(horas)
