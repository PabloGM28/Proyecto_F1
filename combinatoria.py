from itertools import permutations

def generate_combinations(strings,n):
    # Genera todas las permutaciones posibles de los strings en n posiciones
    permutations_list = permutations(strings*(n+1), (n+1))
    # Convierte las permutaciones en conjuntos para eliminar duplicados basados en la cantidad de cada elemento
    unique_combinations = {tuple(sorted(perm)) for perm in permutations_list}
    unique_combinations = [comb for comb in unique_combinations if len(set(comb)) > 1]

    return unique_combinations

# Ejemplo de uso
strings = ["soft", "medium", "high"]
combinations = generate_combinations(strings,2)
for comb in combinations:
    print(comb)
