from tkinter import *
from tkinter import messagebox
import mysql.connector
from PIL import Image, ImageTk


def search_slot():
    plate = entry_plate.get().strip()
    if not plate:
        messagebox.showerror("Error", "Enter Plate Number")
        return
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="parking",
        port=3306
    )
    mycur = mydb.cursor()
    mycur.execute("""
                  SELECT slot_id
                  FROM slots
                  WHERE slot_id = (SELECT slot_id
                                   FROM checkin_checkout
                                   WHERE vehicle_id = (SELECT vehicle_id FROM vehicles WHERE plate_no = %s)
                                     AND checkout_time IS NULL)
                  """, (plate,))

    result = mycur.fetchone()
    if result:
        messagebox.showinfo("Vehicle Slot", f"Vehicle is in Slot: {result[0]}")
    else:
        messagebox.showinfo("Vehicle Slot", "Vehicle is not checked-in")

    mycur.close()
    mydb.close()
    win.destroy()

win = Tk()
win.title("Search Vehicle Slot")
win.geometry("600x450")
win.configure(bg="#e6f2ff")
img = Image.open("cars.jpg")
bg = ImageTk.PhotoImage(img)
background_label = Label(win, image=bg)
background_label.place(x=0, y=0, relwidth=1, relheight=1)
frame = Frame(win, bg="white", padx=20, pady=20, bd=2, relief=RIDGE)
frame.place(relx=0.5, rely=0.5, anchor=CENTER)

f_label = ("Century Schoolbook", 14, "bold")
f_entry = ("Century Schoolbook", 12)
f_button = ("Century Schoolbook", 12, "bold")

Label(frame, text="Search Vehicle Slot", font=("Century Schoolbook", 16, "bold"), bg="white").pack(pady=(0, 15))
Label(frame, text="Vehicle Plate Number:", font=f_label, bg="white").pack(pady=(5, 5))
entry_plate = Entry(frame, font=f_entry, bd=2, relief=GROOVE)
entry_plate.pack(pady=(0, 10), ipadx=5, ipady=5)

Button(frame, text="Search Slot", font=f_button, width=15, bg="#4CAF50", fg="white", command=search_slot).pack( pady=(10, 5), ipady=5)
Button(frame, text="Back -->", font=f_button, width=15, bg="#f44336", fg="white", command=win.destroy).pack(pady=(5, 0),ipady=5)

win.mainloop()
