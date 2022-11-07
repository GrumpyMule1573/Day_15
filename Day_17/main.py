from question_model import Question
from quiz_brain import QuizBrain
from data import question_data, second_questions

q_bank = []
for question in question_data:
    q_text = question["text"]
    q_answer = question["answer"]
    q_bank.append(Question(q_text, q_answer))

q_bank_2 = []
for question in second_questions:
    q_text = question["question"]
    q_answer = question["correct_answer"]
    q_bank_2.append(Question(q_text, q_answer))

quiz = QuizBrain(q_bank_2)
quiz.next_question()





