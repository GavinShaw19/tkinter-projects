import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk


class FoodViewer:

    def __init__(self, root):
        self.root = root
        self.root.title("Food Viewer")
        self.root.geometry("400x300")

        
        self.img_frame = Frame(self.root)
        self.img_frame.pack()

        self.rbdBtn_frame = Frame(self.root)
        self.rbdBtn_frame.pack()

        
        self.img1 = Image.open("chicken.jpg").resize((400, 230))
        self.imgOne = ImageTk.PhotoImage(self.img1)

        self.img2 = Image.open("pie.jpg").resize((400, 230))
        self.imgTwo = ImageTk.PhotoImage(self.img2)

        self.img3 = Image.open("pizza.jpg").resize((400, 230))
        self.imgThree = ImageTk.PhotoImage(self.img3)

        self.img4 = Image.open("steak.jpg").resize((400, 230))
        self.imgFour = ImageTk.PhotoImage(self.img4)

        
        self.lbl = Label(self.img_frame, image=self.imgOne)
        self.lbl.pack()

        
        self.var = IntVar()
        self.var.set(1)

        
        self.radio_a = Radiobutton(
            self.rbdBtn_frame, text="Chicken",
            variable=self.var, value=1,
            command=self.on_radio_select
        )
        self.radio_a.pack(side="left", padx=10)

        self.radio_b = Radiobutton(
            self.rbdBtn_frame, text="Pie",
            variable=self.var, value=2,
            command=self.on_radio_select
        )
        self.radio_b.pack(side="left", padx=10)

        self.radio_c = Radiobutton(
            self.rbdBtn_frame, text="Pizza",
            variable=self.var, value=3,
            command=self.on_radio_select
        )
        self.radio_c.pack(side="left", padx=10)

        self.radio_d = Radiobutton(
            self.rbdBtn_frame, text="Steak",
            variable=self.var, value=4,
            command=self.on_radio_select
        )
        self.radio_d.pack(side="left", padx=10)

    
    def on_radio_select(self):
        choice = self.var.get()

        if choice == 1:
            self.lbl.config(image=self.imgOne)
        elif choice == 2:
            self.lbl.config(image=self.imgTwo)
        elif choice == 3:
            self.lbl.config(image=self.imgThree)
        elif choice == 4:
            self.lbl.config(image=self.imgFour)



if __name__ == "__main__":
    root = tk.Tk()
    app = FoodViewer(root)
    root.mainloop()
