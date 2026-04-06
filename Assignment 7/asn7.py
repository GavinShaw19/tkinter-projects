# converter.py
# Student: Gavin Shaw | Course: Graphic User Interface Dev. | Project: Assignment 7 (PySide6) |

import sys
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QLabel, QLineEdit, QPushButton,
    QRadioButton, QGroupBox, QVBoxLayout, QHBoxLayout, QGridLayout,
    QMessageBox, QFrame
)
from PySide6.QtGui import QPixmap, QFont
from PySide6.QtCore import Qt

INCH_TO_METER = 0.0254


class ConverterWindow(QMainWindow):
    """Main window for the measurement converter app."""

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Measurement Converter")
        self.setGeometry(200, 200, 800, 450)

        self.build_ui()
        self.wire_events()
        self.reset_form()

    def build_ui(self):
        """Build all widgets and layouts."""
        central = QWidget()
        self.setCentralWidget(central)

        # ----- Title -----
        self.lblTitle = QLabel("Converter App")
        self.lblTitle.setAlignment(Qt.AlignCenter)
        self.lblTitle.setFont(QFont("Arial", 22, QFont.Bold))

        self.lblInstructions = QLabel("Enter a value and choose conversion")
        self.lblInstructions.setAlignment(Qt.AlignCenter)
        self.lblInstructions.setFont(QFont("Arial", 14))

        # ----- Input -----
        self.txtInput = QLineEdit()
        self.txtInput.setPlaceholderText("Enter a number")
        self.txtInput.setAlignment(Qt.AlignCenter)
        self.txtInput.setFont(QFont("Arial", 14))
        self.txtInput.setFixedWidth(180)

        # ----- Radio Buttons -----
        self.grpConversion = QGroupBox("Convert Measurement")
        self.grpConversion.setFont(QFont("Arial", 13, QFont.Bold))

        self.rbInToM = QRadioButton("Inches to Meters")
        self.rbMToIn = QRadioButton("Meters to Inches")

        self.rbInToM.setFont(QFont("Arial", 12))
        self.rbMToIn.setFont(QFont("Arial", 12))

        radioLayout = QVBoxLayout()
        radioLayout.addWidget(self.rbInToM)
        radioLayout.addWidget(self.rbMToIn)
        self.grpConversion.setLayout(radioLayout)

        # ----- Result -----
        self.lblResult = QLabel("")
        self.lblResult.setAlignment(Qt.AlignCenter)
        self.lblResult.setFont(QFont("Arial", 16))
        self.lblResult.setWordWrap(True)
        self.lblResult.setMinimumHeight(60)

        # ----- Image -----
        self.imgFrame = QFrame()
        self.imgFrame.setFrameShape(QFrame.Box)
        self.imgFrame.setLineWidth(2)

        self.imgLabel = QLabel()
        self.imgLabel.setAlignment(Qt.AlignCenter)

        pix = QPixmap("house.png")
        self.imgLabel.setPixmap(
            pix.scaled(220, 220, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        )

        imgLayout = QVBoxLayout()
        imgLayout.addWidget(self.imgLabel)
        self.imgFrame.setLayout(imgLayout)

        # ----- Buttons -----
        self.btnConvert = QPushButton("Convert")
        self.btnClear = QPushButton("Clear")
        self.btnExit = QPushButton("Exit")

        self.btnConvert.setFont(QFont("Arial", 13))
        self.btnClear.setFont(QFont("Arial", 13))
        self.btnExit.setFont(QFont("Arial", 13))

        self.btnConvert.setMinimumHeight(45)
        self.btnClear.setMinimumHeight(45)
        self.btnExit.setMinimumHeight(45)

        # ----- Left Side Layout -----
        leftLayout = QVBoxLayout()
        leftLayout.addWidget(self.lblTitle)
        leftLayout.addWidget(self.lblInstructions, alignment=Qt.AlignCenter)
        leftLayout.addWidget(self.txtInput, alignment=Qt.AlignCenter)
        leftLayout.addWidget(self.grpConversion)
        leftLayout.addWidget(self.lblResult)

        buttonLayout = QHBoxLayout()
        buttonLayout.addWidget(self.btnConvert)
        buttonLayout.addWidget(self.btnClear)
        buttonLayout.addWidget(self.btnExit)

        leftLayout.addLayout(buttonLayout)

        # ----- Main Layout -----
        mainLayout = QHBoxLayout()
        mainLayout.addWidget(self.imgFrame)
        mainLayout.addLayout(leftLayout)

        central.setLayout(mainLayout)

        # ----- Styling -----
        self.setStyleSheet("""
            QMainWindow {
                background-color: #d8cff2;
            }

            QLabel {
                color: black;
            }

            QLineEdit {
                background-color: #5b008f;
                color: white;
                border: 2px solid white;
                padding: 8px;
            }

            QGroupBox {
                border: 2px solid white;
                border-radius: 8px;
                margin-top: 10px;
                padding: 10px;
                background-color: #5b008f;
                color: white;
            }

            QRadioButton {
                color: white;
                padding: 4px;
            }

            QPushButton {
                background-color: #e6ddff;
                border: 2px solid white;
                padding: 10px;
            }

            QPushButton:hover {
                background-color: #cdb8ff;
            }

            QFrame {
                background-color: white;
                padding: 10px;
            }
        """)

    def wire_events(self):
        """Connect buttons to functions."""
        self.btnConvert.clicked.connect(self.on_convert)
        self.btnClear.clicked.connect(self.on_clear)
        self.btnExit.clicked.connect(QApplication.instance().quit)

    def reset_form(self):
        """Reset the form to default settings."""
        self.txtInput.clear()
        self.lblResult.clear()
        self.rbInToM.setChecked(True)
        self.txtInput.setFocus()

    def show_error(self, message):
        """Show an error message box."""
        QMessageBox.critical(self, "Error", message)

    def on_clear(self):
        """Clear all input/output fields."""
        self.reset_form()

    def on_convert(self):
        """Validate input and perform the selected conversion."""
        text = self.txtInput.text().strip()

        if text == "":
            self.show_error("Please enter a value.")
            return

        try:
            value = float(text)
        except ValueError:
            self.show_error("Value entered is not numeric.")
            return

        if value <= 0:
            self.show_error("Converted value is negative.")
            return

        if self.rbInToM.isChecked():
            result = value * INCH_TO_METER
            self.lblResult.setText(f"{value:.3f} inches = {result:.3f} meters")
        else:
            result = value / INCH_TO_METER
            self.lblResult.setText(f"{value:.3f} meters = {result:.3f} inches")


def main():
    app = QApplication(sys.argv)
    window = ConverterWindow()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
