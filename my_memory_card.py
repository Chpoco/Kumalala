from PyQt5.QtCore import Qt 
from random import randint
from PyQt5.QtWidgets import QGroupBox, QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QHBoxLayout, QRadioButton
class DangeonMaster():
    def __init__(self, text, ans1, ans2, ans3, ans4, true):
        self.text = text
        self.ans1 = ans1
        self.ans2 = ans2
        self.ans3 = ans3
        self.ans4 = ans4
        self.true = true
q1 = [
     DangeonMaster('Кто ты?', 'эль примо', 'леон', 'кольт', '4', 4),
     DangeonMaster('Кто из них мужчина?', '8', '2', '0', '4', 3),
     DangeonMaster('кто белый?', '0', '1', '4', '2', 2),
     DangeonMaster('ты устал?', '4', 'yes', 'конечно', 'да', 1),
     DangeonMaster('когда Казахстан стал Казахстаном', '1000', '2000', '3000', '4000', 2)
]
app = QApplication([])
b = QWidget()
b.setWindowTitle("Memory Card")
b.move(0, 0)
b.resize(1368, 768)
b.show()
d = QVBoxLayout()
negr = QLabel()
white = QPushButton('Начать вопросы!')
d.addWidget(negr, alignment = Qt.AlignCenter)
RadioGroupBox = QGroupBox('Варианты бравлеров:')
a1 = QRadioButton()
a2 = QRadioButton()
a3 = QRadioButton()
a4 = QRadioButton()
g1 = QHBoxLayout()
g2 = QVBoxLayout()
g3 = QVBoxLayout()
g2.addWidget(a1)
g2.addWidget(a2)
g3.addWidget(a3)
g3.addWidget(a4)
g1.addLayout(g2)
g1.addLayout(g3)
RadioGroupBox.hide()
GroupBox = QGroupBox("5")
negr.hide()
x = QLabel('Здраствуй ты зашел в бравл страс')
m = QLabel('программа написанна на языке програмирования')
v = QLabel('приложение черное,белого почему то нету')
o = QVBoxLayout
o.addWidget(x, alignment = Qt.AlignCenter)
o.addWidget(m, alignment = Qt.AlignCenter)
o.addWidget(v, alignment = Qt.AlignCenter)

GroupBox.setLayout(o)


GroupBox.setLayout(d)
GroupBox.show()
f = QVBoxLayout()
l = QLabel('Правильный ответ:')
f.addWidget(l)
GroupBox2 = QGroupBox()
GroupBox2.setLayout(f)
GroupBox2.hide()
RadioGroupBox.setLayout(g1)
#d.addWidget(RadioGroupBox)
right_answer = 0

def negers(whiters):
    global right_answer
    right_answer = whiters.true
    negr.setText(whiters.text)
    a1.setText(whiters.ans1)
    a2.setText(whiters.ans2)
    a3.setText(whiters.ans3)
    a4.setText(whiters.ans4)
negers(q1.pop(0))
count = 0
tnuoc = 0
def bull():
    global right_answer
    global count
    global tnuoc
    global GroupBox
    
    if white.text() == 'Начать вопросы!':
        white.setText('Ответить:')
        GroupBox.hide()

    elif white.text() == 'Ответить:':
        white.setText('Следующий:')
        negr.show()
        GroupBox2.show()
        RadioGroupBox.hide()
        ans = 0
        if a1.isChecked():
            ans  = 1
        if a2.isChecked():
            ans  = 2
        if a3.isChecked():
            ans  = 3
        if a4.isChecked():
            ans  = 4
        if ans == right_answer:
            l.setText('Верный ответ')
            count +=1
        else:
            l.setText('Попуск')
            tnuoc +=1
    elif white.text() == 'Следующий:':
        RadioGroupBox.show()
        GroupBox2.hide()        
        white.setText('Ответить:')
        if len(q1) > 0:
            negers(q1.pop(randint(0, len(q1)-1)))
        else:
            white.hide()
            RadioGroupBox.hide()
            GroupBox2.show()             
            l.setText('Правильных ответов:' + str(count))
            negr.setText('Неправильных ответов:' + str(tnuoc))

    
white.clicked.connect(bull)
d.addWidget(GroupBox2)

d.addWidget(white, alignment = Qt.AlignCenter)
b.setLayout(d)









app.exec_()