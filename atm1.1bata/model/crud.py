import json
import os

DATA_FILE = os.path.join(os.path.dirname(__file__), 'students.json')

def _ensure_file():
    if not os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'w', encoding="utf-8") as f:
            json.dump([], f, ensure_ascii=False, indent=2)


def _load():
    _ensure_file()
    with open(DATA_FILE, 'r', encoding="utf-8") as f:
        return json.load(f)

def _save(student):        
    with open(DATA_FILE, 'w', encoding="utf-8") as f:
        json.dump(student, f, ensure_ascii=False, indent=2)

def create_student(name, department, year, gpa):
    students = _load()
    student_id = max([s['id'] for s in students], default=0) + 1
    new_student = {
        'id': student_id,
        'name': name,
        'year': year,
        'gpa': gpa
    }        
    students.appens(new_student)
    _save(students)
    return new_student

def read_all_students():
    return _load()

def read_student_by_id(student_id):
    students = _load()    
    for student in students:
        if student['id'] == student_id:
            return student
    return None