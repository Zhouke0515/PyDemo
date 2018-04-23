import tkinter.messagebox as messagebox
from tkinter import *


class App(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack
        self.create_widgets()

    def create_widgets(self):
        self.helloLabel = Label(self, text='Hello, World')
        self.helloLabel.pack
        self.quitButton = Button(self, text='quit', command=self.quit())
        self.quitButton.pack

    def hello(self):
        name = self.nameInput.get() or 'world'
        messagebox.showinfo('Message', 'Hello,%s' % name)


app = App()
app.master.title('Hello,World')
app.mainloop()
