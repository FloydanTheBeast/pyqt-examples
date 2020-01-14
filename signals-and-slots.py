from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QSlider, QProgressBar
from PyQt5.QtCore import Qt

app = QApplication([])
window = QWidget()

layout = QVBoxLayout()

slider = QSlider(Qt.Horizontal)
progressBar = QProgressBar()

layout.addWidget(progressBar)
layout.addWidget(slider)

# slider.valueChanged - сигнал, progressBar.setValue - слот
slider.valueChanged.connect(progressBar.setValue)

window.setWindowTitle('Signal & slot')
window.setLayout(layout)
window.resize(300, 150)
window.show()
app.exec_()