import random
import time

# ----------------------------
# ALGORITMOS DE ORDENAMIENTO
# ----------------------------

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    menores = [x for x in arr[1:] if x <= pivot]
    mayores = [x for x in arr[1:] if x > pivot]
    return quicksort(menores) + [pivot] + quicksort(mayores)

# ------------------------
# ALGORITMOS DE BÚSQUEDA
# ------------------------

def linear_search(arr, target):
    for i, val in enumerate(arr):
        if val == target:
            return i
    return -1

def binary_search(arr, target):
    left, right = 0, len(arr)-1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

# ------------------------
# FUNCIONES AUXILIARES
# ------------------------

def generate_random_list(size, lower=1, upper=10000):
    return [random.randint(lower, upper) for _ in range(size)]

def measure_time(func, *args):
    start = time.perf_counter()
    result = func(*args)
    end = time.perf_counter()
    return end - start, result

# ------------------------
# PROGRAMA PRINCIPAL
# ------------------------

def main():
    print("📦 Simulación de búsqueda y ordenamiento en un sistema logístico\n")

    tamaño_lista = 1000
    lista_original = generate_random_list(tamaño_lista)
    objetivo = lista_original[tamaño_lista // 2]

    print(f"Se generó una lista de {tamaño_lista} productos aleatorios.")
    print(f"El producto a localizar tiene el código: {objetivo}\n")

    # Búsqueda en lista desordenada
    tiempo_lineal, pos_lineal = measure_time(linear_search, lista_original, objetivo)
    print(f"🔍 Búsqueda lineal (depósito desordenado): producto encontrado en el casillero {pos_lineal}, tiempo = {tiempo_lineal:.6f} segundos")

    tiempo_binaria_desordenada, pos_binaria_desordenada = measure_time(binary_search, lista_original, objetivo)
    print(f"🔍 Búsqueda binaria (depósito desordenado): resultado = {pos_binaria_desordenada}, tiempo = {tiempo_binaria_desordenada:.6f} segundos ❌ (búsqueda inválida)\n")

    # Ordenamiento con Bubble Sort
    lista_bubble = lista_original.copy()
    tiempo_bubble, _ = measure_time(bubble_sort, lista_bubble)
    print(f"📊 Bubble Sort ordenó la lista en {tiempo_bubble:.6f} segundos")

    # Ordenamiento con Insertion Sort
    lista_insertion = lista_original.copy()
    tiempo_insertion, _ = measure_time(insertion_sort, lista_insertion)
    print(f"📊 Insertion Sort ordenó la lista en {tiempo_insertion:.6f} segundos")

    # Ordenamiento con Selection Sort
    lista_selection = lista_original.copy()
    tiempo_selection, _ = measure_time(selection_sort, lista_selection)
    print(f"📊 Selection Sort ordenó la lista en {tiempo_selection:.6f} segundos")

    # Ordenamiento con QuickSort (devuelve lista nueva)
    lista_quick = lista_original.copy()
    tiempo_quick, lista_quick_ordenada = measure_time(quicksort, lista_quick)
    print(f"📊 QuickSort ordenó la lista en {tiempo_quick:.6f} segundos\n")

    # Usamos lista_quick_ordenada para búsquedas ordenadas

    # Búsqueda en lista ordenada (QuickSort)
    tiempo_lineal_ordenada, pos_lineal_ordenada = measure_time(linear_search, lista_quick_ordenada, objetivo)
    print(f"🔍 Búsqueda lineal (depósito ordenado): producto encontrado en el casillero {pos_lineal_ordenada}, tiempo = {tiempo_lineal_ordenada:.6f} segundos")

    tiempo_binaria, pos_binaria = measure_time(binary_search, lista_quick_ordenada, objetivo)
    print(f"🔍 Búsqueda binaria (depósito ordenado): producto encontrado en el casillero {pos_binaria}, tiempo = {tiempo_binaria:.6f} segundos ✅\n")

    print("📦 Resumen de la simulación logística:")
    print("- La búsqueda lineal encuentra el producto siempre, pero es más lenta.")
    print("- La búsqueda binaria es mucho más rápida, pero necesita que el inventario esté ordenado.")
    print("- Ordenar los productos previamente mejora la eficiencia, especialmente si hay búsquedas frecuentes.")
    print("- Los algoritmos de ordenamiento simples son demasiado lentos para grandes volúmenes, mientras que QuickSort ofrece un equilibrio ideal entre velocidad y practicidad.")
    print("- En un entorno logístico real, mantener el inventario estructurado ahorra tiempo y recursos.\n")




if __name__ == "__main__":
    main()
