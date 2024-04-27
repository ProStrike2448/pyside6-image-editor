import sys

from PySide6.QtWidgets import (
    QApplication,
    QHBoxLayout,
    QLabel,
    QListWidget,
    QPushButton,
    QVBoxLayout,
    QWidget,
)

app = QApplication(sys.argv)

window = QWidget()
window.setObjectName("window")
window.setWindowTitle("Easy Editor")
window.resize(700, 500)

lb_image = QLabel("Image")
btn_dir = QPushButton("Folder")
lw_files = QListWidget()

btn_left = QPushButton("Turn left")
btn_right = QPushButton("Turn right")
btn_flip = QPushButton("Flip")
btn_sharpen = QPushButton("Sharpen")
btn_bw = QPushButton("BW")

vl_files = QVBoxLayout()
vl_files.addWidget(btn_dir)
vl_files.addWidget(lw_files)

hl_controls = QHBoxLayout()
hl_controls.addWidget(btn_left)
hl_controls.addWidget(btn_right)
hl_controls.addWidget(btn_flip)
hl_controls.addWidget(btn_sharpen)
hl_controls.addWidget(btn_bw)

vl_image = QVBoxLayout()
vl_image.addWidget(lb_image)
vl_image.addLayout(hl_controls)

hl_main = QHBoxLayout()
hl_main.addLayout(vl_files, stretch=1)
hl_main.addLayout(vl_image, stretch=3)

window.setLayout(hl_main)

window.show()
app.exec()
