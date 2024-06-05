import sys
import controller
from PyQt6.QtWidgets import ( QMainWindow, QApplication, QVBoxLayout, QHBoxLayout,
    QLabel, QRadioButton, QComboBox, QListWidget, QTextEdit,
    QSpinBox, QDoubleSpinBox, QSlider, QWidget, QPushButton,)
from PyQt6.QtCore import Qt


class MainWindow(QMainWindow):


    def __init__(self):
        super(MainWindow, self).__init__()


        self.setWindowTitle("Random Genre Generator")

        # Main layout ####################################################
        main_layout = QHBoxLayout()


        # Top and bottom panes ############################################
        top_pane = QVBoxLayout()
        bottom_pane = QVBoxLayout()

        title_label = QLabel("Random Genre Generator")

         # Set fonts ########################################################
        h1_font = title_label.font()
        h1_font.setPointSize(30)
        title_label.setFont(h1_font)

        # Results label #######################################################
        self.results_title_label = QLabel()
        h2_font = self.results_title_label.font()
        h2_font.setPointSize(26)
        self.results_title_label.setFont(h2_font)

        self.results_label = QLabel("Select a genre or story and how many generations you want")
        p_font = self.results_label.font()
        p_font.setPointSize(16)
        self.results_label.setFont(p_font)

        # Add top pane widgets ##################################################
        self.genre_radio = QRadioButton()
        self.genre_radio.setText("Genre")
        self.genre_radio.setChecked(True)
        self.story_cb = QRadioButton()
        self.story_cb.setText("Story")
        slider_label = QLabel("Amount of Generations")
        self.gen_slider = QSlider()
        self.gen_btn = QPushButton("Generate")
        self.gen_btn.clicked.connect(self.generate)

        # Add top pane widgets #####################################################
        top_pane.addWidget(title_label)
        top_pane.addWidget(self.genre_radio)
        top_pane.addWidget(self.story_cb)
        top_pane.addWidget(slider_label)
        top_pane.addWidget(self.gen_slider)
        top_pane.addWidget(self.gen_btn)

        # Add bottom pane widgets ###################################################
        bottom_pane.addWidget(self.results_title_label)
        bottom_pane.addWidget(self.results_label)

        # Add the two panes to the layout ###########################################
        main_layout.addLayout(top_pane)
        main_layout.addLayout(bottom_pane)

        # Set the main Layout #########################################################
        gui = QWidget()
        gui.setLayout(main_layout)
        self.setCentralWidget(gui)

        # Generate the results ########################################################
        
    def generate(self):
        genre = self.genre_radio.text()
        story = self.story_cb.text()
        number = self.gen_slider.value()

        if self.genre_radio.isChecked():
            response = controller.genre_response()
        else:
            response = controller.story_response()
       

        self.results_label.setText(response)









    
    
app = QApplication(sys.argv)


window = MainWindow()
window.show()
    
app.exec()