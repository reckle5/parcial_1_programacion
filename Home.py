from Funciones import *
import os

bandera_nombres = True
bandera_puntajes = True
bandera_ganador = True


array_participantes = generar_array(5,0)
matriz_puntajes = inicializar_matriz(5,3,0)

while True:
    os.system("cls")
    match menu_principal():


        case "1":
            if not bandera_nombres:
                print("\n *** ERROR! LOS PARTICIPANTES YA FUERON INGRESADOS ***")
            else:
                print("\nCARGUE LOS NOMBRES DE LOS PARTICIPANTES:\n")
                cargar_array_str(array_participantes,"Ingrese el nombre del participante n°",2)
                print("\n PARTICIPANTES INGRESADOS:\n")
                print(mostrar_array(array_participantes))
                bandera_nombres = False
        case "2":

            if bandera_nombres:
                print("\n **** Debe ingresar los nombres de los participantes anters de ingresar las puntuaciones ****")
            elif not bandera_puntajes:
                print("\n *** ERROR! LOS PARTICIPANTES YA FUERON INGRESADOS ***")
            else:
                print("\nINGRESE LA PUNTUACION DE CADA JURADO:\n")
                cargar_datos_matriz(matriz_puntajes,"Puntaje del Jurado n°")
                bandera_puntajes = False
        case "3":
            if  bandera_nombres or  bandera_puntajes:
                print("\n **** Debe ingresar los nombres y puntajes para acceder a esta opcion  ****")
            else:
                suma_de_puntajes = sumar_fila_matriz(matriz_puntajes)
                promedio_participantes = calcular_promedio(suma_de_puntajes,3)
                print(mostrar_puntajes(array_participantes,matriz_puntajes,promedio_participantes))
        case "4":
            if bandera_nombres or  bandera_puntajes:
                print("\n **** Debe ingresar los nombres y puntajes para acceder a esta opcion  ****")
            else:
                print("\nPARTICIPANTES CON PROMEDIO MENOR A 4:")
                print(mostrar_promedio_participantes(array_participantes,promedio_participantes,4,True))
        case "5":
            if bandera_nombres or bandera_puntajes:
                print("\n **** Debe ingresar los nombres y puntajes para acceder a esta opcion  ****")
            else:
                print("\nPARTICIPANTES CON PROMEDIO MENOR A 8:")
                print(mostrar_promedio_participantes(array_participantes,promedio_participantes,8,True))
        case "6":
            if bandera_nombres or bandera_puntajes:
                print("\n **** Debe ingresar los nombres y puntajes para acceder a esta opcion  ****")
            else:
                print("\nLOS PROMEDIO DE LOS JURADOS FUERON:")
                suma_de_puntajes_jurados = sumar_columnas_matriz(matriz_puntajes)
                promedio_jurados = calcular_promedio(suma_de_puntajes_jurados,len(array_participantes))
                print(mostrar_array(promedio_jurados,f"Jurado n° "))
        case "7": 
            if bandera_nombres or bandera_puntajes:
                print("\n **** Debe ingresar los nombres y puntajes para acceder a esta opcion  ****")
            else: 
                jurado_estrico,jurado_generoso,promedio_min,promedio_max = calcular_tipo_de_jurado(promedio_jurados)
                print(f"\nel jurado mas estrico fue n°{jurado_estrico}, con un promedio de {promedio_min}")
        case "8":
            if bandera_nombres or bandera_puntajes:
                print("\n **** Debe ingresar los nombres y puntajes para acceder a esta opcion  ****")
            else:
                jurado_estrico,jurado_generoso,promedio_min,promedio_max = calcular_tipo_de_jurado(promedio_jurados)
                print(f"\nel jurado mas generoso fue n°{jurado_generoso}, con un promedio de {promedio_max}")
        case "9":
            if bandera_nombres or bandera_puntajes:
                print("\n **** Debe ingresar los nombres y puntajes para acceder a esta opcion  ****")
            else:
                print("\nPARTICIPANTES CON LA MISMA PUNTUACION FINAL:\n")
                grupo_participantes,mismo_puntaje = buscar_mismo_puntaje(promedio_participantes,array_participantes)
                msj = "\n ** Error! no hay ningun participante con el mismo promedio final **"
                print(mostrar_participantes_con_promedios_iguales(grupo_participantes,mismo_puntaje,msj))
        case "10":
            if bandera_nombres or bandera_puntajes:
                print("\n **** Debe ingresar los nombres y puntajes para acceder a esta opcion  ****")
            else:
                print(bucador_de_participantes(array_participantes,matriz_puntajes,promedio_participantes))
        case "11":
            if bandera_nombres or bandera_puntajes:
                print("\n **** Debe ingresar los nombres y puntajes para acceder a esta opcion  ****")
            else:
                ordenar_promedio_mayor(array_participantes,matriz_puntajes,promedio_participantes)
                print(mostrar_top_3(array_participantes,promedio_participantes))
        case "12":
            if bandera_nombres or bandera_puntajes:
                print("\n **** Debe ingresar los nombres y puntajes para acceder a esta opcion  ****")
            else:
                print("\nPARTICIPANTES ORDENADOS ALFABETICAMENTE:\n")
                ordenar_alfabeticamente(array_participantes,matriz_puntajes,promedio_participantes)
                print(mostrar_puntajes(array_participantes,matriz_puntajes,promedio_participantes))
        case "13":
            if bandera_nombres or bandera_puntajes:
                print("\n **** Debe ingresar los nombres y puntajes para acceder a esta opcion  ****")
            else:
                ordenar_promedio_mayor(array_participantes,matriz_puntajes,promedio_participantes)
                hay_ganador = (calcular_ganador(promedio_participantes))
                print(mostrar_si_hay_empate(hay_ganador,array_participantes,matriz_puntajes,promedio_participantes))
                bandera_ganador = False
        case "14":
            if bandera_nombres or bandera_puntajes:
                print("\n **** Debe ingresar los nombres y puntajes para acceder a esta opcion  ****")
            elif bandera_ganador:
                print("\n **** Para desempatar debe primero acceder a la opcion 13, de ser necesario se desempatara. ****")
            elif hay_ganador:
                print("\n **** El desempate no es una opciona, el ganador ya fue elegido  **** ")
            else: 
                ganador = calcular_ganador_desempate(promedio_participantes)
                print("\n ¡DESEMPATE! El ganador será elegido al azar entre los puntajes mas altos\n El ganador es:\n")
                print(mostrar_puntaje_participante(array_participantes[ganador],matriz_puntajes[ganador],promedio_participantes[ganador]))
        case _:
            pass
    
    input("\npresione para continuar..")


