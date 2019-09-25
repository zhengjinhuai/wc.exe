# blank_line = 0
# comment_line = 0
# code_line = 0
# is_comment_block = False  # 用来标识代码是否为多行注释块
# with open(r'F:\san.py', 'r', encoding='UTF-8') as f:
#     while True:
#         line = f.readline()
#         if not line:
#             break  # 文件读取结束
#         line = line.strip()
#         print(line)
#
#         # 统计空行行数，多行注释中的空行当作注释处理
#         print(line.startswith('"""'), line.endswith('"""'), line.startswith("'''"), line.endswith("'''"), is_comment_block)
#         if line == "" and not is_comment_block:
#             blank_line += 1
#
#         # 统计注释行数有四种情况
#         # 1. 单个符号开头，如'#'
#         # 2. 多行注释符在同一行的情况
#         # 3. 多行注释符之间的行数
#         elif line.startswith("#") or \
#                 (line.startswith('"""') and line.endswith('"""') and len(line) > 3) or \
#                 (line.startswith("'''") and line.endswith("'''") and len(line) > 3) or \
#                 (is_comment_block and not (line.endswith('"""') or line.endswith("'''"))):
#             comment_line += 1
#         # 4. 多行注释符的开始行和结束行
#         elif line.startswith('"""') or line.endswith('"""') or \
#                 line.startswith("'''") or line.endswith("'''"):
#             is_comment_block = not is_comment_block
#             comment_line += 1
#         else:
#             code_line += 1
#
# print(code_line, blank_line, comment_line)

import PyQt5