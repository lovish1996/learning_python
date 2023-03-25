def get_grade(marks):
    if marks > 90:
        return 'A'
    elif 80 < marks <= 90:
        return 'B'
    elif 60 <= marks <= 80:
        return 'C'
    elif 0 <= marks < 60:
        return 'D'
    else:
        return 'Invalid Grade!'


if __name__ == '__main__':
    student_marks = int(input('Enter your marks (between 0 and 100): '))
    grade = get_grade(student_marks)
    print(grade)
