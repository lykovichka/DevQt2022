"""
Реализовать окно, которое будет объединять в себе сразу два предыдущих виджета
"""


from PySide6 import QtWidgets
from c_weatherapi_widget import Window as Weather
from b_systeminfo_widget import Window as System

class Window(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.initUi()


    def initUi(self):

        self.system = System()
        self.weather = Weather()

        self.setWindowTitle("System and Weather")

        self.lableSystem = QtWidgets.QLabel()
        self.lableSystem.setText("Информация о системе")

        self.lableWeather = QtWidgets.QLabel()
        self.lableWeather.setText("Информация о погоде")


        layoutSystem = QtWidgets.QVBoxLayout()
        layoutSystem.addWidget(self.lableSystem)
        layoutSystem.addWidget(self.system)

        layoutWeather = QtWidgets.QVBoxLayout()
        layoutWeather.addWidget(self.lableWeather)
        layoutWeather.addWidget(self.weather)

        layout = QtWidgets.QVBoxLayout()
        layout.addLayout(layoutSystem)
        layout.addLayout(layoutWeather)

        self.setLayout(layout)



if __name__ == "__main__":
    app = QtWidgets.QApplication()

    window = Window()
    window.show()

    app.exec()