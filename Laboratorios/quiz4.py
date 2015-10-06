chance = 0
segundos = 0
while chance < 6:
    time_seg = int(input("Ingrese el tiempo en segundos: "))
    chance +=1
    if time_seg / 60:
            segundos = 60 - time_seg % 60
            print(segundos)