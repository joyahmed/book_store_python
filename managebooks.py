from multiprocessing import managers
from tkinter import *
import addbook
import sqlite3

con = sqlite3.connect('book_management.db')
cur = con.cursor()


class ManageBooks(Toplevel):
    def __init__(self):
        Toplevel.__init__(self)
        self.geometry('650x650+620+200')
        self.title = ('Manage Books')
        self.iconbitmap("icons/icon.ico")
        self.resizable(False, False)

        # Frames

        # Top Frame
        self.top = Frame(self, height=150, bg='white')
        self.top.pack(fill=X)

        # Bottom Frame

        self.bottom_frame = Frame(self, height=500, bg='#00FFFF')
        self.bottom_frame.pack(fill=X)

        # Heading, image, and date
        self.top_image = PhotoImage(file='icons/addbook.png')
        self.top_image_label = Label(
            self.top, image=self.top_image, bg='white')
        self.top_image_label.place(x=120, y=10)
        self.heading = Label(
            self.top, text='Manage Books', font='roboto 15 bold', fg='#5C5CFF', bg='white')
        self.heading.place(x=260, y=60)

        # Scrollbar
        self.scroll_bar = Scrollbar(self.bottom_frame, orient=VERTICAL)

        # Listbox
        self.list_box = Listbox(self.bottom_frame, width=70, height=31)
        self.list_box.grid(row=0, column=0, padx=(40, 0))
        self.scroll_bar.config(command=self.list_box.yview)
        self.list_box.config(yscrollcommand=self.scroll_bar.set)
        self.scroll_bar.grid(row=0, column=1, sticky=N+S)

        # Button
        button_add = Button(self.bottom_frame, text='Add',
                            width=12, font='roboto 12 bold', fg='#5C5CFF', command=self.funcAddBook)
        button_add.grid(row=0, column=2, sticky=N, padx=25, pady=10)

        button_update = Button(self.bottom_frame, text='Update',
                               width=12, font='roboto 12 bold', fg='#5C5CFF')
        button_update.grid(row=0, column=2, sticky=N, padx=25, pady=50)

        button_display = Button(self.bottom_frame, text='Display',
                                width=12, font='roboto 12 bold', fg='#5C5CFF')
        button_display.grid(row=0, column=2, sticky=N, padx=25, pady=90)

        button_delete = Button(self.bottom_frame, text='Delete',
                               width=12, font='roboto 12 bold', fg='#5C5CFF')
        button_delete.grid(row=0, column=2, sticky=N, padx=25, pady=130)

    def funcAddBook(self):
        add = addbook.AddBook()
