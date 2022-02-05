from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from calculator import Ui_Window

class calculator(QMainWindow, Ui_Window):
	def __init__(self, *args, obj=None, **kwargs):
		super().__init__()
		self.setupUi(self)
		self.show()

if __name__ == '__main__':
	app = QApplication([])
	app.setApplicationName("Calculator")
	a = calculator()
	app.exec_()