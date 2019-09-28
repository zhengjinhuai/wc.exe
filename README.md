# wc.exe
Imitate the function of program wc.exe

# 项目简介
wc.exe是一个常见的工具，它能够统计文本文件的字符数、单词数和行数。本次项目要求写一个命令行程序，模仿已有的wc.exe的功能，并加以扩充，同时使用GUI进行可视化
具体功能要求：

1. 程序处理用户需求的模式为：wc.exe [parameter] [file_name]
2. 基本功能：
- wc.exe -c file.c    //返回文件 file.c 的字符数
- wc.exe -w file.c    //返回文件 file.c 的词的数目
- wc.exe -l file.c    //返回文件 file.c 的行数
3. 扩展功能：
- -s   递归处理目录下符合条件的文件
-a   返回更复杂的数据（代码行 / 空行 / 注释行）
4. 高级功能：
- -x 参数。如果命令行有这个参数，程序会显示图形界面，用户可以通过界面选取单个文件，程序就会显示文件的字符数、行数等全部统计信息。
- 需求举例：wc.exe -s -a *.c

---
# 使用说明
1. 下载wc.exe文件
2. 使用方法：`wc.exe [parameter] [file_name]`，或者进行可视化`wc.exe -x`
3. 在终端进行代码覆盖率测试
- `coverage run -p wc_cmd.py -c -a -w -l 路径名 -s 通配符`
- `coverage run -p wc_cmd.py -x`
- 进行多次测试，最后合并多份结果：`coverage combine`
- 显示结果：`coverage report`
- HTML显示结果并保存：`coverage html -d covhtml`


4. 在终端进行`.exe`文件的打包生成
- `pyinstaller -F wc_cmd.py  -n wc.exe --hidden-import wc_gui --hidden-import file_processor`
- 打包的前提是要确保所需模块都已经安装好

5. 在终端进性效能测试
- `python -m cProfile -s cumulative  wc_cmd.py -c -a -w -l test_filename`
