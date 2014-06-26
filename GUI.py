#!/usr/bin/python
# -*- coding: utf-8 -*-

'''

# to extract the code and explanation part of an algorithm 

# it extract code for codeforces,codechef,geeksforgeeks.

# used beautifulsoup

# used Tkinter for interface

# utf-8 encoding is done 

'''
from PIL import Image, ImageTk

from Tkinter import Tk, Label, BOTH,TOP,Text,W,N,E,S,END

from ttk import  Style,Button,Frame

import tkFileDialog

import tkMessageBox

import SOURCE

from SOURCE import *

import sys,inspect,time

class Example(Frame):
  
    def __init__(self, parent):

        Frame.__init__(self, parent)   
         
        self.parent = parent

        self.dd=SOURCE.app()
        
        self.initUI()
   
    def initUI(self):
        
        root.protocol("WM_DELETE_WINDOW", self.handler)
        

       # window=Tkinter.Tk()

        self.parent.title("Code Download Manager")

        self.pack(fill=BOTH, expand=1)

        self.centerWindow()

        style = Style()

       # style.configure("TFrame", background="#333")

        bard = Image.open("globe.jpg")

        bardejov = ImageTk.PhotoImage(bard)

        label1 = Label(self, image=bardejov)

        label1.image = bardejov

        label1.place(x=0,y=0)

     


        self.b=Button(self, text="SUBMIT",command=self.cdm1)

        self.b.place(x=640,y=330)

        self.lbl = Label(self, text="ENTER URL : ",fg="black",bg="green", font="Times 12 bold")

        self.lbl.place(x=420,y=297)

        self.area = Text(self)

        self.area.place(x=550,y=300,width=300, height=20)

        self.lb2 = Label(self, text="  CODE DOWNLOAD MANAGER ",fg="black",bg="white" ,font="Times 20 bold",anchor="center")

        self.lb2.place(x=450,y=60)

       # window.mainloop()
        root.wm_iconbitmap('dsf.ico')

    def centerWindow(self):

        sw = self.parent.winfo_screenwidth()

        sh = self.parent.winfo_screenheight()

       # print sw

        #print sh

        self.parent.geometry('%dx%d+%d+%d' % (sw, sh, 0, 0))


    def handler(self):

      if tkMessageBox.askokcancel("Quit?", "Are you sure you want to quit?"):

         root.destroy()


    def cdm1(self):

                   self.file_opt = options = {}

                   self.text= self.area.get("0.0",END)


                   global ff,gg

                   
                   self.filename =tkFileDialog.asksaveasfilename(**self.file_opt)

#                   print self.filename
                      

                   (ff,gg)=self.dd.cdm1(self.text,self.filename)


                   self.step=0
       

                   if(gg!=0):

                      self.step = ((ff + 1)/(gg))*100
   

                   if self.step >= 100:
                        
                      #  self.timer.stop()

                        tkMessageBox.showinfo("Status of Download","CODE HAS BEEN SUCCESSFULLY DOWNLOADED :)")

                        return
                
                   else:
                        tkMessageBox.showinfo("Status of Download"," ERROR IN DOWNLOAD DUE TO NETWORK PROBLEM :(")
                        return
                     
        
def main():
    global root

    root = Tk()

    root.geometry("280x170+640+440")

    app = Example(root)

    root.mainloop()  


if __name__ == '__main__':
    
    main()
