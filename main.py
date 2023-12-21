"""Starting script for the CBS checker
launches a window
"""

import sys

from PyQt6.QtWidgets import QApplication
from gui import MainWindow

if __name__ == "__main__":
    program = QApplication(sys.argv)
    window = MainWindow()
    window.show()

    program.exec()
