from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import mysql.connector

win = Tk()
win.title("Vehicle Registration")
win.geometry("600x600")

img = Image.open("cars.jpg")
bg = ImageTk.PhotoImage(img)
background_label = Label(win, image=bg)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

def register_vehicle():
    owner = entry_owner.get().strip()
    plate = entry_plate.get().strip()
    vtype = vehicle_type.get().strip()

    if not owner or not plate or not vtype:
        messagebox.showerror("Error", "All fields are required")
        return

    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="parking",
        port=3306
    )
    mycur = mydb.cursor()
    mycur.execute(
        "INSERT INTO vehicles (owner_name, plate_no, vehicle_type) VALUES (%s,%s,%s)",(owner, plate, vtype)
    )
    mydb.commit()

    messagebox.showinfo("Success", "Vehicle Registered Successfully")
    entry_owner.delete(0, END)
    entry_plate.delete(0, END)
    vehicle_type.set("Select Type")
    win.destroy()

frame = Frame(win, bg="white", padx=20, pady=20)
frame.pack(pady=100)
f1= ("Century Schoolbook",20,"bold")
f2=("Century Schoolbook",18)
Label(frame, text="Owner Name:", font=f1, bg="white").pack(pady=5)
entry_owner = Entry(frame, font=f2)
entry_owner.pack(pady=5)
Label(frame, text="Plate Number:", font=f1, bg="white").pack(pady=5)
entry_plate = Entry(frame, font=f2)
entry_plate.pack( pady=5)

Label(frame, text="Vehicle Type:", font=f1, bg="white").pack( pady=5)
vehicle_type = StringVar()
vehicle_type.set("Select Type")
dropdown = OptionMenu(frame, vehicle_type,"Scooty", "Car", "Bike", "Truck", "Bus", "Other")
dropdown.config(font=f2, width=15)
dropdown.pack(pady=5)

Button(frame, text="Register", font=f1, width=15, command=register_vehicle,background="green").pack(pady=10)
Button(frame, text="Back-->", font=("Century Schoolbook",13,"bold"),background="red", command=exit).pack(pady=10)

win.mainloop()

