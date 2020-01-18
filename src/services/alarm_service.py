import sqlite3
from crontab import CronTab
from sqlalchemy import select, update, create_engine

from entities.alarm import Alarm

ALARMS = Alarm.__table__

class AlarmService:
    def __init__(self):
        super().__init__()
        engine = create_engine('sqlite:///src/alarms.db', echo = True)
        self.connection = engine.connect()

    def get_all_alarms(self):
        s = ALARMS.select()
        # print(str(s))
        
        # for row in all_alarms:
        #     print(row)
        #     print(row[1])
        # for row in all_alarms:
        #     print (row)
        return self.connection.execute(s)
    
    def get_active_alarms(self):
        # self.cursor.execute("SELECT * FROM alarms WHERE active=1 ")
        # s = Alarm.__table__.select().where(Alarm.__table__.c.active=1)
        # table = Alarm.__table__
        s = ALARMS.select().where(ALARMS.c.alarm_active == 1)
        # print(str(s))
        active_alarms = self.connection.execute(s)
        # session = DBSession()
        # active_alarms = session.query(Alarm).filter(Alarm.active==1).all()
        # for row in active_alarms:
        #     print(row)
        #     print(row[1])
        # session.close()
        return active_alarms

    def update_scheduled_time(self, alarm, new_scheduled_time):
        u = ALARMS.update()\
            .where(ALARMS.c.alarm_id == alarm.alarm_id)\
            .values(scheduled_time=new_scheduled_time)
        print(str(u))
        self.connection.execute(u)

    
    def get_alarm_by_id(self, alarm_id):
        s = ALARMS.select().where(ALARMS.c.alarm_id == alarm_id)
        alarm = self.connection.execute(s).fetchone()
        print(str(alarm))
        return alarm

    def print_all_alarms(self):
        for alarm in self.get_all_alarms():
            print(alarm[1])

    def initiate_cron(self, cron_exp):
        cron = CronTab(user=True)
        job = cron.new(command='echo hello_world')
        job.hour.on(22)
        job.minute.on(19)
        cron.write()

    def set_alarm_active(self, _alarm_id, _active):
        self.get_active_alarms()
        
        u = ALARMS.update()\
                .where(ALARMS.c.alarm_id == _alarm_id)\
                .values(alarm_active=bool(_active))
        print(str(u))
        self.connection.execute(u)

        



def main():
    # with open('resources/sql/alarms_table.sql') as f: s = f.read()
    # print(s)

    # init
    connection = sqlite3.connect('src/alarms.db')
    # c = connection.cursor()
    # c.execute(s)
    # c.execute("INSERT INTO alarms VALUES ('dummy', '09:00:00')")
    # c.execute("INSERT INTO alarms VALUES ('dummy2', '10:00:00')")
    # connection.commit()

    alarmService = AlarmService()
    alarmService.get_all_alarms()
    alarmService.get_active_alarms()

    # cleanup
    # c.execute('drop table alarms')

if __name__ == "__main__":
    main()


