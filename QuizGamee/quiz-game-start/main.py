from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for question in question_data[0]["results"]:
    question_object = Question(q_text=question["question"], q_answer=question["correct_answer"])
    question_bank.append(question_object)

quiz = QuizBrain(question_bank)
while quiz.still_has_questions():
    quiz.next_question()

percent = round(quiz.score*100/quiz.question_number, 2)
if percent >= 70.00:
    print(f"Fantastic!!! Future TRIVIA-MAN in the making... You got {percent}%.")
elif percent >= 50.00:
    print(f"Amazing!! You sure are a geek!... You got {percent}%.")
else:
    print(f"Good work! You probably learned a lot! You got {percent}%.")
