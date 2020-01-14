from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QGridLayout

app = QApplication([])
window = QWidget()

grid = QGridLayout()
window.setLayout(grid)

grid.addWidget(QPushButton('1'), 1, 1)
grid.addWidget(QPushButton('2'), 1, 2)
grid.addWidget(QPushButton('3'), 2, 1)
grid.addWidget(QPushButton('4'), 2, 2)

window.show()
app.exec_()