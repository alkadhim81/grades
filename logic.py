from PyQt6.QtWidgets import *
from gui import *
import csv

class Logic(QMainWindow, Ui_MainWindow):
    def __init__(self) -> None:
        """
        Hides all the scores labels and line text.
        Runs the function scores based on the number entered in the attempts box.
        Runs the submit function when the submit buttin is clicked.
        """

        super().__init__()
        self.setupUi(self)
        self.score1_label.hide()
        self.score2_label.hide()
        self.score3_label.hide()
        self.score4_label.hide()
        self.score1_line.hide()
        self.score2_line.hide()
        self.score3_line.hide()
        self.score4_line.hide()
        self.attempts.textChanged.connect(self.scores)
        self.submit_button.clicked.connect(lambda: self.submit())

    def scores(self) -> None:
        """
        Will show/hide scores label and text line based on number of attempts entered.
        """
        num_attempts: int = self.attempts.text()
        try:
            num_attempts = int(num_attempts)
            if num_attempts not in [1,2,3,4]:
                raise ValueError
        except ValueError:
            self.message.setText("Number of attempts must be 1-4")
            self.message.setStyleSheet("color: red;")
            return

        if num_attempts >= 1:
            self.score1_label.show()
            self.score1_line.show()
        if num_attempts >= 2:
            self.score2_label.show()
            self.score2_line.show()
        if num_attempts >= 3:
            self.score3_label.show()
            self.score3_line.show()
        if num_attempts == 4:
            self.score4_label.show()
            self.score4_line.show()
        self.message.clear()



    def submit(self):
        """
        Will send name, scores, and final grades to csv document after hitting submit.
        """
        name: str =''
        score1: int=0
        score2: int=0
        score3: int=0
        score4: int=0
        final: float = 0
        num_attempts: int = self.attempts.text()

        try:
            num_attempts = int(num_attempts)
            if num_attempts not in [1,2,3,4]:
                raise ValueError
        except ValueError:
            self.message.setText("Number of attempts must be 1-4")
            self.message.setStyleSheet("color: red;")
            return
        name = self.name.text()
        try:
            if name == '':
                raise ValueError
        except ValueError:
            self.message.setText("Please enter in a Student's name.")
            self.message.setStyleSheet("color: red;")
            return
        if num_attempts >= 1:
            score1= self.score1_line.text()
            try:
                score1 = int(score1)
                if score1 < 0 or score1 > 100:
                    raise ValueError
            except ValueError:
                self.message.setText("Score must be between 0-100.")
                self.message.setStyleSheet("color: red;")
                return

        if num_attempts >= 2:
            score2 = self.score2_line.text()
            try:
                score2 = int(score2)
                if score2 < 0 or score2>100:
                    raise ValueError
            except ValueError:
                self.message.setText("Score must be between 0-100.")
                self.message.setStyleSheet("color: red;")
                return
        if num_attempts >= 3:
            score3 = self.score3_line.text()
            try:
                score3 = int(score3)
                if score3 < 0 or score3 > 100:
                    raise ValueError
            except ValueError:
                self.message.setText("Score must be between 0-100.")
                self.message.setStyleSheet("color: red;")
                return
        if num_attempts == 4:
            score4 = self.score4_line.text()
            try:
                score4 = int(score4)
                if score4 < 0 or score4 > 100:
                    raise ValueError
            except ValueError:
                self.message.setText("Score must be between 0-100.")
                self.message.setStyleSheet("color: red;")
                return

        if num_attempts == 1:
            final = score1

        if num_attempts == 2:
            final = (score1+score2) / 2

        if num_attempts == 3:
            final = (score1 + score2 + score3) / 3

        if num_attempts == 4:
            final = (score1 +score2 +score3 + score4) / 4

        final = round(final, 2)

        with open('Grades.csv', 'a', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow([name, score1, score2, score3, score4, final])
            self.message.setText("Grades Submitted!")
            self.message.setStyleSheet("color: blue;")
