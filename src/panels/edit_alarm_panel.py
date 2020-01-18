from PyQt5.QtWidgets import QGroupBox, QLabel, QHBoxLayout, QVBoxLayout, QSlider, QWidget, QPushButton
from PyQt5.QtCore import Qt, pyqtSignal

from services.alarm_service import AlarmService

class EditAlarmPanel(QGroupBox):

    quit_signal = pyqtSignal()

    def __init__(self, alarm_id):
        super().__init__()
        layout = QVBoxLayout()


        # layout.addWidget(QLabel(str(alarm_id)))

        self.alarm_service = AlarmService()
        self.alarm = self.alarm_service.get_alarm_by_id(alarm_id)
        print(str(self.alarm))

        layout.addWidget(QLabel(self.alarm[1]))

        scheduled_time = self.alarm[2]
        print(scheduled_time)
        split_time = scheduled_time.split(':')
        self.hours = int(split_time[0])
        self.minutes = int(split_time[1])

        self.hour_label = QLabel()
        hour_slider = QSlider(Qt.Horizontal)
        hour_slider.setMinimum(0)
        hour_slider.setMaximum(23)
        hour_slider.setValue(self.hours)
        hour_layout = QHBoxLayout()
        hour_layout.addWidget(self.hour_label)
        hour_layout.addWidget(hour_slider)
        hour_slider.valueChanged.connect(self.hours_changed)
        hour_widget = QWidget()
        hour_widget.setLayout(hour_layout)
        layout.addWidget(hour_widget)

        self.minute_label = QLabel()
        minute_slider = QSlider(Qt.Horizontal)
        minute_slider.setMinimum(0)
        minute_slider.setMaximum(59)
        minute_slider.setValue(self.minutes)
        # minute_slider.setTickPosition(QSlider.TicksBelow)
        minute_layout = QHBoxLayout()
        minute_layout.addWidget(self.minute_label)
        minute_layout.addWidget(minute_slider)
        minute_slider.valueChanged.connect(self.minutes_changed)
        minute_widget = QWidget()
        minute_widget.setLayout(minute_layout)
        layout.addWidget(minute_widget)

        save_cancel_buttons = QWidget()
        save_cancel_layout = QHBoxLayout()
        save_button = QPushButton('Save')
        save_button.clicked.connect(self.save)
        save_cancel_layout.addWidget(save_button)
        cancel_button = QPushButton('Cancel')
        cancel_button.clicked.connect(self.quit)
        save_cancel_layout.addWidget(cancel_button)
        save_cancel_buttons.setLayout(save_cancel_layout)
        layout.addWidget(save_cancel_buttons)

        self.setLayout(layout)

        self.update_time_label(self.hour_label, self.hours)
        self.update_time_label(self.minute_label, self.minutes)

    def update_time_label(self, qlabel, value):
        qlabel.setText(str(value).zfill(2))

    def hours_changed(self, value):
        self.hours = value
        self.update_time_label(self.hour_label, self.hours)
        # self.hour_label.setText(str(self.hours))

    def minutes_changed(self, value):
        self.minutes = value
        self.update_time_label(self.minute_label, self.minutes)
        # self.minute_label.setText(str(self.minutes))

    # def update_current_alarm(self):
    #     new_scheduled_time = "%d:%d" % (self.hours, self.minutes)
    #     print('before update (using getter): ' + self.alarm.scheduled_time)
    #     print('new time: ' + new_scheduled_time)
    #     self.alarm.scheduled_time =new_scheduled_time

    def save(self):
        # self.update_current_alarm()
        new_scheduled_time = "%d:%d" % (self.hours, self.minutes)
        self.alarm_service.update_scheduled_time(self.alarm, new_scheduled_time)
        self.quit()

    def quit(self):
        self.quit_signal.emit()
