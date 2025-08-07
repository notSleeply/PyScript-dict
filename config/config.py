import os

# 配置词典文件名词
dictName = 'dictionary'

# 配置文件路径
dictTxt = os.path.join('./dict', f'{dictName}.txt')
processedTxt = os.path.join('./processed', f'processed_{dictName}.txt')
output_dir = os.path.join('./dictJson/', f'{dictName}')

# 词性正则
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

# 初始化词性解释字典
POS_TYPES = ['n', 'v', 'adj', 'adv', 'prep', 'conj', 'pron', 'other']