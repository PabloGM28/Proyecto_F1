import degradacion
import tyre
import numpy as np
import combinatoria
laps = 57
vida_esperada = [12,25,30]
degradacion_por_tipos = degradacion.degradation(43,35,4,3,5,'medium',6,0.3)
velocidades = [2, 1.5, 1]
tiempo_neumatico = np.zeros((3,laps))

for i in (0,1,2):
    print(i)
    print(velocidades[i], degradacion_por_tipos[i], vida_esperada[i])
    tiempo_neumatico[int(i),:] = tyre.laptime(laps,vida_esperada[i],degradacion_por_tipos[i],velocidades[i])


#print(tiempo_neumatico)
# tiempo_neumatico = np.zeros((3,laps,laps))
# for i in range(2):
#     for j in range(laps-1):
#             matriz_de_tiempos[i,j,j]= tiempo_neumatico[i,laps,j-laps]

from itertools import combinations_with_replacement






