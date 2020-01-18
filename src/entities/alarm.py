from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy import Column, Integer, String, Boolean, Table
from sqlalchemy.ext.hybrid import hybrid_property

Base = declarative_base()

class Alarm(Base):
    __table__ = Table('alarms', Base.metadata,

    Column("alarm_id", Integer, primary_key=True),
    Column("alarm_label", String),
    Column("scheduled_time", String),
    Column("description", String),
    Column("alarm_active", Boolean))
    #
    # @hybrid_property
    # def alarm_id(self):
    #     return self._alarm_id
    #
    # @hybrid_property
    # def scheduled_time(self):
    #     return self.scheduled_time
    #
    # @scheduled_time.setter
    # def scheduled_time(self, scheduled_time):
    #     print('new_scheduled time: ' + scheduled_time)
    #     self.scheduled_time = scheduled_time


    
    def __repr__(self):
        return "<User(id='%d', label='%s', time='%s', active='%r')>" % (
            self._alarm_id, self._alarm_label, self._scheduled_time, self._alarm_active)
