from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtGui import QCloseEvent

from src.services.cron_service import CronService


class AlarmQMainWindow(QMainWindow):
    
    def __init__(self):
        super(AlarmQMainWindow, self).__init__()

    def closeEvent(self, closeEvent: QCloseEvent) -> None:
        # TODO: properly close all threads when quitting
        cron_service = CronService.get_instance()
        cron_service.stop_all()
        super(AlarmQMainWindow, self).closeEvent(closeEvent)

    # def close(self) -> bool:
