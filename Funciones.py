from typing import Literal
from Inputs import *
import random

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
    print("11- Mostrar Top 3")
    print("12- Mostrar participantes ordenados alfabeticamente")
    print("13- Mostrar ganador")
    print("14- Desempatar")

def menu_principal() -> str | None:
    """
    imprime un menu y solicita que se elija una opción, se valida la opción ingresada, si es valida se retorna la misma sino se muestra un msj de error.
    """
    imprimir_menu()

    opcion_elegida = input("Seleccione una opcion: ")
    if validar_entero(opcion_elegida) and validar_rango_inclusivo(1,14,int(opcion_elegida)):
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
        fila = generar_array(cantidad_columnas,valor_inicial)

        matriz += [fila]
    return matriz

#FUNCIONES PARA IMPRIMIR DATOS

def mostrar_array(array:list,msj_opcional="") -> str:
    """
    Genera un string con los elementos del array, cada uno precedido por su índice y un mensaje opcional.

    Args:
        array (list): Lista de elementos a mostrar.
        msj_opcional (str): Texto que se antepone a cada línea (por ejemplo: "Opción ").

    Returns:
        str: Cadena con todos los elementos formateados.
    """
    msj = ""
    for i in range(len(array)):
        msj += f"{msj_opcional}{i + 1}- {array[i]}\n"
    return msj

def mostrar_mismo_puntaje(matriz_nombres,array_puntajes) -> str:
    """
    Muestra los participantes agrupados por promedio repetido.

    Args:
        array_puntajes(list): Lista de promedios repetidos.
        matriz_nombres(list): Lista de listas con nombres de los participantes que tienen ese promedio.

    Returns:
        str: Cadena con los promedios y los participantes que los comparten.
    """
    msj = ""
    for i in range(len(matriz_nombres)): 
        msj += f"PARTICIPANTES CON PROMEDIO: {array_puntajes[i]:.2f}\n"
        for nombre in range(len(matriz_nombres[i])):
            msj += f"- {matriz_nombres[i][nombre]}\n"
    return msj
    
def mostrar_puntajes(array_nombres:list,matriz_puntajes:list,array_promedios:list) -> str:
    """
    Muestra todos los participantes con sus puntajes por jurado y su promedio.

    Args:
        array_nombres (list): Lista de nombres de participantes.
        matriz_puntajes (list): Matriz con los puntajes por jurado.
        array_promedios (list): Lista de promedios por participante.

    Returns:
        str: Texto con la información completa de cada participante.
    """
    msj = ""
    for f in range(len(matriz_puntajes)):
        msj += f"\nPARTICIPANTE: {array_nombres[f]}"
        for c in range(len(matriz_puntajes[f])):
           msj += f" \n-Puntaje Jurado n°{c + 1}: {matriz_puntajes[f][c]}"

        msj += f"\nPROMEDIO : {array_promedios[f]:.2f}/10\n"
        
    return msj

def mostrar_puntaje_participante(array_nombres:list,matriz_puntaje:list,array_promedios:list) -> str:
    """
    Muestra los puntajes por jurado y el promedio de un solo participante.

    Args:
        nombre (str): Nombre del participante.
        puntajes (list): Lista de puntajes por jurado.
        promedio (float): Promedio del participante.

    Returns:
        str: Texto con la información del participante.
    """
    msj = f"\nPARTICIPANTE: {array_nombres}"

    for i in range(len(matriz_puntaje)):
        msj += f"\n-Puntaje Jurado n°{i + 1}: {matriz_puntaje[i]}"

    msj += f"\nPROMEDIO : {array_promedios:.2f}"
    return msj

def mostrar_promedio_participantes(array_nombres:list,array_promedios:list,promedio:int,menor:bool) -> str:
    """
    Muestra los participantes cuyo promedio es mayor o menor que un valor de referencia.

    Args:
        array_nombres (list): Lista de nombres de los participantes.
        array_promedios (list): Lista de promedios de los participantes.
        promedio (int): Valor de comparación.
        menor (bool): Si es True, muestra quienes tienen menos que el promedio dado; si es False, quienes tienen más.

    Returns:
        str: Texto con los participantes que cumplen la condición, o un mensaje de error si no hay ninguno.
    """
    contador = 0
    msj = ""
    for i in range(len(array_promedios)):
        if menor:
            if array_promedios[i] < promedio:
                contador += 1
                msj += f"{array_nombres[i]}, tuvo promedio de {array_promedios[i]:.2f}/10\n"
        else:
            if array_promedios[i] > promedio:
                contador += 1
                msj += f"{array_nombres[i]} tuvo promedio de {array_promedios[i]:.2f}/10\n"

    if contador == 0:
        msj += "ERROR! No hay nigun participante que cumpla con los requisitos."
    return msj

