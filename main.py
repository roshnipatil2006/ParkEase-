from tkinter import *
from PIL import Image, ImageTk
import os

win = Tk()
win.configure(bg="black")

path = Image.open("parking.jpg")
render = ImageTk.PhotoImage(path)
img = Label(win, image=render)
img.place(x=0, y=0)

def start_app():
    win.destroy()
    os.system("python dashboard.py")

win.title("Parking Management System")
win.geometry("1200x670")

f1 = ("Arial", 28, "bold")
title_label = Label(win, text="Parking Management System", font=f1, bg="lightgrey").pack(pady=130)

f2 = ("Arial", 15, "bold")
start_button = Button(win, text="Start", command=start_app, width=15, height=2, font=f2, background="lightgrey", borderwidth=2)
start_button.pack(pady=10)

win.mainloop()
