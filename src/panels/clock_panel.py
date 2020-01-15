from PyQt5.QtWidgets import QLabel, QVBoxLayout, QGroupBox, QSizePolicy
from PyQt5.QtCore import QTimer, QTime
from dynamic_font_size_label import DynamicFontSizeLabel

class ClockPanel(QGroupBox):

    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        self.clock = DynamicFontSizeLabel()
        # self.clock.setSizePolicy(QSizePolicy(QSizePolicy.Ignored,
        #                                      QSizePolicy.Ignored))  
        self.updateClock()
        layout.addWidget(self.clock)
        self.setLayout(layout)

        # start ticking
        self.tick()

    def get_current_time(self):
        return QTime.currentTime().toString('HH:mm')

    def updateClock(self):
        self.clock.setText(self.get_current_time())

    def tick(self):
        timer = QTimer(self)
        timer.timeout.connect(self.updateClock)
        # every second
        timer.start(1000)
