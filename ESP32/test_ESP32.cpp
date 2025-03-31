#include <Arduino.h>
#include "esp_system.h"

void sumaEnteros();
void sumaFlotantes();

void sumaEnteros() {
  volatile uint32_t total = 0;
  for (uint32_t i = 0; i < 333333; i++) {
      total += i;
  }
}

void sumaFlotantes() {
  volatile float total = 0.0;
  for (uint32_t i = 0; i < 240000; i++) {
      total += i;
  }
}

void ejecutarPrueba(int frecuencia) {
    if (frecuencia == 240 || frecuencia == 160 || frecuencia == 80 || frecuencia == 40 || frecuencia == 20 || frecuencia == 10) {
        Serial.flush();  // Limpiar el buffer serial
        delay(100);
        setCpuFrequencyMhz(frecuencia);  
        delay(500);  
        
        Serial.end();  // Reiniciar comunicación serie
        delay(500);
        Serial.begin(115200);
        delay(500);
    } else {
        Serial.println("Frecuencia no válida");
        return;
    }

    Serial.print("\nFrecuencia actual: ");
    Serial.print(getCpuFrequencyMhz());
    Serial.println(" MHz");

    uint32_t start_time = millis();
    sumaEnteros();
    uint32_t tiempo_enteros = millis() - start_time;

    start_time = millis();
    sumaFlotantes();
    uint32_t tiempo_flotantes = millis() - start_time;

    Serial.print("Tiempo suma enteros (ms): ");
    Serial.println(tiempo_enteros);

    Serial.print("Tiempo suma flotantes (ms): ");
    Serial.println(tiempo_flotantes);
}

void setup() {
    Serial.begin(115200);
    delay(2000);  
    Serial.println("\nIniciando pruebas de rendimiento...");

    ejecutarPrueba(240);
    ejecutarPrueba(160);
    ejecutarPrueba(80);
    ejecutarPrueba(40);
    ejecutarPrueba(20);
    ejecutarPrueba(10);

    Serial.println("\nFin de la prueba.");

     
    Serial.end();  // Cerrar la comunicación serial al final
}

void loop() {
}
