from PyQt5.QtWidgets import QGroupBox, QVBoxLayout, QLabel, QPushButton


class AlarmTriggeredPanel(QGroupBox):

    def __init__(self):
        super().__init__()
        self.layout = QVBoxLayout()
        self.layout.addWidget(QLabel("It's time!!!"))

        # if snoozing enabled
        snooze = QPushButton('Snooze')
        self.layout.addWidget(snooze)
        # TODO: implement snooze button

        dismiss = QPushButton('Dismiss')
        self.layout.addWidget(dismiss)
        # TODO: implement dismiss button

        self.setLayout(self.layout)


