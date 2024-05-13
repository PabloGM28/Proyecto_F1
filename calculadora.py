import degradacion
import tyre
import numpy as np

vida_esperada = [12,25,30]
degradacion_por_tipos = degradacion.degradation(43,35,4,3,5,'medium',6,0.3)
velocidades = [2, 1.5, 1]
tiempo_neumatico = np.zeros((3,57))

for i in (0,1,2):
    print(i)
    print(velocidades[i], degradacion_por_tipos[i], vida_esperada[i])
    tiempo_neumatico[int(i),:] = tyre.laptime(57,vida_esperada[i],degradacion_por_tipos[i],velocidades[i])


#print(tiempo_neumatico)
tiempo_neumatico = np.zeros((3,57))
for i in range(1):
    for j in range(1):
        for k in range(56):
            matriz_de_tiempos[i,j,k]= tiempo_neumatico[i]