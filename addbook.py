from tkinter import *
import sqlite3

con = sqlite3.connect('book_management.db')
cur = con.cursor()


class AddBook(Toplevel):
    def __init__(self):
        Toplevel.__init__(self)
        self.geometry('650x650+620+200')
        self.title = ('Add Book')
        self.resizable(False, False)
