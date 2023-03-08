from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog, QLineEdit
import os
import shutil

import sys

from output import Ui_MainWindow  # Replace with the name of your generated UI file


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    count = 0
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        # upload buttons clicked
        self.browse1.clicked.connect(self.on_button1_clicked)
        self.browse2.clicked.connect(self.on_button2_clicked)
        self.browse3.clicked.connect(self.on_button3_clicked)

        # OK button
        self.ok.clicked.connect(self.on_ok_clicked)
        # Cancel button
        self.cancel.clicked.connect(self.on_cancel_clicked)

    def on_button1_clicked(self):
        directory = QFileDialog.getExistingDirectory(self, "Select Directory")
        if directory:
            # Do something with the selected directory
            print(f"Selected directory: {directory}")
            self.srcpath.setText(str(directory))
    
    def on_button2_clicked(self):
        directory = QFileDialog.getExistingDirectory(self, "Select Directory")
        if directory:
            # Do something with the selected directory
            print(f"Selected directory: {directory}")
            self.destpath.setText(str(directory))

    def on_button3_clicked(self):
        filename, _ = QFileDialog.getOpenFileName(self, "Open File", "", "All Files (*);;Text Files (*.txt)")
        if filename:
            # Do something with the selected file
            print(f"Selected file: {filename}")
            self.textfile.setText(str(filename))
    
    
    def on_ok_clicked(self):
        if self.count==0:
            self.count= self.count+1
            src = self.srcpath.toPlainText()
            dest = self.destpath.toPlainText()
            textfile = self.textfile.toPlainText()
            
            # Open the text file containing filenames
            with open(textfile) as f:
                # Loop through each line in the file
                for line in f:
                    # Strip any whitespace from the line
                    filename = line.strip()

                    # print(filename)
                    # Build the full source and destination paths
                    source_path = os.path.join(src, filename)
                    destination_path = os.path.join(dest, filename)

                    # Move the file
                    shutil.copy(source_path, destination_path)
                    for widget in QtWidgets.QApplication.allWidgets():
                        if isinstance(widget, QtWidgets.QMainWindow):
                            widget.close()
    
    def on_cancel_clicked(self):
        print("Cancel clicked")
        for widget in QtWidgets.QApplication.allWidgets():
            if isinstance(widget, QtWidgets.QMainWindow):
                widget.close()

    

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
