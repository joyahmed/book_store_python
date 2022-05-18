from tkinter import *
from tkinter import messagebox
import sqlite3

con = sqlite3.connect('book_management.db')
cur = con.cursor()


class AddBook(Toplevel):
    def __init__(self):
        Toplevel.__init__(self)
        self.geometry('750x420+550+200')
        self.title = ('Add Book')
        self.iconbitmap("icons/icon.ico")
        self.resizable(False, False)

        # Frames

        # Top Frame
        self.top = Frame(self, height=150, bg='white')
        self.top.pack(fill=X)

        # Bottom Frame
        self.bottom_frame = Frame(self, height=420, bg='#00FFFF')
        self.bottom_frame.pack(fill=X)

        # Heading, image, and date
        self.top_image = PhotoImage(file='icons/addbook.png')
        self.top_image_label = Label(
            self.top, image=self.top_image, bg='white')
        self.top_image_label.place(x=120, y=10)
        self.heading = Label(
            self.top, text='Add Book', font='roboto 15 bold', fg='#5C5CFF', bg='white')
        self.heading.place(x=350, y=60)

        ########################################################################

        # Labels and Entries

        # Name
        self.name_label = Label(
            self.bottom_frame, text='Name     ', font='roboto 12 bold', fg='white', bg='#8A8AFF')
        self.name_label.place(x=80, y=60)

        self.name_entry = Entry(self.bottom_frame, width=30, bd=4)
        self.name_entry.place(x=170, y=60)

        # Author
        self.author_label = Label(
            self.bottom_frame, text='Author   ', font='roboto 12 bold', fg='white', bg='#8A8AFF')
        self.author_label.place(x=390, y=60)

        self.author_entry = Entry(self.bottom_frame, width=30, bd=4)
        self.author_entry.place(x=480, y=60)

        # Price
        self.price_label = Label(
            self.bottom_frame, text='Price      ', font='roboto 12 bold', fg='white', bg='#8A8AFF')
        self.price_label.place(x=80, y=120)

        self.price_entry = Entry(self.bottom_frame, width=30, bd=4)
        self.price_entry.place(x=170, y=120)

        # Quantity
        self.quantity_label = Label(
            self.bottom_frame, text='Quantity', font='roboto 12 bold', fg='white', bg='#8A8AFF')
        self.quantity_label.place(x=390, y=120)

        self.quantity_entry = Entry(self.bottom_frame, width=30, bd=4)
        self.quantity_entry.place(x=480, y=120)

        # Button
        button = Button(self.bottom_frame, text='Save Book',
                        font='roboto 12 bold', fg='white', bg='#5C5CFF', padx=20, pady=10, command=self.addBook)
        button.place(x=300, y=180)

    def addBook(self):
        name = self.name_entry.get()
        author = self.author_entry.get()
        price = self.price_entry.get()
        quantity = self.quantity_entry.get()

        if(name and author and price and quantity != ""):
            try:
                query = "INSERT INTO 'books' (name, author, price, quantity) VALUES(?, ?, ?, ?)"
                cur.execute(query, (name, author, price, quantity))
                con.commit()
                self.withdraw()
                messagebox.showinfo(
                    'Success', 'New book added to database successfully', icon='info')

            except:
                messagebox.showerror(
                    'Error', 'Couldn\'t add to database!', icon='warning')
                self.withdraw()
        else:
            messagebox.showerror(
                'Error', 'You must fill up all fields!', icon='warning')
