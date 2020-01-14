from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QSlider, QLabel
from PyQt5.QtCore import Qt, pyqtSignal

class ColorPicker(QWidget):
    scrollChanged = pyqtSignal(tuple, name='ScrollChanged')
    color = { 'r': 0, 'g': 0, 'b': 0 }

    def __init__(self):
        super().__init__()

        self.sliders = [QSlider(Qt.Horizontal) for i in range(3)]
        layout = QVBoxLayout()
        
        for i in range(len(self.sliders)):
            layout.addWidget(self.sliders[i])
            self.sliders[i].setMaximum(255)
            self.sliders[i].valueChanged.connect(self.handleScroll)
            self.sliders[i].setObjectName(f'{i+1}')

        self.label = QLabel('Текст для примера')
        self.label.setStyleSheet('font-size: 16px; font-weight: 800')

        layout.addWidget(self.label)
        self.setLayout(layout)
        self.show()

    def changeColor(self, value):
        print(self.color)
        self.color[value[0]] = value[1]
        self.label.setStyleSheet(f"color: rgb({self.color.get('r')}, \
            {self.color.get('g')}, {self.color.get('b')}); font-size: 16px; font-weight: 800")

    def handleScroll(self, value):
        name = self.sender().objectName()
        if (name == '1'):
            self.scrollChanged.emit(('r', value))
        if (name == '2'):
            self.scrollChanged.emit(('g', value))
        if (name == '3'):
            self.scrollChanged.emit(('b', value))


if __name__ == '__main__':
    app = QApplication([])
    colorPicker = ColorPicker()
    colorPicker.ScrollChanged.connect(colorPicker.changeColor)
    app.exec_()