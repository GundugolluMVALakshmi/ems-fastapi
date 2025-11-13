# 📌 Employee Management System (EMS) – FastAPI CRUD Project

A simple and clean **Employee Management System** built using **FastAPI**, **SQLite**, and **SQLAlchemy**.
This project implements **CRUD operations** (Create, Read, Update, Delete) for managing employee data.

---

## 🚀 Features

✔ Add new employees
✔ View all employees
✔ Get employee by ID
✔ Update employee details
✔ Delete employee
✔ Automatically generates API docs using Swagger UI
✔ Uses SQLite database
✔ Uses FastAPI + SQLAlchemy ORM

---

## 🗂️ Tech Stack

* **FastAPI** – Web framework
* **Uvicorn** – ASGI server
* **SQLAlchemy** – ORM
* **SQLite** – Database
* **Pydantic** – Data validation

---

## 📦 Installation & Setup

### 1️⃣ Clone the repository

```bash
git clone https://github.com/GundugolluMVALakshmi/ems-fastapi.git
cd ems-fastapi
```

### 2️⃣ Create virtual environment

```bash
python -m venv venv
```

### 3️⃣ Activate venv

**Windows:**

```bash
venv\Scripts\activate
```

### 4️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the project

```bash
uvicorn main:app --reload
```

---

## 🔗 API Endpoints

| Method | Endpoint          | Description         |
| ------ | ----------------- | ------------------- |
| GET    | `/employees`      | Get all employees   |
| POST   | `/employees`      | Create new employee |
| GET    | `/employees/{id}` | Get employee by ID  |
| PUT    | `/employees/{id}` | Update employee     |
| DELETE | `/employees/{id}` | Delete employee     |

---

## 📘 Swagger Documentation

FastAPI automatically provides UI docs:

👉 **[http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)**

---

## 📚 Database

This project uses **SQLite** (`employees.db`) for simplicity.

---

## ❤️ Author

**Gundugollu Mohana Venkata Achuta Lakshmi**

---

## 🌟 If you like this project, give it a star ⭐!

---


