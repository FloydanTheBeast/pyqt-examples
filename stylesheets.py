from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout

app = QApplication([])
window = QWidget()

# Применение стилей напрямую к элементу
window.setStyleSheet('background-color: #0E171E')

layout = QVBoxLayout()

btn = QPushButton('Кнопка')

# Применение стилей по классу
btn.setStyleSheet('QPushButton { padding: 2ex; background-color: #1E272E; color: #FFF; border-radius: 8px; } \
                QPushButton:hover { background-color: #3E474E;}')

label1 = QLabel('Обычный текст')

label2 = QLabel('Кастомный текст')
label2.setObjectName('danger')

# Примененение стилей по названию
app.setStyleSheet('QLabel { color: #FFF; font-size: 16px } QLabel#danger { color: red; font-weight: 800 }')

layout.addWidget(label1)
layout.addWidget(label2)
layout.addWidget(btn)

window.setLayout(layout)
window.resize(400, 200)
window.show()
app.exec_()