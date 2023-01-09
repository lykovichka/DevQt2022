# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'b_systeminfo_widget_ui.ui'
##
## Created by: Qt User Interface Compiler version 6.4.1
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLCDNumber, QLabel,
    QSizePolicy, QSlider, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(296, 259)
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.labelCPU = QLabel(Form)
        self.labelCPU.setObjectName(u"labelCPU")
        self.labelCPU.setMinimumSize(QSize(200, 25))
        self.labelCPU.setMaximumSize(QSize(200, 25))
        font = QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(True)
        self.labelCPU.setFont(font)

        self.horizontalLayout.addWidget(self.labelCPU)

        self.lcdNumberCPU = QLCDNumber(Form)
        self.lcdNumberCPU.setObjectName(u"lcdNumberCPU")
        self.lcdNumberCPU.setMinimumSize(QSize(60, 25))
        self.lcdNumberCPU.setMaximumSize(QSize(50, 25))
        font1 = QFont()
        font1.setPointSize(16)
        font1.setBold(True)
        font1.setItalic(True)
        self.lcdNumberCPU.setFont(font1)
        self.lcdNumberCPU.setSmallDecimalPoint(False)
        self.lcdNumberCPU.setSegmentStyle(QLCDNumber.Flat)
        self.lcdNumberCPU.setProperty("intValue", 0)

        self.horizontalLayout.addWidget(self.lcdNumberCPU)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.labelRAM = QLabel(Form)
        self.labelRAM.setObjectName(u"labelRAM")
        self.labelRAM.setMinimumSize(QSize(200, 25))
        self.labelRAM.setMaximumSize(QSize(200, 25))
        self.labelRAM.setFont(font)

        self.horizontalLayout_2.addWidget(self.labelRAM)

        self.lcdNumberCRAM = QLCDNumber(Form)
        self.lcdNumberCRAM.setObjectName(u"lcdNumberCRAM")
        self.lcdNumberCRAM.setMinimumSize(QSize(60, 25))
        self.lcdNumberCRAM.setMaximumSize(QSize(50, 25))
        self.lcdNumberCRAM.setSegmentStyle(QLCDNumber.Flat)

        self.horizontalLayout_2.addWidget(self.lcdNumberCRAM)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.labelCPU_2 = QLabel(Form)
        self.labelCPU_2.setObjectName(u"labelCPU_2")
        self.labelCPU_2.setMinimumSize(QSize(200, 25))
        self.labelCPU_2.setMaximumSize(QSize(200, 25))
        self.labelCPU_2.setFont(font)

        self.horizontalLayout_3.addWidget(self.labelCPU_2)

        self.lcdNumberDelay = QLCDNumber(Form)
        self.lcdNumberDelay.setObjectName(u"lcdNumberDelay")
        self.lcdNumberDelay.setMinimumSize(QSize(60, 25))
        self.lcdNumberDelay.setMaximumSize(QSize(50, 25))
        self.lcdNumberDelay.setFont(font1)
        self.lcdNumberDelay.setSegmentStyle(QLCDNumber.Flat)

        self.horizontalLayout_3.addWidget(self.lcdNumberDelay)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalSlider = QSlider(Form)
        self.horizontalSlider.setObjectName(u"horizontalSlider")
        self.horizontalSlider.setOrientation(Qt.Horizontal)

        self.verticalLayout.addWidget(self.horizontalSlider)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.labelCPU.setText(QCoreApplication.translate("Form", u"CPU", None))
        self.labelRAM.setText(QCoreApplication.translate("Form", u"RAM", None))
        self.labelCPU_2.setText(QCoreApplication.translate("Form", u"\u0412\u0440\u0435\u043c\u044f \u0437\u0430\u0434\u0435\u0440\u0436\u043a\u0438", None))
    # retranslateUi

