# UNIVERSIDAD NACIONAL DE CORDOBA
# Sistemas de Computacion
# Trabajo Practico 1: Rendimiento

**Alumnos:**
- Medran, Constanza
- Martin, Tomas
- Diaz, Mateo

**Grupo:** Multitaskers

**Docentes:** 
- Jorge, Javier
- Solinas, Miguel

# Introducción

El rendimiento y la eficiencia de los sistemas computacionales son aspectos fundamentales en la toma de decisiones relacionadas con hardware y software. En este trabajo práctico, exploramos diversos aspectos del rendimiento de los computadores mediante la aplicación de técnicas de benchmarking y análisis de resultados.


# Benchmarks
Un benchmark es una prueba o conjunto de pruebas diseñadas para medir el rendimiento de un sistema, componente de hardware o software en determinadas tareas. Tiene como objetivo objetivo proporcionar datos comparables sobre la eficiencia, velocidad y capacidad de procesamiento de diferentes dispositivos o programas.

## Benchmarks para tareas cotidianas
| Tarea                                       | Benchmark      |
|---------------------------------------------|---------------|
| Medir el ancho de banda de redes y rendimiento de conexión | iPerf         |
| Navegación web, uso general de aplicaciones | PCMark 10     |
| Comprimir y descomprimir archivos           | 7-Zip (integrado) |
| Rendimiento CPU y GPU                        | Cinebench     |
| Medir el rendimiento de fragmentos de código de Python | pyperf        |
| Evaluar el rendimiento de bases de datos (especialmente MySQL) | Sysbench      |

## Rendimiento de los procesadores para Compilar el Kernel de Linux
Utilizamos los datos proporcionados en el enlace de referencia y calculando la aceleracion o speedup: 

$$ \text{Rendimiento} = \frac{1}{T} $$

Armamos la siguiente tabla:

| Procesador          | Tiempo (s) | Rendimiento (1/s) | Rendimiento (%)    |
|---------------------|------------|--------------------|-------------------|
| Intel i5-13600K    | 83 ± 3     | 0,0120             | 1,2%               |
| AMD Ryzen 9 5900X  | 97 ± 7     | 0,0103             | 1,03%              |
| AMD Ryzen 9 7950X  | 53 ± 3     | 0,0188             | 1,88%              |

### Aceleracion del Ryzen 9 7950X
Para calcular la aceleracion en comparacion a los otros procesadores, usamos la formula:

$$ \text{Speedup} = \frac{Rendimiento Mejorado}{Rendimiento Base} $$

**En comparación con Intel Core i5-13600K**  

$$ \text{Speedup} = \frac{83}{53} = 1.566 $$

**En comparación con AMD Ryzen 9 5900X**  

$$ \text{Speedup} = \frac{97}{53} = 1.830 $$


## Time Profiling

Cada integrante del grupo ejecutó el código y se obtuvó una imagen que reúne toda la información de la ejecución realizada, como se muestra a continuación.

### Ejecuciones

![Screenshot from 2025-03-31 10-51-47](https://github.com/user-attachments/assets/d047d6b5-9bba-47b6-a244-2ad3493ad4bd)

En las imágenes se muestra el análisis de tiempo del programa ejecutado por cada miembro del equipo. Este análisis nos proporciona información sobre el tiempo de ejecución de cada función dentro del programa.

En primer lugar, se puede observar que la imagen proporciona información sobre los llamados a las funciones, detallando qué función llamó a cuál y cuántas veces se realizó cada llamado. Además, muestra cómo aumenta el tiempo de ejecución si la función llamada dentro también tarda en completarse. Por ejemplo, new_func1 podría llegar a ser la responsable de que func1 demore la ejecución, pero en este caso no es así.

También, viendo la salida del flat profile que brinda gprof, se puede encontrar que la ejecución 1 parece tener el mejor rendimiento general, ya que completa la ejecución del código más rápidamente (10.21 segundos), seguida de la ejecución 2 (14.61 segundos) y finalmente la ejecución 3 (18.49 segundos). Esto puede ser indicativo de diferencias en el rendimiento del procesador, la memoria, la optimización del sistema operativo o la carga del sistema (procesos en segundo plano) de cada equipo.

A pesar de que el total de tiempo en cada máquina es diferente, las proporciones del tiempo de ejecución dentro de cada máquina (porcentaje de tiempo dedicado a cada función) son relativamente consistentes entre las tres salidas.

Podemos concluir, analizando las tres ejecuciones, que func1 es la función que más tiempo consume, con un porcentaje del tiempo que varía entre el 54.73% y el 58.04%. Esto sugiere que func1 es una función clave en el programa que requiere optimización si se quiere mejorar el rendimiento.



