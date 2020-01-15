from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy import Column, Integer, String, Boolean

Base = declarative_base()

class Alarm(Base):
    __tablename__ = 'alarms'

    alarm_id = Column(Integer, primary_key=True)
    alarm_label = Column(String)
    scheduled_time = Column(String)
    description = Column(String)
    alarm_active = Column(Boolean)
    
    def __repr__(self):
        return "<User(id='%d', label='%s', time='%s', active='%r')>" % (
            self.alarm_id, self.alarm_label, self.scheduled_time, self.alarm_active)
