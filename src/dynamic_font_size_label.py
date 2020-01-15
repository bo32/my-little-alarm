from PyQt5.QtWidgets import QLabel, QSizePolicy
from PyQt5.QtGui import QFontMetrics
from PyQt5.QtCore import Qt

class DynamicFontSizeLabel(QLabel):
    def __init__(self):
        super().__init__()

        self.setSizePolicy(QSizePolicy(QSizePolicy.Ignored,
                                             QSizePolicy.Ignored))  

        self.setMinSize(14)
        self.setAlignment(Qt.AlignCenter)

    def setMinSize(self, minfs):        

        f = self.font()
        f.setPixelSize(minfs)
        br = QFontMetrics(f).boundingRect(self.text())
        
        self.setMinimumSize(br.width(), br.height())

    def resizeEvent(self, event):
        super().resizeEvent(event)

        if not self.text():
            return

        #--- fetch current parameters ----

        f = self.font()
        cr = self.contentsRect()

        #--- find the font size that fits the contentsRect ---

        fs = 1                    
        while True:

            f.setPixelSize(fs)
            br =  QFontMetrics(f).boundingRect(self.text())

            if br.height() <= cr.height() and br.width() <= cr.width():
                fs += 1
            else:
                f.setPixelSize(max(fs - 1, 1)) # backtrack
                break  

        #--- update font size ---

        self.setFont(f)   
