from fastapi import FastAPI, HTTPException, Query
from models import Student
from rep import StudentRepository

app = FastAPI(
    title="Student Mark Service (SMS)",
    version="1.0"
)

repo = StudentRepository()


# --------------------
# HOME / HEALTH CHECK
# --------------------

@app.get("/")
def home():
    return {
        "message": "Student Mark Service (SMS)"
    }


# --------------------
# CREATE - POST
# --------------------

@app.post("/students", response_model=Student)
def create_student(student: Student):

    try:
        return repo.create(student)

    except ValueError as e:
        raise HTTPException(
            status_code=400,
            detail=str(e)
        )


# --------------------
# READ ALL - GET
# --------------------

@app.get("/students", response_model=list[Student])
def get_students(
    name: str | None = Query(
        default=None,
        description="Filter students by name"
    )
):
    students = repo.get_all()

    if name:
        students = [
            student
            for student in students
            if student.name.lower() == name.lower()
        ]

    return students


# --------------------
# READ ONE - GET
# --------------------

@app.get("/students/{student_id}", response_model=Student)
def get_student(
    student_id: int
):

    student = repo.get(student_id)

    if student is None:
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    return student


# --------------------
# UPDATE - PUT
# --------------------

@app.put("/students/{student_id}", response_model=Student)
def update_student(
    student_id: int,
    student: Student
):

    updated = repo.update(
        student_id,
        student
    )

    if updated is None:
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    return updated


# --------------------
# DELETE - DELETE
# --------------------

@app.delete("/students/{student_id}")
def delete_student(
    student_id: int
):

    deleted = repo.delete(student_id)

    if deleted is None:
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    return {
        "message": "Student deleted successfully",
        "student_id": student_id
    }