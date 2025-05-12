# Práctica de Algoritmos de Ordenamiento

## 📌 Información General

- **Título:** Teoria de la Complejidad
- **Asignatura:** Estructura de Datos
- **Carrera:** Computación
- **Estudiante:** Victoria Andrade e Isabel Ullauri
- **Fecha:** 11/5/2025
- **Profesor:** Ing. Pablo Torres

---
# 📊 Comparativa de Algoritmos de Ordenamiento en Python

## 🛠️ Descripción

Este proyecto en Python implementa y compara el rendimiento de diferentes metodos de ordenamiento con arreglos de distintos tamaños. Los métodos incluidos son:

- Método Burbuja
- Método Burbuja Optimizado
- Método Selección
- Método Inserción
- Método Shell

Se realiza una medición del tiempo de ejecución de cada algoritmo utilizando `time.perf_counter_ns()` para mayor precisión. Finalmente, los resultados se grafican con `matplotlib` para visualizar el comportamiento de cada método en función del tamaño del arreglo.

---

## 🚀 Ejecución

`python app.py`

---

# 📊 Salida esperada
```plaintext

Ejecutando... Tamaño: 5000, Algoritmo: Burbuja...
Tamano: 5000, Algoritmo: burbuja, Tiempo: 1.1183 segundos
[Tiempo total acumulado] 1.12 segundos

Ejecutando... Tamaño: 5000, Algoritmo: Burbuja Optimizado...
Tamano: 5000, Algoritmo: burbujaoptimizado, Tiempo: 1.0317 segundos
[Tiempo total acumulado] 2.14 segundos

Ejecutando... Tamaño: 5000, Algoritmo: Insercion...
Tamano: 5000, Algoritmo: insercion, Tiempo: 0.3802 segundos
[Tiempo total acumulado] 2.53 segundos

Ejecutando... Tamaño: 5000, Algoritmo: Seleccion...
Tamano: 5000, Algoritmo: seleccion, Tiempo: 0.3934 segundos
[Tiempo total acumulado] 2.92 segundos

Ejecutando... Tamaño: 5000, Algoritmo: Shell...
Tamano: 5000, Algoritmo: shell, Tiempo: 0.0112 segundos
[Tiempo total acumulado] 2.94 segundos

Ejecutando... Tamaño: 10000, Algoritmo: Burbuja...
Tamano: 10000, Algoritmo: burbuja, Tiempo: 4.4639 segundos
[Tiempo total acumulado] 7.40 segundos

Ejecutando... Tamaño: 10000, Algoritmo: Burbuja Optimizado...
Tamano: 10000, Algoritmo: burbujaoptimizado, Tiempo: 4.8608 segundos
[Tiempo total acumulado] 12.27 segundos

Ejecutando... Tamaño: 10000, Algoritmo: Insercion...
Tamano: 10000, Algoritmo: insercion, Tiempo: 2.3016 segundos
[Tiempo total acumulado] 14.57 segundos

Ejecutando... Tamaño: 10000, Algoritmo: Seleccion...
Tamano: 10000, Algoritmo: seleccion, Tiempo: 2.1238 segundos
[Tiempo total acumulado] 16.72 segundos

Ejecutando... Tamaño: 10000, Algoritmo: Shell...
Tamano: 10000, Algoritmo: shell, Tiempo: 0.0226 segundos
[Tiempo total acumulado] 16.75 segundos

Ejecutando... Tamaño: 30000, Algoritmo: Burbuja...
Tamano: 30000, Algoritmo: burbuja, Tiempo: 47.4927 segundos
[Tiempo total acumulado] 64.24 segundos

Ejecutando... Tamaño: 30000, Algoritmo: Burbuja Optimizado...
Tamano: 30000, Algoritmo: burbujaoptimizado, Tiempo: 46.1711 segundos
[Tiempo total acumulado] 110.42 segundos

Ejecutando... Tamaño: 30000, Algoritmo: Insercion...
Tamano: 30000, Algoritmo: insercion, Tiempo: 17.7527 segundos
[Tiempo total acumulado] 128.16 segundos

Ejecutando... Tamaño: 30000, Algoritmo: Seleccion...
Tamano: 30000, Algoritmo: seleccion, Tiempo: 17.6632 segundos
[Tiempo total acumulado] 145.83 segundos

Ejecutando... Tamaño: 30000, Algoritmo: Shell...
Tamano: 30000, Algoritmo: shell, Tiempo: 0.1465 segundos
[Tiempo total acumulado] 145.97 segundos
```

Y al finalizar, se mostrará una gráfica comparativa




## EJEMPLO DE ADICIÓN DE DATOS EN ESTE INFORME

Eje X: Tamaño del arreglo.

Eje Y: Tiempo de ejecución (en segundos).

![Figuras](figuras.png)


##  CONCLUCIONES CON TERMINOLOGIA DE NOTACION 

 - La comparación de los métodos de ordenamiento muestra diferencias grandes en el tiempo de ejecución a medida que aumenta el tamaño del arreglo. Los algoritmos con complejidad cuadrática O(n^2), como Burbuja, Burbuja Optimizado, Inserción y Selección, muestran un crecimiento exponencial en su tiempo de procesamiento, volviéndose poco prácticos para tamaños grandes.Por el contrario, el algoritmo Shell, que tiene un mejor rendimiento teórico en promedio O(n log^2 n), demuestra una eficiencia notable en todos los casos. Esto confirma que, para aplicaciones prácticas donde el tamaño de los datos puede escalar, algoritmos como Shell resultan mucho más eficientes y adecuados. 
