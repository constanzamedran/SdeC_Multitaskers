import matplotlib.pyplot as plt
import csv

# Ruta al archivo de resultados
ARCHIVO_RESULTADOS = "/home/mateod/Documents/resultados.csv"  # Ajusta la ruta al archivo CSV

# Inicialización de listas para almacenar los datos
frecuencias = []
tiempos_enteros = []
tiempos_flotantes = []

# Leer el archivo de resultados
try:
    with open(ARCHIVO_RESULTADOS, "r") as archivo:
        lector = csv.reader(archivo)
        
        # Saltar encabezado
        next(lector)

        # Leer cada fila de datos
        for fila in lector:
            if len(fila) == 3:  # Asegurarse de que cada fila tenga los 3 valores necesarios
                frecuencia = int(fila[0])  # Frecuencia
                tiempo_enteros = int(fila[1])  # Tiempo en la suma de enteros
                tiempo_flotantes = int(fila[2])  # Tiempo en la suma de flotantes

                # Almacenar los datos
                frecuencias.append(frecuencia)
                tiempos_enteros.append(tiempo_enteros)
                tiempos_flotantes.append(tiempo_flotantes)
except FileNotFoundError:
    print(f"❌ El archivo {ARCHIVO_RESULTADOS} no se encuentra.")
except Exception as e:
    print(f"❌ Error al leer el archivo: {e}")

# Crear gráficos para los datos
plt.figure(figsize=(10, 6))

# Gráfico para la suma de enteros
plt.subplot(2, 1, 1)  # Subplot (2 filas, 1 columna, gráfico 1)
plt.plot(frecuencias, tiempos_enteros, marker='o', linestyle='-', color='b', label='Suma Enteros')
plt.title('Tiempo de Suma de Enteros vs Frecuencia de CPU')
plt.xlabel('Frecuencia (MHz)')
plt.ylabel('Tiempo (ms)')
plt.grid(True)
plt.legend()

# Gráfico para la suma de flotantes
plt.subplot(2, 1, 2)  # Subplot (2 filas, 1 columna, gráfico 2)
plt.plot(frecuencias, tiempos_flotantes, marker='o', linestyle='-', color='r', label='Suma Flotantes')
plt.title('Tiempo de Suma de Flotantes vs Frecuencia de CPU')
plt.xlabel('Frecuencia (MHz)')
plt.ylabel('Tiempo (ms)')
plt.grid(True)
plt.legend()

# Ajustar la disposición para que los gráficos no se solapen
plt.tight_layout()


