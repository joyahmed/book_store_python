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
            self.top, text='Book Store Management App', font='roboto 15 bold', fg='#32CD32', bg='white')
        self.heading.place(x=260, y=60)
        self.date_label = Label(
            self.top, text='Date: ' + str(date), font='roboto 12 bold', bg='white', fg='#32CD32')
        self.date_label.place(x=490, y=10)