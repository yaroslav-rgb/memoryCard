from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QApplication, 
    QWidget, 
    QPushButton, 
    QLabel, 
    QVBoxLayout, 
    QHBoxLayout, 
    QMessageBox, 
    QRadioButton,
    QGroupBox, 
    QButtonGroup)

from random import shuffle


class Question():
    def __init__(self, question, rightAns, wrongAns1, wrongAns2, wrongAns3):
        self.question = question
        self.rightAns = rightAns
        self.wrongAns1 = wrongAns1
        self.wrongAns2 = wrongAns2
        self.wrongAns3 = wrongAns3 


q1 = Question('Какого типа данных нет в Python?', 'duble' , 'int' , 'float', 'str')
q2 = Question('Может ли быть индекс списка отрицательным?', 'да', 'нет', 'иногда', 'только в функции')
q3 = Question('Что может быть ключом в словаре?', 'число', 'функция', 'переменная', 'виджеты')
q4 = Question('Какой функции нет в Python?', 'text', 'print', 'input', 'len')
q5 = Question('Какая самая последняя версия Windows?', '11', '10', '12', '9')
q6 = Question('Какими клавишами открыть панель со смайликами на Windows?', 'win+ю', 'win+f', 'alt+f4', 'shift+p')
q7 = Question('Какими клавишами поменять язык на клавиатуре?', 'shift+alt', 's+alt', 'alt+f4', 'fn+shift')
q8 = Question('Какого виджета в pyqt5 нет?', 'QSintax', 'QLabel', 'QVBoxLayout', 'QRadioButton')
#q9 = Question('')
question_list = list()
question_list.append(q1)
question_list.append(q2)
question_list.append(q3)
question_list.append(q4)
question_list.append(q5)
question_list.append(q6)
question_list.append(q7)
question_list.append(q8)
shuffle(question_list) 

question_counter = 0
n = len(question_list)

right = 0
wrong = 0
total = 0

def ask(q):
    global answers, question
    shuffle(answers)
    question.setText(q.question)
    answers[0].setText(q.rightAns)
    answers[1].setText(q.wrongAns1)
    answers[2].setText(q.wrongAns2)
    answers[3].setText(q.wrongAns3)

def check_answer():
    global answers, res_label, right_ans, right, wrong, total
    if answers[0].isChecked():
        total += 1
        right += 1
        res_label.setText('правильно 👍')
        right_ans.setText(f'\nПравильно: {right}\nНеправильно: {wrong}\n Cтатистика: {round(right/total*100,)}%')
    else:
        total += 1
        wrong += 1
        res_label.setText('неправильно 😢')
        right_ans.setText(f'Правильный ответ: {answers[0].text()}\nПравильно: {right}\nНеправильно: {wrong}\n Cтатистика: {round(right/total*100,)}%')
        

def btn_click():
    global question_counter
    if btn.text() == 'Ответить':
        if rbtn1.isChecked() or rbtn2.isChecked() or rbtn3.isChecked() or rbtn4.isChecked():
            check_answer()
            RadioGroupBox.hide()
            AnsGroupBox.show()
            if question_counter == n:
                btn.setText('Завершить')
            else:
                btn.setText('Далее')
        else:
            pass
    elif btn.text() == 'Далее':
        if question_counter < n:
            ask(question_list[question_counter])
            question_counter += 1
            uncheck()
            AnsGroupBox.hide()
            RadioGroupBox.show()
            btn.setText('Ответить')
        else:
            pass
       
def uncheck():
    btn_group.setExclusive(False)
    rbtn1.setChecked(False)
    rbtn2.setChecked(False)
    rbtn3.setChecked(False)
    rbtn4.setChecked(False)
    btn_group.setExclusive(True)

app = QApplication([])
desktop = app.desktop() 

main_win = QWidget()
main_win.setStyleSheet('background-image: url(bgi.png)')
main_win.resize(800, 600)
main_win.setWindowTitle('MemoryCard')

question = QLabel('Какой национальности не существует?')
question.setStyleSheet("font-size: 12pt;")
btn = QPushButton('Ответить')

RadioGroupBox = QGroupBox('варианты ответов')
btn_group = QButtonGroup()
rbtn1 = QRadioButton('Энцы')
rbtn2 = QRadioButton('Смурфы')
rbtn3 = QRadioButton('Чулымцы')
rbtn4 = QRadioButton('Алеуты')
btn_group.addButton(rbtn1)
btn_group.addButton(rbtn2)
btn_group.addButton(rbtn3)
btn_group.addButton(rbtn4)

answers = [rbtn1, rbtn2 ,rbtn3 ,rbtn4]

main_line = QVBoxLayout()
line1 = QHBoxLayout()
line2 = QVBoxLayout()
line3 = QVBoxLayout()
line2.addWidget(rbtn1, alignment=Qt.AlignLeft)
line2.addWidget(rbtn2, alignment=Qt.AlignLeft)
line3.addWidget(rbtn3, alignment=Qt.AlignLeft)
line3.addWidget(rbtn4, alignment=Qt.AlignLeft)
line1.addLayout(line2)
line1.addLayout(line3)
RadioGroupBox.setLayout(line1)

AnsGroupBox = QGroupBox('результат теста')
res_label = QLabel('правильно/неправильно')
right_ans = QLabel('правильный ответ')
line = QVBoxLayout()
res_line = QHBoxLayout()
right_ans_line = QHBoxLayout()
res_line.addWidget(res_label, alignment=Qt.AlignLeft)
right_ans_line.addWidget(right_ans, alignment=Qt.AlignCenter)
line.addLayout(res_line)
line.addLayout(right_ans_line)
AnsGroupBox.setLayout(line)
AnsGroupBox.hide()

main_line.addWidget(question, alignment=(Qt.AlignHCenter | Qt.AlignVCenter))
main_line.addWidget(RadioGroupBox)
main_line.addWidget(AnsGroupBox)
main_line.addWidget(btn, alignment=(Qt.AlignHCenter | Qt.AlignVCenter))
main_win.setLayout(main_line)

ask(question_list[question_counter])
question_counter += 1
btn.clicked.connect(btn_click)

main_win.show()
app.exec_()