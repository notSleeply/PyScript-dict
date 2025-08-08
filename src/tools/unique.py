"""
`unique.py` - **工具模块**
1. 提供获取唯一文件名和目录名的函数
2. 用于避免文件名冲突
3. 确保在导出文件时不会覆盖已有文件
"""
import os

def get_unique_filename(filepath):
    """
    - 函数名: 获取唯一文件名
    - 作用: 获取唯一文件名
    - 参数:
        filepath (str): 原始文件路径
    - 返回:
        str: 唯一文件路径
    """
    if not os.path.exists(filepath):
        return filepath
    directory = os.path.dirname(filepath)
    filename = os.path.basename(filepath)
    name, ext = os.path.splitext(filename)
    counter = 1
    while True:
        new_filename = f"{name}{counter}{ext}"
        new_filepath = os.path.join(directory, new_filename)
        if not os.path.exists(new_filepath):
            return new_filepath
        counter += 1


def get_unique_dir(dir):
    """
    - 函数名: 获取唯一目录名
    - 作用: 获取唯一目录名
    - 参数:
        dir (str): 原始目录路径
    - 返回:
        str: 唯一目录路径
    """
    if not os.path.exists(dir):
        return dir
    count = 1
    while True:
        new_dir = f"{dir}_{count}"
        if not os.path.exists(new_dir):
            return new_dir
        count += 1