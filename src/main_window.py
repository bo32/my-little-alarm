from PyQt5.QtWidgets import QWidget, QStackedWidget, QVBoxLayout
from PyQt5.QtGui import QWindow
from PyQt5.QtCore import pyqtSlot
from panels.clock_panel import ClockPanel
from panels.alarms_panel import Alarms
from panels.menu_buttons_panel import MenuButtons
from panels.settings_panel import SettingsPanel

@pyqtSlot()

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()
        self.stackedWidget =  QStackedWidget()
        self.stackedWidget.addWidget(ClockPanel())
        self.stackedWidget.addWidget(Alarms())
        self.stackedWidget.addWidget(SettingsPanel())
        layout.addWidget(self.stackedWidget)

        menu_buttons = MenuButtons()
        menu_buttons.display_alarms.connect(self.display_alarms)
        menu_buttons.display_clock.connect(self.display_clock)
        menu_buttons.display_settings.connect(self.display_settings)
        layout.addWidget(menu_buttons)



        self.setLayout(layout)

    def display_clock(self):
        self.stackedWidget.setCurrentIndex(0)

    def display_alarms(self):
        self.stackedWidget.setCurrentIndex(1)

    def display_settings(self):
        self.stackedWidget.setCurrentIndex(2)