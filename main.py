from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QWidget, QHBoxLayout, QVBoxLayout, QGroupBox, QRadioButton,
                             QPushButton, QLabel, QButtonGroup)
from random import shuffle

class Question():
    def __init__(self,question,right_answer,wrong1,wrong2,wrong3):
        self.question=question
        self.right_answer=right_answer
        self.wrong1=wrong1
        self.wrong2=wrong2
        self.wrong3=wrong3

# -------------- Создание самого приложения --------------
app = QApplication([])


# -------------- Радио группа под варианты ответов --------------
radioGroup = QGroupBox("Варианты ответов")

buttonGroup=QButtonGroup()

rbtn_1 = QRadioButton("1.")
rbtn_2 = QRadioButton("2.")
rbtn_3 = QRadioButton("3.")
rbtn_4 = QRadioButton("4.")

v_line1 = QVBoxLayout()
h_line1 = QHBoxLayout()
h_line2 = QHBoxLayout()

h_line1.addWidget(rbtn_1)
h_line1.addWidget(rbtn_2)

h_line2.addWidget(rbtn_3)
h_line2.addWidget(rbtn_4)

v_line1.addLayout(h_line1)
v_line1.addLayout(h_line2)

radioGroup.setLayout(v_line1)

buttonGroup.addButton(rbtn_1)
buttonGroup.addButton(rbtn_2)
buttonGroup.addButton(rbtn_3)
buttonGroup.addButton(rbtn_4)
answers=[rbtn_1,rbtn_2,rbtn_3,rbtn_4]

# -------------- Группа под результат --------------
ansGroup = QGroupBox('Результат теста')

label_1 = QLabel('Правильно/неправильно')
label_2 = QLabel('"Правильный ответ"')

v_line2 = QVBoxLayout()

v_line2.addWidget(label_1)
v_line2.addWidget(label_2)

ansGroup.setLayout(v_line2)


# -------------- Создание кнопки и надписи вопроса --------------
btn_OK = QPushButton("Ответить")
label_question = QLabel("Когда родился Пушкин?")


# -------------- Создание направляющих --------------
layout_question = QHBoxLayout()
layout_radioGroups = QHBoxLayout()
layout_ans_btn = QHBoxLayout()


# -------------- Добавляем все полученные виджеты на направляющие --------------
layout_question.addWidget(label_question, alignment=Qt.AlignCenter) # сначала надпись вопроса
layout_radioGroups.addWidget(radioGroup)  # добавляем группу вопросов
layout_radioGroups.addWidget(ansGroup)  # добавляем группу результата
layout_ans_btn.addWidget(btn_OK, stretch=2)  # добавляем кнопку

ansGroup.hide()  # прячем одну из групп



def showresult():
    radioGroup.hide()
    ansGroup.show()
    btn_OK.setText('следующий вопрос')

def showquestion():
    buttonGroup.setExclusive(False)
    rbtn_1.setChecked(False)
    rbtn_2.setChecked(False)
    rbtn_3.setChecked(False)
    rbtn_4.setChecked(False)
    buttonGroup.setExclusive(True)
    radioGroup.show()
    ansGroup.hide()
    btn_OK.setText('Ответить')



def ask(q:Question):
    shuffle(answers)
    answers[0].setText(q.right_answer)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)

    label_question.setText(q.question)

    label_2.setText(q.right_answer)

    showquestion()

questions_list = []
questions_list.append(
    Question('Государственный язык Португалии',
    'Португальский','Английский','Испанский','Французкий'
    ))
questions_list.append(
    Question('Какого цвета снег',
    'Белый','Желтый','Красный','Серо-Буро-Малиновый'
    ))
questions_list.append(
    Question('Почему осенью листья желтеют и опадают',
    'Потому что они становятся сухими','Чтобы дерево охладилось','Незнаю','Потому что природа так сказала'
    ))
questions_list.append(
    Question('Правда ли что собакам можно шоколад?',
    'Нет','Да','Конечно можно','незнаю'
    ))
questions_list.append(
    Question('Сколько месяцев в году имеют 28 дней?',
    'Все','один, и это Февраль','6','наверное 11'
    ))


def show_correct(result):
    label_1.setText(result)
    showresult()

def check_answer():
    if answers[0].isChecked():
        show_correct('Правильно!')
    else:
        if (
            answers[1].isChecked()
            or answers[2].isChecked()
            or answers[3].isChecked()
            ):
            show_correct('Неправильно!')

def next_question():
    window.cur_question+=1
    if window.cur_question >= len(questions_list):
        window.cur_question = 0
    q = questions_list[window.cur_question]
    ask(q)

def click_ok():
    if btn_OK.text() == 'Ответить':
        check_answer()
    else:
        next_question()
    


# -------------- Создание главной направляющей и наполнение ее нашими направляющими --------------
main_layout = QVBoxLayout()
main_layout.addLayout(layout_question, stretch=2)
main_layout.addLayout(layout_radioGroups, stretch=8)
main_layout.addStretch(1)
main_layout.addLayout(layout_ans_btn, stretch=1)
main_layout.addStretch(1)

btn_OK.clicked.connect(click_ok)
# -------------- Создание окна и установка главной направляющей --------------
window = QWidget()
window.setLayout(main_layout)

window.cur_question=-1
next_question()

# -------------- Изменение параметров окна --------------
window.setWindowTitle("Memory Card")
window.resize(600, 400)

# -------------- Показ окна и запуск приложения --------------
window.show()
app.exec_()
