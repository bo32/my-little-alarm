from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QApplication, QStackedWidget
from main_window import MainWindow
from alarm_qmainwindow import AlarmQMainWindow

from services.alarm_service import AlarmService
from services.cron_service import CronService

from src.panels.alarm_triggered_panel import AlarmTriggeredPanel

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



        window = AlarmQMainWindow()

        self.stacked_widget = QStackedWidget()
        self.stacked_widget.addWidget(MainWindow())
        self.stacked_widget.addWidget(AlarmTriggeredPanel())
        window.setCentralWidget(self.stacked_widget)

        # window.showFullScreen()

        # flags = Qt.WindowFlags
        # window.setWindowFlags()
        self.init()
        
        window.show()
        # window.closeEvent(lambda state: self.quitting)

        # window.closeEvent.connect(self.quitting)
        # app.quit.connect(self.quitting)
        app.exec_()


    def init(self):
        self.start_alarms()
        
    def start_alarms(self):
        alarmService = AlarmService()
        active_alarms = alarmService.get_active_alarms()
        # TODO Start CRON
        # print(str(len(active_alarms)))
        # alarmService.initiate_cron('whatever')
        cron_service = CronService.get_instance()
        for alarm in active_alarms:
            cron = alarm.scheduled_time
            print(cron)
            cron_service.start_alarm(cron)

        # FOR dev purposes only! -------------
        import datetime
        next_minute_cron = (datetime.datetime.now() + datetime.timedelta(minutes=1)).strftime("%H:%M")
        print(str(next_minute_cron))
        cron_service.start_alarm(next_minute_cron)
        # ------------------------------------

        cron_service.wait()
        cron_service.alarm_triggered.connect(self.display_alarm_triggered_panel)

    def display_alarm_triggered_panel(self):
        self.stacked_widget.setCurrentIndex(1)

    @pyqtSlot(name="aboutToQuit")
    def quitting(self):
        print('heyyy')

if __name__ == "__main__":
    MainApplication()
