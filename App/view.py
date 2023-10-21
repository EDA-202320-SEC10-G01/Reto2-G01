"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad
 * de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 """

import config as cf
import sys
import controller
from DISClib.ADT import list as lt
from DISClib.ADT import stack as st
from DISClib.ADT import queue as qu
from DISClib.ADT import map as mp
from DISClib.DataStructures import mapentry as me
assert cf
from tabulate import tabulate
import traceback

"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""


def new_controller():
    """
        Se crea una instancia del controlador
    """
    
    return controller.new_controller()

def print_menu():
    print("Bienvenido")
    print("1- Cargar información")
    print("2- Listar los ultimos N partidos de unequipo segun su condicion")
    print("3- Listar los primeros N goles anotados por un jugador")
    print("4- Consultar los partidos que disputo un equipo durante un periodo especifico")
    print("5- Consultar los partidos relacionados con un torneo durante un periodo especifico")
    print("6- Consultar las anotaciones de un jugador durante un periodo especifico")
    print("7- EClasificar los N mejores equipos del año dentro de un torno especifico")
    print("8- Clasificar los N mejores anotadores en partidos oficiales dentro de un periodo especifico")
    print("9- Consultar el desempeño historico de una seleccion en torneos oficiales")
    print("0- Salir")

def load_and_sort_data(control):
    """
    Carga los datos
    """
    
    #Interactua con el usuario para pedir el tamaño de los datos y el algoritmo de ordenamiento
    
    tamaño = input("""Ingrese el numero asociado al tamaño de la muestra: \n
    1. Small \n
    2. 5% \n
    3. 10 % \n
    4. 20 % \n
    5. 30 % \n
    6. 50 % \n
    7. 80 % \n
    8. Large \n""")
    
    algoritmo = input("""Ingrese el numero asociado al algoritmo de ordenamiento que desea utilizar: \n
    1. Selection Sort \n
    2. Insertion Sort \n
    3. Shell Sort \n
    4. Merge Sort \n
    5. Quick Sort \n""")
    
    
    tiempo_carga, tiempo_ordenamiento, memoria = controller.load_and_sort_data(control, tamaño, algoritmo)
    
    print("=============== Carga de Datos ==================")
    print(f"\nTiempo de carga: {tiempo_carga} ms")
    print(f"\nTiempo de ordenamiento: {tiempo_ordenamiento} ms")
    print(f"\nMemoria utilizada: {memoria} kB")
    
#Funciones para mostrar los datos    
      
def print_table(data, headers):
    
    """
    Imprime los datos en forma de tabla
    """
    
    #Se verifica que haya datos para mostrar
    
    if lt.size(data) == 0:
        print("No se encontraron datos para mostrar")
        
    #Se crea una sublista de máximo 6 elementos para mostrar

    elif lt.size(data) > 6:
        first_three = lt.subList(data, 1, 3) 
        last_three = lt.subList(data, lt.size(data)-2, 3)
        combined_list = lt.newList("ARRAY_LIST")
        
        for i in lt.iterator(first_three):
            lt.addLast(combined_list, i)
        
        for i in lt.iterator(last_three):
            lt.addLast(combined_list, i)
     
    #Se imprimen los datos en forma de tabla 
        
        print(f"\nDe {lt.size(data)} elementos, se muestran los primeros y ultimos 3\n")
        print(tabulate(lt.iterator(combined_list), headers, tablefmt="fancy_grid"))
        
    else:
        print(f"\nSe encontraron {lt.size(data)} elementos mostrados a continuacion\n")
        print(tabulate(lt.iterator(data), headers, tablefmt="fancy_grid"))
              
def print_data(control):
    
    """
    Funcion para mostrar los datos cargados al usuario (results, shootouts, goalscorers)
    """
    
    #Se establecen los encabezados de las tablas de los tres archivos a cargar
    
    headers_results = {"date": "Fecha",
                    "home_team": "Equipo local",
                    "away_team": "Equipo visitante",
                    "home_score": "Marcador local",
                    "away_score": "Marcador visitante",
                    "tournament": "Torneo",
                    "city": "Ciudad",
                    "country": "País",
                    "neutral": "Neutral"}
    
    headers_goalscorer = {"date": "Fecha",
                    "home_team": "Equipo local",
                    "away_team": "Equipo visitante",
                    "team": "Equipo",
                    "scorer": "Anotador",
                    "minute": "Minuto",
                    "own_goal": "Autogol",
                    "penalty": "Penal"}
    
    headers_shootouts = {"date": "Fecha",
                    "home_team": "Equipo local",
                    "away_team": "Equipo visitante",
                    "winner": "Ganador"}
    
    #Se muestran los datos al usuario
    
    print_table(control["results"], headers_results)
    print_table(control["goalscorers"], headers_goalscorer)
    print_table(control["shootouts"], headers_shootouts)
    
#Funciones para mostrar los requerimientos

def print_req_1(control):
    
    """
    Se ejecuta el requerimiento 1 para posteriormente mostrar los resultados al usuario
    """
    
    #Se piden los datos al usuario
    
    equipo = input("Ingrese el nombre del equipo que desea consultar\n")
    n_partidos = input("Ingrese el numero de partidos que desea consultar\n")
    condicion = input("Ingrese la condicion que desea consultar\n1. Local\n2. Visitante\n3. Indiferente\n")

    #Se establecen los encabezados de la tabla
    
    headers = {"date": "Fecha",
                   "home_team": "Equipo local",
                   "away_team": "Equipo visitante",
                   "home_score": "Marcador local",
                   "away_score": "Marcador visitante",
                   "tournament": "Torneo",
                   "city": "Ciudad",
                   "country": "País",
                   "neutral": "Neutral"}
    
    #Se llama la funcion del controlador

    controller_response = controller.req_1(control, n_partidos, equipo, condicion)
    
    n_equipos, n_partidos_equipo, n_partidos_condicion, partidos = controller_response[0]
    
    #Se muestra la funcion al usuario
    
    condiciones = {"1": "Local", "2": "Visitante", "3": "Indiferente"}
    
    print("\n=============== Datos del usuario ==================")
    print(f"\nEquipo: {equipo}")
    print(f"\nNumero de partidos recientes: {n_partidos}")
    print(f"\nCondicion: {condiciones[condicion]}")
    
    print("\n=============== Resultados ==================")
    print(f"\nTiempo de ejecución del algoritmo: {controller_response[1]} ms")
    print(f"\nUso de memoria del algoritmo: {controller_response[2]} KB")
    print(f"\nSe encontraron {n_equipos} equipos con informacion disponible")
    print(f"\nSe encontraron {n_partidos_equipo} partidos del equipo {equipo}")
    print(f"\nSe encontraron {n_partidos_condicion} partidos del equipo {equipo} en condicion de {condiciones[condicion]}")
    
    print_table(partidos, headers)

def print_req_2(control):
    """
    Imprime los resultados del requerimiento 2 en la consola.
    """
    
    #Se piden los datos al usuario
    jugador = input("Ingrese el nombre del jugador que desea consultar\n")
    n_goles = input("Ingrese el numero de goles mas recientes que desea consultar\n")
    
    #Define los encabezados para la tabla que se imprimirá
    
    headers =  {"date": "Fecha",
                "home_team": "Equipo local",
                "away_team": "Equipo visitante",
                "team": "Equipo",
                "scorer": "Anotador",
                "minute": "Minuto",
                "own_goal": "Autogol",
                "penalty": "Penal"}
    
    #Consulta los datos y recupera los resultados
    
    controller_response = controller.req_2(control, n_goles, jugador)
    
    n_jugadores, n_goles_jugador, n_goles_jugador_penal, goles = controller_response[0]
    
    #Imprime la entrada del usuario y los resultados de la consulta}
    print("\n=============== Datos del usuario ==================")
    print(f"\nJugador: {jugador}")
    print(f"\nNumero de goles recientes: {n_goles}")
    
    print("\n=============== Resultados ==================")
    print(f"\nTiempo de ejecución del algoritmo: {controller_response[1]} ms")
    print(f"\nUso de memoria del algoritmo: {controller_response[2]} KB")
    print(f"\nSe encontraron {n_jugadores} jugadores")
    print(f"\nSe encontraron {n_goles_jugador} goles del jugador {jugador}")
    print(f"\nSe encontraron {n_goles_jugador_penal} goles de penal del jugador {jugador}")
    
    #Imprime la tabla de resultados de la consulta
    print_table(goles, headers)
    
def print_req_3(control):
    
    # Solicita al usuario el equipo y el rango de fechas a consultar
    equipo = input("Ingrese el nombre del equipo que desea consultar\n")
    año_inicial = input("Ingrese el año inicial que desea consultar\n")
    mes_inicial = input("Ingrese el mes inicial que desea consultar\n")
    dia_inicial = input("Ingrese el dia inicial que desea consultar\n")
    año_final = input("Ingrese el año final que desea consultar\n")
    mes_final = input("Ingrese el mes final que desea consultar\n")
    dia_final = input("Ingrese el dia final que desea consultar\n")
    
    # Formatea el rango de fechas como cadenas de texto
    
    fecha_inicial = f"{año_inicial}-{mes_inicial}-{dia_inicial}"
    fecha_final = f"{año_final}-{mes_final}-{dia_final}"
    
    # Define los encabezados para la tabla que se imprimirá
    
    headers = {"date": "Fecha",
                "home_team": "Equipo local",
                "away_team": "Equipo visitante",
                "home_score": "Marcador local",
                "away_score": "Marcador visitante",
                "tournament": "Torneo",
                "city": "Ciudad",
                "country": "País",
                "neutral": "Neutral",
                "penalties": "Penales",
                "autogoles": "Autogoles"}
    
    # Consulta los datos y recupera los resultados
    
    controller_response = controller.req_3(control, equipo, fecha_inicial, fecha_final)
    
    n_equipos, n_partidos_equipo_local, n_partidos_equipo_visitante, partidos_equipo = controller_response[0]
    
    # Imprime la entrada del usuario y los resultados de la consulta
    
    print("\n=============== Datos del usuario ==================")
    print(f"\nEquipo: {equipo}")
    print(f"\nFecha inicial: {año_inicial}-{mes_inicial}-{dia_inicial}")
    print(f"\nFecha final: {año_final}-{mes_final}-{dia_final}")
    
    print("\n=============== Resultados ==================")
    print(f"\nTiempo de ejecución del algoritmo: {controller_response[1]} ms")
    print(f"\nUso de memoria del algoritmo: {controller_response[2]} KB")
    print(f"\nSe encontraron {n_equipos} equipos")
    print(f"\nSe encontraron {n_partidos_equipo_local} partidos del equipo {equipo} como local")
    print(f"\nSe encontraron {n_partidos_equipo_visitante} partidos del equipo {equipo} como visitante")
    
    # Imprime la tabla de resultados de la consulta
    print_table(partidos_equipo, headers)
                  
def print_req_4(control):
    """
    Imprime los resultados del requerimiento 4 en la consola.

    Args:
    control: objeto Control que maneja los datos.

    Returns:
    None
    """
    # Solicita al usuario el torneo y el rango de fechas a consultar
    torneo = input("Ingrese el nombre del torneo que desea consultar\n")
    año_inicial = input("Ingrese el año inicial que desea consultar\n")
    mes_inicial = input("Ingrese el mes inicial que desea consultar\n")
    dia_inicial = input("Ingrese el dia inicial que desea consultar\n")
    año_final = input("Ingrese el año final que desea consultar\n")
    mes_final = input("Ingrese el mes final que desea consultar\n")
    dia_final = input("Ingrese el dia final que desea consultar\n")
    
    # Formatea el rango de fechas como cadenas de texto
    fecha_inicial = f"{año_inicial}-{mes_inicial}-{dia_inicial}"
    fecha_final = f"{año_final}-{mes_final}-{dia_final}"
    
    # Define los encabezados para la tabla que se imprimirá
    headers = {"date": "Fecha",
               "country": "País",
                "city": "Ciudad",
                "home_team": "Equipo local",
                "away_team": "Equipo visitante",
                "home_score": "Marcador local",
                "away_score": "Marcador visitante",
                "penalties": "Penales",
                "ganador_penales": "Ganador penales"}
    
    # Consulta los datos y recupera los resultados
    
    controller_response = controller.req_4(control, torneo, fecha_inicial, fecha_final)
    
    n_torneos, n_paises, n_ciudades, n_partidos_torneo, n_partidos_penales, partidos_torneo = controller_response[0]
    
    # Imprime la entrada del usuario y los resultados de la consulta
    print("\n=============== Datos del usuario ==================")
    print(f"\nTorneo: {torneo}")
    print(f"\nFecha inicial: {año_inicial}-{mes_inicial}-{dia_inicial}")
    print(f"\nFecha final: {año_final}-{mes_final}-{dia_final}")
    
    print("\n=============== Resultados ==================")
    print(f"\nTiempo de ejecución del algoritmo: {controller_response[1]} ms")
    print(f"\nUso de memoria del algoritmo: {controller_response[2]} KB")
    print(f"\nSe encontraron {n_torneos} torneos")
    print(f"\nSe encontraron {n_paises} paises en el torneo {torneo}")
    print(f"\nSe encontraron {n_ciudades} ciudades en el torneo {torneo}")
    print(f"\nSe encontraron {n_partidos_torneo} partidos en el torneo {torneo}")
    print(f"\nSe encontraron {n_partidos_penales} partidos definidos por penales en el torneo {torneo}")
    
    # Imprime la tabla de resultados de la consulta
    print_table(partidos_torneo, headers)

def print_req_5(control):
    """
    Función que solicita al usuario información para realizar la consulta de la petición 5 y muestra los resultados obtenidos.
    
    Parámetros:
    control (Controlador): objeto de la clase Controlador encargado de manejar las peticiones del usuario.
    """
    
    # Se solicita al usuario la información necesaria para realizar la consulta
    anotador = input("Ingrese el nombre del anotador que desea consultar\n")
    año_inicial = input("Ingrese el año inicial que desea consultar\n")
    mes_inicial = input("Ingrese el mes inicial que desea consultar\n")
    dia_inicial = input("Ingrese el dia inicial que desea consultar\n")
    año_final = input("Ingrese el año final que desea consultar\n")
    mes_final = input("Ingrese el mes final que desea consultar\n")
    dia_final = input("Ingrese el dia final que desea consultar\n")
    
    # Se construyen las fechas en formato yyyy-mm-dd
    fecha_inicial = f"{año_inicial}-{mes_inicial}-{dia_inicial}"
    fecha_final = f"{año_final}-{mes_final}-{dia_final}"
    
    # Se definen los encabezados de la tabla de resultados
    headers = {"scorer": "antoador",
               "date": "Fecha",
               "minute": "Minuto",
               "home_team": "Equipo local",
               "away_team": "Equipo visitante",
               "team": "Equipo del jugador",
               "home_score": "Marcador local",
                "away_score": "Marcador visitante",
                "tournament": "Torneo",
                "penalty": "Penal",
                "own_goal": "Autogol"}
    
    # Se realiza la consulta y se obtienen los resultados
    
    controller_response = controller.req_5(control, anotador, fecha_inicial, fecha_final)
    
    n_jugadores, n_anotaciones, n_torneos, n_penales, n_autogoles, anotaciones = controller_response[0]
    
    # Se muestran los resultados obtenidos
    print("\n=============== Datos del usuario ==================")
    print(f"\nAnotador: {anotador}")
    print(f"\nFecha inicial: {año_inicial}-{mes_inicial}-{dia_inicial}")
    print(f"\nFecha final: {año_final}-{mes_final}-{dia_final}")
    
    print("\n=============== Resultados ==================")
    print(f"\nTiempo de ejecución del algoritmo: {controller_response[1]} ms")
    print(f"\nUso de memoria del algoritmo: {controller_response[2]} KB")
    print(f"\nSe encontraron {n_jugadores} jugadores")
    print(f"\nSe encontraron {n_anotaciones} anotaciones por parte de {anotador}")
    print(f"\nSe encontraron {n_torneos} torneos donde anoto {anotador}")
    print(f"\nSe encontraron {n_penales} penales")
    print(f"\nSe encontraron {n_autogoles} autogoles")
    
    # Se muestra la tabla de resultados
    print_table(anotaciones, headers)
        
def print_req_6(control):
    """
    Función que imprime los resultados de la consulta 6 en una tabla.
    La consulta 6 permite consultar los equipos con mejor rendimiento en un torneo y año específico.

    Args:
    control: objeto de la clase Controlador que permite acceder a los métodos de consulta.

    Returns:
    None
    """

    # Se solicita al usuario el número de equipos, el torneo y el año a consultar
    n_equipos = input("Ingrese el numero de equipos que desea consultar\n")
    torneo = input("Ingrese el nombre del torneo que desea consultar\n")
    año = input("Ingrese el año que desea consultar\n")
    
    # Se llama al método req_6 del controlador para obtener los equipos a mostrar y el número de equipos encontrados
    
    controller_response = controller.req_6(control, n_equipos, torneo, año)
    
    equipos_a_mostrar, equipos_encontrados = controller_response[0]
    
    # Se definen los encabezados de la tabla
    headers = {"equipo": "Equipo",
               "puntos_totales": "Puntos totales",
               "diferencia_goles": "Diferencia de goles",
               "partidos_jugados": "Partidos jugados",
               "goles_penal": "Goles de penal",
               "autogoles": "Autogoles",
               "victorias": "Victorias",
               "empates": "Empates",
               "derrotas": "Derrotas",
               "goles_favor": "Goles a favor",
               "goles_contra": "Goles en contra"}
    
    # Se imprimen los datos de la consulta
    print("\n=============== Datos del usuario ==================")
    print(f"\nTorneo: {torneo}")
    print(f"\nAño de consulta: {año}")
    print(f"\nFecha inicial: {año}-01-01")
    print(f"\nFecha final: {año}-12-31")
    print(f"\nEquipos a mostrar: Top {n_equipos}")
    
    # Se imprimen los resultados de la consulta
    print("\n=============== Resultados ==================")
    print(f"\nTiempo de ejecución del algoritmo: {controller_response[1]} ms")
    print(f"\nUso de memoria del algoritmo: {controller_response[2]} KB")
    print(f"Se encontraron {equipos_encontrados} equipos\n")
    print_table(equipos_a_mostrar, headers)

def print_req_7(control):
    """
    Imprime los resultados de la consulta de la requisito 7 en una tabla.
    La función solicita al usuario el nombre del torneo, el puntaje, la fecha inicial y la fecha final.
    Luego llama a la función req_7 del controlador para obtener los resultados y los imprime en una tabla.

    :param control: objeto de la clase Controlador
    :return: None
    """
    
    # Diccionario con los nombres de las columnas de la tabla
    headers = {"jugador": "Jugador",
               "puntos": "Puntos",
               "goles": "Goles",
               "goles_penal": "Goles de penal",
               "autogoles": "Autogoles",
               "minuto_promedio": "Minuto promedio",
               "goles_en_victorias": "Goles en victorias",
               "goles_en_empates": "Goles en empates",
                "goles_en_derrotas": "Goles en derrotas",
                "ultimo_partido": "Ultimo partido"}
    
    # Solicita al usuario los datos de la consulta
    torneo = input("Ingrese el nombre del torneo que desea consultar\n")
    puntaje = input("Ingrese el puntaje que desea consultar\n")
    año_inicial = input("Ingrese el año inicial que desea consultar\n")
    mes_inicial = input("Ingrese el mes inicial que desea consultar\n")
    dia_inicial = input("Ingrese el dia inicial que desea consultar\n")
    año_final = input("Ingrese el año final que desea consultar\n")
    mes_final = input("Ingrese el mes final que desea consultar\n")
    dia_final = input("Ingrese el dia final que desea consultar\n")
    
    # Formatea las fechas en un string
    fecha_inicial = f"{año_inicial}-{mes_inicial}-{dia_inicial}"
    fecha_final = f"{año_final}-{mes_final}-{dia_final}"
    
    # Llama a la función req_7 del controlador para obtener los resultados
    
    controller_response = controller.req_7(control, torneo, puntaje, fecha_inicial, fecha_final)
    
    n_torneos, n_anotadores, n_anotadores_puntaje, n_goles, n_partidos, n_autogoles, n_penalties, jugadores = controller_response[0]
    
    # Imprime los datos de la consulta
    print("\n=============== Datos del usuario ==================")
    print(f"\nTorneo: {torneo}")
    print(f"\nJugadores con {puntaje} de puntaje")
    print(f"\nFecha inicial: {año_inicial}-{mes_inicial}-{dia_inicial}")
    print(f"\nFecha final: {año_final}-{mes_final}-{dia_final}")
    
    # Imprime los resultados de la consulta
    print("\n=============== Resultados ==================")
    print(f"\nTiempo de ejecución del algoritmo: {controller_response[1]} ms")
    print(f"\nUso de memoria del algoritmo: {controller_response[2]} KB")
    print(f"\nSe encontraron {n_torneos} torneos")
    print(f"\nSe encontraron {n_anotadores} anotadores en el torneo {torneo}")
    print(f"\nSe encontraron {n_partidos} partidos en el torneo {torneo}")
    print(f"\nSe encontraron {n_goles} goles en el torneo {torneo}")
    print(f"\nSe encontraron {n_autogoles} autogoles en el torneo {torneo}")
    print(f"\nSe encontraron {n_penalties} penales en el torneo {torneo}")
    print(f"\nSe encontraron {n_anotadores_puntaje} anotadores con {puntaje} de puntaje")
    
    # Imprime la tabla con los resultados
    print_table(jugadores, headers)
    

# Se crea el controlador asociado a la vista
control = new_controller()

# main del reto
if __name__ == "__main__":
    """
    Menu principal
    """
    working = True
    #ciclo del menu
    while working:
        print_menu()
        inputs = input('Seleccione una opción para continuar\n')
        if int(inputs) == 1:
            print("Cargando información de los archivos ....\n")
            data = load_and_sort_data(control)
            data_size = controller.get_datasize(control)
            print_data(control)
            print(f'Se cargaron {data_size[0]} resultados, {data_size[1]} penales y {data_size[2]} goleadores\n')
        elif int(inputs) == 2:
            print_req_1(control)    

        elif int(inputs) == 3:
            print_req_2(control)

        elif int(inputs) == 4:
            print_req_3(control)

        elif int(inputs) == 5:
            print_req_4(control)

        elif int(inputs) == 6:
            print_req_5(control)

        elif int(inputs) == 7:
            print_req_6(control)

        elif int(inputs) == 8:
            print_req_7(control)

        elif int(inputs) == 9:
            print_req_8(control)

        elif int(inputs) == 0:
            working = False
            print("\nGracias por utilizar el programa")
        else:
            print("Opción errónea, vuelva a elegir.\n")
    sys.exit(0)
