# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'asn8.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QGroupBox, QLabel,
    QLineEdit, QMainWindow, QMenuBar, QPushButton,
    QSizePolicy, QStatusBar, QWidget)

class Ui_root(object):
    def setupUi(self, root):
        if not root.objectName():
            root.setObjectName(u"root")
        root.setEnabled(True)
        root.resize(500, 300)
        self.centralwidget = QWidget(root)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.lblFrPerson = QGroupBox(self.centralwidget)
        self.lblFrPerson.setObjectName(u"lblFrPerson")
        self.gridLayout = QGridLayout(self.lblFrPerson)
        self.gridLayout.setObjectName(u"gridLayout")
        self.btnQ = QPushButton(self.lblFrPerson)
        self.btnQ.setObjectName(u"btnQ")

        self.gridLayout.addWidget(self.btnQ, 7, 1, 1, 1)

        self.lblPhone = QLabel(self.lblFrPerson)
        self.lblPhone.setObjectName(u"lblPhone")

        self.gridLayout.addWidget(self.lblPhone, 6, 1, 1, 1)

        self.entEmail = QLineEdit(self.lblFrPerson)
        self.entEmail.setObjectName(u"entEmail")

        self.gridLayout.addWidget(self.entEmail, 5, 4, 1, 1)

        self.entPhone = QLineEdit(self.lblFrPerson)
        self.entPhone.setObjectName(u"entPhone")

        self.gridLayout.addWidget(self.entPhone, 6, 4, 1, 1)

        self.lblEmail = QLabel(self.lblFrPerson)
        self.lblEmail.setObjectName(u"lblEmail")

        self.gridLayout.addWidget(self.lblEmail, 5, 1, 1, 1)

        self.lblFirst = QLabel(self.lblFrPerson)
        self.lblFirst.setObjectName(u"lblFirst")

        self.gridLayout.addWidget(self.lblFirst, 1, 1, 1, 1)

        self.entFirst = QLineEdit(self.lblFrPerson)
        self.entFirst.setObjectName(u"entFirst")

        self.gridLayout.addWidget(self.entFirst, 1, 4, 1, 1)

        self.entLast = QLineEdit(self.lblFrPerson)
        self.entLast.setObjectName(u"entLast")

        self.gridLayout.addWidget(self.entLast, 4, 4, 1, 1)

        self.lblLast = QLabel(self.lblFrPerson)
        self.lblLast.setObjectName(u"lblLast")

        self.gridLayout.addWidget(self.lblLast, 4, 1, 1, 1)

        self.btnR = QPushButton(self.lblFrPerson)
        self.btnR.setObjectName(u"btnR")

        self.gridLayout.addWidget(self.btnR, 7, 2, 1, 1)

        self.btnS = QPushButton(self.lblFrPerson)
        self.btnS.setObjectName(u"btnS")

        self.gridLayout.addWidget(self.btnS, 7, 4, 1, 1)


        self.gridLayout_2.addWidget(self.lblFrPerson, 1, 0, 1, 1)

        root.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(root)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 500, 33))
        root.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(root)
        self.statusbar.setObjectName(u"statusbar")
        root.setStatusBar(self.statusbar)

        self.retranslateUi(root)

        QMetaObject.connectSlotsByName(root)
    # setupUi

    def retranslateUi(self, root):
        root.setWindowTitle(QCoreApplication.translate("root", u"Form", None))
        self.lblFrPerson.setTitle(QCoreApplication.translate("root", u"Personal Information", None))
        self.btnQ.setText(QCoreApplication.translate("root", u"Quit", None))
        self.lblPhone.setText(QCoreApplication.translate("root", u"Phone Number", None))
        self.lblEmail.setText(QCoreApplication.translate("root", u"Email", None))
        self.lblFirst.setText(QCoreApplication.translate("root", u"*First Name", None))
        self.lblLast.setText(QCoreApplication.translate("root", u"*Last Name", None))
        self.btnR.setText(QCoreApplication.translate("root", u"Reset", None))
        self.btnS.setText(QCoreApplication.translate("root", u"Submit", None))
    # retranslateUi

