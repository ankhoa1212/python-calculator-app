# to handle application's termination and exit status
import sys

# import QApplication and all the required widgets
from PyQt6.QtWidgets import QApplication, QLabel, QWidget, QPushButton

# import windows screen resolution (for Windows OS)
from win32api import GetSystemMetrics

# if command-line arguments are needed, then can use sys.argv to handle them instead
args = []

# create instance of QApplication
app = QApplication(args)

# create application's GUI
window = QWidget()
window.setWindowTitle("App")
window_width = GetSystemMetrics(0)
window_height = GetSystemMetrics(1)
window.setGeometry(0, 0, window_width, window_height)
helloMsg = QLabel("<h1>Hello, World!</h1>", parent=window)  # QLabel can display HTML formatted text
helloMsg.move(int(window_width / 2), int(window_height / 2))

button = QPushButton("OK", parent=window)
button.move(int(window_width / 2), int(window_height / 2) + int(window_height / 10))
# show the application
window.show()

# run application event loop
sys.exit(app.exec())
