from typing import Literal
from Inputs import *

#FUNCIONES DE INICIALIZACIÓN
def imprimir_menu():
    """Imprime el menu de opciones
    """
    print("***   COMPETENCIA DE BAILE ***")
    print("------------------------------")
    print("1- Cargar participantes")
    print("2- Cargar puntuaciones")
    print("3- Mostrar puntuaciones")
    print("4- Mostrar participantes con promedio menor a 4")
    print("5- Mostrar participante con promedio menor a 8")
    print("6-  Mostrar promedio de cada jurado")
    print("7- Mostrar al jurado mas estricto")
    print("8- Mostrar el jurado mas generoso")
    print("9- Mostrar participantes con puntuaciones iguales")
    print("10- Buscar participante por nombre")
    print("11- Mostrar participantes ordenados alfabeticamente")
    

def menu_principal() -> str | None:
    """
    imprime un menu y solicita que se elija una opción, se valida la opción ingresada, si es valida se retorna la misma sino se muestra un msj de error.
    """
    imprimir_menu()

    opcion_elegida = input("Seleccione una opcion: ")
    if validar_entero(opcion_elegida) and validar_rango_inclusivo(1,12,int(opcion_elegida)):
        return opcion_elegida
    else:
        return print("\nError! opcion no valida, vuelva a intentarlo. ")
    
def generar_array(longitud:int, valor_inicial:any)-> list:
    """
    Crea un array de una dimensión con un valor inicial.

    Args:
        longitud (int): tamaño del array a generar.
        valor_inicial (any): valor que llenará cada posición del array.

    Returns:
        list: array de longitud `longitud` donde cada elemento es `valor_inicial`.
    """
    array = [valor_inicial] * longitud
    return array

def inicializar_matriz(cantidad_filas:int,cantidad_columnas:int,valor_inicial:any)-> list:
    """
    Crea una matriz con un valor inicial en todas sus celdas.

    Args:
        cantidad_filas (int): número de filas de la matriz.
        cantidad_columnas (int): número de columnas de cada fila.
        valor_inicial (any): valor con el que se inicializarán todas las posiciones.

    Returns:
        list: matriz de tamaño cantidad_filas x cantidad_columnas, donde cada elemento es valor_inicial.
    """
    matriz = []

    for i in range(cantidad_filas):
        fila = [valor_inicial] * cantidad_columnas

        matriz += [fila]
    return matriz


#FUNCIONES PARA IMPRIMIR DATOS

def mostrar_array(array:list,msj_opcional=""):
    """
    Imprime los elementos de una lista, con índice y mensaje opcional.

    Args:
        array (list): lista de elementos a imprimir.
        msj_opcional (str): texto que se antepone a cada elemento impreso.

    Returns:
        None: imprime directamente en consola.
    """
    for i in range(len(array)):
        print(f"{msj_opcional}{i + 1}- {array[i]}")

def mostrar_mismo_puntaje(matriz:list,array:list):
    """
    Muestra los grupos de participantes que tienen el mismo puntaje promedio.

    Args:
        matriz (list): Lista de listas, donde cada sublista contiene nombres de participantes con el mismo puntaje.
        array (list): Lista de puntajes promedio correspondientes a cada grupo en 'matriz'.

    Prints:
        Imprime el puntaje promedio seguido de los nombres de los participantes que lo obtuvieron.
    """
    for f in range(len(matriz)): 
        print(f"PARTICIPANTES CON PROMEDIO: {array[f]:.2f}")
        for c in range(len(matriz[f])):
            print(f"-{matriz[f][c]}")

def mostrar_puntajes(matriz_puntaje:list,array_nombres:list,array_promedio:list):
    """
    Imprime los puntajes y el promedio de cada participante.

    Args:
        matriz_puntaje (list): matriz que contiene los puntajes por jurado para cada participante.
        array_nombres (list): nombres de los participantes.
        array_promedio (list): promedios de puntaje de los participantes.
    """
    for f in range(len(matriz_puntaje)):
        print(f"\nPARTICIPANTE: {array_nombres[f]}")
        for c in range(len(matriz_puntaje[f])):
            print(f" -Puntaje Jurado n°{c + 1}: {matriz_puntaje[f][c]}")

        print(f"PROMEDIO : {array_promedio[f]:.2f}\n")

