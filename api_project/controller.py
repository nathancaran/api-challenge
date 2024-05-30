import sys
from tkinter.ttk import Widget
from PyQt6.QtWidgets import ( QMainWindow, QApplication, QVBoxLayout, QHBoxLayout,
    QLabel, QCheckBox, QComboBox, QListWidget, QTextEdit,
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
        self.genre_cb = QCheckBox()
        self.genre_cb.setSuffix("Genre")
        self.story_cb = QCheckBox()
        self.story_cb.setSuffix(" Gallons")
        self.gen_num = QSlider("Amount of Generations")
        self.gen_btn = QPushButton("Generate")
        self.gen_btn.clicked.connect(self.generate)

        # Add top pane widgets #####################################################
        top_pane.addWidget(title_label)
        top_pane.addWidget(self.genre_cb)
        top_pane.addWidget(self.story_cb)
        top_pane.addWidget(self.gen_num)
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
        
        import requests as re

        url = "https://binaryjazz.us/wp-json/genrenator/v1/genre/", "https://binaryjazz.us/wp-json/genrenator/v1/story/"

        response = re.get(url)

        if response.ok:
            print(response.text)
        else:
            print(f"There was an error: {response.status_code}")
        
        def generate(self):
            genre = self.genre_cb.value()
            story = self.story_cb.value()
            number = self.gen_num.value()
        
        try:
            if self.genre_cb == True and self.story_cb == False:
                print response

        self.results_label.setText(response)









    
    
    app = QApplication(sys.argv)


window = MainWindow()
window.show()
    
app.exec()