import degradacion
import tyre
import numpy as np
import combinatoria
laps = 57
vida_esperada = {"soft":12,"medium":25,"hard":30}
degradacion_por_tipos = degradacion.degradation(43,35,4,3,5,'medium',6,0.3)
velocidades = {"soft":1.6,"medium":1.2,"hard":0.8}
types = ["soft","medium","hard"]

tiempo_neumatico = {"soft":np.zeros((1,laps)),"medium":np.zeros((1,laps)),"hard":np.zeros((1,laps))}

for i in types:

    tiempo_neumatico[i] = tyre.laptime(laps, vida_esperada[i], degradacion_por_tipos[i], velocidades[i])

# print(tiempo_neumatico) # Este print de prueba me enseña que efectivamente mis tiempos estan ordenados y asociados a  los valores.









