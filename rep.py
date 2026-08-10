from models import Student



class StudentRepository:

    def __init__(self):
        self.students = {}

    # CREATE
    def create(self, student: Student):
        if student.id in self.students:
            raise ValueError("Student already exists")

        self.students[student.id] = student
        return student

    # READ ONE
    def get(self, student_id: int):
        return self.students.get(student_id)

    # READ ALL
    def get_all(self):
        return list(self.students.values())

    # UPDATE
    def update(self, student_id: int, student: Student):
        if student_id not in self.students:
            return None

        self.students[student_id] = student
        return student

    # DELETE
    def delete(self, student_id: int):
        if student_id not in self.students:
            return None

        return self.students.pop(student_id)