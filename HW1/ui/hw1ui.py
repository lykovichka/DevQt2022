# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'hw1ui.ui'
##
## Created by: Qt User Interface Compiler version 6.4.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QAbstractButton, QApplication, QCalendarWidget, QCheckBox,
    QDialogButtonBox, QFrame, QGridLayout, QGroupBox,
    QHBoxLayout, QHeaderView, QLabel, QLineEdit,
    QMainWindow, QMenu, QMenuBar, QPlainTextEdit,
    QProgressBar, QPushButton, QRadioButton, QSizePolicy,
    QSlider, QSpacerItem, QStatusBar, QTabWidget,
    QTableWidget, QTableWidgetItem, QTextEdit, QToolBox,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1013, 705)
        MainWindow.setMinimumSize(QSize(924, 705))
        self.action = QAction(MainWindow)
        self.action.setObjectName(u"action")
        self.action_2 = QAction(MainWindow)
        self.action_2.setObjectName(u"action_2")
        self.action_3 = QAction(MainWindow)
        self.action_3.setObjectName(u"action_3")
        self.action_4 = QAction(MainWindow)
        self.action_4.setObjectName(u"action_4")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_43 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_43.setObjectName(u"verticalLayout_43")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.verticalLayout_42 = QVBoxLayout(self.tab)
        self.verticalLayout_42.setObjectName(u"verticalLayout_42")
        self.verticalLayout_41 = QVBoxLayout()
        self.verticalLayout_41.setObjectName(u"verticalLayout_41")
        self.horizontalLayout_68 = QHBoxLayout()
        self.horizontalLayout_68.setObjectName(u"horizontalLayout_68")
        self.verticalLayout_40 = QVBoxLayout()
        self.verticalLayout_40.setObjectName(u"verticalLayout_40")
        self.horizontalLayout_64 = QHBoxLayout()
        self.horizontalLayout_64.setObjectName(u"horizontalLayout_64")
        self.textEdit_29 = QTextEdit(self.tab)
        self.textEdit_29.setObjectName(u"textEdit_29")
        self.textEdit_29.setMinimumSize(QSize(200, 0))
        self.textEdit_29.setMaximumSize(QSize(200, 16777215))

        self.horizontalLayout_64.addWidget(self.textEdit_29)

        self.horizontalSpacer_12 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_64.addItem(self.horizontalSpacer_12)

        self.verticalLayout_37 = QVBoxLayout()
        self.verticalLayout_37.setObjectName(u"verticalLayout_37")
        self.radioButton = QRadioButton(self.tab)
        self.radioButton.setObjectName(u"radioButton")

        self.verticalLayout_37.addWidget(self.radioButton)

        self.radioButton_2 = QRadioButton(self.tab)
        self.radioButton_2.setObjectName(u"radioButton_2")

        self.verticalLayout_37.addWidget(self.radioButton_2)

        self.radioButton_3 = QRadioButton(self.tab)
        self.radioButton_3.setObjectName(u"radioButton_3")

        self.verticalLayout_37.addWidget(self.radioButton_3)

        self.radioButton_7 = QRadioButton(self.tab)
        self.radioButton_7.setObjectName(u"radioButton_7")

        self.verticalLayout_37.addWidget(self.radioButton_7)


        self.horizontalLayout_64.addLayout(self.verticalLayout_37)


        self.verticalLayout_40.addLayout(self.horizontalLayout_64)

        self.horizontalLayout_65 = QHBoxLayout()
        self.horizontalLayout_65.setObjectName(u"horizontalLayout_65")
        self.groupBox_24 = QGroupBox(self.tab)
        self.groupBox_24.setObjectName(u"groupBox_24")
        self.verticalLayout_39 = QVBoxLayout(self.groupBox_24)
        self.verticalLayout_39.setObjectName(u"verticalLayout_39")
        self.verticalLayout_38 = QVBoxLayout()
        self.verticalLayout_38.setObjectName(u"verticalLayout_38")
        self.checkBox_2 = QCheckBox(self.groupBox_24)
        self.checkBox_2.setObjectName(u"checkBox_2")

        self.verticalLayout_38.addWidget(self.checkBox_2)

        self.checkBox_3 = QCheckBox(self.groupBox_24)
        self.checkBox_3.setObjectName(u"checkBox_3")

        self.verticalLayout_38.addWidget(self.checkBox_3)

        self.checkBox_4 = QCheckBox(self.groupBox_24)
        self.checkBox_4.setObjectName(u"checkBox_4")

        self.verticalLayout_38.addWidget(self.checkBox_4)

        self.checkBox_5 = QCheckBox(self.groupBox_24)
        self.checkBox_5.setObjectName(u"checkBox_5")

        self.verticalLayout_38.addWidget(self.checkBox_5)


        self.verticalLayout_39.addLayout(self.verticalLayout_38)


        self.horizontalLayout_65.addWidget(self.groupBox_24)

        self.horizontalSpacer = QSpacerItem(170, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_65.addItem(self.horizontalSpacer)


        self.verticalLayout_40.addLayout(self.horizontalLayout_65)


        self.horizontalLayout_68.addLayout(self.verticalLayout_40)

        self.toolBox = QToolBox(self.tab)
        self.toolBox.setObjectName(u"toolBox")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.page.setGeometry(QRect(0, 0, 476, 414))
        self.verticalLayout_33 = QVBoxLayout(self.page)
        self.verticalLayout_33.setObjectName(u"verticalLayout_33")
        self.horizontalLayout_63 = QHBoxLayout()
        self.horizontalLayout_63.setObjectName(u"horizontalLayout_63")
        self.label = QLabel(self.page)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(150, 0))
        self.label.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout_63.addWidget(self.label)

        self.lineEdit = QLineEdit(self.page)
        self.lineEdit.setObjectName(u"lineEdit")

        self.horizontalLayout_63.addWidget(self.lineEdit)


        self.verticalLayout_33.addLayout(self.horizontalLayout_63)

        self.horizontalLayout_62 = QHBoxLayout()
        self.horizontalLayout_62.setObjectName(u"horizontalLayout_62")
        self.label_68 = QLabel(self.page)
        self.label_68.setObjectName(u"label_68")
        self.label_68.setMinimumSize(QSize(150, 0))
        self.label_68.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout_62.addWidget(self.label_68)

        self.lineEdit_2 = QLineEdit(self.page)
        self.lineEdit_2.setObjectName(u"lineEdit_2")

        self.horizontalLayout_62.addWidget(self.lineEdit_2)


        self.verticalLayout_33.addLayout(self.horizontalLayout_62)

        self.horizontalLayout_61 = QHBoxLayout()
        self.horizontalLayout_61.setObjectName(u"horizontalLayout_61")
        self.label_69 = QLabel(self.page)
        self.label_69.setObjectName(u"label_69")
        self.label_69.setMinimumSize(QSize(150, 0))
        self.label_69.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout_61.addWidget(self.label_69)

        self.lineEdit_3 = QLineEdit(self.page)
        self.lineEdit_3.setObjectName(u"lineEdit_3")

        self.horizontalLayout_61.addWidget(self.lineEdit_3)


        self.verticalLayout_33.addLayout(self.horizontalLayout_61)

        self.horizontalLayout_60 = QHBoxLayout()
        self.horizontalLayout_60.setObjectName(u"horizontalLayout_60")
        self.label_70 = QLabel(self.page)
        self.label_70.setObjectName(u"label_70")
        self.label_70.setMinimumSize(QSize(150, 0))
        self.label_70.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout_60.addWidget(self.label_70)

        self.lineEdit_4 = QLineEdit(self.page)
        self.lineEdit_4.setObjectName(u"lineEdit_4")

        self.horizontalLayout_60.addWidget(self.lineEdit_4)


        self.verticalLayout_33.addLayout(self.horizontalLayout_60)

        self.verticalSpacer = QSpacerItem(20, 257, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_33.addItem(self.verticalSpacer)

        self.toolBox.addItem(self.page, u"\u041a\u043e\u043d\u0442\u0430\u043a\u0442\u043d\u044b\u0435 \u0434\u0430\u043d\u043d\u044b\u0435 \u043a\u043e\u0441\u043c\u043e\u043d\u0430\u0432\u0442\u043e\u0432")
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.page_2.setGeometry(QRect(0, 0, 494, 422))
        self.verticalLayout_34 = QVBoxLayout(self.page_2)
        self.verticalLayout_34.setObjectName(u"verticalLayout_34")
        self.textEdit_28 = QTextEdit(self.page_2)
        self.textEdit_28.setObjectName(u"textEdit_28")

        self.verticalLayout_34.addWidget(self.textEdit_28)

        self.toolBox.addItem(self.page_2, u"\u0420\u0430\u0437\u0434\u0435\u043b \u043e \u0441\u0435\u0431\u0435")
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.verticalLayout_35 = QVBoxLayout(self.page_3)
        self.verticalLayout_35.setObjectName(u"verticalLayout_35")
        self.plainTextEdit = QPlainTextEdit(self.page_3)
        self.plainTextEdit.setObjectName(u"plainTextEdit")

        self.verticalLayout_35.addWidget(self.plainTextEdit)

        self.toolBox.addItem(self.page_3, u"\u0411\u043e\u0440\u0442\u043e\u0432\u0430\u044f \u0438\u043d\u0444\u043e\u0440\u043c\u0430\u0446\u0438\u044f")
        self.page_4 = QWidget()
        self.page_4.setObjectName(u"page_4")
        self.verticalLayout_36 = QVBoxLayout(self.page_4)
        self.verticalLayout_36.setObjectName(u"verticalLayout_36")
        self.calendarWidget = QCalendarWidget(self.page_4)
        self.calendarWidget.setObjectName(u"calendarWidget")

        self.verticalLayout_36.addWidget(self.calendarWidget)

        self.toolBox.addItem(self.page_4, u"\u041a\u0430\u043b\u0435\u043d\u0434\u0430\u0440\u044c")

        self.horizontalLayout_68.addWidget(self.toolBox)


        self.verticalLayout_41.addLayout(self.horizontalLayout_68)

        self.horizontalLayout_67 = QHBoxLayout()
        self.horizontalLayout_67.setObjectName(u"horizontalLayout_67")
        self.horizontalLayout_66 = QHBoxLayout()
        self.horizontalLayout_66.setObjectName(u"horizontalLayout_66")
        self.pushButton = QPushButton(self.tab)
        self.pushButton.setObjectName(u"pushButton")

        self.horizontalLayout_66.addWidget(self.pushButton)

        self.pushButton_14 = QPushButton(self.tab)
        self.pushButton_14.setObjectName(u"pushButton_14")

        self.horizontalLayout_66.addWidget(self.pushButton_14)


        self.horizontalLayout_67.addLayout(self.horizontalLayout_66)

        self.buttonBox = QDialogButtonBox(self.tab)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.horizontalLayout_67.addWidget(self.buttonBox)


        self.verticalLayout_41.addLayout(self.horizontalLayout_67)


        self.verticalLayout_42.addLayout(self.verticalLayout_41)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.verticalLayout_44 = QVBoxLayout(self.tab_2)
        self.verticalLayout_44.setObjectName(u"verticalLayout_44")
        self.groupBox = QGroupBox(self.tab_2)
        self.groupBox.setObjectName(u"groupBox")
        self.verticalLayout_21 = QVBoxLayout(self.groupBox)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.horizontalLayout_30 = QHBoxLayout()
        self.horizontalLayout_30.setObjectName(u"horizontalLayout_30")
        self.groupBox_9 = QGroupBox(self.groupBox)
        self.groupBox_9.setObjectName(u"groupBox_9")
        self.groupBox_9.setMaximumSize(QSize(16777215, 181))
        self.gridLayout_7 = QGridLayout(self.groupBox_9)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.label_44 = QLabel(self.groupBox_9)
        self.label_44.setObjectName(u"label_44")
        self.label_44.setMinimumSize(QSize(160, 0))

        self.horizontalLayout_12.addWidget(self.label_44)

        self.lineEdit_26 = QLineEdit(self.groupBox_9)
        self.lineEdit_26.setObjectName(u"lineEdit_26")
        self.lineEdit_26.setMinimumSize(QSize(85, 0))
        self.lineEdit_26.setMaximumSize(QSize(90, 22))

        self.horizontalLayout_12.addWidget(self.lineEdit_26)


        self.gridLayout_7.addLayout(self.horizontalLayout_12, 0, 0, 1, 1)

        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.label_45 = QLabel(self.groupBox_9)
        self.label_45.setObjectName(u"label_45")
        self.label_45.setMinimumSize(QSize(160, 0))

        self.horizontalLayout_13.addWidget(self.label_45)

        self.lineEdit_27 = QLineEdit(self.groupBox_9)
        self.lineEdit_27.setObjectName(u"lineEdit_27")
        self.lineEdit_27.setMinimumSize(QSize(85, 0))
        self.lineEdit_27.setMaximumSize(QSize(90, 22))

        self.horizontalLayout_13.addWidget(self.lineEdit_27)


        self.gridLayout_7.addLayout(self.horizontalLayout_13, 1, 0, 1, 1)

        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.label_46 = QLabel(self.groupBox_9)
        self.label_46.setObjectName(u"label_46")
        self.label_46.setMinimumSize(QSize(160, 0))

        self.horizontalLayout_14.addWidget(self.label_46)

        self.lineEdit_28 = QLineEdit(self.groupBox_9)
        self.lineEdit_28.setObjectName(u"lineEdit_28")
        self.lineEdit_28.setMinimumSize(QSize(85, 0))
        self.lineEdit_28.setMaximumSize(QSize(90, 22))

        self.horizontalLayout_14.addWidget(self.lineEdit_28)


        self.gridLayout_7.addLayout(self.horizontalLayout_14, 2, 0, 1, 1)

        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.label_47 = QLabel(self.groupBox_9)
        self.label_47.setObjectName(u"label_47")
        self.label_47.setMinimumSize(QSize(160, 0))

        self.horizontalLayout_15.addWidget(self.label_47)

        self.lineEdit_29 = QLineEdit(self.groupBox_9)
        self.lineEdit_29.setObjectName(u"lineEdit_29")
        self.lineEdit_29.setMinimumSize(QSize(85, 0))
        self.lineEdit_29.setMaximumSize(QSize(90, 16777215))

        self.horizontalLayout_15.addWidget(self.lineEdit_29)


        self.gridLayout_7.addLayout(self.horizontalLayout_15, 3, 0, 1, 1)

        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.label_48 = QLabel(self.groupBox_9)
        self.label_48.setObjectName(u"label_48")
        self.label_48.setMinimumSize(QSize(160, 0))

        self.horizontalLayout_16.addWidget(self.label_48)

        self.lineEdit_30 = QLineEdit(self.groupBox_9)
        self.lineEdit_30.setObjectName(u"lineEdit_30")
        self.lineEdit_30.setMinimumSize(QSize(85, 0))
        self.lineEdit_30.setMaximumSize(QSize(90, 22))

        self.horizontalLayout_16.addWidget(self.lineEdit_30)


        self.gridLayout_7.addLayout(self.horizontalLayout_16, 4, 0, 1, 1)


        self.horizontalLayout_30.addWidget(self.groupBox_9)

        self.groupBox_10 = QGroupBox(self.groupBox)
        self.groupBox_10.setObjectName(u"groupBox_10")
        self.groupBox_10.setMaximumSize(QSize(16777215, 181))
        self.gridLayout_8 = QGridLayout(self.groupBox_10)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.horizontalLayout_17 = QHBoxLayout()
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.label_24 = QLabel(self.groupBox_10)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setMinimumSize(QSize(120, 0))

        self.horizontalLayout_17.addWidget(self.label_24)

        self.textEdit_10 = QTextEdit(self.groupBox_10)
        self.textEdit_10.setObjectName(u"textEdit_10")
        self.textEdit_10.setMaximumSize(QSize(90, 22))
        self.textEdit_10.setFrameShape(QFrame.WinPanel)
        self.textEdit_10.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.textEdit_10.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.horizontalLayout_17.addWidget(self.textEdit_10)


        self.gridLayout_8.addLayout(self.horizontalLayout_17, 0, 0, 1, 1)

        self.horizontalLayout_18 = QHBoxLayout()
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.label_25 = QLabel(self.groupBox_10)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setMinimumSize(QSize(120, 0))

        self.horizontalLayout_18.addWidget(self.label_25)

        self.textEdit_11 = QTextEdit(self.groupBox_10)
        self.textEdit_11.setObjectName(u"textEdit_11")
        self.textEdit_11.setMaximumSize(QSize(90, 22))
        self.textEdit_11.setFrameShape(QFrame.WinPanel)
        self.textEdit_11.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.textEdit_11.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.horizontalLayout_18.addWidget(self.textEdit_11)


        self.gridLayout_8.addLayout(self.horizontalLayout_18, 1, 0, 1, 1)

        self.horizontalLayout_19 = QHBoxLayout()
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.label_26 = QLabel(self.groupBox_10)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setMinimumSize(QSize(120, 0))

        self.horizontalLayout_19.addWidget(self.label_26)

        self.textEdit_12 = QTextEdit(self.groupBox_10)
        self.textEdit_12.setObjectName(u"textEdit_12")
        self.textEdit_12.setMaximumSize(QSize(90, 22))
        self.textEdit_12.setFrameShape(QFrame.WinPanel)
        self.textEdit_12.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.textEdit_12.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.horizontalLayout_19.addWidget(self.textEdit_12)


        self.gridLayout_8.addLayout(self.horizontalLayout_19, 2, 0, 1, 1)

        self.horizontalLayout_20 = QHBoxLayout()
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.label_27 = QLabel(self.groupBox_10)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setMinimumSize(QSize(120, 0))

        self.horizontalLayout_20.addWidget(self.label_27)

        self.textEdit_13 = QTextEdit(self.groupBox_10)
        self.textEdit_13.setObjectName(u"textEdit_13")
        self.textEdit_13.setMaximumSize(QSize(90, 22))
        self.textEdit_13.setFrameShape(QFrame.WinPanel)
        self.textEdit_13.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.textEdit_13.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.horizontalLayout_20.addWidget(self.textEdit_13)


        self.gridLayout_8.addLayout(self.horizontalLayout_20, 3, 0, 1, 1)

        self.horizontalLayout_21 = QHBoxLayout()
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.label_28 = QLabel(self.groupBox_10)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setMinimumSize(QSize(120, 0))

        self.horizontalLayout_21.addWidget(self.label_28)

        self.textEdit_14 = QTextEdit(self.groupBox_10)
        self.textEdit_14.setObjectName(u"textEdit_14")
        self.textEdit_14.setMaximumSize(QSize(90, 22))
        self.textEdit_14.setFrameShape(QFrame.WinPanel)
        self.textEdit_14.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.textEdit_14.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.horizontalLayout_21.addWidget(self.textEdit_14)


        self.gridLayout_8.addLayout(self.horizontalLayout_21, 4, 0, 1, 1)


        self.horizontalLayout_30.addWidget(self.groupBox_10)

        self.groupBox_11 = QGroupBox(self.groupBox)
        self.groupBox_11.setObjectName(u"groupBox_11")
        self.groupBox_11.setMinimumSize(QSize(400, 0))
        self.groupBox_11.setMaximumSize(QSize(16777215, 181))
        self.horizontalLayout_31 = QHBoxLayout(self.groupBox_11)
        self.horizontalLayout_31.setObjectName(u"horizontalLayout_31")
        self.tableWidget_2 = QTableWidget(self.groupBox_11)
        if (self.tableWidget_2.columnCount() < 3):
            self.tableWidget_2.setColumnCount(3)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        if (self.tableWidget_2.rowCount() < 3):
            self.tableWidget_2.setRowCount(3)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(0, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(1, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(2, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget_2.setItem(0, 0, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableWidget_2.setItem(0, 1, __qtablewidgetitem7)
        brush = QBrush(QColor(0, 0, 0, 255))
        brush.setStyle(Qt.SolidPattern)
        brush1 = QBrush(QColor(0, 255, 127, 255))
        brush1.setStyle(Qt.SolidPattern)
        __qtablewidgetitem8 = QTableWidgetItem()
        __qtablewidgetitem8.setBackground(brush1);
        __qtablewidgetitem8.setForeground(brush);
        self.tableWidget_2.setItem(0, 2, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tableWidget_2.setItem(1, 0, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tableWidget_2.setItem(1, 1, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        __qtablewidgetitem11.setBackground(brush1);
        self.tableWidget_2.setItem(1, 2, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.tableWidget_2.setItem(2, 0, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.tableWidget_2.setItem(2, 1, __qtablewidgetitem13)
        brush2 = QBrush(QColor(255, 0, 0, 255))
        brush2.setStyle(Qt.SolidPattern)
        __qtablewidgetitem14 = QTableWidgetItem()
        __qtablewidgetitem14.setBackground(brush2);
        self.tableWidget_2.setItem(2, 2, __qtablewidgetitem14)
        self.tableWidget_2.setObjectName(u"tableWidget_2")
        self.tableWidget_2.setAlternatingRowColors(False)

        self.horizontalLayout_31.addWidget(self.tableWidget_2)


        self.horizontalLayout_30.addWidget(self.groupBox_11)


        self.verticalLayout_21.addLayout(self.horizontalLayout_30)

        self.horizontalLayout_32 = QHBoxLayout()
        self.horizontalLayout_32.setObjectName(u"horizontalLayout_32")
        self.verticalLayout_11 = QVBoxLayout()
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.groupBox_12 = QGroupBox(self.groupBox)
        self.groupBox_12.setObjectName(u"groupBox_12")
        self.gridLayout_9 = QGridLayout(self.groupBox_12)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.horizontalLayout_33 = QHBoxLayout()
        self.horizontalLayout_33.setObjectName(u"horizontalLayout_33")
        self.verticalLayout_12 = QVBoxLayout()
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalSlider_6 = QSlider(self.groupBox_12)
        self.verticalSlider_6.setObjectName(u"verticalSlider_6")
        self.verticalSlider_6.setMinimumSize(QSize(100, 0))
        self.verticalSlider_6.setOrientation(Qt.Vertical)

        self.verticalLayout_12.addWidget(self.verticalSlider_6)

        self.label_29 = QLabel(self.groupBox_12)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setMinimumSize(QSize(100, 0))

        self.verticalLayout_12.addWidget(self.label_29)


        self.horizontalLayout_33.addLayout(self.verticalLayout_12)

        self.verticalLayout_13 = QVBoxLayout()
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalSlider_7 = QSlider(self.groupBox_12)
        self.verticalSlider_7.setObjectName(u"verticalSlider_7")
        self.verticalSlider_7.setMinimumSize(QSize(100, 0))
        self.verticalSlider_7.setOrientation(Qt.Vertical)

        self.verticalLayout_13.addWidget(self.verticalSlider_7)

        self.label_30 = QLabel(self.groupBox_12)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setMinimumSize(QSize(100, 0))

        self.verticalLayout_13.addWidget(self.label_30)


        self.horizontalLayout_33.addLayout(self.verticalLayout_13)

        self.verticalLayout_14 = QVBoxLayout()
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalSlider_8 = QSlider(self.groupBox_12)
        self.verticalSlider_8.setObjectName(u"verticalSlider_8")
        self.verticalSlider_8.setMinimumSize(QSize(100, 0))
        self.verticalSlider_8.setOrientation(Qt.Vertical)

        self.verticalLayout_14.addWidget(self.verticalSlider_8)

        self.label_31 = QLabel(self.groupBox_12)
        self.label_31.setObjectName(u"label_31")

        self.verticalLayout_14.addWidget(self.label_31)


        self.horizontalLayout_33.addLayout(self.verticalLayout_14)

        self.verticalLayout_15 = QVBoxLayout()
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalSlider_9 = QSlider(self.groupBox_12)
        self.verticalSlider_9.setObjectName(u"verticalSlider_9")
        self.verticalSlider_9.setMinimumSize(QSize(100, 0))
        self.verticalSlider_9.setOrientation(Qt.Vertical)

        self.verticalLayout_15.addWidget(self.verticalSlider_9)

        self.label_32 = QLabel(self.groupBox_12)
        self.label_32.setObjectName(u"label_32")
        self.label_32.setMinimumSize(QSize(100, 0))

        self.verticalLayout_15.addWidget(self.label_32)


        self.horizontalLayout_33.addLayout(self.verticalLayout_15)

        self.horizontalSpacer_6 = QSpacerItem(100, 20, QSizePolicy.Ignored, QSizePolicy.Minimum)

        self.horizontalLayout_33.addItem(self.horizontalSpacer_6)

        self.verticalLayout_16 = QVBoxLayout()
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalSlider_10 = QSlider(self.groupBox_12)
        self.verticalSlider_10.setObjectName(u"verticalSlider_10")
        self.verticalSlider_10.setMinimumSize(QSize(100, 0))
        self.verticalSlider_10.setOrientation(Qt.Vertical)

        self.verticalLayout_16.addWidget(self.verticalSlider_10)

        self.label_33 = QLabel(self.groupBox_12)
        self.label_33.setObjectName(u"label_33")
        self.label_33.setMinimumSize(QSize(100, 0))

        self.verticalLayout_16.addWidget(self.label_33)


        self.horizontalLayout_33.addLayout(self.verticalLayout_16)


        self.gridLayout_9.addLayout(self.horizontalLayout_33, 1, 0, 1, 1)

        self.groupBox_13 = QGroupBox(self.groupBox_12)
        self.groupBox_13.setObjectName(u"groupBox_13")
        self.groupBox_13.setMaximumSize(QSize(16777215, 185))
        self.gridLayout_10 = QGridLayout(self.groupBox_13)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.horizontalLayout_34 = QHBoxLayout()
        self.horizontalLayout_34.setObjectName(u"horizontalLayout_34")
        self.label_6 = QLabel(self.groupBox_13)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout_34.addWidget(self.label_6)

        self.textEdit_15 = QTextEdit(self.groupBox_13)
        self.textEdit_15.setObjectName(u"textEdit_15")
        self.textEdit_15.setMaximumSize(QSize(16777215, 22))

        self.horizontalLayout_34.addWidget(self.textEdit_15)


        self.gridLayout_10.addLayout(self.horizontalLayout_34, 0, 0, 1, 1)

        self.horizontalLayout_35 = QHBoxLayout()
        self.horizontalLayout_35.setObjectName(u"horizontalLayout_35")
        self.label_7 = QLabel(self.groupBox_13)
        self.label_7.setObjectName(u"label_7")

        self.horizontalLayout_35.addWidget(self.label_7)

        self.textEdit_16 = QTextEdit(self.groupBox_13)
        self.textEdit_16.setObjectName(u"textEdit_16")
        self.textEdit_16.setMaximumSize(QSize(16777215, 22))

        self.horizontalLayout_35.addWidget(self.textEdit_16)


        self.gridLayout_10.addLayout(self.horizontalLayout_35, 1, 0, 1, 1)

        self.horizontalLayout_36 = QHBoxLayout()
        self.horizontalLayout_36.setObjectName(u"horizontalLayout_36")
        self.label_8 = QLabel(self.groupBox_13)
        self.label_8.setObjectName(u"label_8")

        self.horizontalLayout_36.addWidget(self.label_8)

        self.textEdit_17 = QTextEdit(self.groupBox_13)
        self.textEdit_17.setObjectName(u"textEdit_17")
        self.textEdit_17.setMaximumSize(QSize(16777215, 22))

        self.horizontalLayout_36.addWidget(self.textEdit_17)


        self.gridLayout_10.addLayout(self.horizontalLayout_36, 2, 0, 1, 1)

        self.horizontalLayout_37 = QHBoxLayout()
        self.horizontalLayout_37.setObjectName(u"horizontalLayout_37")
        self.label_9 = QLabel(self.groupBox_13)
        self.label_9.setObjectName(u"label_9")

        self.horizontalLayout_37.addWidget(self.label_9)

        self.textEdit_18 = QTextEdit(self.groupBox_13)
        self.textEdit_18.setObjectName(u"textEdit_18")
        self.textEdit_18.setMaximumSize(QSize(16777215, 22))

        self.horizontalLayout_37.addWidget(self.textEdit_18)


        self.gridLayout_10.addLayout(self.horizontalLayout_37, 3, 0, 1, 1)


        self.gridLayout_9.addWidget(self.groupBox_13, 0, 0, 1, 1)


        self.verticalLayout_11.addWidget(self.groupBox_12)


        self.horizontalLayout_32.addLayout(self.verticalLayout_11)

        self.verticalLayout_17 = QVBoxLayout()
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.groupBox_14 = QGroupBox(self.groupBox)
        self.groupBox_14.setObjectName(u"groupBox_14")
        self.gridLayout_11 = QGridLayout(self.groupBox_14)
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.verticalLayout_18 = QVBoxLayout()
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.progressBar_7 = QProgressBar(self.groupBox_14)
        self.progressBar_7.setObjectName(u"progressBar_7")
        self.progressBar_7.setMinimumSize(QSize(80, 0))
        self.progressBar_7.setMaximumSize(QSize(80, 16777215))
        self.progressBar_7.setValue(100)
        self.progressBar_7.setOrientation(Qt.Vertical)

        self.verticalLayout_18.addWidget(self.progressBar_7)

        self.label_34 = QLabel(self.groupBox_14)
        self.label_34.setObjectName(u"label_34")
        self.label_34.setMinimumSize(QSize(80, 0))

        self.verticalLayout_18.addWidget(self.label_34)


        self.gridLayout_11.addLayout(self.verticalLayout_18, 0, 2, 1, 1)

        self.verticalLayout_19 = QVBoxLayout()
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.progressBar_8 = QProgressBar(self.groupBox_14)
        self.progressBar_8.setObjectName(u"progressBar_8")
        self.progressBar_8.setMinimumSize(QSize(80, 0))
        self.progressBar_8.setValue(75)
        self.progressBar_8.setOrientation(Qt.Vertical)

        self.verticalLayout_19.addWidget(self.progressBar_8)

        self.label_35 = QLabel(self.groupBox_14)
        self.label_35.setObjectName(u"label_35")
        self.label_35.setMinimumSize(QSize(80, 0))

        self.verticalLayout_19.addWidget(self.label_35)


        self.gridLayout_11.addLayout(self.verticalLayout_19, 0, 1, 1, 1)

        self.verticalLayout_20 = QVBoxLayout()
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.progressBar_9 = QProgressBar(self.groupBox_14)
        self.progressBar_9.setObjectName(u"progressBar_9")
        self.progressBar_9.setMinimumSize(QSize(80, 0))
        self.progressBar_9.setValue(35)
        self.progressBar_9.setOrientation(Qt.Vertical)

        self.verticalLayout_20.addWidget(self.progressBar_9)

        self.label_36 = QLabel(self.groupBox_14)
        self.label_36.setObjectName(u"label_36")
        self.label_36.setMinimumSize(QSize(80, 0))

        self.verticalLayout_20.addWidget(self.label_36)


        self.gridLayout_11.addLayout(self.verticalLayout_20, 0, 0, 1, 1)


        self.verticalLayout_17.addWidget(self.groupBox_14)

        self.groupBox_15 = QGroupBox(self.groupBox)
        self.groupBox_15.setObjectName(u"groupBox_15")
        self.gridLayout_12 = QGridLayout(self.groupBox_15)
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.horizontalSpacer_7 = QSpacerItem(83, 17, QSizePolicy.Ignored, QSizePolicy.Minimum)

        self.gridLayout_12.addItem(self.horizontalSpacer_7, 0, 0, 1, 1)

        self.pushButton_6 = QPushButton(self.groupBox_15)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setMinimumSize(QSize(75, 75))
        self.pushButton_6.setMaximumSize(QSize(75, 75))
        font = QFont()
        font.setPointSize(28)
        self.pushButton_6.setFont(font)

        self.gridLayout_12.addWidget(self.pushButton_6, 0, 1, 1, 1)

        self.horizontalSpacer_8 = QSpacerItem(82, 17, QSizePolicy.Ignored, QSizePolicy.Minimum)

        self.gridLayout_12.addItem(self.horizontalSpacer_8, 0, 2, 1, 1)

        self.horizontalLayout_38 = QHBoxLayout()
        self.horizontalLayout_38.setObjectName(u"horizontalLayout_38")
        self.pushButton_7 = QPushButton(self.groupBox_15)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setMinimumSize(QSize(75, 75))
        self.pushButton_7.setMaximumSize(QSize(75, 75))
        self.pushButton_7.setFont(font)

        self.horizontalLayout_38.addWidget(self.pushButton_7)

        self.pushButton_8 = QPushButton(self.groupBox_15)
        self.pushButton_8.setObjectName(u"pushButton_8")
        self.pushButton_8.setMinimumSize(QSize(75, 75))
        self.pushButton_8.setMaximumSize(QSize(75, 75))
        self.pushButton_8.setFont(font)

        self.horizontalLayout_38.addWidget(self.pushButton_8)

        self.pushButton_9 = QPushButton(self.groupBox_15)
        self.pushButton_9.setObjectName(u"pushButton_9")
        self.pushButton_9.setMinimumSize(QSize(75, 75))
        self.pushButton_9.setMaximumSize(QSize(75, 75))
        self.pushButton_9.setFont(font)
        self.pushButton_9.setText(u"\u2192")

        self.horizontalLayout_38.addWidget(self.pushButton_9)


        self.gridLayout_12.addLayout(self.horizontalLayout_38, 1, 0, 1, 3)


        self.verticalLayout_17.addWidget(self.groupBox_15)


        self.horizontalLayout_32.addLayout(self.verticalLayout_17)


        self.verticalLayout_21.addLayout(self.horizontalLayout_32)


        self.verticalLayout_44.addWidget(self.groupBox)

        self.tabWidget.addTab(self.tab_2, "")

        self.verticalLayout_43.addWidget(self.tabWidget)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menuBar = QMenuBar(MainWindow)
        self.menuBar.setObjectName(u"menuBar")
        self.menuBar.setGeometry(QRect(0, 0, 1013, 26))
        self.menu = QMenu(self.menuBar)
        self.menu.setObjectName(u"menu")
        self.menuHelp = QMenu(self.menuBar)
        self.menuHelp.setObjectName(u"menuHelp")
        MainWindow.setMenuBar(self.menuBar)

        self.menuBar.addAction(self.menu.menuAction())
        self.menuBar.addAction(self.menuHelp.menuAction())
        self.menu.addAction(self.action)
        self.menu.addAction(self.action_2)
        self.menu.addAction(self.action_3)
        self.menuHelp.addAction(self.action_4)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(1)
        self.toolBox.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.action.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u043a\u0440\u044b\u0442\u044c", None))
        self.action_2.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u043a\u0440\u044b\u0442\u044c \u0432", None))
        self.action_3.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u043a\u0440\u044b\u0442\u044c", None))
        self.action_4.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0438\u043a\u0442\u043e \u043d\u0430\u043c \u0443\u0436\u0435 \u043d\u0435 \u043f\u043e\u043c\u043e\u0436\u0435\u0442", None))
        self.textEdit_29.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u0417\u0434\u0435\u0441\u044c \u0434\u043e\u043b\u0436\u0435\u043d \u0431\u044b\u0442\u044c \u043a\u0430\u043a\u043e\u0439-\u0442\u043e \u0442\u0435\u043a\u0441\u0442</p></body></html>", None))
        self.textEdit_29.setPlaceholderText("")
        self.radioButton.setText(QCoreApplication.translate("MainWindow", u"\u041a\u043d\u043e\u043f\u043a\u0430 1", None))
        self.radioButton_2.setText(QCoreApplication.translate("MainWindow", u"\u041a\u043d\u043e\u043f\u043a\u0430 2", None))
        self.radioButton_3.setText(QCoreApplication.translate("MainWindow", u"\u041a\u043d\u043e\u043f\u043a\u0430 3", None))
        self.radioButton_7.setText(QCoreApplication.translate("MainWindow", u"\u041a\u043d\u043e\u043f\u043a\u0430 4", None))
        self.groupBox_24.setTitle(QCoreApplication.translate("MainWindow", u"GroupBox for CheckBox", None))
        self.checkBox_2.setText(QCoreApplication.translate("MainWindow", u"CheckBox", None))
        self.checkBox_3.setText(QCoreApplication.translate("MainWindow", u"CheckBox", None))
        self.checkBox_4.setText(QCoreApplication.translate("MainWindow", u"CheckBox", None))
        self.checkBox_5.setText(QCoreApplication.translate("MainWindow", u"CheckBox", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u0424\u0430\u043c\u0438\u043b\u0438\u044f", None))
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u0444\u0430\u043c\u0438\u043b\u0438\u044e \u043a\u043e\u0441\u043c\u043e\u043d\u0430\u0432\u0442\u0430", None))
        self.label_68.setText(QCoreApplication.translate("MainWindow", u"\u0418\u043c\u044f", None))
        self.lineEdit_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u0438\u043c\u044f \u043a\u043e\u0441\u043c\u043e\u043d\u0430\u0432\u0442\u0430", None))
        self.label_69.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u0447\u0435\u0441\u0442\u0432\u043e", None))
        self.lineEdit_3.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u043e\u0442\u0447\u0435\u0441\u0442\u0432\u043e \u043a\u043e\u0441\u043c\u043e\u043d\u0430\u0432\u0442\u0430", None))
        self.label_70.setText(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u043d\u0442\u0430\u043a\u0442\u043d\u044b\u0439 \u0442\u0435\u043b\u0435\u0444\u043e\u043d", None))
        self.lineEdit_4.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u043d\u043e\u043c\u0435\u0440 \u0442\u0435\u043b\u0435\u0444\u043e\u043d\u0430", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page), QCoreApplication.translate("MainWindow", u"\u041a\u043e\u043d\u0442\u0430\u043a\u0442\u043d\u044b\u0435 \u0434\u0430\u043d\u043d\u044b\u0435 \u043a\u043e\u0441\u043c\u043e\u043d\u0430\u0432\u0442\u043e\u0432", None))
        self.textEdit_28.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.textEdit_28.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u043f\u043e\u043b\u043d\u0438\u0442\u0435 \u0434\u043e\u043f\u043e\u043b\u043d\u0438\u0442\u0435\u043b\u044c\u043d\u0443\u044e \u0438\u043d\u0444\u043e\u0440\u043c\u0430\u0446\u0438\u044e \u043e \u0441\u043e\u0442\u0440\u0443\u0434\u043d\u0438\u043a\u0435", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_2), QCoreApplication.translate("MainWindow", u"\u0420\u0430\u0437\u0434\u0435\u043b \u043e \u0441\u0435\u0431\u0435", None))
        self.plainTextEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u0438\u043d\u0444\u043e\u0440\u043c\u0430\u0446\u0438\u044e \u043e \u0434\u0432\u0438\u0433\u0430\u0442\u0435\u043b\u044f\u0445, \u0437\u0430\u043f\u043e\u043b\u043d\u0435\u043d\u043d\u043e\u0441\u0442\u0438 \u0431\u0430\u043a\u043e\u0432, \u0442\u0435\u043c\u043f\u0435\u0440\u0430\u0442\u0443\u0440\u044b \u043d\u0430 \u0431\u043e\u0440\u0442\u0443 \u0438 \u0442.\u0434.", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_3), QCoreApplication.translate("MainWindow", u"\u0411\u043e\u0440\u0442\u043e\u0432\u0430\u044f \u0438\u043d\u0444\u043e\u0440\u043c\u0430\u0446\u0438\u044f", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_4), QCoreApplication.translate("MainWindow", u"\u041a\u0430\u043b\u0435\u043d\u0434\u0430\u0440\u044c", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0436\u043c\u0438 \u043d\u0430 \u043c\u0435\u043d\u044f!", None))
        self.pushButton_14.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0435\u0442, \u043d\u0430\u0436\u043c\u0438 \u043d\u0430 \u043c\u0435\u043d\u044f!", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"\u0420\u0430\u0437\u0434\u0435\u043b1", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u043d\u0441\u043e\u043b\u044c \u0443\u043f\u0440\u0430\u0432\u043b\u0435\u043d\u0438\u044f", None))
        self.groupBox_9.setTitle(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u043e\u0440\u0434\u0438\u043d\u0430\u0442\u044b", None))
        self.label_44.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0441\u043e\u0442\u0430 \u043e\u0440\u0431\u0438\u0442\u044b", None))
        self.lineEdit_26.setText(QCoreApplication.translate("MainWindow", u"20000 \u043a\u043c", None))
        self.label_45.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043a\u043e\u0440\u043e\u0441\u0442\u044c \u0432\u0440\u0430\u0449\u0435\u043d\u0438\u044f", None))
        self.lineEdit_27.setText(QCoreApplication.translate("MainWindow", u"7\u04318 \u043c/\u0441", None))
        self.label_46.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043a\u043e\u0440\u043e\u0441\u0442\u044c \u041a\u0410", None))
        self.lineEdit_28.setText(QCoreApplication.translate("MainWindow", u"500 \u043a\u043c/\u0447", None))
        self.label_47.setText(QCoreApplication.translate("MainWindow", u"\u0428\u0438\u0440\u043e\u0442\u0430", None))
        self.lineEdit_29.setText(QCoreApplication.translate("MainWindow", u"43", None))
        self.label_48.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u043b\u0433\u043e\u0442\u0430", None))
        self.lineEdit_30.setText(QCoreApplication.translate("MainWindow", u"76", None))
        self.groupBox_10.setTitle(QCoreApplication.translate("MainWindow", u"\u041f\u0430\u0440\u0430\u043c\u0435\u0442\u0440\u044b \u043a\u043e\u0440\u0430\u0431\u043b\u044f", None))
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"\u0422\u0435\u043c\u043f\u0435\u0440\u0430\u0442\u0443\u0440\u0430 \u043d\u0430 \u0431\u043e\u0440\u0442\u0443", None))
        self.textEdit_10.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt; font-weight:600; color:#ffaa00;\">25 \u0421</span></p></body></html>", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0430\u0437\u0433\u0435\u0440\u043c\u0435\u0442\u0438\u0437\u0430\u0446\u0438\u044f", None))
        self.textEdit_11.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:7pt; font-weight:600; color:#00ff00;\">\u041e\u0442\u0441\u0443\u0442\u0441\u0442\u0432\u0443\u0435\u0442</span></p></body></html>", None))
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"\u0411\u0430\u043a \u21161", None))
        self.textEdit_12.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; color:#ffaa00;\">34%</span></p></body></html>", None))
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"\u0411\u0430\u043a \u21162", None))
        self.textEdit_13.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; color:#00ff00;\">75%</span></p></body></html>", None))
        self.label_28.setText(QCoreApplication.translate("MainWindow", u"\u0411\u0430\u043a \u21163", None))
        self.textEdit_14.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; color:#00ff00;\">100%</span></p></body></html>", None))
        self.groupBox_11.setTitle(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0441\u0442\u043e\u044f\u043d\u0438\u0435 \u043a\u043e\u0441\u043c\u043e\u043d\u0430\u0432\u0442\u043e\u0432", None))
        ___qtablewidgetitem = self.tableWidget_2.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"\u0422\u0435\u043c\u043f\u0435\u0440\u0430\u0442\u0443\u0440\u0430", None));
        ___qtablewidgetitem1 = self.tableWidget_2.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0430\u0432\u043b\u0435\u043d\u0438\u0435", None));
        ___qtablewidgetitem2 = self.tableWidget_2.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0442\u0440\u0435\u0441\u0441", None));
        ___qtablewidgetitem3 = self.tableWidget_2.verticalHeaderItem(0)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u0441\u043c\u043e\u043d\u0430\u0432\u0442 1", None));
        ___qtablewidgetitem4 = self.tableWidget_2.verticalHeaderItem(1)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u0441\u043c\u043e\u043d\u0430\u0432\u0442 2", None));
        ___qtablewidgetitem5 = self.tableWidget_2.verticalHeaderItem(2)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u0441\u043c\u043e\u043d\u0430\u0432\u0442 3", None));

        __sortingEnabled = self.tableWidget_2.isSortingEnabled()
        self.tableWidget_2.setSortingEnabled(False)
        ___qtablewidgetitem6 = self.tableWidget_2.item(0, 0)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"36,6", None));
        ___qtablewidgetitem7 = self.tableWidget_2.item(0, 1)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"140/70", None));
        ___qtablewidgetitem8 = self.tableWidget_2.item(0, 2)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"\u041d\u043e\u0440\u043c\u0430", None));
        ___qtablewidgetitem9 = self.tableWidget_2.item(1, 0)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"36,8", None));
        ___qtablewidgetitem10 = self.tableWidget_2.item(1, 1)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"120/60", None));
        ___qtablewidgetitem11 = self.tableWidget_2.item(1, 2)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"\u041d\u043e\u0440\u043c\u0430", None));
        ___qtablewidgetitem12 = self.tableWidget_2.item(2, 0)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"36,5", None));
        ___qtablewidgetitem13 = self.tableWidget_2.item(2, 1)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"170/100", None));
        ___qtablewidgetitem14 = self.tableWidget_2.item(2, 2)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"\u0410\u0445\u0442\u0443\u043d\u0433", None));
        self.tableWidget_2.setSortingEnabled(__sortingEnabled)

        self.groupBox_12.setTitle(QCoreApplication.translate("MainWindow", u"\u0423\u043f\u0440\u0430\u0432\u043b\u0435\u043d\u0438\u0435 \u043e\u0441\u043d\u043e\u0432\u043d\u044b\u043c\u0438 \u0434\u0432\u0438\u0433\u0430\u0442\u0435\u043b\u044f\u043c\u0438", None))
        self.label_29.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0432\u0438\u0433\u0430\u0442\u0435\u043b\u044c \u21161", None))
        self.label_30.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0432\u0438\u0433\u0430\u0442\u0435\u043b\u044c \u21162", None))
        self.label_31.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0432\u0438\u0433\u0430\u0442\u0435\u043b\u044c \u21163", None))
        self.label_32.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0432\u0438\u0433\u0430\u0442\u0435\u043b\u044c \u21164", None))
        self.label_33.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0431\u0449\u0430\u044f \u0442\u044f\u0433\u0430", None))
        self.groupBox_13.setTitle(QCoreApplication.translate("MainWindow", u"\u041f\u0430\u0440\u0430\u043c\u0435\u0442\u0440\u044b \u0434\u0432\u0438\u0433\u0430\u0442\u0435\u043b\u0435\u0439", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0432\u0438\u0433\u0430\u0442\u0435\u043b\u044c \u21161", None))
        self.textEdit_15.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:7pt; font-weight:600; color:#aa0000;\">\u0421\u043a\u043e\u0440\u043e \u0432\u0437\u043e\u0440\u0432\u0435\u0442\u0441\u044f</span></p></body></html>", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0432\u0438\u0433\u0430\u0442\u0435\u043b\u044c \u21162", None))
        self.textEdit_16.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:7pt; font-weight:600; color:#00ff00;\">\u041d\u043e\u0440\u043c\u0430</span></p></body></html>", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0432\u0438\u0433\u0430\u0442\u0435\u043b\u044c \u21163", None))
        self.textEdit_17.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:7pt; font-weight:600; color:#aaaa00;\">\u0412\u043d\u0438\u043c\u0430\u043d\u0438\u0435</span></p></body></html>", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0432\u0438\u0433\u0430\u0442\u0435\u043b\u044c \u21164", None))
        self.textEdit_18.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:7pt; font-weight:600; color:#00ff00;\">\u041d\u043e\u0440\u043c\u0430</span></p></body></html>", None))
        self.groupBox_14.setTitle(QCoreApplication.translate("MainWindow", u"\u0422\u043e\u043f\u043b\u0438\u0432\u043e", None))
        self.label_34.setText(QCoreApplication.translate("MainWindow", u"\u0411\u0430\u043a \u21163", None))
        self.label_35.setText(QCoreApplication.translate("MainWindow", u"\u0411\u0430\u043a \u21162", None))
        self.label_36.setText(QCoreApplication.translate("MainWindow", u"\u0411\u0430\u043a \u21161", None))
        self.groupBox_15.setTitle(QCoreApplication.translate("MainWindow", u"\u0423\u043f\u0440\u0430\u0432\u043b\u0435\u043d\u0438\u0435 \u043c\u0430\u043d\u0435\u0432\u0440\u043e\u0432\u044b\u043c\u0438 \u0434\u0432\u0438\u0433\u0430\u0442\u0435\u043b\u044f\u043c\u0438", None))
        self.pushButton_6.setText(QCoreApplication.translate("MainWindow", u"\u2191", None))
        self.pushButton_7.setText(QCoreApplication.translate("MainWindow", u"\u2190", None))
        self.pushButton_8.setText(QCoreApplication.translate("MainWindow", u"\u2193", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"\u0420\u0430\u0437\u0434\u0435\u043b 2", None))
        self.menu.setTitle(QCoreApplication.translate("MainWindow", u"\u041c\u0435\u043d\u044e", None))
        self.menuHelp.setTitle(QCoreApplication.translate("MainWindow", u"Help", None))
    # retranslateUi

