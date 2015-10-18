def agregarNotas(estudiantes, nombre, quiz1, quiz2, quiz3, quiz4, quiz5):
    promedio = int(quiz1 + quiz2 + quiz3 + quiz4 + quiz5) / 5
    estudiantes[nombre] = promedio

def guardarNotas(estudiantes, archivo):
    out_file = open(archivo, "wt")
    out_file.write(estudiantes + "," + promedio + "\n")
    out_file.close()

def mostrarMenu():
    print('1. Imprimir notas')
    print('2. Agregar notas')
    print('3. Guardar notas')
    print('4. Salir')
    print()

if __name__ == '__main__':
    estudiantes = {}
    opcion_menu = 0
    while True:
        mostrarMenu()
        try:
            opcion_menu = int(input("Indica una opcion (1-4): "))
        except:
            print("Opcion no valida")
        else:
            if opcion_menu == 1:
                imprimirNotas(estudiantes)
            elif opcion_menu == 2:
                print("Agregar nombre y quizzes")
                nombre = input("nombre: ")
                quiz1 = int(input("quiz1: "))
                quiz2 = int(input("quiz2: "))
                quiz3 = int(input("quiz3: "))
                quiz4 = int(input("quiz4: "))
                quiz5 = int(input("quiz5: "))
                promedio = int(quiz1 + quiz2 + quiz3 + quiz4 + quiz5) / 5
                print("El promedio de este estudiante es: " + str(promedio))
                agregarNotas(estudiantes, nombre, quiz1, quiz2, quiz3, quiz4, quiz5)
            elif opcion_menu == 3:
                archivo = input("Archivo a guardar: ")
                guardarNotas(estudiantes, archivo)
            elif opcion_menu == 4:
                break
            else:
                print("Opcion no valida")
                mostrarMenu()

print("Hasta luego!")
