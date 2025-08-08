"""
`save.py` - **保存模块**
1. 提供将内容保存到文件的函数
"""

from tools.unique import get_unique_filename

def save_to_file(content, file):
    """
    - 函数名: save_to_file
    - 作用: 将内容保存到文件
    - 参数:
        content (str): 要保存的内容
        file (str): 目标文件路径
    - 返回:
        str: 实际保存的文件路径
    """
    unique_filename = get_unique_filename(file)
    with open(unique_filename, 'w', encoding='utf-8') as f:
        f.write(content)
    return unique_filename