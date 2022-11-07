from question_model import Question


class QuizBrain:
    def __init__(self, q_input):
        self.question_number = 0
        self.question_list = q_input
        self.score = 0

    def next_question(self):
        correct = True
        while correct:
            ask_question = input(f"Question {self.question_number+1}: {self.question_list[self.question_number].text}"
                                 f"\nYour answer (true/false): ").lower()
            if ask_question in ("true", "false"):
                if ask_question == self.question_list[self.question_number].answer.lower():
                    self.question_number += 1
                    self.score += 1
                    print(f"That's right! Correct answers {self.score}/{self.question_number}\n")
                elif ask_question != self.question_list[self.question_number].answer.lower():
                    self.question_number += 1
                    print(f"Incorrect. Your score is {self.score}/{self.question_number}\n")
                if self.question_number == len(self.question_list):
                    print(f"All questions answered! Your final score is {self.score}/{self.question_number}")
                    correct = False


