import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox
from asn8_ui import Ui_root

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_root()
        self.ui.setupUi(self)

        self.ui.btnS.clicked.connect(self.submit)
        self.ui.btnR.clicked.connect(self.reset)
        self.ui.btnQ.clicked.connect(self.close)

    def submit(self):
        first = self.ui.entFirst.text()
        last = self.ui.entLast.text()
        email = self.ui.entEmail.text()
        phone = self.ui.entPhone.text()

        if first == "" or last == "":
            QMessageBox.warning(self, "Error", "First and Last name required.")
        else:
            QMessageBox.information(
                self,
                "Submitted",
                f"First Name: {first}\nLast Name: {last}\nEmail: {email}\nPhone: {phone}"
            )

    def reset(self):
        self.ui.entFirst.clear()
        self.ui.entLast.clear()
        self.ui.entEmail.clear()
        self.ui.entPhone.clear()

app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec())
