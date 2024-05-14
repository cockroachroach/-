from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
import random
import sys
import json

class evaluateWindow(QWidget):
    def __init__(self):
        super().__init__()

        def get_input():
            #读取json文件
            with open('enormousArgot.json', 'r', encoding='utf-8') as file:
                data = json.load(file)
            #接收输入
            input_text = line_edit.text()
            theme = input_text
            article = ""
            #引用语料库数据
            principal = data["jushi"]
            start = data["theme"]
            exit = data["end"]
            bosh = data["among"]
            #生成文章
            while len(article) < 70:
                branch = random.randint(0, 70)
                if branch < 20:
                    article += "\n\n"
                if branch < 30:
                    random.shuffle(principal)
                    speech = principal[0]
                    speech = speech.replace("a", random.choice(start))
                    speech = speech.replace("b", random.choice(exit))
                    article += speech
                else:
                    random.shuffle(bosh)
                    article += bosh[0]

            article = article.replace('x', theme)
            label2.setText(article)
            label1.setText("")

        self.setWindowTitle("巨模高抽锐评系统")
        self.setGeometry(600, 300, 600, 300)

        layout = QVBoxLayout()

        # 添加标题Label
        title_label = QLabel("<font color='red' size='6'>巨量黑话，模因轰炸，高次反转，抽象矩阵锐评系统</font>")
        title_label.setAlignment(Qt.AlignHCenter)  # 水平居中对齐
        layout.addWidget(title_label)

        label1 = QLabel("请输入你想要锐评的内容:")
        label2 = QLabel("")
        layout.addWidget(label2)
        layout.addWidget(label1)

        line_edit = QLineEdit()
        layout.addWidget(line_edit)

        button = QPushButton("锐评一下")
        button.clicked.connect(get_input)
        layout.addWidget(button)

        self.setLayout(layout)

