import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("tkinter Form")
root.geometry("500x300")

lblFr = tk.LabelFrame(root, text="Personal Information")
lblFr.pack(padx=15, pady=15, fill="x")

brand_bg = "blue"
brand_fg = "white"

lblFirst = tk.Label(lblFr, text="*First Name:", bg=brand_bg, fg=brand_fg)
lblFirst.grid(column=0, row=0, padx=6, pady=6, sticky="e")

entFirst = tk.Entry(lblFr)
entFirst.grid(column=1, row=0, padx=6, pady=6, sticky="w")

lblLast = tk.Label(lblFr, text="*Last Name:", bg=brand_bg, fg=brand_fg)
lblLast.grid(column=0, row=1, padx=6, pady=6, sticky="e")

entLast = tk.Entry(lblFr)
entLast.grid(column=1, row=1, padx=6, pady=6, sticky="w")

lblEmail = tk.Label(lblFr, text="Email:")
lblEmail.grid(column=0, row=2, padx=6, pady=6, sticky="e")

entEmail = tk.Entry(lblFr)
entEmail.grid(column=1, row=2, padx=6, pady=6, sticky="w")

lblPhone = tk.Label(lblFr, text="Phone:")
lblPhone.grid(column=0, row=3, padx=6, pady=6, sticky="e")

entPhone = tk.Entry(lblFr)
entPhone.grid(column=1, row=3, padx=6, pady=6, sticky="w")

fraButtons = tk.Frame(root)
fraButtons.pack(pady=10)

def displayData():
    first = entFirst.get()
    last = entLast.get()
    email = entEmail.get()
    phone = entPhone.get()

    msg = (
        f"Welcome to tkinter, {first}\n"
        f"You entered:\n"
        f"Name: {first} {last}\n"
        f"Email: {email}\n"
        f"Phone: {phone}"
    )

    messagebox.showinfo("Information", msg)

def Clear():
    entFirst.delete(0, tk.END)
    entLast.delete(0, tk.END)
    entEmail.delete(0, tk.END)
    entPhone.delete(0, tk.END)

btnS = tk.Button(fraButtons, text="Submit", width=5, command=displayData)
btnS.pack(side=tk.LEFT, padx=8)

btnR = tk.Button(fraButtons, text="Reset", width=5, command=Clear)
btnR.pack(side=tk.LEFT, padx=8)

btnQ = tk.Button(fraButtons, text="Quit", width=5, command=root.destroy)
btnQ.pack(side=tk.LEFT, padx=8)

root.mainloop()
