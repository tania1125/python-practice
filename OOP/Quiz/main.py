from data import question_data
from question_model import Question
from quiz_brain import QuizzBrain

question_bank = []

for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    question_obj = Question(question_text, question_answer)
    question_bank.append(question_obj)

quizz = QuizzBrain(questions_passed= question_bank)
quizz.next_question()
while quizz.still_has_questions():
    quizz.next_question()

print("You have completed the quiz!")
print(f"Your final score is: {quizz.score}/{quizz.question_number}")