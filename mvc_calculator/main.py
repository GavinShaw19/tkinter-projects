import sys
from PySide6.QtWidgets import QApplication
from controller import CalculatorController

app = QApplication(sys.argv)

window = CalculatorController()
window.show()

sys.exit(app.exec())