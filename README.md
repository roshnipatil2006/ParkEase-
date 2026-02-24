# ParkEase – Smart Parking Management System

ParkEase is a Python-based desktop application built using Tkinter and MySQL that efficiently manages parking operations including vehicle registration, slot assignment, payment processing, and checkout management.

This project follows a modular architecture where each functionality is implemented in a separate Python file for better scalability and maintainability.

---

## 📌 Features

- 🚘 Vehicle Registration
- 🅿️ Automated Slot Assignment
- 📊 Real-Time Slot Availability
- 🔍 Search Vehicle & Slot Details
- 💳 Payment Management
- 🚪 Vehicle Checkout & Slot Release
- 🖥️ Interactive Dashboard GUI
- 🗄️ MySQL Database Integration

---

## 🏗️ Project Structure

```
ParkEase/
│── main.py
│── dashboard.py
│── vehicle_registration.py
│── assign_slot.py
│── free_slot.py
│── search_vehicle_slot.py
│── payment.py
│── checkout.py
│── assets/
│     ├── cars.jpg
│     ├── dashboard.jpg
│     ├── parking.jpg
│     ├── project.jpg
│     ├── park_new.jpg
│     ├── OIP.webp
│── requirements.txt
│── README.md
│── .gitignore
```

---

## 🛠️ Technologies Used

- Python
- Tkinter (GUI)
- MySQL
- mysql-connector-python
- Pillow (PIL)

---

## 🗄️ Database Setup

1. Install MySQL.
2. Create a database:
   ```sql
   CREATE DATABASE parkease;
   ```
3. Create required tables (vehicles, slots, payments, etc.).
4. Update your MySQL credentials in the database connection file.

---

## ▶️ Installation & Run

### 1️⃣ Clone Repository

```bash
git clone https://github.com/yourusername/ParkEase.git
cd ParkEase
```

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ Run Application

```bash
python main.py
```

---

## 🎯 Concepts Applied

- Modular Programming
- Event-Driven GUI
- CRUD Operations
- Database Connectivity
- Backend–Frontend Integration

---

## 🚀 Future Enhancements

- Admin Authentication
- Parking Analytics Dashboard
- Online Payment Integration
- Web Version Deployment
- Report Generation

---

## 👩‍💻 Author

Roshni Patil  
Computer Science Engineering Student  

---

⭐ If you like this project, consider giving it a star!
