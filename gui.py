import sys
import PyQt5
from PyQt5.QtWidgets import (QWidget, QPushButton, QApplication,
                             QMessageBox, QLineEdit, QTextEdit,
                             QLabel, QGridLayout, QCheckBox,
                             QListWidget, QFileDialog)
from PyQt5.QtCore import Qt
import file_processor as fp


class WCExample(QWidget):
    def __init__(self):
        super(WCExample, self).__init__()
        self.init_ui()

    def init_ui(self):

        self.calculate_button = QPushButton("统计结果", self)
        self.cancel_button = QPushButton("清空界面", self)

        self.file_path = QPushButton("文件路径")
        # self.file_path.setAlignment(Qt.AlignCenter)
        self.filename_edit = QLineEdit()

        self.target_file = QLabel("通配符")
        self.target_file.setAlignment(Qt.AlignCenter)
        self.glob_edit = QLineEdit()

        self.char_box = QCheckBox('计算字符数', self)
        self.line_box = QCheckBox('计算总行数', self)
        self.word_box = QCheckBox('计算单词数', self)
        self.more_box = QCheckBox('计算复杂项', self)
        self.find_box = QCheckBox('通配符查询', self)

        self.result_edit = QTextEdit()

        grid = QGridLayout()
        grid.setSpacing(10)

        grid.addWidget(self.file_path, 1, 0)
        grid.addWidget(self.filename_edit, 1, 1, 1, 4)
        grid.addWidget(self.target_file, 1, 5)
        grid.addWidget(self.glob_edit, 1, 6)
        grid.addWidget(self.char_box, 2, 0)
        grid.addWidget(self.line_box, 2, 1)
        grid.addWidget(self.word_box, 2, 2)
        grid.addWidget(self.more_box, 2, 3)
        grid.addWidget(self.find_box, 2, 4)
        grid.addWidget(self.calculate_button, 2, 5)
        grid.addWidget(self.cancel_button, 2, 6)
        grid.addWidget(self.result_edit, 3, 0, 7, 0)

        # 设置信号
        self.file_path.clicked.connect(self.get_file_path)
        self.calculate_button.clicked.connect(self.calculate_results)
        self.cancel_button.clicked.connect(self.clear_all)

        self.setLayout(grid)
        self.setGeometry(500, 400, 800, 400)
        self.setWindowTitle('wc')

    def closeEvent(self, event):
        """关闭窗口前确认"""
        reply = QMessageBox.question(self, '确认退出', "是否关闭程序？",
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

    def get_file_path(self):
        file_path, file_type = QFileDialog.getOpenFileName(self, "选择文件")
        self.filename_edit.clear()
        self.filename_edit.setText(file_path)

    def calculate_results(self):
        choose_file = self.filename_edit.text()
        select_char = self.char_box.isChecked()
        select_word = self.word_box.isChecked()
        select_line = self.line_box.isChecked()
        select_more = self.more_box.isChecked()
        select_find = self.find_box.isChecked()
        if not choose_file:
            print('None')
        elif select_find:
            source_file = self.filename_edit.text()
            glob_file = self.glob_edit.text()
            list_file = fp.FileProcessor.recursive_directory(source_file, glob_file)
            for i in range(len(list_file)):
                self.result_edit.append('文件路径：' + list_file[i])
                if select_char:
                    char_sum = fp.FileProcessor.calculate_char_sum(list_file[i])
                    self.result_edit.append('字符数为：' + str(char_sum))
                if select_word:
                    word_sum = fp.FileProcessor.calculate_word_sum(list_file[i])
                    self.result_edit.append('单词数为：' + str(word_sum))
                if select_line:
                    line_sum = fp.FileProcessor.calculate_line_sum(list_file[i])
                    self.result_edit.append('总行数为：' + str(line_sum))
                if select_more:
                    code_line, blank_line, comment_line = fp.FileProcessor.calculate_another_sum(list_file[i])
                    self.result_edit.append('代码行数为：' + str(code_line))
                    self.result_edit.append('空白行数为：' + str(blank_line))
                    self.result_edit.append('注释行数为：' + str(comment_line))
        else:
            self.result_edit.append('文件路径: ' + choose_file)
            if select_char:
                char_sum = fp.FileProcessor.calculate_char_sum(choose_file)
                self.result_edit.append('字符数为：' + str(char_sum))
            if select_word:
                word_sum = fp.FileProcessor.calculate_word_sum(choose_file)
                self.result_edit.append('单词数为：' + str(word_sum))
            if select_line:
                line_sum = fp.FileProcessor.calculate_line_sum(choose_file)
                self.result_edit.append('总行数为：' + str(line_sum))
            if select_more:
                code_line, blank_line, comment_line = fp.FileProcessor.calculate_another_sum(choose_file)
                self.result_edit.append('代码行数为：' + str(code_line))
                self.result_edit.append('空白行数为：' + str(blank_line))
                self.result_edit.append('注释行数为：' + str(comment_line))

    def clear_all(self):
        self.filename_edit.clear()
        self.glob_edit.clear()
        self.result_edit.clear()


def wc_gui():
    app = QApplication(sys.argv)
    gui = WCExample()
    gui.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    wc_gui()
