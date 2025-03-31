import serial
import re

# Ruta del puerto serie (ajusta según tu sistema)
PUERTO_SERIAL = "/dev/ttyACM0"  # Linux
# PUERTO_SERIAL = "COM3"  # Windows

BAUDRATE = 115200
ARCHIVO_SALIDA = "/home/mateod/Documents/resultados.csv"  # Ruta del archivo CSV en Linux
# ARCHIVO_SALIDA = "C:/Users/TuUsuario/Documents/resultados.csv"  # Windows

# Expresión regular para detectar líneas correctas (números separados por comas)
patron_linea = re.compile(r"^\d+,\d+,\d+$")

try:
    with serial.Serial(PUERTO_SERIAL, BAUDRATE, timeout=2) as esp32, open(ARCHIVO_SALIDA, "w", newline="") as archivo:
        print("📡 Esperando el inicio de la prueba...")
        archivo.write("Frecuencia,Tiempo Enteros,Tiempo Flotantes\n")  # Encabezado CSV

        # Esperar a que aparezca "Iniciando pruebas de rendimiento..."
        while True:
            linea = esp32.readline().decode().strip()
            if "Iniciando pruebas de rendimiento" in linea:
                print("🚀 Prueba iniciada, comenzando captura de datos...")
                break  # Salimos del bucle y comenzamos a leer datos

        while True:
            linea = esp32.readline().decode().strip()

            # Si la línea contiene "Fin de la prueba", terminamos la captura
            if "Fin de la prueba" in linea:
                print("✅ Prueba terminada, guardando datos y cerrando...")
                break  # Salir del bucle

            # Ignorar líneas vacías o con caracteres basura
            if not linea or not patron_linea.match(linea):
                continue  

            print(linea)  # Mostrar en pantalla
            archivo.write(linea + "\n")  # Guardar en el archivo

except Exception as e:
    print("❌ Error:", e)

