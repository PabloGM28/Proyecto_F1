import heapq

def encontrar_minimos(matriz, n):
    # Crear una lista para almacenar los valores con sus posiciones
    valores_con_posiciones = []
    # Recorrer la matriz para obtener los valores y sus posiciones
    for i, fila in enumerate(matriz):
        for j, valor in enumerate(fila):
            valores_con_posiciones.append((valor, (i, j)))
    # Obtener los n valores mínimos usando heapq.nsmallest
    minimos = heapq.nsmallest(n, valores_con_posiciones, key = lambda x: x[0])
    return minimos



# # Ejemplo de uso:
# matriz = [
#     [5, 12, 17, 9, 3],
#     [13, 4, 8, 14, 1],
#     [9, 6, 3, 7, 21],
#     [5, 7, 9, 3, 11]
# ]

# n = 5
# minimos = encontrar_minimos(matriz, n)

# print(f'Los {n} valores mínimos y sus posiciones son:')
# for valor, (i, j) in minimos:
#     print(f'Valor: {valor}, Posición: ({i}, {j})')