def mostrar_participante_puntaje(matriz:list,array:list,array_promedio:list):
    """
    Imprime los puntajes y promedio de un único participante.

    Args:
        matriz (list): lista de puntajes del participante.
        array (list): nombre del participante.
        array_promedio (list): promedio de puntaje del participante.
    """
    print(f"\nPARTICIPANTE: {array}")

    for i in range(len(matriz)):
        print(f" -Puntaje Jurado n°{i + 1}: {matriz[i]}")

    print(f"PROMEDIO : {array_promedio:.2f}")  

def mostrar_promedio_participantes(array_promedios:list,array_nombres:list,promedio:int,menor:bool):
    """
    Muestra los participantes cuyo promedio es menor o mayor que un valor dado.

    Args:
        array_promedios (list): Lista de promedios numéricos de los participantes.
        array_nombres (list): Lista de nombres de los participantes, en el mismo orden que 'array_promedios'.
        promedio (int): Valor de referencia con el que se compararán los promedios.
        menor (bool): Si es True, se mostrarán los participantes con promedio menor que el dado.
                      Si es False, se mostrarán los participantes con promedio mayor que el dado.

    Prints:
        - Nombre y promedio de cada participante que cumple la condición.
        - Si ningún participante cumple, imprime un mensaje de error.
    """
    contador = 0

    for i in range(len(array_promedios)):
        if menor:
            if array_promedios[i] < promedio:
                contador += 1
                print(f"{array_nombres[i]}, tuvo promedio de {array_promedios[i]:.2f}")
        else:
            if array_promedios[i] > promedio:
                contador += 1
                print(f"{array_nombres[i]} tuvo promedio de {array_promedios[i]:.2f}")

    if contador == 0:
        print("ERROR! No hay nigun participante que cumpla con los requisitos.")

def comprobar_array_vacio(valor_uno,valor_dos) -> bool:
    """
    Verifica si ambas listas están vacías.

    Args:
        valor_uno (list): Primera lista.
        valor_dos (list): Segunda lista.

    Returns:
        bool: True si ambas listas están vacías, False en caso contrario.
    """
    if valor_uno == [] and valor_dos == []:
        return True
    else:
        return False

def mostrar_segun_retorno(valor_uno,valor_dos,msj_error:str) -> str | None:
    """
    Muestra los resultados de participantes con puntajes iguales o un mensaje de error si no hay datos.

    Args:
        valor_uno (list): Lista de listas con participantes que comparten el mismo puntaje.
        valor_dos (list): Lista de puntajes correspondientes a cada grupo.
        msj_error (str): Mensaje a mostrar si ambas listas están vacías.

    Returns:
        str | None: Devuelve el mensaje de error si no hay datos, de lo contrario imprime los resultados.
    """
    if comprobar_array_vacio(valor_uno,valor_dos) :
        return msj_error
    else:
        mostrar_mismo_puntaje(valor_uno,valor_dos)
  
#FUNCIONES DE CARGA DE DATOS

