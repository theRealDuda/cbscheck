"""Module containing all the gui operations for the CBS"""
from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import (QMainWindow,
                            QPushButton,
                            QLabel,
                            QLineEdit,
                            QVBoxLayout,
                            QWidget)
from cbs import is_cbs, need_to_move

class AboutWindow(QMainWindow):
    """
    Defines the about window. Just text and general behaviour.
    Args:
        QMainWindow (QMainWindow_): The about window.
    """
    def __init__(self):
        super().__init__()
        self.setStyleSheet("background-color: white;")
        self.setWindowTitle("About.")

        self.setFixedSize(QSize(400, 320))

        self.info = QLabel()

        self.info.setText(
            "This is a program made for checking brace sequences for correctness."
            "\nTo use it: "
            "\nPut the sequence in."
            "\nAnd press Enter or the Check button."
            "\nEnjoy!")
        layout = QVBoxLayout()

        layout.addWidget(self.info,0,Qt.AlignmentFlag.AlignTop|Qt.AlignmentFlag.AlignHCenter)

        container = QWidget()
        container.setLayout(layout)

        self.setCentralWidget(container)

def start_about() -> None:
    """Function used for staring the about
    window in a way that saves it from the GC
    I think it is needed for the about window
    """
    about = AboutWindow()
    return about

class MainWindow(QMainWindow):
    """The main window class.
    Handles input, parsing is delegated to the cbs module.
    Args:
        QMainWindow (QMainWindow): The main window.
    """
    def __init__(self):
        """Sets up constants, widgets and handles signals.
        Those signals are:
        button.clicked.connect(self.get_result) which is the check button

        self.about_button.clicked.connect(self.show_about) which is the about window

        input.returnPressed.connect(self.get_result) for input using the return key
        """
        super().__init__()

        self.about_wnd = AboutWindow()

        self.setStyleSheet("background-color: white;")
        self.setWindowTitle("CBSCheck v1")

        self.setFixedSize(QSize(800, 640))

        self.help_text = QLabel()
        self.help_text.setText("To use the program:"
            "\nInput the brace sequence in the field"
            "below and press enter or the check button.")
        self.help_text.setAlignment(Qt.AlignmentFlag.AlignHCenter)

        self.label = QLabel()

        self.button = QPushButton()
        self.button.setText("Check")

        self.about_button = QPushButton()
        self.about_button.setText("About")

        self.input = QLineEdit()

        layout = QVBoxLayout()

        layout.addWidget(self.help_text,0,Qt.AlignmentFlag.AlignHCenter)
        layout.addWidget(self.input,0,Qt.AlignmentFlag.AlignTop)
        layout.addWidget(self.label,1,Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignTop)
        layout.addWidget(self.about_button,1,\
            Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignBottom)
        layout.addWidget(self.button,1, Qt.AlignmentFlag.AlignBottom)

        self.button.clicked.connect(self.get_result)

        self.about_button.clicked.connect(self.show_about)
        self.input.returnPressed.connect(self.get_result)

        container = QWidget()
        container.setLayout(layout)

        self.setCentralWidget(container)

    def get_result(self):
        """Used for getting and setting
         the result of the checks on the input
         maybe a different name is needed?
         """
        if is_cbs(self.input.text().strip()):
            res = "This is a correct brace sequence!"
        else:
            changes = str(need_to_move(self.input.text().strip()))
            if changes != "1":
                res = "This is not a correct brace sequence. "\
                + changes\
                + " braces need to be moved for this to be a CBS."
            else:
                res = "This is not a correct brace sequence."\
                + changes\
                + " brace needs to be moved for this to be a CBS."


        self.label.setText(res)

    def show_about(self):
        """Function used for getting the
             about window up and running.
             Very important!
             """
        self.about_wnd = start_about()
        self.about_wnd.show()
