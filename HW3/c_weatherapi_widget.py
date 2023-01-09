"""
Реализовать виджет, который будет работать с потоком WeatherHandler из модуля a_threads

Создавать форму можно как в ручную, так и с помощью программы Designer

Форма должна содержать:
1. поле для ввода широты и долготы (после запуска потока они должны блокироваться)
2. поле для ввода времени задержки (после запуска потока оно должно блокироваться)
3. поле для вывода информации о погоде в указанных координатах
4. поток необходимо запускать и останавливать при нажатие на кнопку
"""
from PySide6 import QtWidgets, QtCore
from a_threads import WeatherHandler
from HW3.UI.weather_ui import Ui_Form


class Window(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.weatherinfo = WeatherHandler(lat=0, lon=0)
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.initUi()
        self.initSignals()




    def initUi(self):

        self.ui.spinBox.setValue(2)


    def initSignals(self):

        self.ui.pushButton.clicked.connect(self.pressButton)

        self.weatherinfo.weatherInfoReceived.connect(self.weatherInfoReceive)




    def pressButton(self):

        if self.ui.pushButton.text() == "Узнаем погоду!":
            self.weatherThreadOn()
        else:
            self.weatherThreadOff()



    def weatherThreadOn(self):

        lat = self.ui.lineEditLatitude.text()
        lon = self.ui.lineEditLongitude.text()

        delay = self.ui.spinBox.value()

        self.weatherinfo.setUrl(lat, lon)
        self.weatherinfo.setDelay(delay)
        self.weatherinfo.start()

        self.ui.pushButton.setText("Хватит")

        self.ui.lineEditLatitude.setEnabled(False)
        self.ui.lineEditLongitude.setEnabled(False)

        self.ui.spinBox.setEnabled(False)



    def weatherThreadOff(self):

        self.weatherinfo.stop()

        self.ui.pushButton.setText("Узнаем погоду!")

        self.ui.spinBox.setEnabled(True)
        self.ui.lineEditLatitude.setEnabled(True)
        self.ui.lineEditLongitude.setEnabled(True)



    def weatherInfoReceive(self, data):

        latitude = str(data['latitude'])
        longitude = str(data['longitude'])
        temperature = str(data['current_weather']['temperature'])
        windspeed = str(data['current_weather']['windspeed'])
        winddirection = str(data['current_weather']['winddirection'])

        time = QtCore.QDateTime.currentDateTime().toString('HH:mm:ss')

        self.ui.plainTextEdit.appendPlainText(f"Широта: {latitude}\n"
                                              f"Долгота: {longitude}\n"
                                              f"Температура: {temperature}оC\n"
                                              f"Скорость ветра: {windspeed}м/с\n"
                                              f"Направление ветра: {winddirection}\n"
                                              f"Время: {time}\n")

    def closeEvent(self, event):
        self.weatherinfo.terminate()


if __name__ == "__main__":
    app = QtWidgets.QApplication()

    window = Window()
    window.show()

    app.exec()