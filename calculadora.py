import degradacion
import tyre
import numpy as np
import combinatoria
import minimos

laps = 10
vida_esperada = {"soft":20,"medium":25,"hard":40}
degradacion_por_tipos = degradacion.degradation(43,35,4,3,5,'medium',6,0.3)
velocidades = {"soft":1.05,"medium":1.003,"hard":1}
types = ["soft","medium","hard"]
tiempo_neumatico = {"soft":np.zeros((1,laps)),"medium":np.zeros((1,laps)),"hard":np.zeros((1,laps))}


for i in types:
    tiempo_neumatico[i] = tyre.laptime(laps, vida_esperada[i], degradacion_por_tipos[i], velocidades[i])
# print(tiempo_neumatico) # Este print de prueba me enseña que efectivamente mis tiempos estan ordenados y asociados a  los valores.


diccionario_estrategias = {}

tiempos_estrategia = []

#Primero genero todas las combinaciones posibles para la carrera:
for paradas in range(1,4):
    n = int(paradas)
    combinaciones = combinatoria.generate_combinations(types,n) # Hasta aqui funciona si se comenta lo siguiente a 17:58 de la tarde de 14/05
    #print(combinaciones)
# El siguiente paso es ver, para cada estrategia, el tiempo total que se puede hacer con las n vueltas mas rapidas disponibles:
for estrategia in combinaciones:
            # Para cada iteracion, la matriz de tiempos empieza sin nada, y se rellena con los vectores de neumatico
            matriz_tiempos = []
            # Para cada estrategia, relleno la matriz con tantas filas como neumaticos se vayan a usar y los tiempos de estos:
            for neumatico in estrategia:            
                matriz_tiempos.append(tiempo_neumatico[neumatico]) # Llenamos la matriz con los tiempos de neumaticos en orden

            #  print(matriz_tiempos) 
            vueltas_carrera = minimos.encontrar_minimos(matriz_tiempos,laps)
            
            suma = 0 # inicializo a cero el tiempo de carrera:
            for valor, (i,j) in vueltas_carrera:
                #print(valor)
                suma = suma + valor #tiempo total siguiendo la estrategia de ahora: "elemento" es una tupla del tipo ('neumatico','neumatico',...)
            print(suma)
    
            print(len(estrategia))
            diccionario_estrategias[estrategia] = matriz_tiempos
            tiempos_estrategia.append(suma+len(estrategia))       
    

print(tiempos_estrategia)

# estrategia_ganadora_raw = min(tiempos_estrategia)
# posicion = tiempos_estrategia.index(min(tiempos_estrategia))
estrategias = list(diccionario_estrategias.keys())
estrategia_ganadora = estrategias[tiempos_estrategia.index(min(tiempos_estrategia))]

print(estrategia_ganadora)
    
    #print(diccionario_estrategias)

    # with open('diccionario_estrategias.json', 'w') as file:
    #     json.dump(diccionario_estrategias, file, indent=4)

    #print(diccionario_estrategias)
        
  
        











