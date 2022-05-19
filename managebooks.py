from multiprocessing import managers
from tkinter import *
from tkinter import messagebox
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
        self.attributes("-topmost", True)

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

        books = cur.execute("SELECT * FROM books").fetchall()
        print(books)
        count = 0
        for book in books:
            self.list_box.insert(count, str(book[0])+'-'+book[1]+'-'+book[2])

            count += 1

        # Button
        button_add = Button(self.bottom_frame, text='Add',
                            width=12, font='roboto 12 bold', fg='#5C5CFF', command=self.funcAddBook)
        button_add.grid(row=0, column=2, sticky=N, padx=25, pady=10)

        button_update = Button(self.bottom_frame, text='Update',
                               width=12, font='roboto 12 bold', fg='#5C5CFF', command=self.funcUpdateBook)
        button_update.grid(row=0, column=2, sticky=N, padx=25, pady=50)

        button_detail = Button(self.bottom_frame, text='Detail',
                               width=12, font='roboto 12 bold', fg='#5C5CFF', command=self.functionBookDetail)
        button_detail.grid(row=0, column=2, sticky=N, padx=25, pady=90)

        button_delete = Button(self.bottom_frame, text='Delete',
                               width=12, font='roboto 12 bold', fg='#5C5CFF', command=self.funcDeleteBook)
        button_delete.grid(row=0, column=2, sticky=N, padx=25, pady=130)

    def funcAddBook(self):
        add = addbook.AddBook()
        self.withdraw()

    def funcUpdateBook(self):
        global book_id
        selected_item = self.list_box.curselection()
        book = self.list_box.get(selected_item)
        book_id = book.split('-')[0]
        updatepage = Update()
        self.withdraw()

    def functionBookDetail(self):
        global book_id
        selected_item = self.list_box.curselection()
        book = self.list_box.get(selected_item)
        book_id = book.split('-')[0]
        displaypage = Display()
        self.destroy()

    def funcDeleteBook(self):
        global book_id
        selected_item = self.list_box.curselection()
        book = self.list_box.get(selected_item)
        book_id = book.split('-')[0]

        message_box = messagebox.askquestion(
            'Warning', 'Are you sure you want to delete this book?', icon='warning', parent=self)

        if message_box == 'yes':
            try:
                cur.execute("DELETE FROM books WHERE id = ?", (book_id, ))
                con.commit()
                self.withdraw()
                messagebox.showinfo(
                    'Success', 'Book has been deleted!', parent=self)

            except:
                messagebox.showerror(
                    'Info', 'Book could not be deleted!', parent=self)
                self.withdraw()


class Update(Toplevel):
    def __init__(self):
        Toplevel.__init__(self)
        self.geometry('750x420+550+200')
        self.title = ('Update Book')
        self.resizable(False, False)
        self.iconbitmap("icons/icon.ico")
        self.attributes("-topmost", True)

        # Get Book from DB
        global book_id

        book = cur.execute(
            "SELECT * FROM books WHERE id = ?", (book_id, ))

        book_info = book.fetchall()
        print(book_info)
        self.book_id = book_info[0][0]
        self.book_name = book_info[0][1]
        self.book_author = book_info[0][2]
        self.book_price = book_info[0][3]
        self.book_quantity = book_info[0][4]

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
        self.top_image_label.place(x=110, y=10)
        self.heading = Label(
            self.top, text='Update Book', font='roboto 15 bold', fg='#5C5CFF', bg='white')
        self.heading.place(x=330, y=60)

        ########################################################################

        # Labels and Entries

        # Name
        self.name_label = Label(
            self.bottom_frame, text='  Name      ', font='roboto 12 bold', fg='white', bg='#8A8AFF')
        self.name_label.place(x=60, y=60)

        self.name_entry = Entry(self.bottom_frame, width=35, bd=4)
        self.name_entry.insert(0, self.book_name)
        self.name_entry.place(x=140, y=60)

        # Author
        self.author_label = Label(
            self.bottom_frame, text='  Author     ', font='roboto 12 bold', fg='white', bg='#8A8AFF')
        self.author_label.place(x=390, y=60)

        self.author_entry = Entry(self.bottom_frame, width=35, bd=4)
        self.author_entry.insert(0, self.book_author)
        self.author_entry.place(x=470, y=60)

        # Price
        self.price_label = Label(
            self.bottom_frame, text='  Price        ', font='roboto 12 bold', fg='white', bg='#8A8AFF')
        self.price_label.place(x=60, y=120)

        self.price_entry = Entry(self.bottom_frame, width=35, bd=4)
        self.price_entry.insert(0, self.book_price)
        self.price_entry.place(x=140, y=120)

        # Quantity
        self.quantity_label = Label(
            self.bottom_frame, text='  Quantity  ', font='roboto 12 bold', fg='white', bg='#8A8AFF')
        self.quantity_label.place(x=390, y=120)

        self.quantity_entry = Entry(self.bottom_frame, width=35, bd=4)
        self.quantity_entry.insert(0, self.book_quantity)
        self.quantity_entry.place(x=470, y=120)

        # Button
        button = Button(self.bottom_frame, text='Update Book',
                        font='roboto 12 bold', fg='white', bg='#5C5CFF', padx=20, pady=10, command=self.updateBook)
        button.place(x=300, y=180)

    def updateBook(self):
        id = self.book_id
        name = self.name_entry.get()
        author = self.author_entry.get()
        price = self.price_entry.get()
        quantity = self.quantity_entry.get()

        try:
            query = "UPDATE books SET name = ?, author = ?, price = ?, quantity = ? WHERE id = ?"
            cur.execute(query, (name, author, price, quantity, id))
            con.commit()
            messagebox.showinfo(
                'Success', 'Book has been updated!', icon='info')
            self.withdraw()

        except:
            messagebox.showinfo(
                'Warning', 'Book has not been updated!', icon='warning')
            self.withdraw()


