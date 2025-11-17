from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional, List
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import sessionmaker, declarative_base, Session

# -------------------
# DATABASE SETUP
# -------------------

DATABASE_URL = "sqlite:///./employees.db"

engine = create_engine(
    DATABASE_URL, connect_args={"check_same_thread": False}
)

SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)

Base = declarative_base()


class EmployeeDB(Base):
    __tablename__ = "employees"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    role = Column(String, nullable=False)
    salary = Column(Integer, nullable=True)


Base.metadata.create_all(bind=engine)

# -------------------
# PYDANTIC MODELS
# -------------------

class EmployeeCreate(BaseModel):
    name: str
    email: str
    role: str
    salary: Optional[int] = None


class EmployeeUpdate(BaseModel):
    name: Optional[str] = None
    email: Optional[str] = None
    role: Optional[str] = None
    salary: Optional[int] = None


class EmployeeOut(BaseModel):
    id: int
    name: str
    email: str
    role: str
    salary: Optional[int]

    class Config:
        orm_mode = True


# -------------------
# FASTAPI APP
# -------------------

app = FastAPI(
    title="StaffTrack API",
    description="StaffTrack - Employee Management System built using FastAPI, SQLite, and SQLAlchemy",
    version="1.0.0"
)



def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# CREATE EMPLOYEE
@app.post("/employees", response_model=EmployeeOut, tags=["Employees"])
def create_employee(emp: EmployeeCreate):
    db: Session = next(get_db())

    existing = db.query(EmployeeDB).filter(EmployeeDB.email == emp.email).first()
    if existing:
        raise HTTPException(status_code=400, detail="Email already exists")

    new_emp = EmployeeDB(
        name=emp.name, email=emp.email,
        role=emp.role, salary=emp.salary
    )

    db.add(new_emp)
    db.commit()
    db.refresh(new_emp)

    return new_emp


# GET ALL EMPLOYEES
@app.get("/employees", response_model=List[EmployeeOut], tags=["Employees"])
def get_employees():
    db: Session = next(get_db())
    return db.query(EmployeeDB).all()


# GET EMPLOYEE BY ID
@app.get("/employees/{emp_id}", response_model=EmployeeOut, tags=["Employees"])
def get_employee(emp_id: int):
    db: Session = next(get_db())
    emp = db.query(EmployeeDB).filter(EmployeeDB.id == emp_id).first()

    if not emp:
        raise HTTPException(status_code=404, detail="Employee not found")

    return emp


# UPDATE EMPLOYEE
@app.put("/employees/{emp_id}", response_model=EmployeeOut, tags=["Employees"])
def update_employee(emp_id: int, data: EmployeeUpdate):
    db: Session = next(get_db())
    emp = db.query(EmployeeDB).filter(EmployeeDB.id == emp_id).first()

    if not emp:
        raise HTTPException(status_code=404, detail="Employee not found")

    updates = data.dict(exclude_unset=True)
    for key, value in updates.items():
        setattr(emp, key, value)

    db.commit()
    db.refresh(emp)
    return emp


# DELETE EMPLOYEE
@app.delete("/employees/{emp_id}", tags=["Employees"])
def delete_employee(emp_id: int):
    db: Session = next(get_db())
    emp = db.query(EmployeeDB).filter(EmployeeDB.id == emp_id).first()

    if not emp:
        raise HTTPException(status_code=404, detail="Employee not found")

    db.delete(emp)
    db.commit()
    return {"message": "Employee deleted successfully"}

