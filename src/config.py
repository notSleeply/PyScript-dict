"""
`config.py` - **配置模块**
1. 定义词典名称、类型、路径等配置参数
"""

import os

types = {
    'txt':'txt',
    'json':'json',
    'csv':'csv',
}
""" 支持的文件类型列表 """

dict_list = {
    '百词斩':'百词斩词典',
}
""" 支持的词典列表 """


dict_name = dict_list['百词斩']
""" 词典名称，用于生成文件名和路径 """

dict_type = types["txt"]
""" 原始词典文件类型 """

dict_out_type = types["txt"]
""" 导出文件类型"""

dict_raw = os.path.join('../dict/raw', f'{dict_name}.{dict_type}')
""" 原词典文件路径 """

dict_processed = os.path.join('../dict/processed', dict_out_type, f'processed_{dict_name}.{dict_out_type}')
""" 处理后词典文件路径 """

