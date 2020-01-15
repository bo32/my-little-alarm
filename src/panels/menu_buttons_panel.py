from PyQt5.QtWidgets import QGroupBox, QHBoxLayout, QPushButton
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtGui import QIcon

class MenuButtons(QGroupBox):

    display_clock = pyqtSignal()
    display_alarms = pyqtSignal()
    display_settings = pyqtSignal()

    def __init__(self):
        super().__init__()
        layout = QHBoxLayout()

        self.clock_button = QPushButton('Clock')
        # self.clock_button.setStyleSheet("""
        #     image: url("images/clock.svg")
        #     """)
        # icon = QIcon("images/clock.svg")
        # icon.setColor('white')
        # self.clock_button.setIcon(icon)
        self.alarms_button = QPushButton('Alarms')
        self.settings_button = QPushButton('Settings')

        self.buttons = [ self.clock_button, self.alarms_button, self.settings_button ]
        for button in self.buttons:
            button.setCheckable(True)
            button.clicked.connect(self.uncheck_other_buttons)
            button.clicked.connect(self.change_panel)
            layout.addWidget(button)

        self.clock_button.click()

        self.setLayout(layout)

    def uncheck_other_buttons(self):
        clicked_button = self.sender()
        for button in self.buttons:
            button.setChecked(button == clicked_button)
    
    def change_panel(self):
        clicked_button = self.sender()
        # update panel
        if clicked_button == self.clock_button:
            self.display_clock.emit()
        if clicked_button == self.alarms_button:
            self.display_alarms.emit()
        if clicked_button == self.settings_button:
            self.display_settings.emit()




    