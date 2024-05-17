import degradacion
import tyre
import numpy as np
import combinatoria
import json
import minimos
laps = 57
vida_esperada = {"soft":12,"medium":25,"hard":30}
degradacion_por_tipos = degradacion.degradation(43,35,4,3,5,'medium',6,0.3)
velocidades = {"soft":1.6,"medium":1.2,"hard":0.8}
types = ["soft","medium","hard"]

tiempo_neumatico = {"soft":np.zeros((1,laps)),"medium":np.zeros((1,laps)),"hard":np.zeros((1,laps))}

for i in types:

    tiempo_neumatico[i] = tyre.laptime(laps, vida_esperada[i], degradacion_por_tipos[i], velocidades[i])

# print(tiempo_neumatico) # Este print de prueba me enseña que efectivamente mis tiempos estan ordenados y asociados a  los valores.

diccionario_estrategias = {}
for paradas in range(1,4):
    n = int(paradas)
    combinaciones = combinatoria.generate_combinations(types,n) # Hasta aqui funciona si se comenta lo siguiente a 17:58 de la tarde de 14/05
    print(combinaciones)

    for elemento in combinaciones:
        # Para cada iteracion, la matriz de tiempos empieza sin nada, y se rellena con los vectores de neumatico
        matriz_tiempos = []
        for element in elemento:            
            matriz_tiempos.append(tiempo_neumatico[element]) # Llenamos la matriz con los tiempos de neumaticos en orden
          #  print(matriz_tiempos)
        
        combi1 = minimos.encontrar_minimos(matriz_tiempos,laps)
        suma = 0 # inicializo a cero el tiempo de carrera:
        for valor, (i,j) in combi1:
            #print(valor)
            suma = suma + valor #tiempo total siguiendo la estrategia de ahora: "elemento" es una tupla del tipo ('neumatico','neumatico',...)
        print(suma)
        #suma =+ paradas

        matriz_tiempos.append(suma)
        diccionario_estrategias[elemento] = matriz_tiempos
    
    #print(diccionario_estrategias)

    # with open('diccionario_estrategias.json', 'w') as file:
    #     json.dump(diccionario_estrategias, file, indent=4)

    #print(diccionario_estrategias)
        
  
        











