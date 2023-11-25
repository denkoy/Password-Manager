from tkinter import Tk,Button,Canvas,PhotoImage
from buttons import Data

class Window:
    def __init__(self):
        self.window = Tk()
        self.window.title("Password Manager")
        self.window.geometry("500x500")
        self.window.config(bg="gray")

        self.canvas = Canvas(width=200,height=200,bg="gray",highlightthickness=0)
        image = PhotoImage(file="logo.png")
        self.canvas.create_image(100,100,image=image)
        self.canvas.pack()

        self.data=Data()


        self.window.mainloop()
