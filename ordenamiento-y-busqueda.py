import random
import time

# --------------------------------------------------------------------------------------------
# ALGORITMOS DE ORDENAMIENTO
# Funciones utilizadas para ordenar listas de datos numéricos simulando información logística

def bubble_sort(lista):
    # Recorre la lista varias veces, comparando e intercambiando elementos adyacentes
    # si están en el orden incorrecto, muy ineficiente para grandes volúmenes de datos
    n = len(lista)
    for i in range(n):
        for j in range(0, n - i - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]

def insertion_sort(lista):
    # Inserta cada nuevo elemento en su posición correcta respecto a los anteriores
    # Es eficiente en listas pequeñas o casi ordenadas
    for i in range(1, len(lista)):
        clave = lista[i]
        j = i - 1
        while j >= 0 and clave < lista[j]:
            lista[j + 1] = lista[j]
            j -= 1
        lista[j + 1] = clave

def selection_sort(lista):
    # Encuentra el menor elemento en cada iteración y lo coloca al inicio del subgrupo
    # Poco eficiente para grandes volúmenes, pero fácil de implementar
    n = len(lista)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if lista[j] < lista[min_idx]:
                min_idx = j
        lista[i], lista[min_idx] = lista[min_idx], lista[i]

def quicksort(lista):
    # Algoritmo de ordenamiento eficiente basado en recursividad
    # Selecciona un pivote y divide la lista en menores y mayores, aplicando recursión en cada parte
    if len(lista) <= 1:
        return lista
    pivote = lista[0]
    menores = [x for x in lista[1:] if x <= pivote]
    mayores = [x for x in lista[1:] if x > pivote]
    return quicksort(menores) + [pivote] + quicksort(mayores)

# --------------------------------------------------------------------------------------------
# ALGORITMOS DE BÚSQUEDA
# Métodos de localización de elementos dentro de listas de datos logísticos

def busqueda_lineal(lista, objetivo):
    # Busca el objetivo comparando secuencialmente cada elemento
    # Funciona sobre listas desordenadas, pero es lenta si la lista es muy grande
    for i, valor in enumerate(lista):
        if valor == objetivo:
            return i
    return -1

def busqueda_binaria(lista, objetivo):
    # Busca el objetivo dividiendo una lista ordenada en mitades
    # Muy eficiente, pero solo funciona si la lista está ya ordenada
    izquierda, derecha = 0, len(lista) - 1
    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        if lista[medio] == objetivo:
            return medio
        elif lista[medio] < objetivo:
            izquierda = medio + 1
        else:
            derecha = medio - 1
    return -1

# --------------------------------------------------------------------------------------------
# FUNCIONES AUXILIARES
# Herramientas de apoyo para simular datos y medir rendimiento

def generar_lista_aleatoria(tamaño, minimo=1, maximo=10000):
    # Genera una lista de valores numéricos aleatorios simulando códigos logísticos
    return [random.randint(minimo, maximo) for _ in range(tamaño)]

def medir_tiempo(funcion, *args):
    # Mide el tiempo de ejecución de una función dada
    inicio = time.perf_counter()
    resultado = funcion(*args)
    fin = time.perf_counter()
    return fin - inicio, resultado

# --------------------------------------------------------------------------------------------
# PROGRAMA PRINCIPAL
# Simulación de búsqueda y ordenamiento aplicada a gestión logística

def main():
    print("Simulación de búsqueda y ordenamiento en logística\n")

    tamaño_lista = 1000 # Tamaño de la lista a procesar
    lista = generar_lista_aleatoria(tamaño_lista) # Lista de datos aleatorios

# Se selecciona un elemento objetivo representando, por ejemplo, un código de envío
    objetivo = lista[tamaño_lista // 2]

    print(f"Lista generada con {tamaño_lista} elementos.")
    print(f"Buscaremos el número {objetivo} para simular búsqueda de producto.\n")

    # 1. Búsqueda Lineal en lista desordenada
    tiempo_lineal, indice_lineal = medir_tiempo(busqueda_lineal, lista, objetivo)
    print(f"Búsqueda Lineal (lista desordenada): índice {indice_lineal}, tiempo {tiempo_lineal:.6f} segundos")

    # 2. Búsqueda Binaria en lista desordenada (resultado probablemente incorrecto)
    tiempo_binaria_desordenada, indice_binaria_desordenada = medir_tiempo(busqueda_binaria, lista, objetivo)
    print(f"Búsqueda Binaria (lista desordenada): índice {indice_binaria_desordenada}, tiempo {tiempo_binaria_desordenada:.6f} segundos (NO válida)\n")

    # 3. Ordenamos la lista con QuickSort
    tiempo_ordenar, lista_ordenada = medir_tiempo(quicksort, lista)
    print(f"Lista ordenada con QuickSort en {tiempo_ordenar:.6f} segundos.\n")

    # 4. Búsqueda Lineal en lista ordenada
    tiempo_lineal_ordenada, indice_lineal_ordenada = medir_tiempo(busqueda_lineal, lista_ordenada, objetivo)
    print(f"Búsqueda Lineal (lista ordenada): índice {indice_lineal_ordenada}, tiempo {tiempo_lineal_ordenada:.6f} segundos")

    # 5. Búsqueda Binaria en lista ordenada
    tiempo_binaria, indice_binaria = medir_tiempo(busqueda_binaria, lista_ordenada, objetivo)
    print(f"Búsqueda Binaria (lista ordenada): índice {indice_binaria}, tiempo {tiempo_binaria:.6f} segundos\n")

    # Resumen
    print("Resumen de análisis:")
    print("- La búsqueda lineal siempre funciona, pero es lenta con listas grandes.")
    print("- La búsqueda binaria es más rápida, pero requiere que la lista esté ordenada.")
    print("- Ordenar los datos antes de buscar puede ahorrar tiempo si se hacen muchas búsquedas.")
    print("- En logística, mantener inventarios ordenados mejora la eficiencia del sistema.")

if __name__ == "__main__":
    main()
