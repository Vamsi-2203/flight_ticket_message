# first import modules
from tkinter import *
import tkinter.messagebox as tmeg
root = Tk()
root.geometry("600x600")
Label(root, text="which country you want to travel in?",font="lucidia 19 bold").pack()

country = ["Australia", "Japan", "India", "Nepal", "England", "USA"]

var = StringVar()
new_var = var.set("nonewhere")
def travel():
    tmeg.showinfo("lets travel", f"so, we are booking your flight to {var.get()}\nWe wish you a happy journey. Thank for booking with us")

for x in range(6):
    Radiobutton(root, text=country[x], variable=var, value=country[x]).pack()

Button(root, text="lets travel", command=travel).pack()

root.mainloop()