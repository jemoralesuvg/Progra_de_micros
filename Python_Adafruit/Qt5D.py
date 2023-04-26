from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QVBoxLayout, QWidget
from PyQt5.QtCore import QTimer
import serial

#Una clase que toma las propiedades QMainWindow
class MainWindow(QMainWindow):
    def __init__(self):         #Método de inicalización, con atributo self
        super().__init__()      
        self.setWindowTitle("Serial Port Test")
        self.setGeometry(100, 100, 400, 200)

        # Create the GUI elements
        self.input_textbox = QLineEdit()
        self.send_button = QPushButton("Send")
        self.sent_label = QLabel("")
        self.output_label = QLabel("")

        # Create a vertical layout and add the elements to it
        layout = QVBoxLayout()
        layout.addWidget(QLabel("Enter text to send:"))
        layout.addWidget(self.input_textbox)
        layout.addWidget(self.send_button)
        layout.addWidget(QLabel("Sent data:"))
        layout.addWidget(self.sent_label)
        layout.addWidget(QLabel("Received data:"))
        layout.addWidget(self.output_label)

        # Create a widget and set the layout on it
        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

        # Connect the send button to the on_send_button_clicked method
        self.send_button.clicked.connect(self.on_send_button_clicked)

        # Initialize the serial port to None
        self.serial_port = None

    def on_send_button_clicked(self):
        if self.serial_port:
            message = self.input_textbox.text().encode()
            self.serial_port.write(message)
            self.input_textbox.setText("")
            self.sent_label.setText(message.decode())

    def update_data(self):
        if self.serial_port and self.serial_port.in_waiting > 0:
            data = self.serial_port.readline()
            self.output_label.setText(data.decode())

    def connect_serial_port(self, port, baudrate):
        self.serial_port = serial.Serial(port, baudrate)
        self.statusBar().showMessage(f"Connected to {port} at {baudrate} baud")
        self.serial_port.flushInput()
        self.serial_port.flushOutput()

if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    window.show()
    timer = QTimer()
    timer.timeout.connect(window.update_data)
    timer.start(50)
    window.connect_serial_port('COM3', 9600)
    app.exec_()
