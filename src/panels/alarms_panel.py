from PyQt5.QtWidgets import QGroupBox, QLabel, QVBoxLayout, QPushButton, QHBoxLayout, QWidget
from PyQt5.QtCore import pyqtSignal

from services.alarm_service import AlarmService

ON_LABEL = 'On'
OFF_LABEL = 'Off'

class AlarmsPanel(QGroupBox):

    edit_alarms = pyqtSignal(int)

    def __init__(self):
        super().__init__()

        self.layout = QVBoxLayout()

        self.alarmService = AlarmService()
        self.display_alarms()
        self.setLayout(self.layout)
    
    def display_alarms(self):
        for alarm in self.alarmService.get_all_alarms():
            line = QWidget()
            layout = QHBoxLayout()

            alarm_id = alarm[0]

            layout.addWidget(QLabel(alarm[1])) # show label
            layout.addWidget(QLabel(alarm[2])) # show time
            
            is_active = alarm[4]# == True
            active_toggle = QPushButton(ON_LABEL if is_active else OFF_LABEL) 
            active_toggle.setCheckable(True)
            active_toggle.setChecked(is_active)
            active_toggle.clicked.connect(lambda state, x=alarm_id: self.active_button_pushed(x))
            layout.addWidget(active_toggle)

            edit = QPushButton('Edit') 
            edit.clicked.connect(lambda state, x=alarm_id: self.edit_alarm(x))
            layout.addWidget(edit)

            line.setLayout(layout)
            self.layout.addWidget(line)

    def active_button_pushed(self, alarm_id):
        state = self.sender().isChecked()
        self.sender().setText(ON_LABEL if state else OFF_LABEL)
        # alarm_id = alarm[0]
        self.alarmService.set_alarm_active(alarm_id, state)

    def edit_alarm(self, alarm_id):
        self.edit_alarms.emit(alarm_id)



