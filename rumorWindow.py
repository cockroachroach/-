from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
import random
import sys
import json
from PyQt5.QtGui import QFont

class rumorWindow(QWidget):
    def __init__(self):
        super().__init__()

        def get_input():
            #读取json文件
            with open('rumor.json', 'r', encoding='utf-8') as file:
                data = json.load(file)
            # 接收输入
            input_text = line_edit.text()
            theme = input_text
            article = ""
            #引用语料库数据
            principal=data["rumor"]
            #生成文章
            random.shuffle(principal)
            article=principal[0]

            article = article.replace('x', theme)
            label2.setText(article)
            label1.setText("")

        self.setWindowTitle("巨模高抽造谣系统")
        self.setGeometry(600, 300, 600, 300)

        layout = QVBoxLayout()

        title_label = QLabel("<font color='red' size='6'>巨量黑话，模因轰炸，高次反转，抽象矩阵造谣系统</font>")
        title_label.setAlignment(Qt.AlignHCenter)  # 水平居中对齐
        layout.addWidget(title_label)

        label1 = QLabel("请输入你想要造谣的对象：")
        layout.addWidget(label1)

        label2 = QLabel("")
        layout.addWidget(label2)

        line_edit=QLineEdit()
        layout.addWidget(line_edit)

        rumorBtn = QPushButton("造谣一下")
        rumorBtn.clicked.connect(get_input)
        layout.addWidget(rumorBtn)

        self.setLayout(layout)

