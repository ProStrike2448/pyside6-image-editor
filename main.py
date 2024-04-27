import sys

from PySide6.QtWidgets import QApplication, QWidget

app = QApplication(sys.argv)

window = QWidget()
window.setObjectName("window")
window.setWindowTitle("Easy Editor")
window.resize(700, 500)

window.show()
app.exec()
