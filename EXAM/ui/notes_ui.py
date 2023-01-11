# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'notes_ui.ui'
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
from PySide6.QtWidgets import (QApplication, QDateTimeEdit, QGroupBox, QHBoxLayout,
    QHeaderView, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QTableWidget, QTableWidgetItem, QTextEdit,
    QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(728, 419)
        Form.setAutoFillBackground(False)
        Form.setStyleSheet(u"background-color: rgb(255, 253, 230);")
        self.verticalLayout_5 = QVBoxLayout(Form)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.groupBoxNewNote = QGroupBox(Form)
        self.groupBoxNewNote.setObjectName(u"groupBoxNewNote")
        font = QFont()
        font.setFamilies([u"Segoe Script"])
        font.setBold(True)
        self.groupBoxNewNote.setFont(font)
        self.verticalLayout = QVBoxLayout(self.groupBoxNewNote)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.groupBoxNewNote)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(100, 25))
        self.label.setMaximumSize(QSize(200, 25))
        self.label.setFont(font)

        self.horizontalLayout.addWidget(self.label)

        self.lineEdit = QLineEdit(self.groupBoxNewNote)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setMinimumSize(QSize(200, 25))
        self.lineEdit.setMaximumSize(QSize(200, 25))
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet(u"background-color: rgb(241, 238, 255);\n"
"background-color: rgb(255, 231, 239);")

        self.horizontalLayout.addWidget(self.lineEdit)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.textEdit = QTextEdit(self.groupBoxNewNote)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setFont(font)
        self.textEdit.setStyleSheet(u"background-color: rgb(255, 231, 239);")

        self.verticalLayout.addWidget(self.textEdit)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.labeDeadLine = QLabel(self.groupBoxNewNote)
        self.labeDeadLine.setObjectName(u"labeDeadLine")
        self.labeDeadLine.setMinimumSize(QSize(100, 25))
        self.labeDeadLine.setMaximumSize(QSize(250, 25))
        font1 = QFont()
        font1.setFamilies([u"Segoe Script"])
        font1.setBold(True)
        font1.setUnderline(False)
        self.labeDeadLine.setFont(font1)

        self.horizontalLayout_3.addWidget(self.labeDeadLine)

        self.dateTimeEdit = QDateTimeEdit(self.groupBoxNewNote)
        self.dateTimeEdit.setObjectName(u"dateTimeEdit")
        self.dateTimeEdit.setStyleSheet(u"background-color: rgb(239, 235, 255);")

        self.horizontalLayout_3.addWidget(self.dateTimeEdit)


        self.verticalLayout.addLayout(self.horizontalLayout_3)


        self.verticalLayout_4.addWidget(self.groupBoxNewNote)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.pushButtonCreate = QPushButton(Form)
        self.pushButtonCreate.setObjectName(u"pushButtonCreate")
        self.pushButtonCreate.setFont(font)
        self.pushButtonCreate.setAutoFillBackground(False)
        self.pushButtonCreate.setStyleSheet(u"background-color: rgb(238, 255, 254);\n"
"border-color: rgb(93, 101, 255);")

        self.horizontalLayout_5.addWidget(self.pushButtonCreate)

        self.pushButtonSave = QPushButton(Form)
        self.pushButtonSave.setObjectName(u"pushButtonSave")
        self.pushButtonSave.setFont(font)
        self.pushButtonSave.setStyleSheet(u"background-color: rgb(238, 255, 254);\n"
"border-color: rgb(93, 101, 255);")

        self.horizontalLayout_5.addWidget(self.pushButtonSave)


        self.verticalLayout_4.addLayout(self.horizontalLayout_5)


        self.horizontalLayout_6.addLayout(self.verticalLayout_4)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.groupBoxNotes = QGroupBox(Form)
        self.groupBoxNotes.setObjectName(u"groupBoxNotes")
        self.groupBoxNotes.setFont(font)
        self.verticalLayout_2 = QVBoxLayout(self.groupBoxNotes)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.tableWidget = QTableWidget(self.groupBoxNotes)
        if (self.tableWidget.columnCount() < 3):
            self.tableWidget.setColumnCount(3)
        font2 = QFont()
        font2.setFamilies([u"Segoe Script"])
        font2.setPointSize(8)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter);
        __qtablewidgetitem.setFont(font2);
        __qtablewidgetitem.setBackground(QColor(255, 253, 230));
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter);
        __qtablewidgetitem1.setFont(font2);
        __qtablewidgetitem1.setBackground(QColor(255, 253, 230));
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        __qtablewidgetitem2.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter);
        __qtablewidgetitem2.setFont(font2);
        __qtablewidgetitem2.setBackground(QColor(255, 253, 230));
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setEnabled(True)
        self.tableWidget.setMinimumSize(QSize(350, 0))
        self.tableWidget.setFont(font)
        self.tableWidget.setStyleSheet(u"background-color: rgb(230, 255, 217);")
        self.tableWidget.setDragEnabled(False)

        self.verticalLayout_2.addWidget(self.tableWidget)


        self.verticalLayout_3.addWidget(self.groupBoxNotes)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.pushButtonShow = QPushButton(Form)
        self.pushButtonShow.setObjectName(u"pushButtonShow")
        self.pushButtonShow.setFont(font)
        self.pushButtonShow.setStyleSheet(u"background-color: rgb(238, 255, 254);\n"
"border-color: rgb(93, 101, 255);")

        self.horizontalLayout_4.addWidget(self.pushButtonShow)

        self.pushButtonDelete = QPushButton(Form)
        self.pushButtonDelete.setObjectName(u"pushButtonDelete")
        self.pushButtonDelete.setFont(font)
        self.pushButtonDelete.setStyleSheet(u"background-color: rgb(238, 255, 254);\n"
"border-color: rgb(93, 101, 255);")

        self.horizontalLayout_4.addWidget(self.pushButtonDelete)


        self.verticalLayout_3.addLayout(self.horizontalLayout_4)


        self.horizontalLayout_6.addLayout(self.verticalLayout_3)


        self.verticalLayout_5.addLayout(self.horizontalLayout_6)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.groupBoxNewNote.setTitle(QCoreApplication.translate("Form", u"\u041d\u043e\u0432\u0430\u044f \u0437\u0430\u043c\u0435\u0442\u043a\u0430", None))
        self.label.setText(QCoreApplication.translate("Form", u"\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435", None))
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("Form", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u043d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u0437\u0430\u043c\u0435\u0442\u043a\u0438", None))
        self.textEdit.setPlaceholderText(QCoreApplication.translate("Form", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u0442\u0435\u043a\u0441\u0442 \u0437\u0430\u043c\u0435\u0442\u043a\u0438", None))
        self.labeDeadLine.setText(QCoreApplication.translate("Form", u"\u0421\u0440\u043e\u043a \u0432\u044b\u043f\u043e\u043b\u043d\u0435\u043d\u0438\u044f", None))
        self.pushButtonCreate.setText(QCoreApplication.translate("Form", u"\u0421\u043e\u0437\u0434\u0430\u0442\u044c", None))
        self.pushButtonSave.setText(QCoreApplication.translate("Form", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c", None))
        self.groupBoxNotes.setTitle(QCoreApplication.translate("Form", u"\u0417\u0430\u043c\u0435\u0442\u043a\u0438", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Form", u"\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Form", u"\u0414\u0430\u0442\u0430 \u0441\u043e\u0437\u0434\u0430\u043d\u0438\u044f", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Form", u"\u0421\u0440\u043e\u043a \u0432\u044b\u043f\u043e\u043b\u043d\u0435\u043d\u0438\u044f", None));
        self.pushButtonShow.setText(QCoreApplication.translate("Form", u"\u041f\u043e\u043a\u0430\u0437\u0430\u0442\u044c/\u0418\u0437\u043c\u0435\u043d\u0438\u0442\u044c", None))
        self.pushButtonDelete.setText(QCoreApplication.translate("Form", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c", None))
    # retranslateUi

