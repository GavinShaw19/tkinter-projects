# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'view.ui'
##
## Created by: Qt User Interface Compiler version 6.11.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QMainWindow,
    QMenuBar, QPushButton, QSizePolicy, QStatusBar,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.num1Input = QLineEdit(self.centralwidget)
        self.num1Input.setObjectName(u"num1Input")
        self.num1Input.setGeometry(QRect(60, 110, 113, 21))
        self.num2Input = QLineEdit(self.centralwidget)
        self.num2Input.setObjectName(u"num2Input")
        self.num2Input.setGeometry(QRect(60, 160, 113, 21))
        self.addButton = QPushButton(self.centralwidget)
        self.addButton.setObjectName(u"addButton")
        self.addButton.setGeometry(QRect(60, 200, 100, 32))
        self.subtractButton = QPushButton(self.centralwidget)
        self.subtractButton.setObjectName(u"subtractButton")
        self.subtractButton.setGeometry(QRect(160, 200, 100, 32))
        self.resultLabel = QLabel(self.centralwidget)
        self.resultLabel.setObjectName(u"resultLabel")
        self.resultLabel.setGeometry(QRect(60, 270, 151, 16))
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(60, 90, 111, 16))
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(60, 140, 111, 16))
        self.multiplyButton = QPushButton(self.centralwidget)
        self.multiplyButton.setObjectName(u"multiplyButton")
        self.multiplyButton.setGeometry(QRect(60, 230, 100, 32))
        self.divideButton = QPushButton(self.centralwidget)
        self.divideButton.setObjectName(u"divideButton")
        self.divideButton.setGeometry(QRect(160, 230, 100, 32))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 33))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.num1Input.setText("")
        self.num2Input.setText("")
        self.addButton.setText(QCoreApplication.translate("MainWindow", u"Add ", None))
        self.subtractButton.setText(QCoreApplication.translate("MainWindow", u"Subtract", None))
        self.resultLabel.setText(QCoreApplication.translate("MainWindow", u"Result: ", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"First Number", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Second Number", None))
        self.multiplyButton.setText(QCoreApplication.translate("MainWindow", u"Multiply", None))
        self.divideButton.setText(QCoreApplication.translate("MainWindow", u"Divide", None))
    # retranslateUi

