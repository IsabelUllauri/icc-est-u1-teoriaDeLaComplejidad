import random
from typing import List, Dict, Callable, Tuple
from benchmarking import Benchmark
from SortingMethods import SortMethods
import time
import matplotlib.pyplot as plt
from collections import defaultdict

class App:

    def __init__(self):
        self.tamanos: List[int] = [5000, 10000,30000,50000,100000]
        self.max_tamano: int = max(self.tamanos)
        self.arreglo_base: List[int] = self.build_arreglo(self.max_tamano)

        self.algoritmos: Dict[str, Callable[[List[int]], List[int]]] = {

            "Burbuja": SortMethods.sort_bubble,
            "Burbuja Optimizado": SortMethods.sort_bubble_optimized,
            "Insercion": SortMethods.sort_insertion,
            "Seleccion": SortMethods.sort_selection,
            "Shell": SortMethods.sort_shell
        }
        self.resultados: List[Tuple[int, str, float]] = []

    def build_arreglo(self, tamano: int) -> List[int]:
        return [random.randint(1, 100000) for _x in range(tamano)]

    
    def main(self) -> None:
        tiempo_inicio_total = time.time()  

        for tam in self.tamanos:
            arreglo = self.arreglo_base[:tam]
            for nombre, metodo in self.algoritmos.items():
                print(f"\n Tamaño: {tam}, Algoritmo: {nombre}...")

                tiempo_algoritmo = Benchmark.medir_tiempo(metodo, arreglo)
                self.resultados.append((tam, nombre, tiempo_algoritmo))

                nombre_formateado = nombre.lower().replace(" ", "")
                print(f"Tamano: {tam}, Algoritmo: {nombre_formateado}, Tiempo: {tiempo_algoritmo:.4f} segundos")

                tiempo_transcurrido = time.time() - tiempo_inicio_total
                print(f"[Tiempo total acumulado] {tiempo_transcurrido:.2f} segundos")

        # grafica de resultados
        from collections import defaultdict
        import matplotlib.pyplot as plt

        tiempos_by_metodo = defaultdict(list)

        for tam in self.tamanos:
            for nombre in self.algoritmos.keys():
                for r in self.resultados:
                    if r[0] == tam and r[1] == nombre:
                        tiempos_by_metodo[nombre].append(r[2])
                        break

        plt.figure(figsize=(10, 6))

        for nombre, tiempos in tiempos_by_metodo.items():
            plt.plot(self.tamanos, tiempos, label=nombre, marker="o")  

        plt.title("Comparativa de métodos")
        plt.xlabel("Tamaños de arreglo")
        plt.ylabel("Tiempo obtenido (en segundos)")
        plt.grid(True)
        plt.legend()
        plt.tight_layout()
        plt.show()
       


if __name__ == "__main__":
    app = App()
    app.main()