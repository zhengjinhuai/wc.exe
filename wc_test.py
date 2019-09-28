import unittest
import file_processor as fp
import os


class TestMethod(unittest.TestCase):
    """单元测试类"""
    def setUp(self):
        """测试夹具，用来初始化变量"""
        self.file_path = os.path.join(os.getcwd(), 'TestFile')
        self.cwd_path = os.getcwd()
        self.char_sum = 0
        self.word_sum = 0
        self.line_sum = 0
        self.blank_line = 0
        self.code_line = 0
        self.comment_line = 0

    def test_char(self):
        """测试只有一个字符的文件"""
        self.char_sum = fp.FileProcessor.calculate_char_sum(os.path.join(self.file_path, 'one_char.py'))
        self.assertEqual(1, self.char_sum, "统计字符出现错误")

    def test_word(self):
        """测试只有一个词的文件"""
        self.word_sum = fp.FileProcessor.calculate_word_sum(os.path.join(self.file_path, 'one_word.py'))
        self.assertEqual(1, self.word_sum, "统计单词出现错误")

    def test_line(self):
        """测试只有一行的文件"""
        self.line_sum = fp.FileProcessor.calculate_line_sum(os.path.join(self.file_path, 'one_line.py'))
        self.assertEqual(1, self.line_sum, "统计行数出现错误")

    def test_more(self):
        """测试一个典型的源文件"""
        [self.code_line, self.blank_line, self.comment_line] \
            = fp.FileProcessor.calculate_another_sum(os.path.join(self.file_path, 'code.py'))
        self.assertEqual([16, 9, 19], [self.code_line, self.blank_line, self.comment_line], "统计出现错误")

    def test_glob(self):
        """测试统配符递归查询并处理"""
        glob_path = r'*.py'
        files_list = fp.FileProcessor.recursive_directory(self.cwd_path, glob_path)
        target_list = [os.path.join(self.cwd_path, 'file_processor.py'),
                       os.path.join(self.cwd_path, 'wc_cmd.py'),
                       os.path.join(self.cwd_path, 'wc_gui.py'),
                       os.path.join(self.cwd_path, 'wc_test.py')]
        self.assertEqual(target_list, files_list, "通配符匹配出现错误")


if __name__ == '__main__':
    test_suite = unittest.TestSuite()

    # 控制用例执行顺序
    tests = [TestMethod('test_char'), TestMethod('test_word'),
             TestMethod('test_line'), TestMethod('test_more'),
             TestMethod('test_glob')]
    test_suite.addTests(tests)

    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(test_suite)
