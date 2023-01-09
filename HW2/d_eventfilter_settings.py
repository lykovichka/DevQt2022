"""
Реализация программу взаимодействия виджетов друг с другом:
Форма для приложения (ui/d_eventfilter_settings.ui)

Программа должна обладать следующим функционалом:

1. Добавить для dial возможность установки значений кнопками клавиатуры(+ и -),
   выводить новые значения в консоль (done)

2. Соединить между собой QDial, QSlider, QLCDNumber
   (изменение значения в одном, изменяет значения в других) (done)

3. Для QLCDNumber сделать отображение в различных системах счисления (oct, hex, bin, dec),
   изменять формат отображаемого значения в зависимости от выбранного в comboBox параметра. (done)

4. Сохранять значение выбранного в comboBox режима отображения
   и значение LCDNumber в QSettings, при перезапуске программы выводить
   в него соответствующие значения (done)
"""

from PySide6 import QtWidgets, QtGui, QtCore
from HW2.ui.d_event import Ui_Form


class Window(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.initUi()
        self.initSignal()

        settings = QtCore.QSettings("LastChange")
        self.ui.comboBox.setCurrentText(settings.value("comboBoxValue", "oct"))
        self.ui.horizontalSlider.setValue(settings.value("value", self.ui.horizontalSlider.value()))

    def initUi(self) -> None:
        """ Инициализация формы """
        self.ui.dial.setNotchesVisible(True)  # Установим градацию dial
        self.ui.comboBox.addItems(['oct', 'hex', 'bin', 'dec'])

    def initSignal(self) -> None:
        """ Инициализация сигналов """

        self.ui.dial.valueChanged.connect(self.dialConnect)
        self.ui.horizontalSlider.valueChanged.connect(self.sliderConnect)
        self.ui.comboBox.currentIndexChanged.connect(self.comboBoxConnect)

        settings = QtCore.QSettings("Eventfilter")
        self.ui.comboBox.setCurrentText(settings.value("comboBoxValue", "oct"))
        self.ui.horizontalSlider.setValue(settings.value("value"))

    def dialConnect(self):

        """ Функция подключения dial"""

        value = self.ui.dial.value()
        self.ui.lcdNumber.display(value)
        self.ui.horizontalSlider.setValue(value)  # связь слайдера с dial

    def sliderConnect(self):

        """ Функция подключения слайдера """

        value = self.ui.horizontalSlider.value()
        self.ui.lcdNumber.display(value)
        self.ui.dial.setValue(value)  # связь dial со слайдерем

    def comboBoxConnect(self):

        """ Функция изменения значений с помощью комбобокса """

        text = self.ui.comboBox.currentText()
        if text == 'oct':
            self.ui.lcdNumber.setOctMode()
        elif text == 'hex':
            self.ui.lcdNumber.setHexMode()
        elif text == 'bin':
            self.ui.lcdNumber.setBinMode()
        elif text == 'dec':
            self.ui.lcdNumber.setDecMode()


    def keyPressEvent(self, event: QtGui.QKeyEvent) -> None:

        """ Подключение клавиш "+" , "-"клавиатуры """

        if event.text() == "+":
            self.ui.dial.setValue(self.ui.dial.value() + 1)
        if event.text() == "-":
            self.ui.dial.setValue(self.ui.dial.value() - 1)

        print(self.ui.dial.value())


    def closeEvent(self, event) -> None:

        """ Событие закрытия окна """

        settings = QtCore.QSettings("LastChange")
        settings.setValue("value", self.ui.horizontalSlider.value())
        settings.setValue("comboBoxValue", self.ui.comboBox.currentText())


if __name__ == "__main__":
    app = QtWidgets.QApplication()

    window = Window()
    window.show()

    app.exec()
