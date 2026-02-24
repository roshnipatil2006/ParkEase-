from tkinter import *
from tkinter import messagebox
import mysql.connector
from PIL import Image, ImageTk

def show_free_slots():
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="parking",
        port=3306
    )
    mycur = mydb.cursor()
    mycur.execute("SELECT slot_id FROM slots WHERE is_available=1")
    slots = mycur.fetchall()
    if slots:
        free_slots = ", ".join(str(s[0]) for s in slots)
        messagebox.showinfo("Free Slots", f"Available Slots: {free_slots}")
    else:
        messagebox.showinfo("Free Slots", "No slots available")
    mycur.close()
    mydb.close()
    win.destroy()

win = Tk()
win.title("Free Parking Slots")
win.geometry("600x450")
win.configure(bg="#e6f2ff")

img = Image.open("cars.jpg")
bg = ImageTk.PhotoImage(img)
background_label = Label(win, image=bg)
background_label.place(x=0, y=0, relwidth=1, relheight=1)
frame = Frame(win, bg="white", padx=20, pady=20, bd=2, relief=RIDGE)
frame.place(relx=0.5, rely=0.5, anchor=CENTER)
f_button = ("Century Schoolbook", 14, "bold")
Label(frame, text="Available Free Slots", font=("Century Schoolbook", 16, "bold"), bg="white").pack(pady=(0,20))

Button(frame, text="Show Free Slots", font=f_button, width=18, bg="#4CAF50", fg="white", command=show_free_slots).pack(pady=(10,10), ipady=5)
Button(frame, text="Back -->", font=f_button, width=18, bg="#f44336", fg="white", command=win.destroy).pack(pady=(5,0), ipady=5)

win.mainloop()