def cargar_datos_matriz(matriz:list,msj:str): 
    """
    Carga manualmente datos numéricos en una matriz (lista de listas), solicitando al usuario las puntuaciones 
    de cada jugador. Cada celda de la matriz se completa con un valor entero validado dentro del rango [1, 10].

    Args:
        matriz (list): Matriz vacía o con estructura predefinida (lista de listas) donde se almacenarán los datos.
        msj (str): Mensaje base que se mostrará al pedir la puntuación de cada celda (por ejemplo: "Ingrese puntuación").

    Precondiciones:
        - Se espera que estén disponibles las siguientes funciones auxiliares:
            - `validar_rango_no_inclusivo(inicio, fin, valor)`: Devuelve True si valor ∈ (inicio, fin).
            - `validar_rango_inclusivo(inicio, fin, valor)`: Devuelve True si valor ∈ [inicio, fin].
            - `pedir_cadena(mensaje, funcion_validadora)`: Solicita entrada del usuario y aplica la función validadora.
            - `validar_entero(valor)`: Devuelve True si el valor es un número entero válido.

    Funcionamiento:
        - Para cada fila (jugador), se imprime un encabezado de carga.
        - Para cada columna (puntaje), se solicita un número entre 1 y 10, reintentando si no es válido.
        - La validación de rangos `no inclusivos` usada en los `if` es redundante, ya que todos los caminos hacen lo mismo.

    Prints:
        - Muestra mensajes indicando qué puntaje se está cargando para cada jugador.
        - Solicita la entrada para cada posición de la matriz.

    Side Effects:
        - Modifica directamente la matriz ingresada por referencia.
    """
    for f in range(len(matriz)):
        if validar_rango_no_inclusivo(0,2,f+1):
            print(f"\nCARGAR PUNTUACIONES DEL JUGADOR {f+1}: ")
        elif validar_rango_no_inclusivo(1,3,f+1):
            print(f"\nCARGAR PUNTUACIONES DEL JUGADOR {f+1}: ")
        elif validar_rango_no_inclusivo(2,4,f+1):
            print(f"\nCARGAR PUNTUACIONES DEL JUGADOR {f+1}: ")
        elif validar_rango_no_inclusivo(3,5,f+1):
            print(f"\nCARGAR PUNTUACIONES DEL JUGADOR {f+1}: ")
        else:
             print(f"\nCARGAR PUNTUACIONES DEL JUGADOR {f+1}: ")

        for c in range(len(matriz[f])):
            if validar_rango_no_inclusivo(0,2,f+1):
                matriz[f][c]= pedir_cadena(f"{msj} {c+1}: ", validar_entero)

                while not validar_rango_inclusivo(1,10,int(matriz[f][c])):
                    matriz[f][c]= pedir_cadena(f"Error, {msj} {c+1}: ", validar_entero)

                matriz[f][c] = int(matriz[f][c])

            elif validar_rango_no_inclusivo(1,3,f+1):
                matriz[f][c]= pedir_cadena(f"{msj} {c+1}: ", validar_entero)

                while not validar_rango_inclusivo(1,10,int(matriz[f][c])):
                    matriz[f][c]= pedir_cadena(f"Error, {msj} {c+1}: ", validar_entero)

                matriz[f][c] = int(matriz[f][c])

            elif validar_rango_no_inclusivo(2,4,f+1):
                matriz[f][c]= pedir_cadena(f"{msj} {c+1}: ", validar_entero)

                while not validar_rango_inclusivo(1,10,int(matriz[f][c])):
                    matriz[f][c]= pedir_cadena(f"Error, {msj} {c+1}: ", validar_entero)

                matriz[f][c] = int(matriz[f][c])

            elif validar_rango_no_inclusivo(3,5,f+1):
                matriz[f][c]= pedir_cadena(f"{msj} {c+1}: ", validar_entero)

                while not validar_rango_inclusivo(1,10,int(matriz[f][c])):
                    matriz[f][c]= pedir_cadena(f"Error, {msj} {c+1}: ", validar_entero)

                matriz[f][c] = int(matriz[f][c])

            else:
                matriz[f][c]= pedir_cadena(f"{msj} {c+1}: ", validar_entero)

                while not validar_rango_inclusivo(1,10,int(matriz[f][c])):
                    matriz[f][c]= pedir_cadena(f"Error, {msj} {c+1}: ", validar_entero)

                matriz[f][c] = int(matriz[f][c])   
    
