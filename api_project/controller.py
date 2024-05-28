import sys
from tkinter.ttk import Widget
from PyQt6.QtWidgets import (QApplication, QMainWindow, QWidget, QHBoxLayout,
                             QVBoxLayout,QLabel,QPushButton,QSpinBox,QLineEdit,QDoubleSpinBox,
                             QCheckBox,QComboBox,QListWidget)
from PyQt6.QtWidgets import ( QMainWindow, QApplication, QVBoxLayout, QHBoxLayout,
    QLabel, QCheckBox, QComboBox, QListWidget, QTextEdit,
    QSpinBox, QDoubleSpinBox, QSlider, QWidget, QPushButton,)
from PyQt6.QtCore import Qt


class MainWindow(QMainWindow):


    def __init__(self):
        super(MainWindow, self).__init__()


        self.setWindowTitle("Random Genre Generator")

        # Main layout ####################
        main_layout = QHBoxLayout()


        # Left and right panes #############
        top_pane = QVBoxLayout()
        left_pane = QVBoxLayout()

        title_label = QLabel("Random Genre Generator")




import requests as re

url = "https://www.boredapi.com/api/activity"

response = re.get(url)

if response.ok:
    print(response.text)
else:
    print(f"There was an error: {response.status_code}")

    app = QApplication(sys.argv)


window = MainWindow()
window.show()
    
app.exec()