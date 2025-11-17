# 📌 StaffTrack-API - Employee Management System (EMS) – FastAPI CRUD Project

A simple and clean Employee Management System built using **FastAPI**, **SQLite**, and **SQLAlchemy**.  
This project implements full **CRUD operations** (Create, Read, Update, Delete) for managing employee data.

---

## 🚀 Features
- ✓ Add new employees  
- ✓ View all employees  
- ✓ Get employee by ID  
- ✓ Update employee details  
- ✓ Delete employee  
- ✓ Auto-generated API Docs (Swagger UI)  
- ✓ SQLite Database  
- ✓ FastAPI + SQLAlchemy ORM  
- ✓ Clean modular backend  

---

## 🗂️ Tech Stack
- **FastAPI** – Web framework  
- **Uvicorn** – ASGI server  
- **SQLAlchemy** – ORM  
- **SQLite** – Database  
- **Pydantic** – Data validation  
- **Python** – Programming language  
- **Git, GitHub** – Version control  

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

### 3️⃣ Activate venv (Windows)
```bash
venv\Scripts\activate
```

### 4️⃣ Install dependencies
```bash
pip install -r requirements.txt
```

### ▶️ Run the project
```bash
uvicorn main:app --reload
```

---

## 🔗 API Endpoints

| Method | Endpoint           | Description              |
|--------|---------------------|--------------------------|
| GET    | /employees          | Get all employees        |
| POST   | /employees          | Create new employee      |
| GET    | /employees/{id}     | Get employee by ID       |
| PUT    | /employees/{id}     | Update employee          |
| DELETE | /employees/{id}     | Delete employee          |

---

## 📘 Swagger Documentation

FastAPI automatically generates UI documentation:

👉 http://127.0.0.1:8000/docs

---

## 🧱 Project Architecture
```
ems-fastapi/
│── main.py              # Main FastAPI application
│── database.py          # DB connection & engine
│── models.py            # SQLAlchemy models
│── schemas.py           # Pydantic schemas
│── crud.py              # CRUD logic functions
│── employees.db         # SQLite database file
│── requirements.txt     # Dependencies
└── README.md            # Documentation
```

---

## 📚 Database
This project uses **SQLite (employees.db)** for simplicity and development speed.

---

## 🚀 Future Enhancements
- Add JWT authentication  
- Add employee search & filtering  
- Add pagination  
- Add unit tests (pytest)  

---

## ❤️ Author
**Gundugollu Mohana Venkata Achuta Lakshmi**

🌟 If you like this project, give it a **star ⭐**!
