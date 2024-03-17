# to handle application's termination and exit status
import sys
# to connect signals with methods that need to take extra args 
from functools import partial

# import PyQt6 components
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
    QApplication,
    QGridLayout,
    QLineEdit,
    QMainWindow,
    QPushButton,
    QVBoxLayout,
    QWidget,
)

WINDOW_SIZE = 250
DISPLAY_HEIGHT = 45
BUTTON_SIZE = 45
ERROR_MESSAGE = "ERROR. TRY AGAIN."

# if command-line arguments are needed, then use sys.argv to handle them instead
args = []

class CalculatorWindow(QMainWindow):
	"""The main window for the calculator (View)"""
	def __init__(self):
		super().__init__()
		self.setWindowTitle("Calculator")
		self.setFixedSize(WINDOW_SIZE, WINDOW_SIZE)
		self.generalLayout = QVBoxLayout()
		centralWidget = QWidget(self)
		centralWidget.setLayout(self.generalLayout)
		self.setCentralWidget(centralWidget)
		self._createDisplay()
		self._createButtons()
	def _createDisplay(self):
		self.display = QLineEdit()
		self.display.setFixedHeight(DISPLAY_HEIGHT)
		self.display.setAlignment(Qt.AlignmentFlag.AlignRight)
		self.display.setReadOnly(True)
		self.generalLayout.addWidget(self.display)
	def _createButtons(self):
		self.buttonMap = {}  # initialize a dictionary to hold the calculator buttons
		buttonsLayout = QGridLayout()
		keyBoard = [
			["7", "8", "9", "/", "C"], 
			["4", "5", "6", "*", "("], 
			["1", "2", "3", "-", ")"], 
			["0", "00", ".", "+", "="]
		]
		for row, keys in enumerate(keyBoard):
            		for col, key in enumerate(keys):
                		self.buttonMap[key] = QPushButton(key)
                		self.buttonMap[key].setFixedSize(BUTTON_SIZE, BUTTON_SIZE)
                		buttonsLayout.addWidget(self.buttonMap[key], row, col)

		self.generalLayout.addLayout(buttonsLayout)  # add grid layout into calculator's general layout
	def setDisplayText(self, text):
		"""set the current text"""
		self.display.setText(text)
		self.display.setFocus()  # set cursor's focus on the display
	def displayText(self):
		"""get the current text"""
		return self.display.text()
	def clearDisplay(self):
		"""clear the current text"""
		self.setDisplayText("") 
class CalculatorController:
	"""The calculator's controller for accessing the GUI, creating math expressions, and connecting the button clicks in the calculator"""
	def __init__(self, model, view):
		self._evaluate = model
		self._view = view
		self._connectSignalsAndSlots()
	
	def _calculateResult(self):
		result = self._evaluate(expression=self._view.displayText())
		self._view.setDisplayText(result)

	def _buildExpression(self, subExpression):
		if self._view.displayText() == ERROR_MESSAGE:
			self._view.clearDisplay()
		expression = self._view.displayText() + subExpression
		self._view.setDisplayText(expression)

	def _connectSignalsAndSlots(self):
		for keySymbol, button in self._view.buttonMap.items():
			if keySymbol not in {"=", "C"}:
				button.clicked.connect(
					partial(self._buildExpression, keySymbol)
				)
		self._view.buttonMap["="].clicked.connect(self._calculateResult)
		self._view.display.returnPressed.connect(self._calculateResult)
		self._view.buttonMap["C"].clicked.connect(self._view.clearDisplay)

def evaluateExpression(expression):
	"""Evaluate the result of the input expression (Model)"""
	try:
		result = str(eval(expression, {}, {}))
	except (SyntaxError, NameError, TypeError, ZeroDivisionError):
		result = ERROR_MESSAGE
	return result

def main():
	"""Calculator's main function"""
	calculatorApp = QApplication(args)  # create instance of QApplication
	calculatorWindow = CalculatorWindow()  # create window for the calculator
	calculatorWindow.show()
	CalculatorController(model=evaluateExpression, view=calculatorWindow)
	sys.exit(calculatorApp.exec())  # run application event loop

if __name__ == "__main__":
	main()