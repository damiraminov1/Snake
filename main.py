import sys
from PyQt5 import QtWidgets

from app.gui.windows.MainWindow import MainWindow


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

main()
