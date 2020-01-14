from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout

app = QApplication([])
window = QWidget()

layout = QVBoxLayout()
layout.addWidget(QPushButton('Кнопка один'))
layout.addWidget(QPushButton('Кнопка два'))

window.setLayout(layout)
window.show()
app.exec_()