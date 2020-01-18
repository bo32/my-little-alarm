from PyQt5.QtWidgets import QWidget, QStackedWidget, QVBoxLayout
from PyQt5.QtCore import pyqtSlot
from panels.clock_panel import ClockPanel
from panels.alarms_panel import AlarmsPanel
from panels.edit_alarm_panel import EditAlarmPanel
from panels.menu_buttons_panel import MenuButtons
from panels.settings_panel import SettingsPanel

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()
        self.stackedWidget =  QStackedWidget()
        self.stackedWidget.addWidget(ClockPanel())
        self.alarms_panel = AlarmsPanel()
        self.stackedWidget.addWidget(self.alarms_panel)
        self.stackedWidget.addWidget(SettingsPanel())
        layout.addWidget(self.stackedWidget)

        menu_buttons = MenuButtons()
        menu_buttons.switch_panel.connect(self.switch_panel)
        layout.addWidget(menu_buttons)
        
        self.alarms_panel.edit_alarms.connect(self.display_edit_alarm)


        self.setLayout(layout)

    @pyqtSlot(int, name="switch_panel")
    def switch_panel(self, panel_index):
        self.stackedWidget.setCurrentIndex(panel_index)

    @pyqtSlot(int, name="edit_alarm")
    def display_edit_alarm(self, alarm_id):
        print('EDIT ' + str(alarm_id))
        # drop alarms panel
        edit_alarm_panel =  EditAlarmPanel(alarm_id)
        self.stackedWidget.insertWidget(1, edit_alarm_panel)
        self.stackedWidget.setCurrentIndex(1)
        self.stackedWidget.removeWidget(self.alarms_panel)
        # display edit alarm panel

        edit_alarm_panel.quit_signal.connect(self.hello)

    @pyqtSlot(name="quit")
    def hello(self):
        print('should close the edit alarm panel')
        
