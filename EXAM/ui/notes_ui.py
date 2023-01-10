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
        Form.resize(885, 412)
        self.verticalLayout_3 = QVBoxLayout(Form)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
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

        self.horizontalLayout.addWidget(self.lineEdit)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.textEdit = QTextEdit(self.groupBoxNewNote)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setFont(font)

        self.verticalLayout.addWidget(self.textEdit)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.labeDeadLine = QLabel(self.groupBoxNewNote)
        self.labeDeadLine.setObjectName(u"labeDeadLine")
        self.labeDeadLine.setMinimumSize(QSize(100, 25))
        self.labeDeadLine.setMaximumSize(QSize(250, 25))

        self.horizontalLayout_3.addWidget(self.labeDeadLine)

        self.dateTimeEdit = QDateTimeEdit(self.groupBoxNewNote)
        self.dateTimeEdit.setObjectName(u"dateTimeEdit")

        self.horizontalLayout_3.addWidget(self.dateTimeEdit)


        self.verticalLayout.addLayout(self.horizontalLayout_3)


        self.horizontalLayout_4.addWidget(self.groupBoxNewNote)

        self.groupBoxNotes = QGroupBox(Form)
        self.groupBoxNotes.setObjectName(u"groupBoxNotes")
        self.groupBoxNotes.setFont(font)
        self.verticalLayout_2 = QVBoxLayout(self.groupBoxNotes)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.tableWidget = QTableWidget(self.groupBoxNotes)
        if (self.tableWidget.columnCount() < 3):
            self.tableWidget.setColumnCount(3)
        font1 = QFont()
        font1.setPointSize(8)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter);
        __qtablewidgetitem.setFont(font1);
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter);
        __qtablewidgetitem1.setFont(font1);
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        __qtablewidgetitem2.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter);
        __qtablewidgetitem2.setFont(font1);
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setMinimumSize(QSize(350, 0))
        self.tableWidget.setFont(font)
        self.tableWidget.setDragEnabled(False)

        self.verticalLayout_2.addWidget(self.tableWidget)


        self.horizontalLayout_4.addWidget(self.groupBoxNotes)


        self.verticalLayout_3.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.pushButtonCreate = QPushButton(Form)
        self.pushButtonCreate.setObjectName(u"pushButtonCreate")
        self.pushButtonCreate.setFont(font)

        self.horizontalLayout_2.addWidget(self.pushButtonCreate)

        self.pushButtonShow = QPushButton(Form)
        self.pushButtonShow.setObjectName(u"pushButtonShow")
        self.pushButtonShow.setFont(font)

        self.horizontalLayout_2.addWidget(self.pushButtonShow)

        self.pushButtonSave = QPushButton(Form)
        self.pushButtonSave.setObjectName(u"pushButtonSave")
        self.pushButtonSave.setFont(font)

        self.horizontalLayout_2.addWidget(self.pushButtonSave)

        self.pushButtonDelete = QPushButton(Form)
        self.pushButtonDelete.setObjectName(u"pushButtonDelete")
        self.pushButtonDelete.setFont(font)

        self.horizontalLayout_2.addWidget(self.pushButtonDelete)


        self.verticalLayout_3.addLayout(self.horizontalLayout_2)


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
        self.groupBoxNotes.setTitle(QCoreApplication.translate("Form", u"\u0417\u0430\u043c\u0435\u0442\u043a\u0438", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Form", u"\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Form", u"\u0414\u0430\u0442\u0430 \u0441\u043e\u0437\u0434\u0430\u043d\u0438\u044f", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Form", u"\u0421\u0440\u043e\u043a \u0432\u044b\u043f\u043e\u043b\u043d\u0435\u043d\u0438\u044f", None));
        self.pushButtonCreate.setText(QCoreApplication.translate("Form", u"\u0421\u043e\u0437\u0434\u0430\u0442\u044c", None))
        self.pushButtonShow.setText(QCoreApplication.translate("Form", u"\u041f\u043e\u043a\u0430\u0437\u0430\u0442\u044c", None))
        self.pushButtonSave.setText(QCoreApplication.translate("Form", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c", None))
        self.pushButtonDelete.setText(QCoreApplication.translate("Form", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c", None))
    # retranslateUi

