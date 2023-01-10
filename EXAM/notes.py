import datetime


from PySide6 import QtWidgets, QtCore
from EXAM.ui.notes_ui import Ui_Form
import json


class Window(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.initJSON()

        self.initUi()
        self.initSignals()

        # settings = QtCore.QSettings('sets.ini', QtCore.QSettings.format())
        # settings.setValue("Key", "Value")


    def initUi(self):

        self.setWindowTitle("Notes")

        self.ui.tableWidget.setColumnWidth(1, 155)
        self.ui.tableWidget.setColumnWidth(2,155)



    def initJSON(self):

        self.unsaved = False
        self.notes_dict = {}
        self.lastNumber = 0


        self.data = {"notes_dict": self.notes_dict}

        try:
            with open("saved_notes/data.json", "r", encoding="utf8") as data:
                self.data = json.load(data)
                self.notes_dict = self.data["notes_dict"]

            for i in range(len(self.notes_dict.keys())):
                self.ui.tableWidget.setItem(i, 0, QtWidgets.QTableWidgetItem(self.notes_dict[i]["title"]))
                self.ui.tableWidget.setItem(i, 1, QtWidgets.QTableWidgetItem(self.notes_dict[i]["dateCreate"]))
                self.ui.tableWidget.setItem(i, 2, QtWidgets.QTableWidgetItem(self.notes_dict[i]["deadline"]))




        except:
            with open("saved_notes/data.json", "w", encoding="utf8") as data:
                self.data = {"notes_dict": self.notes_dict}

                json.dump(self.data, data, indent=4)





    def initSignals(self):

        self.ui.dateTimeEdit.setDateTime(datetime.datetime.now())

        self.ui.pushButtonCreate.clicked.connect(self.buttonCreate)

        self.ui.pushButtonSave.clicked.connect(self.buttonSave)
        self.ui.pushButtonShow.clicked.connect(self.buttonShow)
        self.ui.pushButtonDelete.clicked.connect(self.buttonDelete)



    def buttonCreate(self):
        """ Функция создания новой заметки """
        self.lastNumber += 1

        # json
        datecreate = datetime.datetime.now()
        deadline = self.ui.dateTimeEdit.text()
        head = self.ui.lineEdit.text()

        self.notes_dict[head] = {"title": head,"dateCreate": str(datecreate.strftime("%d.%m.%Y %H:%M")),
                                "text": self.ui.textEdit.toPlainText(), "deadline": deadline}

        with open("saved_notes/data.json", "a", encoding="utf8") as data:
            self.data = {"notes_dict": self.notes_dict}
            json.dump(self.notes_dict, data, indent=4)


        # tableWidget

        self.ui.tableWidget.setRowCount(self.lastNumber)
        self.tableWidgetItem(self.lastNumber)




    def tableWidgetItem(self, index):
        """ Функция заполнения таблицы заметок """

        head = self.ui.lineEdit.text()
        ind = index - 1
        self.ui.tableWidget.setItem(ind, 0, QtWidgets.QTableWidgetItem(self.notes_dict[head]["title"]))
        self.ui.tableWidget.setItem(ind, 1, QtWidgets.QTableWidgetItem(self.notes_dict[head]["dateCreate"]))
        self.ui.tableWidget.setItem(ind, 2, QtWidgets.QTableWidgetItem(self.notes_dict[head]["deadline"]))

        #self.ui.tableWidget.setEnabled(False)

        # #self.ui.tableWidget.setItem(1,2,QtWidgets.QTableWidgetItem("4"))
        # self.ui.tableWidget.sortItems(3, order=QtCore.Qt.SortOrder.AscendingOrder)



    def buttonDelete(self):
        """ Функция активации кнопки "Удалить" с последующим удалением заметки"""

        # tableWidget
        noteitem = []

        row = self.ui.tableWidget.currentRow()
        for i in range(self.ui.tableWidget.columnCount()):
            noteitem.append(self.ui.tableWidget.item(row, i).text())
        self.ui.tableWidget.removeRow(row)

        # json
        del self.notes_dict[noteitem[0]]
        with open("saved_notes/data.json", "A", encoding="utf8") as data:
            self.data = {"notes_dict": self.notes_dict}
            json.dump(self.notes_dict, data, indent=4)



    def buttonShow(self):
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
        string_deadline_date = self.notes_dict[key]["deadline"]
        self.ui.dateTimeEdit.setDateTime(QtCore.QDateTime.fromString(string_deadline_date, "%d.%m.%Y %H:%M"))


    def buttonSave(self):
        """ Функция сохранения изменений в заметке """



        noteitem = []
        row = self.ui.tableWidget.currentRow()
        for i in range(self.ui.tableWidget.columnCount()):
            noteitem.append(self.ui.tableWidget.item(row, i).text())

        head = noteitem[0]

        if head != self.ui.lineEdit.text():

           self.buttonDelete()
           self.buttonCreate()

        else:
            self.notes_dict[head]["title"] = self.ui.lineEdit.text()
            self.notes_dict[head]["text"] = self.ui.textEdit.toPlainText()
            self.notes_dict[head]["deadline"] = self.ui.dateTimeEdit.text()

        self.tableWidgetItem(row)





    # def closeEvent(self, event) -> None:
    #
    #     """ Событие закрытия окна """
    #
    #     settings = QtCore.QSettings('sets.ini', QtCore.QSettings.format())
    #     settings.setValue("key", "Value")


if __name__ == "__main__":
    app = QtWidgets.QApplication()

    window = Window()
    window.show()

    app.exec()
