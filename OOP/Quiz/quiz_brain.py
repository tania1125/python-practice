class QuizzBrain:
    def __init__(self, questions_passed):
        self.question_number = 0
        self.question_list = questions_passed
        self.score = 0
        
    def still_has_questions(self):
            return len(self.question_list) > self.question_number
            

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        input_answer = input(f"Q {self.question_number}: {current_question.question_text} (True/False): ")
        self.check_answer(input_answer, current_question.right_answer)


    def check_answer(self, user_answer, actual_answer):
        if user_answer.lower() == actual_answer.lower():
            self.score += 1
            print("You got it right!")
        else:
            print("it's wrong")
        print(f"The right answer is {actual_answer}")
        print(f"The current score is {self.score}/{self.question_number}")
        print("\n")