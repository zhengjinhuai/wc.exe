import os
import glob


class FileProcessor:

    @staticmethod
    def calculate_char_sum(filename):
        """
        -c file.c 返回文件file.c的字符数

        :param filename: 文件绝对路径
        :return: 统计结果
        """
        char_sum = 0
        if filename and os.path.exists(filename):
            with open(filename, 'r', encoding='utf-8') as f:
                while True:
                    line = f.readline()
                    if not line:
                        break
                    char_sum += len(line.strip())  # 文本中间的空格也算是字符
        else:
            raise OSError('请检查文件路径是否输入正确')
        return char_sum

    @staticmethod
    def calculate_word_sum(filename):
        """
        -w file.c 返回文件的file.c的单词数目

        :param filename: 文件的绝对路径
        :return:  单词总数
        """
        word_sum = 0
        if filename and os.path.exists(filename):
            with open(filename, 'r', encoding='utf-8') as f:
                while True:
                    line = f.readline()
                    if not line:
                        break
                    word_sum += len(line.strip().split())
        else:
            raise OSError('请检查文件路径是否输入正确')

        return word_sum

    @staticmethod
    def calculate_line_sum(filename):
        """
        -l file.c 返回文件file.c的行数

        :param filename: 文件的绝对路径
        :return:  行数
        """
        line_sum = 0
        if filename and os.path.exists(filename):
            with open(filename, 'r', encoding='utf-8') as f:
                while True:
                    line = f.readline()
                    if not line:
                        break
                    line_sum += 1
        else:
            raise OSError('请检查文件路径是否输入正确')
        return line_sum

    @staticmethod
    def recursive_directory(source_file, glob_file):
        """
        -s 递归获取目录下符合条件的文件

        :param source_file:  文件路径
        :param glob_file:  通配符格式
        :return: 符合条件的文件列表
        """
        target_file = os.path.join(source_file, glob_file)
        list_file = glob.glob(target_file, recursive=True)
        if not list_file:
            raise OSError('文件不存在')
        return list_file

    @staticmethod
    def calculate_another_sum(filename):
        """
        -a file.c 返回更复杂的数据（代码行 / 空行 / 注释行）

        代码行：本行包括多于一个字符的代码
        空行  ：本行全部是空格或格式控制字符，如果包括代码，则只有不超过一个可显示的字符，例如“{”
        注释行：本行不是代码行，并且本行包括注释。
                一个有趣的例子是有些程序员会在单字符后面加注释：  } //注释
                在这种情况下，这一行属于注释行。

        :param filename:
        :return: 统计结果
        """
        code_line = 0
        blank_line = 0
        comment_line = 0

        # # 由于不同程序语言的注释符号不一样，所以定义一个配置常量
        # comment_config = {"python": {"start_comment": ['"""', "'''"], "end_comment": ['"""', "'''"], "single": "#"},
        #                   "java": {"start_comment": ["/*"], "end_comment": ["*/"], "single": "//"}}

        is_comment_block = False  # 用来标识代码是否为多行注释块
        if os.path.exists(filename):
            with open(filename, 'r', encoding='utf-8') as f:
                while True:
                    line = f.readline()
                    if not line:
                        break  # 文件读取结束
                    line = line.strip()

                    # 统计空行行数，多行注释中的空行当作注释处理
                    if line == "" and not is_comment_block:
                        blank_line += 1

                    # 统计注释行数有四种情况
                    # 1. 单个符号开头，如'#'
                    # 2. 多行注释符在同一行的情况
                    # 3. 多行注释符之间的行数
                    elif line.startswith("#") or \
                            (line.startswith('"""') and line.endswith('"""') and len(line) > 3) or \
                            (line.startswith("'''") and line.endswith("'''") and len(line) > 3) or \
                            (is_comment_block and not (line.endswith('"""') or line.endswith("'''"))):
                        comment_line += 1
                    # 4. 多行注释符的开始行和结束行
                    elif line.startswith('"""') or line.endswith('"""') or \
                            line.startswith("'''") or line.endswith("'''"):
                        is_comment_block = not is_comment_block
                        comment_line += 1
                    else:
                        code_line += 1
        return code_line, blank_line, comment_line
