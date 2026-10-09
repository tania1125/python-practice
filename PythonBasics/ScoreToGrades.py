student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}

student_grades = {}

for students in student_scores:
    if (student_scores[students] >90 and student_scores[students] <=100):
        student_grades.update({students: "Outstanding"})
    elif (student_scores[students] >80 and student_scores[students] <=90):
        student_grades.update({students:"Exceeds Expectations"})
    elif (student_scores[students] >70 and student_scores[students] <=80):
        student_grades.update( {students:"Acceptable"})
    elif (student_scores[students] <=70):
        student_grades.update({students:"Fail"})
print (student_grades)