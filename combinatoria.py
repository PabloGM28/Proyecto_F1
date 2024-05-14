from itertools import permutations

# Para un numero de paradas dado, me va a calcular todas las combinaciones de neumatico posibles:

def generate_combinations(strings,n):
    # Genera todas las permutaciones posibles de los strings en n posiciones
    permutations_list = permutations(strings*(n+1), (n+1))
    # Convierte las permutaciones en conjuntos para eliminar duplicados basados en la cantidad de cada elemento
    unique_combinations = {tuple(sorted(perm)) for perm in permutations_list}
    unique_combinations = [comb for comb in unique_combinations if len(set(comb)) > 1]
    return unique_combinations

# Ejemplo de uso, queda comentado pero puede usarse para probar esta funcion: Recuerda meter el numero de neumaticos
# y las paradas que quieres hacer en carrera:

strings = ["soft", "medium", "high"]

combinations = generate_combinations(strings,2)
