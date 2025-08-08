"""
`main.py`  - **调度中心**
1. 解析`config` 配置的参数（选择输入文件、解析器、导出类型等）
2. 根据参数调用对应的 `parser/` 模块解析词典
3. 把解析结果交给 `typer/` 模块导出到 `dict/processed/` 对应的子文件夹
"""
from config import dict_name
from parser.words100 import parse_words100

def fun_words100():
    """
    - 函数名:  fun_word100
    - 作用: 调用解析百词斩词典的函数
    """
    parse_words100()


def main():
    match dict_name :
        case "百词斩词典":
            fun_words100()
        case _:
            print(f"未找到对应的词典解析器: {dict_name}")


if __name__ == "__main__":
    main()