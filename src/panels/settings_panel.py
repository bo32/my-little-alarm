from PyQt5.QtWidgets import QGroupBox, QLabel, QVBoxLayout


class SettingsPanel(QGroupBox):

    def __init__(self):
        super().__init__()

        self.layout = QVBoxLayout()
        self.layout.addWidget(QLabel('to be implemented'))

        self.setLayout(self.layout)

