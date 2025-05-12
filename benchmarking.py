import time
from typing import Callable, List

class Benchmark:

    @staticmethod
    def medir_tiempo(func: Callable[[List[int]], List[int]], array: List[int]) -> float:
        
        inicio = time.perf_counter_ns()
        func(array.copy())
        fin = time.perf_counter_ns()

        tiempo_ns = fin - inicio
        tiempo_segundos = tiempo_ns / 1000000000 
        return tiempo_segundos