def mostrar_top_3(array_nombres:list,array_promedios:list) -> str:
    """
    Muestra el podio de los primeros 3 participantes con mayor puntaje promedio.

    Args:
        array_nombres (list): Lista de nombres ordenados por puntaje.
        array_promedios (list): Lista de promedios correspondientes.

    Returns:
        str: Texto con el TOP 3 de participantes.
    """
    contador = 0
    msj = ""
    for i in range(len(array_nombres)):
        msj += f"\n   *** TOP {i +1} ***\n"
        msj += f"PARTICIPANTE: {array_nombres[i]}"
        msj += f"\nPROMEDIO : {array_promedios[i]:.2f}\n"
        contador += 1
        if contador == 3:
            break
    return msj

def mostrar_participantes_con_promedios_iguales(valor_uno,valor_dos,msj_error:str) -> str:
    """
    Muestra los participantes con promedios repetidos, si existen. Si no, muestra un mensaje de error.

    Args:
        valor_uno (list): Lista de listas de participantes por promedio repetido.
        valor_dos (list): Lista de promedios repetidos.
        msj_error (str): Mensaje a mostrar si no hay coincidencias.

    Returns:
        str: Mensaje de error o lista formateada de resultados.
    """
    if comprobar_array_vacio(valor_uno,valor_dos):
        return msj_error
    else:
        msj = mostrar_mismo_puntaje(valor_uno,valor_dos)
        return msj
        

def mostrar_si_hay_empate(booleano:bool,array_nombres:list,matriz_puntajes:list,array_promedios:list) -> str:
    """
    Muestra el resultado final según haya empate o no.

    Args:
        booleano (bool): True si hay un único ganador, False si hay empate.
        array_nombres (list): Lista de nombres.
        matriz_puntajes (list): Matriz de puntajes por jurado.
        array_promedios (list): Lista de promedios.

    Returns:
        str: Mensaje con el ganador o con aviso de desempate.
    """
    if booleano:
        msj= "\nEl ganador de la competencia es:\n" 
        ganador = mostrar_puntaje_participante(array_nombres[0],matriz_puntajes[0],array_promedios[0])
        msj += ganador
        return msj
    else:
        msj = "\nNo hay ganador, hay que ir a DESEMPATE!"
        return msj
  
#FUNCIONES DE CARGA DE DATOS

def cargar_datos_matriz(matriz:list,msj:str)-> list: 
    """
    Carga manualmente datos numéricos en una matriz (lista de listas), solicitando al usuario 
    puntuaciones para cada jugador. Cada celda se valida para que contenga un número entero entre 1 y 10.

    Args:
        matriz (list): Matriz vacía o con estructura predefinida (lista de listas) que se llenará con los datos.
        msj (str): Mensaje base a mostrar al pedir la puntuación de cada celda 
                  (por ejemplo: "Ingrese puntuación del jurado").

    Side Effects:
        - Muestra mensajes en consola indicando qué puntaje se está cargando.
        - Solicita al usuario ingresar datos por consola.
        - Modifica directamente la matriz original (por referencia).

    Returns:
        list: La matriz con los datos cargados y validados.
    """
    for f in range(len(matriz)):
        print(f"\nCARGAR PUNTUACIONES DEL JUGADOR {f+1}: ")
        for c in range(len(matriz[f])):
            matriz[f][c]= pedir_cadena(f"{msj} {c+1}: ", validar_entero)

            while not validar_rango_inclusivo(1,10,int(matriz[f][c])):
                matriz[f][c]= pedir_cadena(f"Error, {msj} {c+1}: ", validar_entero)

            matriz[f][c] = int(matriz[f][c])
    return matriz
    
def cargar_array_str(array:list,msj:str,longitud_str:int) -> bool:
    """
    Solicita al usuario ingresar cadenas de texto para cada posición del array, 
    validando que cumplan con una longitud mínima y solo contengan caracteres alfabéticos.

    Args:
        array (list): Array preexistente que será rellenado con cadenas.
        msj (str): Mensaje base que se mostrará al solicitar cada dato.
        longitud_str (int): Longitud mínima requerida para aceptar una cadena como válida.

    Returns:
        bool: True si se cargó al menos un elemento en el array, False en caso contrario.
        bool: True si el array tiene al menos un elemento después de cargar; False en caso contrario.
    """
    for i in range(len(array)):
        dato = pedir_cadena_doble_validacion(f"{msj} {i + 1}: ",validar_cadena_alfa,validar_longitud,longitud_str)
        dato = convertir_mayuscula(dato)
        array[i] = dato

    if len(array) > 0:
        return True
    else:
        return False

#FUNCIONES DE CALCULOS

