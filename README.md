Here is the exact documentation layout formatted to match your previous submission style, fully updated to reflect your new Python/PyQt5 final desktop application.

You can copy and paste this straight into your final report document!

---

# Water Tracker - Final Project

Course: SEN210 - User Interface Programming

Student: WALEED ALSAHLI

## Project Goal

The goal of this application is to provide a simple, intuitive desktop interface for users to monitor their hydration health directly from their active computer workstations. It addresses the problem of workplace dehydration by removing the friction of secondary mobile tracking devices, allowing students and office workers to quickly maintain consistent daily intake tracking habits.

## Features

* **Incremental Volume Logging: Users can log precise dynamic metric tracking segments via dedicated 250 ml and 500 ml entry buttons.
* **Real-Time Threshold Feedback:** A responsive status text field dynamically tracks incremental goal milestones and warns users when they need to consume more fluid.
* **Intake Metric Eraser:** A specialised control option instantly resets the application's memory variable back to 0 ml to initialise a fresh daily monitoring cycle.

## Implementation Strategy

* Developed using the **Python** language environment and cross-platform native UI rendering frameworks via **PyQt5 bindings**.
* Utilised specialised window layouts subclassing **`QWidget`** to coordinate and control user interface element frames.
* Configured structural linear layout formatting blocks (**`QVBoxLayout`**) to preserve cleanly aligned, vertically centered element distribution on desktop screens.
* Implemented the standard native **Qt Signals and Slots mechanism** to link hardware interface interactions straight to processing functions, keeping interface structures properly divided from mathematical counter adjustments.
