from tkinter import *
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

        self.bottom = Frame(root, height=500, bg='#adff2f')
        self.bottom.pack(fill=X)

        # Heading, image, and date
        self.top_image = PhotoImage(file='icons/addbook.png')
        self.top_image_label = Label(
            self.top, image=self.top_image, bg='white')
        self.top_image_label.place(x=120, y=10)
        self.heading = Label(
            self.top, text='Book Store Management App', font='roboto 15 bold', fg='#ffa500', bg='white')
        self.heading.place(x=260, y=60)
        self.date_label = Label(
            self.top, text='Date: ' + str(date), font='roboto 12 bold', bg='white', fg='#ffa500')
        self.date_label.place(x=490, y=10)


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
