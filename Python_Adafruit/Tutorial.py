from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys

def push():
	print("Btn presionado")

def window():
	app = QApplication(sys.argv)
	win = QMainWindow()
	win.setGeometry(300,300,300,400) #posx, posy, ancho, alto
	win.setWindowTitle("Pruba")

	label = QtWidgets.QLabel(win)
	label.setText("Bienvenidos a Micros")
	label.move(100,150)

	btn1 = QtWidgets.QPushButton(win)
	btn1.setText("Push")
	btn1.move(100,175)
	btn1.clicked.connect(push)


	win.show()
	sys.exit(app.exec_())
window()