def cargar_array_str(array:list,msj:str,longuitud_str:int) -> bool:
    """
    Solicita al usuario cadenas para cada posición de un array y los carga.

    Args:
        array (list): array preexistente que se rellenará.
        msj (str): mensaje base para solicitar cada elemento.
        longuitud_str (int): longitud mínima requerida para la validación de cada cadena.

    Returns:
        bool: True si el array tiene al menos un elemento después de cargar; False en caso contrario.
    """
    for i in range(len(array)):
        dato = pedir_cadena_doble_validacion(f"{msj} {i + 1}: ",validar_cadena_alfa,validar_longuitud,longuitud_str)
        dato = convertir_mayuscula(dato)
        array[i] = dato

    if len(array) > 0:
        return True
    else:
        return False

#FUNCIONES DE CALCULOS

def sumar_fila_matriz(matriz:list) -> list[int]:
    """Suma los valores de cada fila de la matriz.

    Args:
        matriz (list): Matriz de números.

    Returns:
        list[int]: Suma de cada fila.
    """
    array_sumar_filas = generar_array(len(matriz),0)

    for f in range(len(matriz)):
        for c in range(len(matriz[f])):
            array_sumar_filas[f]  += matriz[f][c]

    return array_sumar_filas

def sumar_columnas_matriz(matriz:list) -> list:
    """Suma los valores de cada columna de la matriz.

    Args:
        matriz (list): Matriz de números.

    Returns:
        list: Suma de cada columna.
    """
    array_sumar_columnas = generar_array(len(matriz[0]),0)

    for f in range(len(matriz)):
        for c in range(len(matriz[f])):
            array_sumar_columnas[c]  += matriz[f][c]

    return array_sumar_columnas

def calcular_promedio(array_suma_fila:list,divisor:int) -> list[int]:
    """Calcula el promedio de cada valor del array usando un divisor.

    Args:
        array_suma_fila (list): Lista de sumas.
        divisor (int): Número por el que se divide cada suma.

    Returns:
        list[int]: Promedios calculados.
    """
    array_promedio = generar_array(len(array_suma_fila),0)

    for i in range(len(array_suma_fila)):
        array_promedio[i] = array_suma_fila[i]/divisor
    
    return array_promedio

def calcular_tipo_de_jurado(promedio_jurados:list)-> tuple:
    """Determina el jurado con el mayor y menor promedio.

    Args:
        promedio_jurados (list): Promedios por jurado.

    Returns:
        tuple: (jurado_min, jurado_max, minimo, maximo)
    """
    bandera = True
    jurado_min = 0
    jurado_max = 0
    minimo = None
    maximo = None
 
    for i in range(len(promedio_jurados)):
        if bandera:
            maximo = promedio_jurados[i]
            minimo = promedio_jurados[i]
            jurado_min = i+1
            jurado_max = i+1
            bandera = False
        else:
            if promedio_jurados[i] <  minimo:
                minimo = promedio_jurados[i]
                jurado_min = i+1
            elif promedio_jurados[i] > maximo:
                maximo = promedio_jurados[i]
                jurado_max = i+1

    return jurado_min,jurado_max,minimo,maximo

#FUNCIONES DE BUSQUEDA

def buscar_en_lista(lista:list,valor:any) -> None | bool:
    """Busca si un valor existe en una lista.

    Args:
        lista (list): Lista donde buscar.
        valor (any): Valor a buscar.

    Returns:
        bool | None: True si está, False si no.
    """
    for i in range(len(lista)):
        if valor == lista[i]:
            return True
        
    return False
        
def buscar_indice(lista:list, valor:any) ->  int | Literal[False]:
    """Devuelve el índice de un valor en la lista.

    Args:
        lista (list): Lista donde buscar.
        valor (any): Valor a buscar.

    Returns:
        int | bool: Índice si lo encuentra, False si no.
    """
    for i in range(len(lista)):
        if valor == lista[i]:
            indice = i
            return indice       
    return False

