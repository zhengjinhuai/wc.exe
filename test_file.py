import file_processor as fp
import os


class TestMethod:
    def __init__(self):
        self.char_sum = 0
        self.word_sum = 0
        self.line_sum = 0
        self.blank_line = 0
        self.code_line = 0
        self.comment_line = 0

    def test_char(self, filename):
        self.char_sum = fp.FileProcessor.calculate_char_sum(filename)
        print(filename, '字符数为：', self.char_sum)

    def test_word(self, filename):
        self.word_sum = fp.FileProcessor.calculate_word_sum(filename)
        print(filename, '单词数为：', self.word_sum)

    def test_line(self, filename):
        self.line_sum = fp.FileProcessor.calculate_line_sum(filename)
        print(filename, '总行数为：', self.line_sum)

    def test_more(self, filename):
        self.code_line, self.blank_line, self.comment_line \
            = fp.FileProcessor.calculate_another_sum(filename)
        print(filename, '空白行数为：', self.blank_line)
        print(filename, '代码行数为：', self.code_line)
        print(filename, '注释行数为：', self.comment_line)

    def test_glob(self, source_path, glob_path):
        target_list = fp.FileProcessor.recursive_directory(source_path, glob_path)
        return target_list


if __name__ == '__main__':
    work_path = os.getcwd()
    file_path = os.path.join(work_path, 'testfile')
    file_list = list()
    file_list.append(os.path.join(file_path, 'one_char.py'))
    file_list.append(os.path.join(file_path, 'one_line.py'))
    file_list.append(os.path.join(file_path, 'one_word.py'))
    file_list.append(os.path.join(file_path, 'blank.py'))
    file_list.append(os.path.join(file_path, 'code.py'))
    test = TestMethod()
    # 测试只有一个字符的文件
    test.test_char(file_list[0])
    # 测试只有一行的文件
    test.test_line(file_list[1])
    test.test_word(file_list[1])
    # 测试只有一个单词的文件
    test.test_word(file_list[2])
    # 测试空文件
    test.test_more(file_list[3])
    # 测试一个典型的源文件
    test.test_more(file_list[4])
    # 测试递归处理
    source_path = os.getcwd()
    glob_path = '**/*.py'

    # 返回符合条件的文件
    target_list = test.test_glob(source_path, glob_path)
    # 统计字符数
    for i in range(len(target_list)):
        test.test_char(target_list[i])
        test.test_word(target_list[i])
        test.test_line(target_list[i])
        test.test_more(target_list[i])

