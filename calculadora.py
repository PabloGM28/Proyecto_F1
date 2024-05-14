import degradacion
import tyre
import numpy as np
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

def generate_combinations(strings):
    # Genera todas las combinaciones posibles de los strings en 4 posiciones
    combinations = list(combinations_with_replacement(strings, 4))

    # Descarta combinaciones con los 4 strings iguales
    combinations = [comb for comb in combinations if len(set(comb)) > 1]

    # Descarta combinaciones con la misma cantidad de un tipo de string
    filtered_combinations = []
    for comb in combinations:
        counts = {s: comb.count(s) for s in set(comb)}
        if len(set(counts.values())) == len(counts):
            filtered_combinations.append(comb)

    return filtered_combinations

# Ejemplo de uso
strings = ["soft", "medium", "high"]
combinations = generate_combinations(strings)
for comb in combinations:
    print(comb)





