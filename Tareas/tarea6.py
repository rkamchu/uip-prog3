import os


def Clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

def Menu(NumEnc,lista): 
    Clear()
    print('{0}-{1}\n'.format(NumEnc,len(lista)))
    print('¿Que deporte practica?')
    print()
    for m in range(len(lista)):
        print('{0}. {1}'.format(m + 1,lista[m][0])) 
    print() 

def Porcentaje(TotEnc,EncTot):
    return (TotEnc/EncTot) * 100

def PrintResultados(lista):
    Clear()
    print("Resultados")
    print()
    for NumEnc in range(len(lista)):
        print("{0} - {1}\t\t=\t{2}/{3}\t({4}%)".format(NumEnc +1,lista[NumEnc][0],lista[NumEnc][1],len(lista),Porcentaje(lista[NumEnc][1],len(lista))))
    input()

if __name__ == '__main__':
    omenu = 0
    Encuesta=[['Ajedrez',0],['Atletismo',0],['Baloncesto',0],['Futbol',0],['Karate',0],['Natacion',0],['Volleyball',0],['Flag',0],['Ping Pong',0],['Otros',0]]
    EncTot = len(Encuesta)
    EncuestadoActual = 0
    while EncuestadoActual <= EncTot - 1:
        Menu(EncuestadoActual + 1,Encuesta)
        try: 
            menus = int(input("Seleccione una opcion (1-10): ")) 
        except: 
            print()
            print("Opcion invalida") 
            input()
        else: 
            if menus >= 1 and omenu <= 10:
                Encuesta[menus -1][1] += 1 
                print()
                print("La persona {0} ha seleccionado el deporte {1}".format(EncuestadoActual + 1,menus))
                input()
                EncuestadoActual += 1
            else: 
                print()
                print("Opcion invalida") 
                input()

    PrintResultados(Encuesta)
