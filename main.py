import sys
from PyQt5 import QtWidgets, QtCore

from settings import settings
from app.gui.windows.MainWindow import MainWindow


def main():
    app = QtWidgets.QApplication(sys.argv)
    file = QtCore.QFile(str(settings.styles_path.joinpath("global.css")))
    file.open(QtCore.QFile.ReadOnly | QtCore.QFile.Text)
    stream = QtCore.QTextStream(file)
    app.setStyleSheet(stream.readAll())
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

main()
