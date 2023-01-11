import datetime

from PySide6 import QtWidgets, QtCore, QtGui
from EXAM.ui.notes_ui import Ui_Form
import json


class Window(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.initJSON()

        self.initUi()
        self.initTableWidget()
        self.initSignals()


    def initUi(self) -> None:
        """ Доинициализация формы """

        self.setWindowTitle("Notes")

        self.ui.tableWidget.setColumnWidth(1, 155)
        self.ui.tableWidget.setColumnWidth(2, 155)



    def initSignals(self) -> None:
        """ Инициализация сигналов  """

        self.ui.dateTimeEdit.setDateTime(datetime.datetime.now())

        self.ui.pushButtonCreate.clicked.connect(self.buttonCreate)

        self.ui.pushButtonSave.clicked.connect(self.buttonSave)
        self.ui.pushButtonShow.clicked.connect(self.buttonShow)
        self.ui.pushButtonDelete.clicked.connect(self.buttonDelete)


    def initJSON(self) -> None:
        """ Инициализация JSON файла  """
        self.notes_dict = {}
        self.data = {"notes_dict": self.notes_dict}

        try:
            with open("saved_notes/data.json", "r", encoding="utf8") as data:
                self.data = json.load(data)
                # print(self.data)
                self.notes_dict = self.data["notes_dict"]

        except:
            with open("saved_notes/data.json", "w", encoding="utf8") as data:
                self.data = {"notes_dict": self.notes_dict}

                json.dump(self.data, data, indent=4)


    def initTableWidget(self) -> None:
        """ Функция заполнения таблицы
        заметками, которые были созданы ранее
        и хранятся в json"""

        count = len(self.data["notes_dict"])
        row = 0
        head = (list(self.data["notes_dict"].keys()))

        self.ui.tableWidget.setRowCount(count)

        for key in head:
            if head.index(key) == row:
                self.ui.tableWidget.setItem(row, 0, QtWidgets.QTableWidgetItem(self.notes_dict[key]["title"]))
                self.ui.tableWidget.setItem(row, 1, QtWidgets.QTableWidgetItem(self.notes_dict[key]["dateCreate"]))
                self.ui.tableWidget.setItem(row, 2, QtWidgets.QTableWidgetItem(self.notes_dict[key]["deadline"]))
                row += 1

        self.ui.tableWidget.sortByColumn(2, QtCore.Qt.SortOrder.DescendingOrder)
        #self.ui.tableWidget.setStyleSheet('QTableWidget.column {background-color: red; color: white}')



    def buttonCreate(self) -> None:
        """ Функция создания новой заметки """
        self.lastNumber = len(self.data["notes_dict"])
        print(self.lastNumber)

        # json
        datecreate = datetime.datetime.now()
        deadline = self.ui.dateTimeEdit.text()
        head = self.ui.lineEdit.text()

        self.notes_dict[head] = {"title": head, "dateCreate": str(datecreate.strftime("%d.%m.%Y %H:%M")),
                                 "text": self.ui.textEdit.toPlainText(), "deadline": deadline}

        with open("saved_notes/data.json", "w", encoding="utf8") as data:
            self.data = {"notes_dict": self.notes_dict}
            json.dump(self.data, data, indent=4)

        # tableWidget
        self.ui.tableWidget.insertRow(self.lastNumber)
        self.tableWidgetItem(self.lastNumber)


    def buttonDelete(self) -> None:
        """ Функция активации кнопки "Удалить" с последующим удалением заметки"""

        # tableWidget
        noteitem = []

        row = self.ui.tableWidget.currentRow()
        for i in range(self.ui.tableWidget.columnCount()):
            noteitem.append(self.ui.tableWidget.item(row, i).text())
        self.ui.tableWidget.removeRow(row)

        # json
        del self.notes_dict[noteitem[0]]
        with open("saved_notes/data.json", "w", encoding="utf8") as data:
            self.data = {"notes_dict": self.notes_dict}
            json.dump(self.data, data, indent=4)


    def buttonSave(self) -> None:
        """ Функция сохранения изменений в заметке """

        noteitem = []
        row = self.ui.tableWidget.currentRow()
        for i in range(self.ui.tableWidget.columnCount()):
            noteitem.append(self.ui.tableWidget.item(row, i).text())
        head = noteitem[0]

        # tableWidget
        self.ui.tableWidget.setItem(row, 2, QtWidgets.QTableWidgetItem(self.notes_dict[head]["deadline"]))

        # json
        self.notes_dict[head]["title"] = self.ui.lineEdit.text()
        self.notes_dict[head]["text"] = self.ui.textEdit.toPlainText()
        self.notes_dict[head]["deadline"] = self.ui.dateTimeEdit.text()

        with open("saved_notes/data.json", "w", encoding="utf8") as data:
            self.data = {"notes_dict": self.notes_dict}
            json.dump(self.data, data, indent=4)


    def buttonShow(self) -> None:
        """ Функция отображения текущей заметки в виджете"""

        # tableWidget
        noteitem = []

        row = self.ui.tableWidget.currentRow()
        for i in range(self.ui.tableWidget.columnCount()):
            noteitem.append(self.ui.tableWidget.item(row, i).text())

        # change lineEdit
        self.ui.lineEdit.setText(noteitem[0])

        # change textEdit
        key = noteitem[0]
        self.ui.textEdit.setText(self.notes_dict[key]["text"])

        # change dateTimeEdit Не получилось
        string_date = self.notes_dict[key]["deadline"]
        self.ui.dateTimeEdit.setDateTime(datetime.datetime.strptime(string_date, "%d.%m.%Y %H:%M"))


    def tableWidgetItem(self, ind) -> None:
        """ Функция заполнения таблицы заметок """

        head = self.ui.lineEdit.text()
        # ind = index - 1
        self.ui.tableWidget.setItem(ind, 0, QtWidgets.QTableWidgetItem(self.notes_dict[head]["title"]))
        self.ui.tableWidget.setItem(ind, 1, QtWidgets.QTableWidgetItem(self.notes_dict[head]["dateCreate"]))
        self.ui.tableWidget.setItem(ind, 2, QtWidgets.QTableWidgetItem(self.notes_dict[head]["deadline"]))



if __name__ == "__main__":
    app = QtWidgets.QApplication()

    window = Window()
    window.show()

    app.exec()
