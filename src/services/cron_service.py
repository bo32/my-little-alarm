from src.services.my_scheduler import MyScheduler
from src.services.sound_service import SoundService
from PyQt5.QtCore import pyqtSignal, QObject


class CronService(QObject):

    alarm_triggered = pyqtSignal()
    __instance = None


    def __init__(self):
        super(CronService, self).__init__()
        if CronService.__instance != None:
            raise Exception("This class is a singleton!")
        else:
            CronService.__instance = self
            self.scheduler = MyScheduler()
            self.sound_service = SoundService.get_instance()
            self.event= None

    def start_alarm(self, cron):
        self.scheduler.every().day.at(cron).do(self.test, name="It's time !!!")
        # self.scheduler.every(1).seconds
        print('alarm triggered for ' + cron)


    def wait(self):
        self.event = self.scheduler.run_continuously()

    def test(self, name):
        print(name)
        self.sound_service.play_default_alarm_sound()
        # url = 'http://direct.franceinter.fr/live/franceinter-lofi.mp3'
        # self.sound_service.play_webradio(url)
        self.alarm_triggered.emit()


    def stop_all(self):
        self.event.set()
        self.scheduler.clear()

    @staticmethod
    def get_instance():
        if CronService.__instance == None:
            CronService.__instance = CronService()
        return CronService.__instance
    # def get_scheduler(self):
    #     if self.scheduler == None:
    #         self.scheduler = MyScheduler()
    #     return self.scheduler
