import argparse
import gui
import file_processor as fp


parser = argparse.ArgumentParser(description="Imitate the function of program wc.exe")
parser.add_argument('-c', '--char', default=False, action='store_true',
                    help='calculate the total number of characters',)
parser.add_argument('-w', '--word', default=False, action='store_true',
                    help='calculate the total number of words',)
parser.add_argument('-l', '--line', default=False, action='store_true',
                    help='calculate the total number of lines',)
parser.add_argument('-a', '--another', default=False, action='store_true',
                    help='returns more complex data (lines of code/blank lines/comment lines)')
parser.add_argument('-x', '--gui', default=False, action='store_true',
                    help='Use windows gui')
parser.add_argument('-s', type=str, default=None,
                    help='enter wildcards to recursively process directory eligible files')
parser.add_argument('filename', type=str, nargs='?',
                    help='enter absolute path of file')

args = parser.parse_args()


def main():
    # filename = r"C:\Users\ace87\Desktop\wc.txt"
    print(args)
    if args.gui:
        gui.wc_gui()

    if not args.filename:
        print('未输入文件路径')
    elif args.s is not None:
        list_file = fp.FileProcessor.recursive_directory(args.filename, args.s)
        for i in range(len(list_file)):
            print('文件路径：', list_file[i])
            if args.char:
                char_sum = fp.FileProcessor.calculate_char_sum(list_file[i])
                print('字符数：', char_sum)
            if args.word:
                word_sum = fp.FileProcessor.calculate_word_sum(list_file[i])
                print('单词数：', word_sum)
            if args.line:
                line_sum = fp.FileProcessor.calculate_line_sum(list_file[i])
                print('总行数：', line_sum)
            if args.another:
                code_line, blank_line, comment_line = fp.FileProcessor.calculate_another_sum(list_file[i])
                print('代码行数：', code_line)
                print('空白行数：', blank_line)
                print('注释行数：', comment_line)
    else:
        print('文件路径：', args.filename)
        if args.char:
            char_sum = fp.FileProcessor.calculate_char_sum(args.filename)
            print('字符数：', char_sum)
        if args.word:
            word_sum = fp.FileProcessor.calculate_word_sum(args.filename)
            print('单词数：', word_sum)
        if args.line:
            line_sum = fp.FileProcessor.calculate_line_sum(args.filename)
            print('行数：', line_sum)
        if args.another:
            code_line, blank_line, comment_line = fp.FileProcessor.calculate_another_sum(args.filename)
            print('代码行数：', code_line)
            print('空白行数：', blank_line)
            print('注释行数：', comment_line)


if __name__ == '__main__':
    main()
