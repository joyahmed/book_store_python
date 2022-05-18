from tkinter import *
import addbook
import managebooks
from datetime import date

today = date.today()

date = today.strftime("%B %d, %Y")


class App(object):
    def __init__(self, root):
        self.root = root

        # Frames

        # Top Frame
        self.top = Frame(root, height=150, bg='white')
        self.top.pack(fill=X)

        # Bottom Frame

        self.bottom = Frame(root, height=500, bg='#00FFFF')
        self.bottom.pack(fill=X)

        # Heading, image, and date
        self.top_image = PhotoImage(file='icons/addbook.png')
        self.top_image_label = Label(
            self.top, image=self.top_image, bg='white')
        self.top_image_label.place(x=120, y=10)
        self.heading = Label(
            self.top, text='Book Store Management App', font='roboto 15 bold', fg='#5C5CFF', bg='white')
        self.heading.place(x=260, y=60)
        self.date_label = Label(
            self.top, text='Date: ' + str(date), font='roboto 12 bold', bg='white', fg='#5C5CFF')
        self.date_label.place(x=490, y=10)

        # Update Button

        self.add_button_icon = PhotoImage(file='icons/add_book.png')
        self.add_button = Button(
            self.bottom, text='        Add Books           ', font='roboto 12 bold', fg='#5C5CFF', command=self.openAddBook)
        self.add_button.config(
            image=self.add_button_icon, compound=LEFT)
        self.add_button.place(x=220, y=100)

        # Book List Button

        self.list_button_icon = PhotoImage(file='icons/booklist.png')
        self.list_button = Button(
            self.bottom, text='     Manage Books      ', font='roboto 12 bold', pady=8, fg='#5C5CFF', command=self.openManageBooks)
        self.list_button.config(
            image=self.list_button_icon, compound=LEFT)
        self.list_button.place(x=220, y=200)

    def openAddBook(self):
        newbook = addbook.AddBook()

    def openManageBooks(self):
        allbooks = managebooks.ManageBooks()


def main():
    root = Tk()
    app = App(root)
    root.title('Book Store Management App')
    root.geometry('650x550+350+200')
    root.iconbitmap("icons/icon.ico")
    root.resizable(False, False)
    root.mainloop()


if __name__ == '__main__':
    main()
