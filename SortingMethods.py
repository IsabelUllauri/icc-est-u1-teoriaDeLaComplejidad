from typing import List

class SortMethods:

    @staticmethod
    def sort_shell(arreglo: List[int]) -> List[int]:
        arreglo = arreglo.copy()
        n = len(arreglo)
        gap = n // 2
        while gap > 0:
            for i in range(gap, n):
                temp = arreglo[i]
                j = i
                while j >= gap and arreglo[j - gap] > temp:
                    arreglo[j] = arreglo[j - gap]
                    j -= gap
                arreglo[j] = temp
            gap //= 2
        return arreglo

    @staticmethod
    def sort_bubble_optimized(arreglo: List[int]) -> List[int]:
        arreglo = arreglo.copy()
        n = len(arreglo)
        for i in range(n):
            swapped = False # Variable para optimización
            for j in range(n - i - 1): # La última parte del arreglo ya está ordenada
                if arreglo[j] > arreglo[j + 1]:
                    arreglo[j], arreglo[j + 1] = arreglo[j + 1], arreglo[j]  #Corregir el intercambio
                    swapped = True
            if not swapped: # Si no se hizo ningún cambio, ya está ordenado
                break
        return arreglo

    @staticmethod
    def sort_bubble(arreglo: List[int]) -> List[int]:
        arreglo = arreglo.copy()
        n = len(arreglo)
        for i in range(n):
            for j in range(0, n - i - 1):
                if arreglo[j] > arreglo[j + 1]:
                    arreglo[j], arreglo[j + 1] = arreglo[j + 1], arreglo[j]
        return arreglo

    @staticmethod
    def sort_insertion(arreglo: List[int]) -> List[int]:
        arreglo = arreglo.copy()
        for i in range(1, len(arreglo)):
            pasajero = arreglo[i]
            j = i - 1
            while j >= 0 and arreglo[j] > pasajero:
                arreglo[j + 1] = arreglo[j]
                j -= 1
            arreglo[j + 1] = pasajero
        return arreglo

    @staticmethod
    def sort_selection(arreglo: List[int]) -> List[int]:
        arreglo = arreglo.copy()
        n = len(arreglo)
        for i in range(n):
            indiceMin = i
            for j in range(i + 1, n):
                if arreglo[j] < arreglo[indiceMin]:
                    indiceMin = j
            if indiceMin != i:
                arreglo[i], arreglo[indiceMin] = arreglo[indiceMin], arreglo[i]
        return arreglo

    

