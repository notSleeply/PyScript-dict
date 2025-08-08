"""
`extract.py` - **词典解析模块**
1. 解析词典文本，提取单词和释义
2. 使用正则表达式匹配不同的词性及其释义
"""

import re


def extract_word(entry):
    """
    - 函数名: extract_word
    - 作用: 提取单词
    - 参数:
        entry (str): 词典条目
    - 返回:
        str: 提取的单词
    """
    word_match = re.match(r'^([a-zA-Z-]+)', entry)
    if word_match:
        return word_match.group(1)
    return None