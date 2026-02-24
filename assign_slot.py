from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import mysql.connector
from datetime import datetime

win = Tk()
win.title("Assign Parking Slot")
win.geometry("600x500")

img = Image.open("cars.jpg")
bg = ImageTk.PhotoImage(img)
background_label = Label(win, image=bg)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

def fetch_vehicle_details(event=None):
    plate = entry_plate.get().strip()

    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="roshni@2006",
        database="parking",
        port=3306
    )
    mycur = mydb.cursor()
    mycur.execute("SELECT owner_name, vehicle_type FROM vehicles WHERE plate_no=%s", (plate,))
    record = mycur.fetchone()
    if record:
        label_owner.config(text=f"Owner: {record[0]}")
        label_type.config(text=f"Vehicle Type: {record[1]}")
    else:
        label_owner.config(text="Owner: Not Found")
        label_type.config(text="Vehicle Type: Not Found")
    mycur.close()
    mydb.close()

def assign_slot():
    plate = entry_plate.get().strip()
    if not plate:
        messagebox.showerror("Error","Enter Plate Number")
        return

    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="parking",
        port=3306
    )
    mycur = mydb.cursor()

    mycur.execute("SELECT vehicle_id FROM vehicles WHERE plate_no=%s", (plate,))
    vehicle = mycur.fetchone()
    if not vehicle:
        messagebox.showerror("Error","Vehicle not registered")
        mycur.close()
        mydb.close()
        return
    vehicle_id = vehicle[0]

    mycur.execute("SELECT slot_id FROM slots WHERE is_available=1 LIMIT 1")
    slot = mycur.fetchone()
    if not slot:
        messagebox.showerror("Error","No free slots available")
        mycur.close()
        mydb.close()
        return
    slot_id = slot[0]

    mycur.execute("UPDATE slots SET is_available=0 WHERE slot_id=%s", (slot_id,))
    mycur.execute("INSERT INTO checkin_checkout (vehicle_id, slot_id, checkin_time) VALUES (%s,%s,%s)", (vehicle_id, slot_id, datetime.now()))
    mydb.commit()
    mycur.close()
    mydb.close()

    messagebox.showinfo("Success", f"Slot assigned: {slot_id}")
    entry_plate.delete(0, END)
    label_owner.config(text="Owner: ")
    label_type.config(text="Vehicle Type: ")
    win.destroy()

frame = Frame(win, bg="white", padx=30, pady=30, bd=2, relief=RIDGE)
frame.place(relx=0.5, rely=0.5, anchor=CENTER)

f_title = ("Century Schoolbook", 20, "bold")
f_entry = ("Century Schoolbook", 16)
f_button = ("Century Schoolbook", 16, "bold")

Label(frame, text="Assign Parking Slot", font=("Century Schoolbook", 22, "bold"),
      bg="white", fg="#333").pack(pady=(0, 20))

Label(frame, text="Vehicle Plate Number:", font=f_title, bg="white").pack(pady=(5, 8))
entry_plate = Entry(frame, font=f_entry, bd=2)
entry_plate.pack(pady=(0, 15), ipadx=5, ipady=5)
entry_plate.bind("<KeyRelease>", fetch_vehicle_details)

label_owner = Label(frame, text="Owner: ", font=f_entry, bg="white")
label_owner.pack(pady=(5, 5))
label_type = Label(frame, text="Vehicle Type: ", font=f_entry, bg="white")
label_type.pack(pady=(5, 15))

Button(frame, text="Assign Slot", font=f_button, width=18, bg="#4CAF50", fg="white", command=assign_slot).pack(pady=(5, 10), ipady=5)
Button(frame, text="Back -->", font=("Century Schoolbook", 14, "bold"), bg="#f44336", fg="white", width=12, command=exit).pack(pady= 5, ipady=5)

win.mainloop()
