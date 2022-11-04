from question_model import Question


class QuizBrain:
    def __init__(self, q_input):
        self.question_number = 0
        self.question_list = q_input

    def next_question(self):
        correct = True
        while correct:
            ask_question = input(f"Question {self.question_number+1}: {self.question_list[self.question_number].text}"
                                 f"\nYour answer (true/false): ").lower()
            if ask_question in ("true", "false"):
                if ask_question == self.question_list[self.question_number].answer.lower():
                    if self.question_number == len(self.question_list)-1:
                        print(f"Congratulations, you have answered all {self.question_number+1} questions correctly!")
                        break
                    self.question_number += 1
                    print(f"That's right! Correct answers {self.question_number}/{self.question_number}")
                else:
                    print(f"Incorrect. Final score is {self.question_number}/{self.question_number+1}")
                    correct = False


