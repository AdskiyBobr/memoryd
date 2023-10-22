from layout import*
from data import *
from random import choice, shuffle

ans_buttons = [ans1_button, ans2_button, ans3_button, ans4_button]
shuffle(ans_buttons)

frm = Form("Яка нинішня ціна Опрессора МК2?", "6 000 000 - 8 000 000", "2 275 000 - 3 750 000", "8 000 000 - 10 000 000", "1 000 000 - 2 000 000")
frm_card = FormView(frm, question_label, ans_buttons[0], ans_buttons[1], ans_buttons[2],ans_buttons[3])
frm_card.show()
showQuestion()


def check_result():
    if ans_button.text() == 'Відповісти':
        correct = frm_card.answer_W.is_checked()
        incorrect = frm_card.wrong_answer1_W.isChecked() or frm_card.wrong_answer2_W.isChecked() or frm_card.wrong_answer3_W.isChecked()
        if correct:
            print('Правильно')
            showAnswer()
        if incorrect:
            print("Неправильно!")
            showAnswer()
    else:
        showQuestion()

main_window = QWidget()
main_window.resize(800, 600)

ans_button.clicked.connect(check_result)
main_window.setLayout(main_layout)
main_window.show()
app.exec()
