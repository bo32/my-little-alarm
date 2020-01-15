from PyQt5.QtWidgets import QApplication, QMainWindow
from main_window import MainWindow

from services.alarm_service import AlarmService

APP_FONT_COLOR = 'lightgray'
APP_BACKGROUND_COLOR = 'slategray'

class MainApplication():
    def __init__(self):
        app = QApplication([])
        stylesheet = """QLabel {0} color: {2}; border: 1px dotted red {1}
            QPushButton {0} color: {2} {1}
            QGroupBox {0} border: 1px solid red {1}
            QWidget {0} background-color: {3} {1}
        """.format('{', '}', APP_FONT_COLOR, APP_BACKGROUND_COLOR)
        app.setStyleSheet(stylesheet)

        window = QMainWindow()
        window.setCentralWidget(MainWindow())
        # window.showFullScreen()

        # flags = Qt.WindowFlags
        # window.setWindowFlags()
        self.init()
        
        window.show()
        app.exec_()


    def init(self):
        self.start_alarms()
        
    def start_alarms(self):
        alarmService = AlarmService()
        active_alarms = alarmService.get_active_alarms()
        # TODO Start CRON
        # print(str(len(active_alarms)))
        # alarmService.initiate_cron('whatever')


if __name__ == "__main__":
    MainApplication()
