from PyQt5.QtWidgets import QGroupBox, QLabel, QVBoxLayout, QPushButton, QHBoxLayout, QWidget
from services.alarm_service import AlarmService

class Alarms(QGroupBox):

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

            #
            layout.addWidget(QLabel(alarm[1]))
            #
            is_active = alarm[4] == True
            active_toggle = QPushButton('On' if is_active else 'Off') 
            active_toggle.setCheckable(True)
            active_toggle.setChecked(is_active)

            active_toggle.clicked.connect(lambda state, x=alarm: self.button_pushed(x))

            layout.addWidget(active_toggle)

            line.setLayout(layout)

            # line = QDataWidgetMapper()

            self.layout.addWidget(line)

    # def set_alarm_active(self):
    def button_pushed(self, alarm):
        state = self.sender().isChecked()
        print(str(state))
        self.sender().setText('On' if state else 'Off')
        print(alarm)
        alarm_id = alarm[0]
        self.alarmService.set_alarm_active(alarm_id, state)





