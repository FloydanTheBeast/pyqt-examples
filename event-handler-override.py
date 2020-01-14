from PyQt5.QtWidgets import QApplication, QWidget, QMessageBox, QLabel, QVBoxLayout
from PyQt5.QtCore import Qt

class UI(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()

        self.label = QLabel('x: _; y: _')
        self.label.setStyleSheet('font-size: 48px; font-weight: 800')

        layout.addWidget(self.label)
        layout.setAlignment(Qt.AlignCenter)

        self.setLayout(layout)
        self.showFullScreen()

    def mousePressEvent(self, e):
        self.label.setText(f'x: {e.x()}; y: {e.y()}')

if __name__ == '__main__':
    app = QApplication([])
    ui = UI()
    app.exec_()