# from crontab import CronTab
import schedule
import threading
from queue import Queue
# from schedule import Scheduler
import time

from PyQt5.QtCore import QTimer

from src.services.my_scheduler import MyScheduler


class CronService:

    def __init__(self):
        self.scheduler = MyScheduler()

    def start_alarm(self, cron):
        self.scheduler.every().day.at(cron).do(self.test, name="It's time !!!")
        # self.scheduler.every(1).seconds
        print('alarm triggered for ' + cron)

    def wait(self):
        self.scheduler.run_continuously()


    def test(self, name):
        print(name)
