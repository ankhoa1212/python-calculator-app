# to handle application's termination and exit status
import sys

# import QApplication and all the required widgets
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget

WINDOW_SIZE = 250

# if command-line arguments are needed, then can use sys.argv to handle them instead
args = []

class CalculatorWindow(QMainWindow):
	"""The main window for the calculator (view)"""
	def __init__(self):
		super().__init__()
		self.setWindowTitle("Calculator")
		self.setFixedSize(WINDOW_SIZE, WINDOW_SIZE)
		centralWidget = QWidget(self)
		self.setCentralWidget(centralWidget)

def main():
	"""Calculator's main function"""
	calculatorApp = QApplication(args)  # create instance of QApplication
	calculatorWindow = CalculatorWindow()  # create window for the calculator
	calculatorWindow.show()
	sys.exit(calculatorApp.exec())  # run application event loop

if __name__ == "__main__":
	main()