from question_model import Question
from quiz_brain import QuizBrain
from data import question_data

q_bank = []
for question in question_data:
    q_text = question["text"]
    q_answer = question["answer"]
    q_bank.append(Question(q_text, q_answer))

quiz = QuizBrain(q_bank)
quiz.next_question()




