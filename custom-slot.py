from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QScrollBar, QMessageBox
from PyQt5.QtCore import Qt

class Example(QWidget):

    def __init__(self):
        super(QWidget, self).__init__()
        
        self.scrollBar = QScrollBar(Qt.Horizontal)
        self.scrollBar.valueChanged.connect(self.customSlot)

        self.messageBox = QMessageBox()
        self.messageBox.setIcon(QMessageBox.Information)
        self.messageBox.setWindowTitle('Информация')

        layout = QVBoxLayout()
        layout.addWidget(self.scrollBar)
        self.setLayout(layout)
        self.resize(300, 150)
        self.show()

    def customSlot(self, value):
        self.setWindowTitle(str(value))
        if value == self.scrollBar.maximum():
            self.messageBox.setInformativeText('Был достигнут максимум')
            self.messageBox.exec_()
        if value == self.scrollBar.minimum():
            self.messageBox.setInformativeText('Был достигнут минимум')
            self.messageBox.exec_()

if __name__ == '__main__':
    app = QApplication([])
    element = Example()
    app.exec_()