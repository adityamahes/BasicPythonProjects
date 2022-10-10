from tkinter import *
from quiz_brain import QuizBrain
from functools import partial
THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain): # The colon tells the user what data type is expected (type int)
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)

        self.score = Label(text="Score: 0", bg=THEME_COLOR, fg="white")
        self.score.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(
            150,
            125,
            text="SOME QUESTION TEXT",
            font=("Arial", 15, "italic"),
            fill=THEME_COLOR,
            width=280,
        )
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        correct = PhotoImage(file="./images/true.png")
        self.correct_btn = Button(image=correct, highlightthickness=0, command=partial(self.check_user_answer, "True"))
        self.correct_btn.grid(row=2, column=0)

        incorrect = PhotoImage(file="./images/false.png")
        self.incorrect_btn = Button(image=incorrect, highlightthickness=0, command=partial(self.check_user_answer, "False"))
        self.incorrect_btn.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score.config(text=f"Score: {self.quiz.score}/{self.quiz.question_number}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text=f"You've completed the quiz!!\nYour final score was: {self.quiz.score}/{self.quiz.question_number}")
            self.score.config(text=f"Score: {self.quiz.score}/{self.quiz.question_number}")
            self.correct_btn.config(state="disabled")
            self.incorrect_btn.config(state="disabled")

    def check_user_answer(self, user_choice):
        if self.quiz.check_answer(user_choice):
            self.give_feedback(True)
        else:
            self.give_feedback(False)

    def give_feedback(self, ya):
        if ya:
            self.canvas.config(bg="green")
            self.window.after(1000, self.get_next_question)
        else:
            self.canvas.config(bg="red")
            self.window.after(1000, self.get_next_question)