def sumar_fila_matriz(matriz:list) -> list[int]:
    """
    Suma los valores de cada fila en una matriz numérica.

    Args:
        matriz (list): Matriz de listas, donde cada sublista representa una fila de números.

    Returns:
        list[int]: Lista con la suma de cada fila.
    """
    array_sumar_filas = generar_array(len(matriz),0)

    for f in range(len(matriz)):
        for c in range(len(matriz[f])):
            array_sumar_filas[f]  += matriz[f][c]

    return array_sumar_filas

def sumar_columnas_matriz(matriz:list) -> list[int]:
    """
    Suma los valores de cada columna en una matriz numérica.

    Args:
        matriz (list): Matriz de listas, donde cada sublista representa una fila de números.

    Returns:
        list[int]: Lista con la suma de cada columna.
    """
    array_sumar_columnas = generar_array(len(matriz[0]),0)

    for f in range(len(matriz)):
        for c in range(len(matriz[f])):
            array_sumar_columnas[c]  += matriz[f][c]

    return array_sumar_columnas

def calcular_promedio(array_suma_fila:list,divisor:int) -> list[float]:
    """
    Calcula el promedio dividiendo cada valor de una lista por un divisor.

    Args:
        array_suma_fila (list): Lista con sumas (por ejemplo, suma de filas).
        divisor (int): Valor por el cual dividir cada suma.

    Returns:
        list[float]: Lista de promedios calculados.
    """
    array_promedio = generar_array(len(array_suma_fila),0)

    for i in range(len(array_suma_fila)):
        array_promedio[i] = array_suma_fila[i]/divisor
    
    return array_promedio

