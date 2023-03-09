from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog, QLineEdit
import os
import shutil
import time
import sys

from mainwindow import Ui_MainWindow  as window1 # Replace with the name of your generated UI file
from alert import Ui_MainWindow  as window2 # Replace with the name of your generated UI file

class AlertWindow(QtWidgets.QMainWindow, window2):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        # OK button
        self.ok_2.clicked.connect(self.on_ok2_clicked)

    def on_ok2_clicked(self):
        print("OK clicked")
        for widget in QtWidgets.QApplication.allWidgets():
            if isinstance(widget, QtWidgets.QMainWindow):
                widget.close()

class MainWindow(QtWidgets.QMainWindow, window1):
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
        self.ok.setEnabled(False)
        # Cancel button
        self.cancel.clicked.connect(self.on_cancel_clicked)

    def on_button1_clicked(self):
        directory = QFileDialog.getExistingDirectory(self, "Select Directory")
        if directory:
            # Do something with the selected directory
            # print(f"Selected directory: {directory}")
            self.srcpath.setText(str(directory))
    
    def on_button2_clicked(self):
        directory = QFileDialog.getExistingDirectory(self, "Select Directory")
        if directory:
            # Do something with the selected directory
            # print(f"Selected directory: {directory}")
            self.destpath.setText(str(directory))

    def on_button3_clicked(self):
        filename, _ = QFileDialog.getOpenFileName(self, "Select File", "", "Text files (*.txt)")
        if filename:
            # Do something with the selected file
            # print(f"Selected file: {filename}")
            self.textfile.setText(str(filename))
            src = self.srcpath.toPlainText()
            dest = self.destpath.toPlainText()
            if src!='' and dest!='':
                self.ok.setEnabled(True)
    
    
    def on_ok_clicked(self):
        if self.count==0:
            self.count= self.count+1
            src = self.srcpath.toPlainText()
            dest = self.destpath.toPlainText()
            textfile = self.textfile.toPlainText()
            
            self.successmsg.setText("Files Copying..........")
            
            if src=='' or dest=='' or textfile=='':
                print("Enter Data First")
                self.count=0
            else:
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

                        if os.path.exists(source_path):
                            print("File exists")
                            shutil.copy(source_path, destination_path)
                        else:
                            print("File does not exist")
                        # Move the file
                # newWindow = AlertWindow()
                # newWindow.show()
                time.sleep(3)
                self.successmsg.setText("Files Copied Successfully")
                self.ok.setEnabled(False)
                self.cancel.setText('Close')
            
    
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
