from tkinter import *
from PIL import Image, ImageTk
import os

win = Tk()
win.title("Parking Dashboard")
win.geometry("1600x700")
img = Image.open("img.jpg")
bg = ImageTk.PhotoImage(img)
background_label = Label(win, image=bg)
background_label.place(x=0, y=0, relwidth=1, relheight=1)


def open_vehicle_registration():
    os.system("python vehicle_registration.py")

def open_assign_slot():
    os.system("python assign_slot.py")

def open_checkout():
    os.system("python checkout.py")

def open_free_slots():
    os.system("python free_slot.py")

def open_search_vehicle_slot():
    os.system("python search_vehicle_slot.py")

f1= ("Century Schoolbook",18,"bold")
Button(win, text="Vehicle Registration", width=25, command=open_vehicle_registration ,font=f1).place(x=600, y=50)
Button(win, text="Check In", width=25, command=open_assign_slot,font=f1).place(x=420, y=160)
Button(win, text="Check Out", width=25, command=open_checkout,font=f1).place(x=750, y=260)
Button(win, text="Search Free Slots", width=25, command=open_free_slots,font=f1).place(x=420, y=360)
Button(win, text="Search Vehicle Slot", width=25, command=open_search_vehicle_slot,font=f1).place(x=750, y=460)

win.mainloop()