def buscar_mismo_puntaje(promedio:list,participantes:list)-> list | Literal[False]:
    """Busca participantes con el mismo puntaje promedio y guarda esos puntajes en un array y los nombres que corresponden los guarda en una matriz. .

    Args:
        promedio (list): Lista de promedios.
        participantes (list): Lista de nombres.

    Returns:
        list: Lista de grupos de participantes con mismo puntaje 
    """
    mismo_puntaje = []
    participantes_mismo_puntaje = []

    for i in range(len(promedio)-1):
        for j in range(i + 1,len(promedio)):
            if promedio[i] == promedio[j]:
                valor = promedio[i]

                if not buscar_en_lista(mismo_puntaje,valor):
                    mismo_puntaje += [valor]
                    participantes_mismo_puntaje += [[participantes[i], participantes[j]]]
                else:
                    indice = buscar_indice(mismo_puntaje,valor)
                    if not buscar_en_lista(participantes_mismo_puntaje[indice],participantes[i]):
                        participantes_mismo_puntaje[indice] += [participantes[i]]
    
                    if not buscar_en_lista(participantes_mismo_puntaje[indice],participantes[j]):
                        participantes_mismo_puntaje[indice]  += [participantes[j]]
    
    return participantes_mismo_puntaje,mismo_puntaje

def buscar_por_nombre(array:list,nombre:str) -> int | Literal[False]:
    """Busca un nombre en el array y devuelve su índice.

    Args:
        array (list): Lista de nombres.
        nombre (str): Nombre a buscar.

    Returns:
        int | bool: Índice si se encuentra, False si no.
    """
    for i in range(len(array)):
        if array[i] == nombre:
            return i
    return False

def bucador_participantes(nombres:list,puntajes:list,promedios:list):

    """Busca un participante por nombre e imprime su puntaje y promedio.

    Args:
        nombres (list): Lista de nombres.
        puntajes (list): Lista de listas de puntajes.
        promedios (list): Lista de promedios.
    """
    input = pedir_cadena("Ingrese el nombre del participante: ", validar_cadena_alfa)
    input = convertir_mayuscula(input)

    indice_participante = buscar_por_nombre(nombres,input)

    if verificar_tipo_retorno(indice_participante,bool):
        print("UPS.. No hay ningun jugador con ese nombre")
    else:
        puntaje = puntajes[indice_participante]
        nombre = nombres[indice_participante]
        promedio = promedios[indice_participante]
        msj =f"\n{mostrar_participante_puntaje(puntaje,nombre,promedio)}"
        return msj

#FUNCIONES DE ORDENAMIENTO
def intercambiar_inidces(array,izq,der):
    """
    Intercambia los elementos en las posiciones 'izq' y 'der' de un arreglo.

    Parámetros:
    array (list): Lista en la que se realizará el intercambio.
    izq (int): Índice del primer elemento a intercambiar.
    der (int): Índice del segundo elemento a intercambiar.

    Retorna:
    None: La función modifica la lista original en el lugar.
    """
    aux_izq = array[izq]
    array[izq] = array[der]
    array[der] = aux_izq

def ordenar_alfabeticamente(array_nombres:list,matriz_puntajes:list,promedio:list):
    """
    Ordena alfabéticamente la lista de nombres y reorganiza las listas de puntajes y promedios
    para mantener la correspondencia entre los datos.

    Parámetros:
    array_nombres (list): Lista de nombres que se ordenarán alfabéticamente.
    matriz_puntajes (list): Lista de listas con los puntajes asociados a cada nombre.
    promedio (list): Lista con los promedios correspondientes a cada nombre.

    Retorna:
    tuple: Las tres listas reordenadas (nombres, puntajes y promedios) manteniendo la correspondencia original.
    """
    for izq in range(len(array_nombres)-1):
        for der in range(izq + 1,len(array_nombres)):
            if array_nombres[izq] > array_nombres[der]:
                intercambiar_inidces(array_nombres,izq,der)
                intercambiar_inidces(matriz_puntajes,izq,der)
                intercambiar_inidces(promedio,izq,der)

    return array_nombres,matriz_puntajes,promedio