class Display(Toplevel):
    def __init__(self):
        Toplevel.__init__(self)
        self.geometry('760x360+550+200')
        self.title('Book Detail')
        self.iconbitmap("icons/icon.ico")
        self.resizable(False, False)
        self.attributes("-topmost", True)

        # Get Book from DB
        global book_id

        book = cur.execute(
            "SELECT * FROM books WHERE id = ?", (book_id, ))

        book_info = book.fetchall()
        print(book_info)
        self.book_id = book_info[0][0]
        self.book_name = book_info[0][1]
        self.book_author = book_info[0][2]
        self.book_price = book_info[0][3]
        self.book_quantity = book_info[0][4]

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
        self.top_image_label.place(x=110, y=10)
        self.heading = Label(
            self.top, text='Book Detail', font='roboto 15 bold', fg='#5C5CFF', bg='white')
        self.heading.place(x=320, y=60)

        ########################################################################

        # Labels and Entries

        # Name
        self.name_label = Label(
            self.bottom_frame, text='  Name      ', font='roboto 12 bold', fg='white', bg='#8A8AFF')
        self.name_label.place(x=50, y=60)

        self.name_entry = Entry(self.bottom_frame, width=40, bd=4)
        self.name_entry.insert(0, self.book_name)
        self.name_entry.config(state='disabled')
        self.name_entry.place(x=120, y=60)

        # Author
        self.author_label = Label(
            self.bottom_frame, text='  Author     ', font='roboto 12 bold', fg='white', bg='#8A8AFF')
        self.author_label.place(x=380, y=60)

        self.author_entry = Entry(self.bottom_frame, width=40, bd=4)
        self.author_entry.insert(0, self.book_author)
        self.author_entry.config(state='disabled')
        self.author_entry.place(x=460, y=60)

        # Price
        self.price_label = Label(
            self.bottom_frame, text='  Price       ', font='roboto 12 bold', fg='white', bg='#8A8AFF')
        self.price_label.place(x=50, y=120)

        self.price_entry = Entry(self.bottom_frame, width=40, bd=4)
        self.price_entry.insert(0, self.book_price)
        self.price_entry.config(state='disabled')
        self.price_entry.place(x=120, y=120)

        # Quantity
        self.quantity_label = Label(
            self.bottom_frame, text='  Quantity  ', font='roboto 12 bold', fg='white', bg='#8A8AFF')
        self.quantity_label.place(x=380, y=120)

        self.quantity_entry = Entry(self.bottom_frame, width=40, bd=4)
        self.quantity_entry.insert(0, self.book_quantity)
        self.quantity_entry.config(state='disabled')
        self.quantity_entry.place(x=460, y=120)
