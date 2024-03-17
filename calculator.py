# to handle application's termination and exit status
import sys

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
DISPLAY_HEIGHT = 50
BUTTON_SIZE = 40

# if command-line arguments are needed, then can use sys.argv to handle them instead
args = []

class CalculatorWindow(QMainWindow):
	"""The main window for the calculator (view)"""
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
		self.buttonMap = {}
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

		self.generalLayout.addLayout(buttonsLayout)


def main():
	"""Calculator's main function"""
	calculatorApp = QApplication(args)  # create instance of QApplication
	calculatorWindow = CalculatorWindow()  # create window for the calculator
	calculatorWindow.show()
	sys.exit(calculatorApp.exec())  # run application event loop

if __name__ == "__main__":
	main()