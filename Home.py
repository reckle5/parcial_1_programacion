from Funciones import *
import os

bandera_nombres = True
bandera_puntajes = True

participantes = generar_array(2,0)
puntaje = inicializar_matriz(2,3,0)

while True:
    os.system("cls")
    match menu_principal():

        case "1":

            if not bandera_nombres:
                print("*** ERROR! LOS PARTICIPANTES YA FUERON INGRESADOS ***")
            else:
                print("\nCARGUE LOS NOMBRES DE LOS PARTICIPANTES:\n")
                cargar_array_str(participantes,"Ingrese el nombre del participante n°",2)
                print("\n PARTICIPANTES INGRESADOS:\n")
                mostrar_array(participantes)
                bandera_nombres = False

        case "2":

            if bandera_nombres:
                print("**** Debe ingresar los nombres de los participantes anters de ingresar las puntuaciones ****")
            elif not bandera_puntajes:
                print("*** ERROR! LOS PARTICIPANTES YA FUERON INGRESADOS ***")
            else:
                print("\nINGRESE LA PUNTUACION DE CADA JURADO:\n")
                cargar_datos_matriz(puntaje,"Puntaje del Jurado n°")

                bandera_puntajes = False
            
        case "3":
            if  bandera_nombres or  bandera_puntajes:
                print("**** Debe ingresar los nombres y puntajes para acceder a esta opcion  ****")
            else:
                suma_de_puntajes = sumar_fila_matriz(puntaje)
                promedio_participantes = calcular_promedio(suma_de_puntajes,3)
                mostrar_puntajes(puntaje,participantes,promedio_participantes)

        case "4":
            if bandera_nombres or  bandera_puntajes:
                print("**** Debe ingresar los nombres y puntajes para acceder a esta opcion  ****")
            else:
                print("\nLOS PARTICIPANTES CON PROMEDIO MENOR A 4 FUERON:")
                mostrar_promedio_participantes(promedio_participantes,participantes,4,True)

        case "5":
            if bandera_nombres or bandera_puntajes:
                print("**** Debe ingresar los nombres y puntajes para acceder a esta opcion  ****")
            else:
                print("\nLOS PARTICIPANTES CON PROMEDIO MENOR A 8 FUERON:")
                mostrar_promedio_participantes(promedio_participantes,participantes,8,True)

        case "6":
            if bandera_nombres or bandera_puntajes:
                print("**** Debe ingresar los nombres y puntajes para acceder a esta opcion  ****")
            else:
                print("\nLOS PROMEDIO DE LOS JURADOS FUERON:")
                suma_de_puntajes_jurados = sumar_columnas_matriz(puntaje)
                promedio_jurados = calcular_promedio(suma_de_puntajes_jurados,len(participantes))
                mostrar_array(promedio_jurados,f"Jurado n° ")

        case "7": 
            if bandera_nombres or bandera_puntajes:
                print("**** Debe ingresar los nombres y puntajes para acceder a esta opcion  ****")
            else: 
                jurado_estrico,jurado_generoso,promedio_min,promedio_max = calcular_tipo_de_jurado(promedio_jurados)
                print(f"\nel jurado mas estrico fue n°{jurado_estrico}, con un promedio de {promedio_min}")

        case "8":
            if bandera_nombres or bandera_puntajes:
                print("**** Debe ingresar los nombres y puntajes para acceder a esta opcion  ****")
            else:
                jurado_estrico,jurado_generoso,promedio_min,promedio_max = calcular_tipo_de_jurado(promedio_jurados)
                print(f"\nel jurado mas generoso fue n°{jurado_generoso}, con un promedio de {promedio_max}")

        case "9":
            if bandera_nombres or bandera_puntajes:
                print("**** Debe ingresar los nombres y puntajes para acceder a esta opcion  ****")
            else:
                print("\nPARTICIPANTES CON LA MISMA PUNTUACION FINAL:\n")
                grupo_participantes,mismo_puntaje = buscar_mismo_puntaje(promedio_participantes,participantes)
                msj = "** Error! no hay ningun participante con el mismo promedio final **"
                print(mostrar_segun_retorno(grupo_participantes,mismo_puntaje,msj))

        case "10":
            if bandera_nombres or bandera_puntajes:
                print("**** Debe ingresar los nombres y puntajes para acceder a esta opcion  ****")
            else:
                bucador_participantes(participantes,puntaje,promedio_participantes)
        case "11":
            if bandera_nombres or bandera_puntajes:
                print("**** Debe ingresar los nombres y puntajes para acceder a esta opcion  ****")
            else:
                print("\nPARTICIPANTES ORDENADOS ALFABETICAMENTE:\n")
                ordenar_alfabeticamente(participantes,puntaje,promedio_participantes)
                mostrar_puntajes(puntaje,participantes,promedio_participantes)
        case _:
            pass
    
    input("\npresione para continuar..")


