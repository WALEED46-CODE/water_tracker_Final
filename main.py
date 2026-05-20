import sys
from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QLabel,
    QPushButton,
    QVBoxLayout
)

# Main Window Class
class WaterTracker(QWidget):

    def __init__(self):
        super().__init__()

        # Starting amount of water
        self.water_amount = 0

        # Window settings
        self.setWindowTitle("Water Health Tracker")
        self.setGeometry(200, 200, 300, 250)

        # Title label
        self.title = QLabel("Daily Water Tracker")

        # Water amount label
        self.label = QLabel("Water Drank: 0 ml")

        # Health message label
        self.message = QLabel("Drink more water!")

        # Buttons
        self.button250 = QPushButton("Add 250 ml")
        self.button500 = QPushButton("Add 500 ml")
        self.resetButton = QPushButton("Reset")

        # Connect buttons to functions
        self.button250.clicked.connect(self.add_250)
        self.button500.clicked.connect(self.add_500)
        self.resetButton.clicked.connect(self.reset_water)

        # Layout
        layout = QVBoxLayout()

        layout.addWidget(self.title)
        layout.addWidget(self.label)
        layout.addWidget(self.message)
        layout.addWidget(self.button250)
        layout.addWidget(self.button500)
        layout.addWidget(self.resetButton)

        self.setLayout(layout)

    # Add 250 ml
    def add_250(self):
        self.water_amount += 250
        self.update_display()

    # Add 500 ml
    def add_500(self):
        self.water_amount += 500
        self.update_display()

    # Reset water amount
    def reset_water(self):
        self.water_amount = 0
        self.update_display()

    # Update labels
    def update_display(self):

        self.label.setText(
            f"Water Drank: {self.water_amount} ml"
        )

        # Simple health condition
        if self.water_amount >= 2000:
            self.message.setText("Great! Healthy amount reached.")
        else:
            self.message.setText("Drink more water!")

# Run application
app = QApplication(sys.argv)

window = WaterTracker()
window.show()

sys.exit(app.exec_())