"""
Реализовать виджет, который будет работать с потоком SystemInfo из модуля a_threads

Создавать форму можно как в ручную, так и с помощью программы Designer

Форма должна содержать:
1. поле для ввода времени задержки
2. поле для вывода информации о загрузке CPU
3. поле для вывода информации о загрузке RAM
4. поток необходимо запускать сразу при старте приложения
5. установку времени задержки сделать "горячей", т.е. поток должен сразу
реагировать на изменение времени задержки
"""

from PySide6 import QtWidgets
from a_threads import SystemInfo
from HW3.UI.system_info_widget_ui import  Ui_Form


class Window(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.initUi()
        self.initThreads()
        self.initSignals()



    def initUi(self):

        self.ui.horizontalSlider.setRange(0, 60)


    def initSignals(self):

        self.ui.horizontalSlider.valueChanged.connect(self.sliderChanged)
        self.systemInfo.systemInfoReceived.connect(self.infoRamCpu)


    def sliderChanged(self):

        self.systemInfo.delay = self.ui.horizontalSlider.value()
        self.ui.lcdNumberDelay.display(self.ui.horizontalSlider.value())


    def infoRamCpu(self, cpuRam):

        cpu_value, ram_value = cpuRam
        self.ui.lcdNumberCPU.display(cpu_value)
        self.ui.lcdNumberCRAM.display(ram_value)


    def initThreads(self):
        self.systemInfo = SystemInfo()
        self.systemInfo.start()


    def closeEvent(self, event):
        self.systemInfo.terminate()


if __name__ == "__main__":
    app = QtWidgets.QApplication()

    window = Window()
    window.show()

    app.exec()
