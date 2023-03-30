number_of_students = int(input('Hãy nhập số sinh viên:'))
number_of_subject  = int(input('Hãy nhập số môn học:'))
student_grades = []
average_grades = []

for i in range(number_of_students):
    print(f'Hãy nhập điểm của sinh viên thứ {i+1}')
    grades_temp =[]
    for j in range(number_of_subject):
        grade_temp = float(input(f'Nhập điểm môn thứ {j+1}:'))
        grades_temp.append(grade_temp)
    student_grades.append(grades_temp)    
print(f'Danh sách điểm: {student_grades}')
for student_grade in (student_grades):
    total = 0
    for grade in student_grade:
        total = total + grade
    average_grade = float(total/number_of_subject)
    average_grades.append(average_grade)
    print(f'Điểm trung bình : {average_grade}')
    
