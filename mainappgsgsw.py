import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QTabWidget, QLabel, QMainWindow, QHBoxLayout, QPushButton, QCheckBox, QSlider, QSpinBox

class MainApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Main App with 3 Tabs')
        self.setGeometry(100, 100, 800, 600)
        
        self.dark_mode = False  # Track the dark mode status

        self.init_ui()

    def init_ui(self):
        # Create the main widget and layout
        main_widget = QWidget(self)
        main_layout = QHBoxLayout(main_widget)

        # Create a Tab Widget for the tabs
        self.tabs = QTabWidget()
        self.tabs.addTab(self.create_tab("Tab 1"), "Tab 1")
        self.tabs.addTab(self.create_tab("Tab 2"), "Tab 2")
        self.tabs.addTab(self.create_tab("Tab 3"), "Tab 3")
        self.tabs.addTab(self.create_settings_tab(), "Settings")

        # Add the tab widget to the layout
        main_layout.addWidget(self.tabs)

        # Set the central widget
        self.setCentralWidget(main_widget)

    def create_tab(self, tab_name):
        # Create a QWidget for each tab
        tab = QWidget()
        layout = QVBoxLayout()

        # Label for the tab
        label = QLabel(f'Welcome to {tab_name}', self)
        layout.addWidget(label)

        # Button for each tab
        button = QPushButton(f'Click me in {tab_name}', self)
        button.clicked.connect(lambda: self.on_button_click(tab_name))
        layout.addWidget(button)

        # Additional buttons for more interactivity
        extra_button = QPushButton(f'Extra Action in {tab_name}', self)
        extra_button.clicked.connect(lambda: self.on_extra_button_click(tab_name))
        layout.addWidget(extra_button)

        tab.setLayout(layout)
        return tab

    def on_button_click(self, tab_name):
        # Function to be called when the primary button in the tab is clicked
        print(f'Primary button clicked in {tab_name}')

    def on_extra_button_click(self, tab_name):
        # Function to be called when the extra button in the tab is clicked
        print(f'Extra button clicked in {tab_name}')

    def create_settings_tab(self):
        # Create the Settings tab
        settings_tab = QWidget()
        settings_layout = QVBoxLayout()

        # Dark mode toggle
        self.dark_mode_checkbox = QCheckBox("Enable Dark Mode", self)
        self.dark_mode_checkbox.stateChanged.connect(self.toggle_dark_mode)
        settings_layout.addWidget(self.dark_mode_checkbox)

        # Window size slider
        size_label = QLabel("Adjust Window Size (Width):", self)
        self.size_slider = QSlider(Qt.Horizontal, self)
        self.size_slider.setMinimum(400)
        self.size_slider.setMaximum(1200)
        self.size_slider.setValue(self.width())
        self.size_slider.valueChanged.connect(self.adjust_window_size)
        settings_layout.addWidget(size_label)
        settings_layout.addWidget(self.size_slider)

        # Window position spinner (set top margin or something)
        position_label = QLabel("Set Window Top Margin:", self)
        self.position_spinner = QSpinBox(self)
        self.position_spinner.setRange(0, 200)
        self.position_spinner.setValue(self.y())
        self.position_spinner.valueChanged.connect(self.adjust_window_position)
        settings_layout.addWidget(position_label)
        settings_layout.addWidget(self.position_spinner)

        settings_tab.setLayout(settings_layout)
        return settings_tab

    def toggle_dark_mode(self):
        # Toggle dark mode
        self.dark_mode = not self.dark_mode
        self.update_theme()

    def update_theme(self):
        # Update the theme based on dark mode status
        if self.dark_mode:
            self.setStyleSheet("""
                QWidget {
                    background-color: #2e2e2e;
                    color: white;
                }
                QPushButton {
                    background-color: #444;
                    color: white;
                }
                QLabel {
                    color: white;
                }
            """)
        else:
            self.setStyleSheet("""
                QWidget {
                    background-color: white;
                    color: black;
                }
                QPushButton {
                    background-color: #f0f0f0;
                    color: black;
                }
                QLabel {
                    color: black;
                }
            """)

    def adjust_window_size(self):
        # Adjust the window width based on the slider value
        new_width = self.size_slider.value()
        self.resize(new_width, self.height())

    def adjust_window_position(self):
        # Adjust the window top position based on the spin box value
        new_top = self.position_spinner.value()
        self.move(self.x(), new_top)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_app = MainApp()
    main_app.show()
    sys.exit(app.exec_())
