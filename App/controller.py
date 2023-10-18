"""
 * Copyright 2020, Departamento de sistemas y Computación,
 * Universidad de Los Andes
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
import model
import time
import csv
import tracemalloc

"""
El controlador se encarga de mediar entre la vista y el modelo.
"""


def new_controller():
    """
    Crea una instancia del modelo
    """
    return model.new_data_structs()


#Funciones para la carga de datos

def load_and_sort_data(control, tamaño, algoritmo):
    """
    Carga los datos del reto
    """
    
    
    tamaños = {"1": "small",
               "2": "5pct",
               "3": "10pct",
               "4": "20pct",
               "5": "30pct",
               "6": "50pct",
               "7": "80pct",
               "8": "large"}
    
    tracemalloc.start()
    tiempo_carga = get_time()
    memoria_inicial = get_memory()
    
    if tamaño in list(tamaños.keys()):
        tamaño = tamaños[tamaño]
        
        control["results"] = model.lt.newList("ARRAY_LIST")
        control["shootouts"] = model.lt.newList("ARRAY_LIST")
        control["goalscorers"] = model.lt.newList("ARRAY_LIST")
        
        load_data(control, tamaño, "results")
        load_data(control, tamaño, "shootouts")
        load_data(control, tamaño, "goalscorers")
        model.creating_hash(control) 
     
        
    tiempo_carga = delta_time(tiempo_carga, get_time())
    memoria = delta_memory(get_memory(), memoria_inicial)
    tracemalloc.stop()
    
    tiempo_ordenamiento = get_time()  
    sort(control, algoritmo)
    tiempo_ordenamiento = delta_time(tiempo_ordenamiento, get_time())
    
    return tiempo_carga, tiempo_ordenamiento,  memoria
    
def load_data(control, tamaño, archivo):
    
    file = cf.data_dir + f'/football/{archivo}-utf8-{tamaño}.csv'
    input_file = csv.DictReader(open(file, encoding="utf-8"))
    for fila in input_file:
        model.add_data(control, fila, archivo)

def get_datasize(control):
    """
    Retorna el tamaño de los datos cargados
    """
    return model.get_datasize(control)

#Funciones de ordenamiento

def sort(control, algoritmo):
    """
    Ordena los datos del modelo
    """
    
    model.sort(control, algoritmo)
    

# Funciones de requerimientos

def req_1(control, n_partidos, equipo, condicion):
    
    tracemalloc.start()
    first_time = get_time()
    first_memory = get_memory()
    model_response = model.req_1(control, n_partidos, equipo, condicion)
    last_time = get_time()
    last_memory = get_memory()
    tracemalloc.stop()
    
    time = delta_time(first_time, last_time)
    memory = delta_memory(last_memory, first_memory)
    
    print(f"Tiempo de ejecución: {time} ms")
    print(f"Uso de memoria: {memory} KB")
    
    return model_response

def req_2(control, n_goles, jugador):
    
    tracemalloc.start()
    first_time = get_time()
    first_memory = get_memory()
    model_response = model.req_2(control, n_goles, jugador)
    last_time = get_time()
    last_memory = get_memory()
    tracemalloc.stop()
    
    time = delta_time(first_time, last_time)
    memory = delta_memory(last_memory, first_memory)
    
    print(f"Tiempo de ejecución: {time} ms")
    print(f"Uso de memoria: {memory} KB")
    
    return model_response

def req_3(control, equipo, fecha_inicial, fecha_final):
    
    tracemalloc.start()
    first_time = get_time()
    first_memory = get_memory()
    model_response = model.req_3(control, equipo, fecha_inicial, fecha_final)
    last_time = get_time()
    last_memory = get_memory()
    tracemalloc.stop()
    
    time = delta_time(first_time, last_time)
    memory = delta_memory(last_memory, first_memory)
    
    print(f"Tiempo de ejecución: {time} ms")
    print(f"Uso de memoria: {memory} KB")
    
    return model_response

def req_4(control, torneo, fecha_inicial, fecha_final):
    
    tracemalloc.start()
    first_time = get_time()
    first_memory = get_memory()
    model_response = model.req_4(control, torneo, fecha_inicial, fecha_final)
    last_time = get_time()
    last_memory = get_memory()
    tracemalloc.stop()
    
    time = delta_time(first_time, last_time)
    memory = delta_memory(last_memory, first_memory)
    
    print(f"Tiempo de ejecución: {time} ms")
    print(f"Uso de memoria: {memory} KB")
    
    return model_response

def req_5(control, anotador, fecha_inicial, fecha_final):
    
    tracemalloc.start()
    first_time = get_time()
    first_memory = get_memory()
    model_response = model.req_5(control, anotador, fecha_inicial, fecha_final)
    last_time = get_time()
    last_memory = get_memory()
    tracemalloc.stop()
    
    time = delta_time(first_time, last_time)
    memory = delta_memory(last_memory, first_memory)
    
    print(f"Tiempo de ejecución: {time} ms")
    print(f"Uso de memoria: {memory} KB")
    
    return model_response

def req_6(control, n_equipos, torneo, año):
    
    tracemalloc.start()
    first_time = get_time()
    first_memory = get_memory()
    model_response = model.req_6(control, n_equipos, torneo, año)
    last_time = get_time()
    last_memory = get_memory()
    tracemalloc.stop()
    
    time = delta_time(first_time, last_time)
    memory = delta_memory(last_memory, first_memory)
    
    print(f"Tiempo de ejecución: {time} ms")
    print(f"Uso de memoria: {memory} KB")
    
    return model_response

def req_7(control, torneo, puntaje, fecha_inicio, fecha_fin):
    
    first_time = get_time()
    first_memory = get_memory()
    model_response = model.req_7(control, torneo, puntaje, fecha_inicio, fecha_fin)
    last_time = get_time()
    last_memory = get_memory()
    
    time = delta_time(first_time, last_time)
    memory = delta_memory(last_memory, first_memory)
    
    print(f"Tiempo de ejecución: {time} ms")
    print(f"Uso de memoria: {memory} KB")
    
    return model_response

#Funciones para manejar el tiempo y la memoria

def get_time():
    """
    devuelve el instante tiempo de procesamiento en milisegundos
    """
    return float(time.perf_counter()*1000)

def delta_time(start, end):
    """
    devuelve la diferencia entre tiempos de procesamiento muestreados
    """
    elapsed = float(end - start)
    return elapsed

def get_memory():
    """
    toma una muestra de la memoria alocada en instante de tiempo
    """
    return tracemalloc.take_snapshot()

def delta_memory(stop_memory, start_memory):
    """
    calcula la diferencia en memoria alocada del programa entre dos
    instantes de tiempo y devuelve el resultado en bytes (ej.: 2100.0 B)
    """
    memory_diff = stop_memory.compare_to(start_memory, "filename")
    delta_memory = 0.0

    # suma de las diferencias en uso de memoria
    for stat in memory_diff:
        delta_memory = delta_memory + stat.size_diff
    # de Byte -> kByte
    delta_memory = delta_memory/1024.0
    return delta_memory
