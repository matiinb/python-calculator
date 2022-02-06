from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from calculator import Ui_Window
import pyperclip
import keyboard

global tmpOperator
tmpOperator = ""
global tmpNum
tmpNum = 0
global clearInputField
clearInputField = False

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

		# Add Functionality To Period Button
		self.periodBtn.clicked.connect(lambda: self.addToInput("."))

		# Add Funcionality To Delete Button
		self.delBtn.clicked.connect(self.delFromLast)

		# Add Functionality To Clear Button
		self.clearBtn.clicked.connect(lambda: self.inputField.setText("0"))

		# Add Functionality To Operator Buttons
		self.divisionBtn.clicked.connect(lambda: self.calc("divide"))
		self.multiplyBtn.clicked.connect(lambda: self.calc("multiply"))
		self.subtractBtn.clicked.connect(lambda: self.calc("subtract"))
		self.additionBtn.clicked.connect(lambda: self.calc("addition"))
		self.equalBtn.clicked.connect(lambda: self.calc("equal"))

		# Negativity Toggle Button
		self.negPosBtn.clicked.connect(self.toggleNum)

		# Functionality of the copy button
		self.copyBtn.clicked.connect(lambda: pyperclip.copy(self.inputField.text()))

		# Hotkeys for each button
		keyboard.on_press_key("0", lambda _:self.numZero.click())
		keyboard.on_press_key("1", lambda _:self.numOne.click())
		keyboard.on_press_key("2", lambda _:self.numTwo.click())
		keyboard.on_press_key("3", lambda _:self.numThree.click())
		keyboard.on_press_key("4", lambda _:self.numFour.click())
		keyboard.on_press_key("5", lambda _:self.numFive.click())
		keyboard.on_press_key("6", lambda _:self.numSix.click())
		keyboard.on_press_key("7", lambda _:self.numSeven.click())
		keyboard.on_press_key("8", lambda _:self.numEight.click())
		keyboard.on_press_key("9", lambda _:self.numNine.click())
		keyboard.on_press_key("period", lambda _:self.periodBtn.click())

		keyboard.on_press_key("return", lambda _:self.equalBtn.click())
		keyboard.on_press_key("esc", lambda _:self.clearBtn.click())
		keyboard.on_press_key("delete", lambda _:self.delBtn.click())

		keyboard.on_press_key("/", lambda _:self.divisionBtn.click())
		keyboard.on_press_key("*", lambda _:self.multiplyBtn.click())
		keyboard.on_press_key("-", lambda _:self.subtractBtn.click())
		keyboard.on_press_key("+", lambda _:self.additionBtn.click())

		self.show()

	def toggleNum(self):
		self.inputField.setText(str(float(self.inputField.text()) * -1))

	def addToInput(self, num):
		global tmpOperator
		global clearInputField
		if tmpOperator != "":
			# Clear the input field when a previous operation is done
			if clearInputField:
				self.inputField.setText("0")
				clearInputField = False

		if num == 0 and self.inputField.text() == "0":
			return False
		if num == "." and "." in self.inputField.text():
			return False

		if self.inputField.text() == "0":
			self.inputField.setText("")

		self.inputField.setText(self.inputField.text() + str(num))

	def delFromLast(self):
		self.inputField.setText(self.inputField.text()[0:-1])

		if self.inputField.text() == "":
			self.inputField.setText("0")

	def setTmpVars(operation):
		global tmpOperator
		global tmpNum
		tmpNum = float(self.inputField.text())
		tmpOperator = operation
		self.inputField.setText("0")

	def findResult(self):
		global tmpOperator
		global tmpNum

		match tmpOperator:
			case "divide":
				if float(self.inputField.text()) == 0:
					self.inputField.setText("ERR")
				else:
					self.inputField.setText(str(tmpNum / float(self.inputField.text())))
			case "multiply":
				self.inputField.setText(str(tmpNum * float(self.inputField.text())))
			case "subtract":
				self.inputField.setText(str(tmpNum - float(self.inputField.text())))
			case "addition":
				self.inputField.setText(str(tmpNum + float(self.inputField.text())))

		tmpOperator = ""
		tmpNum = 0

	def calc(self, operation):
		global tmpOperator
		global tmpNum
		global clearInputField
		findEqual = False

		if tmpOperator != "":
			self.findResult()
		
		if tmpNum == ".":
			tmpNum = 0
		if self.inputField.text() == ".":
			self.inputField.setText("0")

		match operation:
			case "equal":
				self.findResult()
			case _:
				tmpNum = float(self.inputField.text())
				tmpOperator = operation
				clearInputField = True

if __name__ == '__main__':
	app = QApplication([])
	app.setApplicationName("Calculator")
	a = calculator()
	app.exec_()