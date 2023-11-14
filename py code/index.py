import time
import random

def multiplicar_matrices_tradicional(matriz1, matriz2):
    if len(matriz1[0]) != len(matriz2):
        raise ValueError("Las matrices no son compatibles para la multiplicación")

    resultado = [[0 for _ in range(len(matriz2[0]))] for _ in range(len(matriz1))]

    for i in range(len(matriz1)):
        for j in range(len(matriz2[0])):
            for k in range(len(matriz2)):
                resultado[i][j] += matriz1[i][k] * matriz2[k][j]

    return resultado

def multiplicar_matrices_eficiente(matriz1, matriz2):
    if len(matriz1[0]) != len(matriz2):
        raise ValueError("Las matrices no son compatibles para la multiplicación")

    resultado = [[0 for _ in range(len(matriz2[0]))] for _ in range(len(matriz1))]

    for i in range(len(matriz1)):
        for j in range(len(matriz2[0])):
            for k in range(len(matriz2)):
                resultado[i][j] += matriz1[i][k] * matriz2[k][j]

    return resultado

def generar_matriz_aleatoria(n):
    return [[random.randint(1, 10) for _ in range(n)] for _ in range(n)]

def imprimir_matriz(matriz):
    for fila in matriz:
        print(fila)

def main():
    n = int(input("Ingrese el tamaño n de las matrices cuadradas: "))

    opcion = input("¿Desea ingresar manualmente los elementos de las matrices? (s/n): ")

    if opcion.lower() == 's':
        matriz_a = [[int(input(f"Ingrese el elemento ({i+1}, {j+1}) para la matriz A: ")) for j in range(n)] for i in range(n)]
        matriz_b = [[int(input(f"Ingrese el elemento ({i+1}, {j+1}) para la matriz B: ")) for j in range(n)] for i in range(n)]
    else:
        matriz_a = generar_matriz_aleatoria(n)
        matriz_b = generar_matriz_aleatoria(n)

    inicio_tradicional = time.time()
    resultado_tradicional = multiplicar_matrices_tradicional(matriz_a, matriz_b)
    fin_tradicional = time.time()

    inicio_eficiente = time.time()
    resultado_eficiente = multiplicar_matrices_eficiente(matriz_a, matriz_b)
    fin_eficiente = time.time()

    print("\nMatriz A:")
    imprimir_matriz(matriz_a)

    print("\nMatriz B:")
    imprimir_matriz(matriz_b)

    print("\nResultado (Método Tradicional):")
    imprimir_matriz(resultado_tradicional)

    print("\nResultado (Método Eficiente):")
    imprimir_matriz(resultado_eficiente)

    tiempo_tradicional = fin_tradicional - inicio_tradicional
    tiempo_eficiente = fin_eficiente - inicio_eficiente

    print(f"\nTiempo de ejecución (Método Tradicional): {tiempo_tradicional} segundos")
    print(f"Tiempo de ejecución (Método Eficiente): {tiempo_eficiente} segundos")

    if tiempo_tradicional < tiempo_eficiente:
        print("\nEl método tradicional fue más rápido.")
    elif tiempo_tradicional > tiempo_eficiente:
        print("\nEl método eficiente fue más rápido.")
    else:
        print("\nAmbos métodos tomaron el mismo tiempo de ejecución.")

if __name__ == "__main__":
    main()
