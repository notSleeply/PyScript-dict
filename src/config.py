import os

dict_name = 'dictionary'
""" 词典名称，用于生成文件名和路径 """

dict_type = 'txt'
""" 原始词典文件类型 """

dict_out_type = 'txt'
""" 导出文件类型"""

dict_raw = os.path.join('../dict/raw', f'{dict_name}.{dict_type}')
""" 原词典文件路径 """

dict_processed = os.path.join('../dict/processed', dict_out_type, f'processed_{dict_name}.{dict_out_type}')
""" 处理后词典文件路径 """

pos_patterns = [
    (r'noun.*?[*]?\s*([\u4e00-\u9fa5；，、]+)', 'n'),
    (r'verb.*?[*]?\s*([\u4e00-\u9fa5；，、]+)', 'v'),
    (r'adjective.*?[*]?\s*([\u4e00-\u9fa5；，、]+)', 'adj'),
    (r'adverb.*?[*]?\s*([\u4e00-\u9fa5；，、]+)', 'adv'),
    (r'preposition.*?[*]?\s*([\u4e00-\u9fa5；，、]+)', 'prep'),
    (r'conjunction.*?[*]?\s*([\u4e00-\u9fa5；，、]+)', 'conj'),
    (r'pronoun.*?[*]?\s*([\u4e00-\u9fa5；，、]+)', 'pron'),
    (r'determiner.*?[*]?\s*([\u4e00-\u9fa5；，、]+)', 'other'),
    (r'exclamation.*?[*]?\s*([\u4e00-\u9fa5；，、]+)', 'other'),
    (r'plural noun.*?[*]?\s*([\u4e00-\u9fa5；，、]+)', 'n'),
    (r'abbreviation.*?[*]?\s*([\u4e00-\u9fa5；，、]+)', 'other')
]
"""  词性正则表达式列表，用于匹配不同的词性及其释义 """

POS_TYPES = ['n', 'v', 'adj', 'adv', 'prep', 'conj', 'pron', 'other']
""" 词性列表，用于结果格式化 """