#!/usr/bin/python
'''
 -*- coding: utf-8 -*-

# to extract the code and explanation part of an algorithm 

# it extract code for codeforces,codechef,geeksforgeeks.

# used beautifulsoup

# used pyqt for interface

# utf-8 encoding is done 

'''
import sys,inspect
from PyQt4 import QtGui,QtCore
import os
from test31 import *
import test31

class Example(QtGui.QWidget):
        
        def __init__(self):

                super(Example, self).__init__()

                self.dd=test31.app()

                self.obj=test31.app()

                self.initUI()
                
        def initUI(self):               
                self.text=""
               
                self.setGeometry(300, 300, 250, 150)        
                       
                self.setWindowTitle('  CODE DOWNLOAD MANAGER  ')

                self.btn = QtGui.QPushButton('Submit', self)

                self.btn.resize(self.btn.sizeHint())

                self.btn.move(630, 350)

                lbl1 = QtGui.QLabel(' CODE DOWNLOAD MANAGER ', self)

                lbl1.move(500, 100)

                font=QtGui.QFont();

                font.setBold(True)
                
                font.setPointSize(20)

                lbl1.setFont(font)

                lbl2 = QtGui.QLabel(' Enter URL: ', self)

                lbl2.move(450, 300)

                font.setBold(True)
                
                font.setPointSize(15)

                lbl2.setFont(font)

                self.le = QtGui.QLineEdit(self)

                self.le.move(610, 300)

                self.le.resize(300, 20)

                #self.center()

                self.btn2 = QtGui.QPushButton(' Click to check status ', self)

                self.btn2.move(580, 420)

                self.btn2.resize(175,25)

                self.btn2.clicked.connect(self.timerEvent)

                self.timer = QtCore.QBasicTimer()

                self.step = 0
                
                self.setGeometry(640, 440, 280, 170)
                
                
                self.setWindowIcon(QtGui.QIcon('web.png')) 

                self.showMaximized()

                self.btn.clicked.connect(self.cdm)

                self.show()
        

        def showDialog(self):
                
                self.text,ok = QtGui.QInputDialog.getText(self, 'Input box', 
                        'Enter URL:')

                if ok:
                        self.le.setText(str(self.text))
                                          
                
           
        def center(self):
                
                qr = self.frameGeometry()

                cp = QtGui.QDesktopWidget().availableGeometry().center()

                qr.moveCenter(cp)
                       
        def closeEvent(self, event):
                
                reply = QtGui.QMessageBox.question(self, 'Message',
                        "Are you sure to quit?", QtGui.QMessageBox.Yes | 
                        QtGui.QMessageBox.No, QtGui.QMessageBox.No)

                if reply == QtGui.QMessageBox.Yes:
                        event.accept()
                else:
                        event.ignore()        
        


        def timerEvent(self, e):
          
                global ff

                global gg

                (ff,gg)=self.obj.func()

                if(gg!=0):
                   self.step = ((ff + 1)/(gg))*100

                if self.step >= 100:
                        
                        self.timer.stop()

                        self.btn2.setText(' Download Completed ')

                        return
                
                else:
                     self.btn2.setText(' Error in Download ')     


        
        def cdm(self):
                   self.text=self.le.text()          
                   self.dd.cdm1(self.text)
                   


 



                
def main():
        
        app = QtGui.QApplication(sys.argv)

        ex = Example()

        sys.exit(app.exec_())


if __name__ == '__main__':
        main()