def calcular_tipo_de_jurado(promedio_jurados:list)-> tuple:
    """
    Determina cuál es el jurado con el mayor y menor promedio.

    Args:
        promedio_jurados (list): Lista de promedios por jurado.

    Returns:
        tuple[int, int, float, float]: 
            - Número del jurado con el menor promedio.
            - Número del jurado con el mayor promedio.
            - Valor mínimo del promedio.
            - Valor máximo del promedio.
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

def calcular_ganador(array_promedios:list) -> bool:
    """
    Determina si hay un único ganador basado en los promedios.

    Compara los dos primeros promedios de la lista (suponiendo que está ordenada de mayor a menor)
    y devuelve False si están empatados.

    Args:
        array_promedios (list): Lista de promedios ordenada de mayor a menor.

    Returns:
        bool: True si hay un único ganador, False si hay empate entre los primeros dos.
    """
    if len(array_promedios) > 1 and array_promedios[0] == array_promedios[1]:
        return False
    else:
        return True


def calcular_ganador_desempate(array_promedios) -> int:
    """
    En caso de empate en el primer puesto, elige aleatoriamente a uno de los empatados como ganador.

    Busca cuántos participantes tienen el mismo promedio que el primero, y selecciona uno al azar.

    Args:
        array_promedios (list): Lista de promedios ordenada de mayor a menor.

    Returns:
        int: Índice del ganador elegido al azar entre los empatados.
    """
    contador = 0

    for i in range( 1,len(array_promedios)):
        if array_promedios[0] == array_promedios[i]:
            contador+=1
    
    ganador_random = random.randint(0,contador-1)

    return ganador_random

#FUNCIONES DE BUSQUEDA

def buscar_en_lista(lista:list,valor:any) -> bool:
    """
    Verifica si un valor está presente dentro de una lista.

    Args:
        lista (list): Lista en la que se busca.
        valor (any): Valor a buscar.

    Returns:
        bool: True si el valor se encuentra en la lista, False si no.
    """
    estado = False
    for i in range(len(lista)):
        if valor == lista[i]:
            estado = True
        
    return estado

def buscar_indice(lista:list, valor:any)  -> int:
    """
    Busca un valor en una lista y devuelve el índice de su primera aparición.

    Args:
        lista (list): Lista donde se buscará el valor.
        valor (any): Valor a buscar en la lista.

    Returns:
        int: Índice del valor si se encuentra, -1 si no está presente.
    """

    for i in range(len(lista)):
        if valor == lista[i]:
            return i 
    return -1

def buscar_mismo_puntaje(array_promedios:list,array_nombres:list)-> tuple[list, list]: 
    """
    Busca participantes que comparten el mismo puntaje promedio.

    Agrupa a los participantes por promedio repetido, y devuelve:
    - una lista de listas con los nombres de participantes que tienen el mismo promedio
    - una lista con los promedios repetidos

    Args:
        array_promedios (list): Lista de promedios de los participantes.
        array_nombres (list): Lista de nombres de los participantes.

    Returns:
        tuple[list, list]: 
            - Lista de grupos de nombres con el mismo puntaje promedio.
            - Lista de los promedios que están repetidos.
    """
    mismo_puntaje = []
    participantes_mismo_puntaje = []

    for i in range(len(array_promedios)-1):
        for j in range(i+1, len(array_promedios)):
            if array_promedios[i] == array_promedios[j]:
                valor = array_promedios[i]

                if not buscar_en_lista(mismo_puntaje,valor):
                    mismo_puntaje += [valor]
                    participantes_mismo_puntaje += [[ array_nombres[i],  array_nombres[j]]]
                else:
                    indice = buscar_indice(mismo_puntaje,valor)
                    if indice != -1:
                        if not buscar_en_lista(participantes_mismo_puntaje[indice], array_nombres[i]):
                            participantes_mismo_puntaje[indice] += [ array_nombres[i]]
        
                        if not buscar_en_lista(participantes_mismo_puntaje[indice], array_nombres[j]):
                            participantes_mismo_puntaje[indice]  += [ array_nombres[j]]
    
    return participantes_mismo_puntaje,mismo_puntaje

def buscar_por_nombre(array_nombres:list,nombre:str) -> int | Literal[False]:
    """Busca un nombre en el array y devuelve su índice.

    Args:
        array (list): Lista de nombres.
        nombre (str): Nombre a buscar.

    Returns:
        int | bool: Índice si se encuentra, False si no.
    """
    for i in range(len(array_nombres)):
        if array_nombres[i] == nombre:
            return i
    return False

def bucador_de_participantes(array_nombres:list,matriz_puntajes:list,array_promedios:list) -> str:
    """
    Pide un nombre de participante al usuario, lo busca en la lista y, si existe, 
    muestra su puntaje y promedio. Si no se encuentra, muestra un mensaje de error.

    Args:
        array_nombres (list): Lista de nombres de participantes.
        matriz_puntajes (list): Lista de listas con puntajes por participante.
        array_promedios (list): Lista de promedios por participante.

    Returns:
        str: Mensaje con los datos del participante o mensaje de error si no se encuentra.
    """
    input = pedir_cadena("Ingrese el nombre del participante: ", validar_cadena_alfa)
    input = convertir_mayuscula(input)

    indice_participante = buscar_por_nombre(array_nombres,input)

    if verificar_tipo_retorno(indice_participante,bool):
        msj = "UPS.. No hay ningun jugador con ese nombre"
    else:
        puntaje = matriz_puntajes[indice_participante]
        nombre = array_nombres[indice_participante]
        promedio = array_promedios[indice_participante]
        msj = f"\n{mostrar_puntaje_participante(nombre,puntaje,promedio)}"
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

def ordenar_alfabeticamente(array_nombres:list,matriz_puntajes:list,array_promedios:list)-> tuple[list, list, list]:
    """
    Ordena alfabéticamente la lista de nombres y reorganiza las listas de puntajes y promedios 
    para mantener la correspondencia entre los datos de cada participante.

    Parámetros:
        array_nombres (list): Lista de nombres a ordenar alfabéticamente.
        matriz_puntajes (list): Lista de listas con los puntajes asociados a cada nombre.
        array_promedios (list): Lista con los promedios correspondientes a cada nombre.

    Retorna:
        tuple[list, list, list]: Las tres listas reordenadas (nombres, puntajes y promedios) 
        según el orden alfabético de los nombres, manteniendo la correspondencia entre datos.
    """
    for izq in range(len(array_nombres)-1):
        for der in range(izq + 1,len(array_nombres)):
            if array_nombres[izq] > array_nombres[der]:
                intercambiar_inidces(array_nombres,izq,der)
                intercambiar_inidces(matriz_puntajes,izq,der)
                intercambiar_inidces(array_promedios,izq,der)

    return array_nombres,matriz_puntajes,array_promedios

def ordenar_promedio_mayor(array_nombres:list,matriz_puntajes:list,array_promedios:list)-> tuple[list, list, list]:
    """
    Ordena las listas de nombres, puntajes y promedios en función del promedio de mayor a menor,
    manteniendo la correspondencia entre los datos de cada participante.

    Parámetros:
        array_nombres (list): Lista de nombres de los participantes.
        matriz_puntajes (list): Lista de listas con los puntajes de cada participante.
        array_promedios (list): Lista con los promedios correspondientes.

    Retorna:
        tuple[list, list, list]: Las tres listas reordenadas (nombres, puntajes y promedios) 
        en orden descendente según los valores de los promedios.
    """
    for izq in range(len(array_promedios)-1):
        for der in range(izq + 1,len(array_promedios)):
            if array_promedios[izq] < array_promedios[der]:
                intercambiar_inidces(array_promedios,izq,der)
                intercambiar_inidces(array_nombres,izq,der)
                intercambiar_inidces(matriz_puntajes,izq,der)

    return array_nombres,matriz_puntajes,array_promedios

