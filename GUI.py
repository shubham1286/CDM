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
from SOURCE import *
import SOURCE
class Example(QtGui.QWidget):
        
        def __init__(self):

                super(Example, self).__init__()

                self.dd=SOURCE.app()

                self.obj=SOURCE.app()

                self.initUI()
                
        def initUI(self):               
                self.text=""

                palette = QtGui.QPalette()

                self.setGeometry(300, 300, 250, 150)        
                       
                self.setWindowTitle('  CODE DOWNLOAD MANAGER  ')

                self.btn = QtGui.QPushButton('Submit', self)

                self.btn.resize(100,20)

                self.btn.move(660, 350)

                lbl1 = QtGui.QLabel(' CODE DOWNLOAD MANAGER ', self)

                lbl1.move(500, 100)

                font=QtGui.QFont();

                font.setBold(True)
                
                font.setPointSize(20)

                lbl1.setFont(font)

                palette.setColor(QtGui.QPalette.Foreground,QtCore.Qt.red)

                lbl1.setPalette(palette)

                lbl2 = QtGui.QLabel(' Enter URL: ', self)

                lbl2.move(450, 300)

                palette.setColor(QtGui.QPalette.Foreground,QtCore.Qt.red)

                lbl2.setPalette(palette)

                font.setBold(True)
                
                font.setPointSize(15)

                lbl2.setFont(font)

                lbl2.show()

                self.le = QtGui.QLineEdit(self)

                self.le.move(610, 300)

                self.le.resize(300, 20)

                palette.setColor(QtGui.QPalette.Background,QtCore.Qt.black)

                self.setPalette(palette)
              

                self.timer = QtCore.QBasicTimer()

                self.step = 0
                
                self.setGeometry(640, 440, 280, 170)
                
                
               # self.setWindowIcon(QtGui.QIcon('web.png')) 

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
          
                    


        
        def cdm(self):
                   global ff,gg
                   
                   self.filename = QtGui.QFileDialog.getSaveFileName(self, "Save file", "", "")
                      
                   self.text=self.le.text()          

                   (ff,gg)=self.dd.cdm1(self.text,self.filename)

                   if(gg!=0):
                      self.step = ((ff + 1)/(gg))*100

                   print self.step   

                   if self.step >= 100:
                        
                        self.timer.stop()
                        QtGui.QMessageBox.information(self,"Status of Download","CODE HAS BEEN SUCCESSFULLY DOWNLOADED :)")

                        return
                
                   else:
                       QtGui.QMessageBox.information(self,"Status of Download"," ERROR IN DOWNLOAD DUE TO NETWORK PROBLEM :(")
                       return
                   


 



                
def main():
        
        app = QtGui.QApplication(sys.argv)

        ex = Example()

        sys.exit(app.exec_())


if __name__ == '__main__':
        main()
