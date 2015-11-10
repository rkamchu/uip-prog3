import Lista as ls
import os


def Clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

def imprimirListaVacia():
    print("\nNo existen Listas, Favor Crear Lista Nueva")
    input()

def Menu(lista_actual,listaNombre): 
    Clear()
    print('LISTA ACTUAL: {0} - {1}\n'.format(lista_actual,listaNombre))
    print('1. Imprimir Articulos') 
    print('2. Agregar Articulo') 
    print('3. Eliminar Articulo') 
    print('4. Seleccionar Lista') 
    print('5. Nueva Lista') 
    print('6. Borrar Lista')
    print('7. Ver Listas')
    print('8. Salir') 
    print() 

def imprimirListas(lista,lista_actual):
    Clear()
    print('LISTA ACTUAL: {0} - {1}\n'.format(lista_actual,ls.getListaNombre(lista,lista_actual)))
    for i in range(len(lista)):
        if i == lista_actual:
            print('{0} - {1}  >>  Lista Actual'.format(i,lista[i][0]))
        else:
            print('{0} - {1}'.format(i,lista[i][0]))


def imprimirArticulos(listaNombre,lista):
    Clear()
    print('LISTA: {0}\n'.format(listaNombre))
    for i in range(len(lista)):
        print('{0} - {1}'.format(i,lista[i]))

def opcionImprimirArticulos(listaNombre,lista):
    imprimirArticulos(listaNombre,lista)
    input('\nPresione cualquier tecla para salir: ')

def opcionAgregarItemLista(listaNombre,lista):
    item = ''
    imprimirArticulos(listaNombre,lista)
    item=input('\nEscribir Nombre del Articulo Nuevo o 00 para salir: ')
    if item.strip() != '00' and item.strip() != "":
        lista = ls.agregarArticulo(lista,item.strip())
    return lista

def opcionBorrarItemLista(listaNombre,lista):
    item = ''
    imprimirArticulos(listaNombre,lista)
            
    try: 
        item=input('\nEscribir Numero del Articulo a Borrar o 00 para salir: ')

        if item != '00':
            itemN = int(item)
    except: 
            print("\nOpcion no valida") 
            input()
    else:
        if item != '00':
            if itemN >= 0 and itemN < len(lista): 
                lista = ls.borrarLista(lista,itemN)
            else:
                print("\nOpcion no valida") 
                input()

    return lista

def opcionSeleccionarLista(lista,lista_actual):
    listaSelec = ''
    imprimirListas(lista,lista_actual)
    try: 
        listaSelec=input('\nNumero de la Lista a Seleccionar (0-{0}) o 00 para Cancelar: '.format(len(lista)-1))
        if listaSelec != '00':
            listaSelecN = int(listaSelec)
    except: 
            print("\nOpcion no valida") 
            input()
    else:
        if listaSelec != '00':
            if listaSelecN >= 0 and listaSelecN < len(lista): 
                lista_actual = listaSelecN
            else:
                print("\nOpcion no valida") 
                input()
    return [lista_actual,lista]

def opcionAgregarLista(lista,lista_actual):
    listaNueva = ''
    imprimirListas(lista,lista_actual)
    listaNueva=input('\nNombre de la Lista Nueva o 00 para Cancelar: ')
    if listaNueva.strip() != '00' and listaNueva.strip():
        lista = ls.agregarLista(lista,listaNueva.strip())
        if lista_actual == -1:
            lista_actual += 1
    return [lista_actual,lista]

def opcionBorrarLista(lista,lista_actual):
    listaBorrar = ''
    imprimirListas(lista,lista_actual)
    try: 
        listaBorrar=input('\nNumero de la Lista a Borrar (0-{0})o 00 para Cancelar: '.format(len(lista)-1))
        if listaBorrar != '00':
            listaBorrarN = int(listaBorrar)
    except: 
            print("\nOpcion no valida") 
            input()
    else:
        if listaBorrar != '00':
            if listaBorrarN >= 0 and listaBorrarN < len(lista): 
                lista = ls.borrarLista(lista,listaBorrarN)
                if lista_actual >= listaBorrarN:
                    if lista_actual == 0 and len(lista) > 0:
                        lista_actual = 0
                    else:
                        lista_actual -= 1
            else:
                print("\nOpcion no valida") 
                input()
            
    return [lista_actual,lista]

def opcionVerListas(lista,lista_actual):
    imprimirListas(lista,lista_actual)
    input('\nPresione cualquier tecla para continuar: ')
         
if __name__ == '__main__':
    lista_actual = -1 
    listas_supermercado = []
    omenu = 0 
    listas_supermercado = ls.cargarListas("Tarea5",listas_supermercado)
    if len(listas_supermercado) > 0:
        lista_actual = 0
    while True: 
        Menu(lista_actual,ls.getListaNombre(listas_supermercado,lista_actual)) 
        try: 
            omenu = int(input("Seleccione una opcion (1-8): ")) 
        except: 
            print("Opcion invalida") 
        else: 
            if omenu == 1:
                if len(listas_supermercado) != 0:
                    opcionImprimirArticulos(listas_supermercado[lista_actual][0],listas_supermercado[lista_actual][1])
                else:
                    imprimirListaVacia()
            elif omenu == 2: 
                if len(listas_supermercado) != 0:
                    listas_supermercado[lista_actual][1] = opcionAgregarItemLista(listas_supermercado[lista_actual][0],listas_supermercado[lista_actual][1])
                else:
                    imprimirListaVacia()
            elif omenu == 3:
                if len(listas_supermercado) != 0:
                    if len(listas_supermercado[lista_actual][1]) != 0:
                        listas_supermercado[lista_actual][1] = opcionBorrarItemLista(listas_supermercado[lista_actual][0],listas_supermercado[lista_actual][1])
                    else:
                        print("\nLista de Supermercado Vacia")
                        input()
                else:
                    imprimirListaVacia()
            elif omenu == 4:
                if len(listas_supermercado) != 0:
                    listas = opcionSeleccionarLista(listas_supermercado,lista_actual)
                    lista_actual = listas[0]
                    listas_supermercado = listas[1]
                else:
                    imprimirListaVacia()   
            elif omenu == 5:
                listas = opcionAgregarLista(listas_supermercado,lista_actual)
                lista_actual = listas[0]
                listas_supermercado = listas[1]
            elif omenu == 6:
                if len(listas_supermercado) != 0:
                    listas = opcionBorrarLista(listas_supermercado,lista_actual)
                    lista_actual = listas[0]
                    listas_supermercado = listas[1]
                else:
                    imprimirListaVacia()        
            elif omenu == 7:
                if len(listas_supermercado) != 0:
                    opcionVerListas(listas_supermercado,lista_actual)
                else:
                    imprimirListaVacia()            
            elif omenu == 8:
                ls.salvarListas("Tarea5.txt",listas_supermercado)
                break 
            else: 
                Clear()
                print("Opcion invalida") 
