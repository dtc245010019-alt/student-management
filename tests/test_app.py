from app import get_students, get_student, search_students

def test_get_students():
    assert len(get_students()) == 2

def test_get_student_found():
    student = get_student(1)
    assert student is not None
    assert student["name"] == "Nguyen Van A"

def test_get_student_not_found():
    assert get_student(999) is None

def test_search_students_case_insensitive():
    result = search_students("nguyen")
    assert len(result) == 1
    assert result[0]["id"] == 1
