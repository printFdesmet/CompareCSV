"""
    TODO: TKinter to create a GUI for the application.
    The GUI should have the following:
    TODO: Create a button to select the first file.
    TODO: Create a textbox to view the selected file. READ-ONLY
    TODO: Create a button to select the second file.
    TODO: Create a textbox to view the selected file. READ-ONLY
    TODO: Create a button to execute comparison.
    TODO: Create an output box that shows the unique headers.
"""

import tkinter as tk
from tkinter import ttk


class GUI(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.hi_there = ttk.Button(self)
        self.hi_there["text"] = "Hello world"
        self.hi_there["command"] = self.say_hi
        self.hi_there.pack(side="top")

    def say_hi(self):
        print("hi there, everyone.")

root = tk.Tk()
app = GUI(master=root)
app.mainloop()
