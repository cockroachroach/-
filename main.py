import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from evaluateWindow import evaluateWindow
from rumorWindow import rumorWindow
from PyQt5.QtGui import QPixmap

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("主界面")
        self.setGeometry(600, 300, 600, 300)

        layout = QVBoxLayout()
        # 添加标题Label
        title_text = "<font color='red' size='6'>巨量黑话，模因轰炸，高次反转，抽象矩阵生成器</font>"
        title_label = QLabel(title_text)
        title_label.setAlignment(Qt.AlignHCenter)  # 水平居中对齐
        layout.addWidget(title_label)
        # 添加其它Label
        desc_text = ("‘为什么巨量黑话掌握者没有使用抽象模因轰炸而是容忍她如数家珍般复读那套令人发笑的破词？’"
                     "——致敬传奇巨模高抽拥有者，网感手法证明者，反转n次信仰玩家adagio")
        desc_label = QLabel(desc_text)
        desc_label.setAlignment(Qt.AlignHCenter)  # 水平居中对齐
        desc_label.setWordWrap(True)  # 允许文本换行
        layout.addWidget(desc_label)
        #插入图片
        pic_label=QLabel(self)
        pixmap=QPixmap("title.png")
        pic_label.setPixmap(pixmap)
        pic_label.setScaledContents(True)
        layout.addWidget(pic_label)
        # 添加按钮
        button_layout = QHBoxLayout()

        rumor_button = QPushButton("造谣模式")
        review_button = QPushButton("锐评模式")
        #绑定点击事件处理函数
        review_button.clicked.connect(self.open_evaluate_mode)
        rumor_button.clicked.connect(self.open_rumor_mode)

        button_layout.addWidget(rumor_button)
        button_layout.addWidget(review_button)

        layout.addLayout(button_layout)

        self.setLayout(layout)

    def open_evaluate_mode(self):
        self.evaluateWindow = evaluateWindow()
        self.evaluateWindow.show()
        self.close()

    def open_rumor_mode(self):
        self.rumorWindow = rumorWindow()  # 创建新窗口
        self.rumorWindow.show()  # 显示新窗口
        self.close()  # 关闭当前窗口


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())