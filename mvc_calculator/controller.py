from PySide6.QtWidgets import QMainWindow
from view import Ui_MainWindow
from model import CalculatorModel


class CalculatorController(QMainWindow):

    def __init__(self):
        super().__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.model = CalculatorModel()

        self.ui.addButton.clicked.connect(self.add_numbers)
        self.ui.subtractButton.clicked.connect(self.subtract_numbers)
        self.ui.multiplyButton.clicked.connect(self.multiply_numbers)
        self.ui.divideButton.clicked.connect(self.divide_numbers)

    def get_numbers(self):
        num1 = float(self.ui.num1Input.text())
        num2 = float(self.ui.num2Input.text())

        return num1, num2

    def add_numbers(self):
        try:
            num1, num2 = self.get_numbers()

            result = self.model.add(num1, num2)

            self.ui.resultLabel.setText(f"Result: {result}")

        except ValueError:
            self.ui.resultLabel.setText("Invalid input")

    def subtract_numbers(self):
        try:
            num1, num2 = self.get_numbers()

            result = self.model.subtract(num1, num2)

            self.ui.resultLabel.setText(f"Result: {result}")

        except ValueError:
            self.ui.resultLabel.setText("Invalid input")

    def multiply_numbers(self):
        try:
            num1, num2 = self.get_numbers()

            result = self.model.multiply(num1, num2)

            self.ui.resultLabel.setText(f"Result: {result}")

        except ValueError:
            self.ui.resultLabel.setText("Invalid input")

    def divide_numbers(self):
        try:
            num1, num2 = self.get_numbers()

            result = self.model.divide(num1, num2)

            self.ui.resultLabel.setText(f"Result: {result}")

        except ValueError:
            self.ui.resultLabel.setText("Invalid input")