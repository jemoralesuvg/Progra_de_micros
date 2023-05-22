import tkinter as tk
import serial
import threading

# Se crea la ventana principal
root = tk.Tk()
root.title("Interfaz serial")

# Se crea un cuadro de entrada para escribir los datos que se enviarán
entry = tk.Entry(root)
entry.pack()

# Se crea un cuadro de texto para mostrar los datos recibidos
text = tk.Text(root)
text.pack()

# Se configura el puerto serial
ser = None

# Función para enviar los datos
def send_data():
	# Se obtienen los datos del cuadro de entrada
	data = entry.get()
	# Se escriben los datos al puerto serial
	ser.write(data.encode())
	print ("dato enviado")

# Función para recibir los datos
def receive_data():
# Mientras se esté ejecutando el hilo
	while True:
		# Se lee una línea del puerto serial seleccionado
		line = ser.read()
		
		# Se decodifica la línea y se muestra en el cuadro de texto
		text.insert('end', line.decode())
			
			
# Función para iniciar el hilo de recepción
def start_receive_thread():
    global ser
    # Se configura el puerto serial
    ser = serial.Serial('COM3', 9600, timeout=1)
    # Se inicia el hilo de recepción
    thread = threading.Thread(target=receive_data)
    thread.daemon = True
    thread.start()

# Se crea el botón de conexión
connect_button = tk.Button(root, text="Conectar", command=start_receive_thread)
connect_button.pack()

# Se crea el botón de enviar
send_button = tk.Button(root, text="Enviar", command=send_data)
send_button.pack()

# Se inicia el bucle principal de la GUI
root.mainloop()
