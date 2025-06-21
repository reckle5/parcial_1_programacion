
def validar_entero(cadena:str) -> bool:
    """
    Comprueba si una cadena representa un número entero positivo.

    Args:
        cadena (str): la cadena de texto que se desea verificar.

    Returns:
        bool: True si la cadena no está vacía y todos sus caracteres son dígitos (0–9); False en caso contrario.
    """
    if len(cadena) > 0:
        retorno = True
        for i in range(len(cadena)):
            valor_ascii = ord(cadena[i])
            if valor_ascii > 57 or valor_ascii < 48:
                retorno = False
                break
    else:
        retorno = False 
    
    return retorno

def validar_cadena_alfa(cadena:str)->bool:
    """
    Comprueba si una cadena contiene solo letras y espacios.

    Args:
        cadena (str): la cadena de texto que se desea verificar.

    Returns:
        bool: True si la cadena no está vacía y todos sus caracteres son letras (A–Z, a–z) o espacios; False en caso contrario.
    """
    if len(cadena) > 0:
        retorno = True
        for i in range(len(cadena)):
            valor_ascii = ord(cadena[i])
            if (valor_ascii > 122 or valor_ascii < 97) and (valor_ascii > 90 or valor_ascii < 65) and (valor_ascii != 32):
                retorno = False
                break
    else:
        retorno = False 
    
    return retorno

def convertir_mayuscula(cadena:str) -> str:
    """
    Convierte todas las letras minúsculas de una cadena a mayúsculas.

    Args:
        cadena (str): la cadena de texto que se desea transformar.

    Returns:
        str: nueva cadena donde cada letra minúscula (a–z) se ha convertido a mayúscula (A–Z); otros caracteres no se modifican.
    """
    cadena_aux = ""
    
    for i in range(len(cadena)):
        valor_ascii = ord(cadena[i])
        if valor_ascii >= 97 and valor_ascii <= 122:
            mayuscula = chr(valor_ascii - 32)
            cadena_aux += mayuscula
        else:
            cadena_aux += cadena[i]
        
    return cadena_aux   

def pedir_cadena(cadena:str,validacion:callable)->str:
    """
    Solicita al usuario una cadena por consola y la valida usando una función.

    Args:
        cadena (str): Mensaje a mostrar para pedir la entrada.
        validacion (callable): Función que toma la entrada y retorna True si es válida.

    Returns:
        str: Cadena ingresada que cumple con la validación.
    """    
    cadena = input(cadena)
    while True:
        if validacion(cadena):
            return cadena
        else:
            cadena = input("ingreso algún caracter invalido,intente otra vez: ")

def pedir_cadena_doble_validacion(cadena:str,validacion_uno:callable,validacion_dos:callable,parametro_dos:int) -> str:
    """
    Solicita al usuario una cadena por consola y la valida con dos funciones.

    Args:
        cadena (str): Mensaje a mostrar para solicitar la entrada.
        validacion_uno (callable): Primera función de validación (solo recibe la cadena).
        validacion_dos (callable): Segunda función de validación (recibe la cadena y un parámetro).
        parametro_dos (int): Parámetro adicional para la segunda validación.

    Returns:
        str: Cadena ingresada que cumple ambas validaciones.
    """ 
    cadena = input(cadena)
    
    while True:
        if validacion_uno(cadena) and validacion_dos(cadena,parametro_dos):
            return cadena
        else:
            cadena = input("ingreso algún caracter invalido,intente otra vez: ")
      
def validar_longitud(dato:str,longitud:int) -> bool:
    """
    Verifica si la longitud de una cadena es mayor que un valor dado.

    Args:
        dato (str): Cadena a evaluar.
        longitud (int): Longitud mínima requerida.

    Returns:
        bool: True si la longitud de la cadena es mayor al valor dado, False en caso contrario.
    """
    if len(dato) > longitud :
        return True
    else:
        return False
    
def validar_rango_inclusivo(rango_uno:int, rango_dos:int, dato:int) -> bool:
    """
    Verifica si un valor entero está dentro de un rango inclusivo.

    Args:
        rango_uno (int): límite inferior (incluido).
        rango_dos (int): límite superior (incluido).
        dato (int): valor a validar.

    Returns:
        bool: True si el dato se encuentra entre los rangos indicados; False en caso contrario.
    """
    if rango_uno <= dato <= rango_dos:
        return True
    else:
        return False

def validar_rango_no_inclusivo(rango_uno:int, rango_dos:int, dato:int) -> bool:
    """
    Verifica si un valor entero está dentro de un rango exclusivo.

    Args:
        rango_uno (int): límite inferior (excluido).
        rango_dos (int): límite superior (excluido).
        dato (int): valor a validar.

    Returns:
        bool: True si el dato se encuentra entre los rangos indicados; False en caso contrario.
    """
    if rango_uno < dato < rango_dos:
        return True
    else:
        return False
    
def verificar_tipo_retorno(variable:any,tipo) -> bool:
    """
    Verifica si el tipo de una variable coincide con el tipo esperado.

    Args:
        variable (any): variable a comprobar.
        tipo: tipo contra el cual se compara (por ejemplo, int, str, list, etc.).

    Returns:
        bool: True si la variable es del tipo indicado, False en caso contrario.
    """
    if type(variable) is tipo:
        return True
    else:
        return False
    
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