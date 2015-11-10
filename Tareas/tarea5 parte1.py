def cargarListas(nombrearchivo,lista): 
    try:
        archivo = open(nombrearchivo, "rt") 
        while True: 
            linea = archivo.readline() 
            if not linea: 
                break 
            linea = linea[:-1] 
            listaNombre, Articulos = linea.split("=")
            if Articulos.strip() == "":
                listaArticulos = []
            else:  
                listaArticulos = Articulos.split(",")
            lista.append([listaNombre,listaArticulos])
        archivo.close() 
    except:
        print("")
    return lista

  
def salvarListas(nommbrearchivo,listas): 
    try:
        archivo = open(nommbrearchivo, "wt") 
        for lista in listas: 
            listaarchivo = ""
            for articulos in lista[1]:
                listaarchivo += "{0},".format(articulos)
            archivo.write(lista[0] + "=" + listaarchivo[:-1] + "\n")
        archivo.close()
    except:
        print("\nError al Guardar Archivo")
        input() 


def getListaNombre(lista,lista_actual):
    if len(lista) == 0:
        return '** LISTA VACIA **'
    else:
        return lista[lista_actual][0]

def agregarLista(lista,listaNombre):
    lista.append([listaNombre,[]])
    return lista

def agregarArticulo(lista,listaNombre):
    lista.append(listaNombre)
    return lista

def borrarLista(lista,listaNumero):
    lista.pop(listaNumero)
    return lista
