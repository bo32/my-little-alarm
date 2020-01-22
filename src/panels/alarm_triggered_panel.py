from PyQt5.QtWidgets import QGroupBox, QVBoxLayout, QLabel, QPushButton

from src.services.sound_service import SoundService


class AlarmTriggeredPanel(QGroupBox):

    def __init__(self):
        super().__init__()
        self.layout = QVBoxLayout()
        self.layout.addWidget(QLabel("It's time!!!"))

        # if snoozing enabled
        snooze = QPushButton('Snooze')
        self.layout.addWidget(snooze)
        snooze.clicked.connect(self.snooze)

        dismiss = QPushButton('Dismiss')
        self.layout.addWidget(dismiss)
        dismiss.clicked.connect(self.dismiss)

        self.setLayout(self.layout)

    def snooze(self):
        SoundService.get_instance().pause_playing()

    def dismiss(self):
        SoundService.get_instance().stop_playing()

