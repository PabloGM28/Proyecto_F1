import degradacion
import tyre
import numpy as np
import combinatoria
import minimos

def estrategia_optima(laps,track_temp, air_temp, high_speed_turns, medium_speed_turns, low_speed_turns, wing_load, length, abrassion,condition):
    vida_esperada = {"soft":int(round(laps**0.2)),"medium":int(round(laps**0.5)),"hard":int(round(laps**0.6))}
    degradacion_por_tipos = degradacion.degradation(track_temp, air_temp, high_speed_turns, medium_speed_turns, low_speed_turns, wing_load, length, abrassion,condition)
    velocidades = {"soft":1,"medium":1.043,"hard":1.083}
    types = ["soft","medium","hard"]
    tiempo_neumatico = {"soft":np.zeros((1,laps)),"medium":np.zeros((1,laps)),"hard":np.zeros((1,laps))}


    for i in types:
        tiempo_neumatico[i] = tyre.laptime(laps, vida_esperada[i], degradacion_por_tipos[i], velocidades[i])
    #print(tiempo_neumatico) # Este print de prueba me enseña que efectivamente mis tiempos estan ordenados y asociados a  los valores.

    diccionario_estrategias = {}
    tiempos_estrategia = []
    diccionario_vueltas_por_tanda = {}
    combinaciones = []

    #Primero genero todas las combinaciones posibles para la carrera:
    for paradas in range(1,4):
        n = int(paradas)
        combinaciones_raw = combinatoria.generate_combinations(types,n) # Hasta aqui funciona si se comenta lo siguiente a 17:58 de la tarde de 14/05
        combinaciones.append(combinaciones_raw)
    #print(combinaciones)
    #print(len(combinaciones))
    paradas = []
    # El siguiente paso es ver, para cada estrategia, el tiempo total que se puede hacer con las n vueltas mas rapidas disponibles:
    for opcion in combinaciones:
        for estrategia in opcion:
                    # Para cada iteracion, la matriz de tiempos empieza sin nada, y se rellena con los vectores de neumatico
                    matriz_tiempos = []
                    # Para cada estrategia, relleno la matriz con tantas filas como neumaticos se vayan a usar y los tiempos de estos:
                    for neumatico in estrategia:            
                        matriz_tiempos.append(tiempo_neumatico[neumatico]) # Llenamos la matriz con los tiempos de neumaticos en orden
                    #  print(matriz_tiempos) 
                    vueltas_carrera = minimos.encontrar_minimos(matriz_tiempos,laps)
                    
                    suma = 0 # inicializo a cero el tiempo de carrera:
                    vueltas_tanda = np.zeros((1,4))
                    contador = 0
                    for valor, (i,j) in vueltas_carrera:
                        #print(valor)
                        suma = suma + valor #tiempo total siguiendo la estrategia de ahora: "elemento" es una tupla del tipo ('neumatico','neumatico',...)
                        #print(i)
                        vueltas_tanda[0,i] += 1
                    suma = suma + len(estrategia)    
                    #diccionario_vueltas_por_tanda.append(vueltas_tanda)
                    #print(len(estrategia))
                    diccionario_estrategias[estrategia] = matriz_tiempos
                    diccionario_vueltas_por_tanda[estrategia] = vueltas_tanda
                    tiempos_estrategia.append(suma)       
                    paradas.append(len(estrategia))

    #print(tiempos_estrategia)
    #print(paradas)
    estrategias = list(diccionario_estrategias.keys())
    estrategia_ganadora = estrategias[tiempos_estrategia.index(min(tiempos_estrategia))]
    estrategia_ganadora_vueltas = estrategias
    #print(diccionario_vueltas_por_tanda)
    #print(estrategia_ganadora)
    
    return estrategia_ganadora
 
# print(estrategia_optima(50,40,35,5,4,3,"medium",6.03,0.4,"sunny"))








