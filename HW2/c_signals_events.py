"""
Реализация программу проверки состояния окна:
Форма для приложения (ui/c_signals_events.ui)

Программа должна обладать следующим функционалом:

1. Возможность перемещения окна по заданным координатам.
2. Возможность получения параметров экрана (вывод производить в plainTextEdit + добавлять время).
    * QtWidgets.QApplication.screens()
    * Кол-во экранов
    * Текущее основное окно
    * Разрешение экрана
    * На каком экране окно находится
    * Размеры окна
    * Минимальные размеры окна
    * Текущее положение (координаты) окна
    * Координаты центра приложения
    * Отслеживание состояния окна (свернуто/развёрнуто/активно/отображено)
3. Возможность отслеживания состояния окна (вывод производить в консоль + добавлять время).
    * При перемещении окна выводить его старую и новую позицию
    * При изменении размера окна выводить его новый размер
"""
import datetime
import time

from PySide6 import QtWidgets, QtCore

from HW2.ui.c_signals_events_design import Ui_Form


class Window(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.initSignals()

    def initSignals(self):
        """ Инициализация сигналов """

        self.ui.pushButtonLT.clicked.connect(lambda: self.move(0, 0))
        self.ui.pushButtonRT.clicked.connect(self.moveRightTop)
        self.ui.pushButtonLB.clicked.connect(self.moveLeftDownn)
        self.ui.pushButtonRB.clicked.connect(self.moveRightDown)
        self.ui.pushButtonCenter.clicked.connect(self.moveCentral)
        self.ui.pushButtonMoveCoords.clicked.connect(self.moveCoords)

        self.ui.pushButtonGetData.clicked.connect(self.getData)

    def moveRightTop(self):
        """ Функция перемещения экрана в правый верхний угол """

        current_screen = QtWidgets.QApplication.screenAt(self.pos())
        screen_width = current_screen.size().width()
        pos_x = screen_width - self.width()

        self.move(pos_x, 0)

    def moveLeftDownn(self):
        """ Функция перемещения экрана в нижний левый угол """

        current_screen = QtWidgets.QApplication.screenAt(self.pos())
        height = current_screen.size().height() - self.height()
        self.move(0, height)

    def moveRightDown(self):
        """ Функция перемещения экрана в правый нижний угол """

        current_screen = QtWidgets.QApplication.screenAt(self.pos())
        width = current_screen.size().width() - self.width()
        height = current_screen.size().height() - self.height()
        self.move(width, height)

    def moveCentral(self):
        """ Функция центрирования экрана"""

        current_screen = QtWidgets.QApplication.screenAt(self.pos())
        width = (current_screen.size().width()) / 2 - (self.width()) / 2
        height = (current_screen.size().height()) / 2 - (self.height()) / 2
        self.move(width, height)

    def moveCoords(self):
        """ Функция перемещения по координатам """

        pos_x = int(self.ui.spinBoxX.text())
        pos_y = int(self.ui.spinBoxY.text())
        self.move(pos_x, pos_y)

    def getData(self):
        """ Функция получения информации и вывода ее """
        current_screen = QtWidgets.QApplication.screenAt(self.pos())

        self.ui.plainTextEdit.appendPlainText(f"Количество экранов - {QtWidgets.QApplication.screens()} \n"
                                              f"Текущее основное окно - {current_screen} \n"
                                              f"Разрешение экрана - {current_screen.size().width()}x{current_screen.size().height()} \n "
                                              f"Размеры окна - {self.width()}x{self.height()} \n"
                                              f"Минимальные размеры окна - {self.minimumWidth()}x{self.minimumHeight()} \n"
                                              f"Текущее положение (координаты) окна - {self.pos().x()}x{self.pos().y()} \n"
                                              f"Координаты центра приложения - {self.pos().x() / 2}x{self.pos().y() / 2} \n"
                                              f"Время {datetime.datetime.now()}")

    def event(self, event_) -> bool:
        # e = f"{time.ctime()}: {event_}"
        # print(e)

        if event_.type() == QtCore.QEvent.Type.Resize:
            print(f"Изменился размер окна {event_.size()} в {time.ctime()}")
            #self.ui.plainTextEdit.appendPlainText(f"Изменился размер окна {event_.size()}"
                                                 # f"в {time.ctime()}")

        elif event_.type() == QtCore.QEvent.Type.Move:
            print(f"Изменилось положение окна {event_.pos()} в {time.ctime()}")
            #self.ui.plainTextEdit.appendPlainText(f"Изменилось положение окна {event_.pos()}"
                                                 # f"в {time.ctime()}")

        return super(Window, self).event(event_)


if __name__ == "__main__":
    app = QtWidgets.QApplication()

    window = Window()
    window.show()

    app.exec()
