import wx
import time
import random
from tkinter import *
import tkinter.messagebox

import socket

class MainWindow:

  def __init__(self):
        self.frame = Tk()
        self.label_name = Label(self.frame, text="name:")
        self.label_age = Label(self.frame, text="age:")
        self.label_sex = Label(self.frame, text="sex:")

        self.text_name = Text(self.frame, height="1", width=30)
        self.text_age = Text(self.frame, height="1", width=30)
        self.text_sex = Text(self.frame, height="1", width=30)

        self.label_name.grid(row=0, column=0)
        self.label_age.grid(row=1, column=0)
        self.label_sex.grid(row=2, column=0)

        self.button_ok = Button(self.frame, text="ok", width=10)
        self.button_cancel = Button(self.frame, text="cancel", width=10)

        self.text_name.grid(row=0, column=1)
        self.text_age.grid(row=1, column=1)
        self.text_sex.grid(row=2, column=1)

        self.button_ok.grid(row=3, column=0)
        self.button_cancel.grid(row=3, column=1)

        self.frame.mainloop()


window = MainWindow()

# app = wx.App()
# win = wx.Frame(None,title='test',size = (400,300))
# win.Show()
# loadButton = wx.Button(win,label = 'open',pos = (200,5),size =(80,25))

# fileName = wx.TextCtrl(win,pos=(5,5),size = (210,25))
# contents = wx.TextCtrl(win, pos=(5, 35), size = (390, 260), style=wx.TE_MULTILINE)
# app.MainLoop()
