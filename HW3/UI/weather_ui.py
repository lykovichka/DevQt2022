# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'c_weatherapi_widget_ui.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QLineEdit,
    QPlainTextEdit, QPushButton, QSizePolicy, QSpacerItem,
    QSpinBox, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(421, 327)
        self.verticalLayout_3 = QVBoxLayout(Form)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.labelLatitude = QLabel(Form)
        self.labelLatitude.setObjectName(u"labelLatitude")
        self.labelLatitude.setMaximumSize(QSize(100, 20))
        font = QFont()
        font.setFamilies([u"Brush Script MT"])
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(True)
        self.labelLatitude.setFont(font)

        self.verticalLayout.addWidget(self.labelLatitude)

        self.lineEditLatitude = QLineEdit(Form)
        self.lineEditLatitude.setObjectName(u"lineEditLatitude")
        self.lineEditLatitude.setMinimumSize(QSize(100, 20))
        self.lineEditLatitude.setMaximumSize(QSize(100, 20))

        self.verticalLayout.addWidget(self.lineEditLatitude)


        self.horizontalLayout_2.addLayout(self.verticalLayout)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.labelLongitude = QLabel(Form)
        self.labelLongitude.setObjectName(u"labelLongitude")
        self.labelLongitude.setMaximumSize(QSize(100, 20))
        self.labelLongitude.setFont(font)

        self.verticalLayout_2.addWidget(self.labelLongitude)

        self.lineEditLongitude = QLineEdit(Form)
        self.lineEditLongitude.setObjectName(u"lineEditLongitude")
        self.lineEditLongitude.setMinimumSize(QSize(100, 20))
        self.lineEditLongitude.setMaximumSize(QSize(100, 20))

        self.verticalLayout_2.addWidget(self.lineEditLongitude)


        self.horizontalLayout_2.addLayout(self.verticalLayout_2)


        self.verticalLayout_3.addLayout(self.horizontalLayout_2)

        self.verticalSpacer = QSpacerItem(20, 6, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.pushButton = QPushButton(Form)
        self.pushButton.setObjectName(u"pushButton")
        font1 = QFont()
        font1.setFamilies([u"Brush Script MT"])
        font1.setPointSize(12)
        font1.setItalic(True)
        self.pushButton.setFont(font1)

        self.horizontalLayout.addWidget(self.pushButton)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)


        self.verticalLayout_3.addLayout(self.horizontalLayout)

        self.plainTextEdit = QPlainTextEdit(Form)
        self.plainTextEdit.setObjectName(u"plainTextEdit")

        self.verticalLayout_3.addWidget(self.plainTextEdit)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")

        self.horizontalLayout_3.addWidget(self.label)

        self.spinBox = QSpinBox(Form)
        self.spinBox.setObjectName(u"spinBox")

        self.horizontalLayout_3.addWidget(self.spinBox)


        self.verticalLayout_3.addLayout(self.horizontalLayout_3)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.labelLatitude.setText(QCoreApplication.translate("Form", u"\u0428\u0438\u0440\u043e\u0442\u0430", None))
        self.lineEditLatitude.setPlaceholderText(QCoreApplication.translate("Form", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u0448\u0438\u0440\u043e\u0442\u0443", None))
        self.labelLongitude.setText(QCoreApplication.translate("Form", u"\u0414\u043e\u043b\u0433\u043e\u0442\u0430", None))
        self.lineEditLongitude.setPlaceholderText(QCoreApplication.translate("Form", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u0434\u043e\u043b\u0433\u043e\u0442\u0443", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"\u0423\u0437\u043d\u0430\u0435\u043c \u043f\u043e\u0433\u043e\u0434\u0443!", None))
        self.label.setText(QCoreApplication.translate("Form", u"\u0412\u0440\u0435\u043c\u044f \u0437\u0430\u0434\u0435\u0440\u0436\u043a\u0438", None))
    # retranslateUi

