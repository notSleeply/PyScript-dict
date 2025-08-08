"""
`main.py`  - **调度中心**
1. 解析`config` 配置的参数（选择输入文件、解析器、导出类型等）
2. 根据参数调用对应的 `parser/` 模块解析词典
3. 把解析结果交给 `typer/` 模块导出到 `dict/processed/` 对应的子文件夹
"""
from config import dict_name
from parser.words100 import parse_word100

def main():
    match dict_name :
        case "百词斩词典":
            parse_word100()



if __name__ == "__main__":
    main()