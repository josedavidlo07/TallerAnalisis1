import random

# Definición de la clase base AlgoritmoOrdenamiento para los algoritmos
class AlgoritmoOrdenamiento:
    def __init__(self, nombre):
        self.nombre = nombre
        self.comparaciones = 0
        self.intercambios = 0

    def ordenar(self, arreglo):
        raise NotImplementedError("Este método debe ser implementado en las subclases.")

    def resetear_contadores(self):
        self.comparaciones = 0
        self.intercambios = 0

# Algoritmo Bubble Sort
class BubbleSort(AlgoritmoOrdenamiento):
    def __init__(self):
        super().__init__("Bubble Sort")

    def ordenar(self, arreglo):
        n = len(arreglo)
        for i in range(n):
            for j in range(0, n-i-1):
                self.comparaciones += 1
                if arreglo[j] > arreglo[j+1]:
                    self.intercambios += 1
                    arreglo[j], arreglo[j+1] = arreglo[j+1], arreglo[j]
        return arreglo

# Algoritmo Selection Sort
class SelectionSort(AlgoritmoOrdenamiento):
    def __init__(self):
        super().__init__("Selection Sort")

    def ordenar(self, arreglo):
        n = len(arreglo)
        for i in range(n):
            min_idx = i
            for j in range(i+1, n):
                self.comparaciones += 1
                if arreglo[j] < arreglo[min_idx]:
                    min_idx = j
            self.intercambios += 1
            arreglo[i], arreglo[min_idx] = arreglo[min_idx], arreglo[i]
        return arreglo

# Algoritmo Insertion Sort
class InsertionSort(AlgoritmoOrdenamiento):
    def __init__(self):
        super().__init__("Insertion Sort")

    def ordenar(self, arreglo):
        for i in range(1, len(arreglo)):
            key = arreglo[i]
            j = i-1
            self.comparaciones += 1
            while j >= 0 and key < arreglo[j]:
                self.comparaciones += 1
                arreglo[j + 1] = arreglo[j]
                j -= 1
                self.intercambios += 1
            arreglo[j + 1] = key
        return arreglo

# Algoritmo Merge Sort
class MergeSort(AlgoritmoOrdenamiento):
    def __init__(self):
        super().__init__("Merge Sort")

    def ordenar(self, arreglo):
        if len(arreglo) <= 1:
            return arreglo
        medio = len(arreglo) // 2
        izquierda = self.ordenar(arreglo[:medio])
        derecha = self.ordenar(arreglo[medio:])
        return self.merge(izquierda, derecha)

    def merge(self, izquierda, derecha):
        resultado = []
        i = j = 0
        while i < len(izquierda) and j < len(derecha):
            self.comparaciones += 1
            if izquierda[i] < derecha[j]:
                resultado.append(izquierda[i])
                i += 1
            else:
                resultado.append(derecha[j])
                j += 1
        resultado.extend(izquierda[i:])
        resultado.extend(derecha[j:])
        return resultado

# Algoritmo Quick Sort
class QuickSort(AlgoritmoOrdenamiento):
    def __init__(self):
        super().__init__("Quick Sort")

    def ordenar(self, arreglo):
        if len(arreglo) <= 1:
            return arreglo
        pivot = arreglo[0]
        izquierda = [x for x in arreglo[1:] if x < pivot]
        derecha = [x for x in arreglo[1:] if x >= pivot]
        self.comparaciones += len(arreglo) - 1  # Comparaciones del pivot
        return self.ordenar(izquierda) + [pivot] + self.ordenar(derecha)

# Función para generar arreglos aleatorios
def generar_arreglos(cantidad, tamaño):
    arreglos = []
    for _ in range(cantidad):
        arreglo = [random.randint(0, 10000) for _ in range(tamaño)]
        arreglos.append(arreglo)
    return arreglos

# Función para realizar la competencia entre algoritmos
def competencia_algoritmos(arreglos, algoritmos):
    resultados = {algoritmo.nombre: {'puntos': 0, 'operaciones': 0} for algoritmo in algoritmos}

    for arreglo in arreglos:
        # Reseteamos los contadores de cada algoritmo
        for algoritmo in algoritmos:
            algoritmo.resetear_contadores()
            arreglo_copy = arreglo[:]
            algoritmo.ordenar(arreglo_copy)
            resultados[algoritmo.nombre]['operaciones'] += algoritmo.comparaciones + algoritmo.intercambios

        # Ordenamos los algoritmos según el número de operaciones
        ranked_algorithms = sorted(algoritmos, key=lambda algo: (algo.comparaciones + algo.intercambios))

        # Asignamos puntos
        for i, algoritmo in enumerate(ranked_algorithms):
            if i == 0:
                resultados[algoritmo.nombre]['puntos'] += 5
            elif i == 1:
                resultados[algoritmo.nombre]['puntos'] += 4
            elif i == 2:
                resultados[algoritmo.nombre]['puntos'] += 3
            elif i == 3:
                resultados[algoritmo.nombre]['puntos'] += 2
            elif i == 4:
                resultados[algoritmo.nombre]['puntos'] += 1

    return resultados

# Función para mostrar los resultados
def mostrar_resultados(resultados):
    print(f"\nResultados de la competencia:")
    print(f"{'Algoritmo':<20}{'Puntos':<10}{'Operaciones Promedio'}")
    for nombre, datos in sorted(resultados.items(), key=lambda x: x[1]['puntos'], reverse=True):
        operaciones_promedio = datos['operaciones'] / 100
        print(f"{nombre:<20}{datos['puntos']:<10}{operaciones_promedio:.2f}")

# Main para ejecutar la competencia
def main():
    N = 1000  # Tamaño de los arreglos
    arreglos = generar_arreglos(100, N)  # Generamos 100 arreglos
    algoritmos = [BubbleSort(), SelectionSort(), InsertionSort(), MergeSort(), QuickSort()]
    
    # Ejecutamos la competencia
    resultados = competencia_algoritmos(arreglos, algoritmos)
    
    # Mostramos los resultados
    mostrar_resultados(resultados)

if __name__ == "__main__":
    main()
