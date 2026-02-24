from tkinter import *
from tkinter import messagebox
import mysql.connector
from datetime import datetime
from PIL import Image, ImageTk

win = Tk()
win.title("Vehicle Check-out")
win.geometry("600x500")

img = Image.open("cars.jpg")
bg = ImageTk.PhotoImage(img)
background_label = Label(win, image=bg)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

f1 = ("Century Schoolbook", 20, "bold")
f2 = ("Century Schoolbook", 16)
f3 = ("Century Schoolbook", 14)
f4 = ("Century Schoolbook", 16, "bold")

def fetch_vehicle_details(event=None):
    plate = entry_plate.get().strip()
    if not plate:
        label_owner.config(text="Owner: ")
        label_type.config(text="Vehicle Type: ")
        return
    mydb = mysql.connector.connect(host="localhost", user="root", password="roshni@2006", database="parking", port=3306)
    mycur = mydb.cursor()
    mycur.execute("SELECT owner_name, vehicle_type FROM vehicles WHERE plate_no=%s", (plate,))
    record = mycur.fetchone()
    if record:
        label_owner.config(text=f"Owner: {record[0]}", fg="black")
        label_type.config(text=f"Vehicle Type: {record[1]}", fg="black")
    else:
        label_owner.config(text="Owner: Not Found", fg="red")
        label_type.config(text="Vehicle Type: Not Found", fg="red")
    mycur.close()
    mydb.close()

def show_payment_window(plate, owner, vtype, checkin_time, checkout_time, amount):
    pay_win = Toplevel(win)
    pay_win.title(f"Payment - {plate}")
    pay_win.geometry("500x400")

    img2 = Image.open("cars.jpg")
    bg2 = ImageTk.PhotoImage(img2)
    background_label2 = Label(pay_win, image=bg2)
    background_label2.image = bg2
    background_label2.place(x=0, y=0, relwidth=1, relheight=1)

    frame = Frame(pay_win, bg="white", padx=20, pady=20, bd=2, relief=RIDGE)
    frame.place(relx=0.5, rely=0.5, anchor=CENTER)

    Label(frame, text="Payment Details", font=f4, bg="white", fg="#333").pack(pady=10)
    Label(frame, text=f"Vehicle: {plate}", font=f2, bg="white").pack(pady=5)
    Label(frame, text=f"Owner: {owner}", font=f2, bg="white").pack(pady=5)
    Label(frame, text=f"Vehicle Type: {vtype}", font=f2, bg="white").pack(pady=5)
    Label(frame, text=f"Check-in: {checkin_time}", font=f2, bg="white").pack(pady=5)
    Label(frame, text=f"Check-out: {checkout_time}", font=f2, bg="white").pack(pady=5)
    Label(frame, text=f"Amount to Pay: Rs.{amount}", font=f2, fg="green", bg="white").pack(pady=10)

    Button(frame, text="Pay Now", font=f3, bg="#4CAF50", fg="white", width=12, command=pay_win.destroy).pack(pady=15, ipady=5)

def checkout_vehicle():
    plate = entry_plate.get().strip()
    if not plate:
        messagebox.showerror("Error", "Enter Plate Number")
        return
    mydb = mysql.connector.connect(host="localhost", user="root", password="", database="parking")
    mycur = mydb.cursor()
    mycur.execute("SELECT vehicle_id, owner_name, vehicle_type FROM vehicles WHERE plate_no=%s", (plate,))
    v = mycur.fetchone()
    if not v:
        messagebox.showerror("Error", "Vehicle not registered")
        mycur.close(); mydb.close()
        return
    vehicle_id, owner, vtype = v
    mycur.execute("SELECT record_id, slot_id, checkin_time FROM checkin_checkout WHERE vehicle_id=%s AND checkout_time IS NULL", (vehicle_id,))
    record = mycur.fetchone()
    if not record:
        messagebox.showerror("Error", "Vehicle not checked-in")
        mycur.close(); mydb.close()
        return
    record_id, slot_id, checkin_time = record
    checkout_time = datetime.now()
    mycur.execute("UPDATE checkin_checkout SET checkout_time=%s WHERE record_id=%s", (checkout_time, record_id))
    mycur.execute("UPDATE slots SET is_available=1 WHERE slot_id=%s", (slot_id,))
    mydb.commit()
    total_seconds = (checkout_time - checkin_time).total_seconds()
    minutes = total_seconds / 60
    rate = 20 if vtype.lower() == "car" else 10
    amount = round((minutes / 60) * rate, 2)
    messagebox.showinfo("Success", "Vehicle " + plate + " checked out successfully!")
    entry_plate.delete(0, END)
    label_owner.config(text="Owner: ")
    label_type.config(text="Vehicle Type: ")
    show_payment_window(plate, owner, vtype, checkin_time, checkout_time, amount)
    mycur.close()
    mydb.close()

frame = Frame(win, bg="#ffffff", padx=30, pady=30, bd=2, relief=RIDGE)
frame.place(relx=0.5, rely=0.5, anchor=CENTER)

Label(frame, text="Vehicle Check-out", font=f1, bg="#ffffff", fg="#333").pack(pady=(0, 15))
Label(frame, text="Plate Number:", font=f2, bg="#ffffff").pack(pady=(5, 8))
entry_plate = Entry(frame, font=f3, bd=2)
entry_plate.pack(pady=(0, 12), ipadx=5, ipady=5)

label_owner = Label(frame, text="Owner: ", font=f3, bg="#ffffff")
label_owner.pack(pady=(5, 5))
label_type = Label(frame, text="Vehicle Type: ", font=f3, bg="#ffffff")
label_type.pack(pady=(5, 15))

Button(frame, text="Check-out", font=f4, width=18, bg="#4CAF50", fg="white", command=checkout_vehicle).pack(pady=(5, 10), ipady=5)
Button(frame, text="Close", font=f4, bg="#f44336", fg="white", width=12, command=win.destroy).pack(pady=(0, 5), ipady=5)

win.mainloop()
