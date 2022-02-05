from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from calculator import Ui_Window


class calculator(QMainWindow, Ui_Window):
	def __init__(self, *args, obj=None, **kwargs):
		super().__init__()
		self.setupUi(self)

		# Adding Functionality For Each Num Button
		self.numZero.clicked.connect(lambda: self.addToInput(0))
		self.numOne.clicked.connect(lambda: self.addToInput(1))
		self.numTwo.clicked.connect(lambda: self.addToInput(2))
		self.numThree.clicked.connect(lambda: self.addToInput(3))
		self.numFour.clicked.connect(lambda: self.addToInput(4))
		self.numFive.clicked.connect(lambda: self.addToInput(5))
		self.numSix.clicked.connect(lambda: self.addToInput(6))
		self.numSeven.clicked.connect(lambda: self.addToInput(7))
		self.numEight.clicked.connect(lambda: self.addToInput(8))
		self.numNine.clicked.connect(lambda: self.addToInput(9))

		# Add Funcionality To Delete Button
		self.delBtn.clicked.connect(self.delFromLast)

		self.show()

	def addToInput(self, num):
		self.inputField.setText(self.inputField.text() + str(num))

	def delFromLast(self):
		self.inputField.setText(self.inputField.text()[0:-1])

if __name__ == '__main__':
	app = QApplication([])
	app.setApplicationName("Calculator")
	a = calculator()
	app.exec_()