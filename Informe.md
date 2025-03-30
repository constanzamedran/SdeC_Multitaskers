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

