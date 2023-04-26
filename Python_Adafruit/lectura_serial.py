import serial
import time

# Configuración del puerto serial
ser = serial.Serial('COM3', 9600)

# Establecer tiempo de inicio
start_time = time.time()
ser.timeout = 1
#ser.write(b'Hola mundo!')

# Ciclo para leer datos del puerto serial durante 10 segundos
while time.time() - start_time < 5:
    # Leer una línea de datos del puerto serial
    data = ser.read().decode().strip()
    # Imprimir los datos recibidos
    print(data)

# Cerrar el puerto serial
ser.close()

#D:\Gits\Micros\Progra_de_micros\Python_Adafruit>python ejemplo_serial.py