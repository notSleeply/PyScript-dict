import re

# 词典文件路径
dictTxt = './dict/dictionary.txt'
# 保存的文件路径
outputTxt = 'processed_dictionary1.txt'

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

# 提取单词
def extract_word(entry):
    word_match = re.match(r'^([a-zA-Z-]+)', entry)
    if word_match:
        return word_match.group(1)
    return None

# 提取所有中文释义
def extract_explanations(entry, pos_patterns):
    pos_explanations = {pos: [] for pos in POS_TYPES}
    
    # 提取所有中文释义
    for pattern, pos in pos_patterns:
        for match in re.finditer(pattern, entry, re.IGNORECASE):
            chinese = match.group(1)
            chinese = re.sub(r'[^\u4e00-\u9fa5；，、]', '', chinese)
            if chinese and chinese not in pos_explanations[pos]:
                pos_explanations[pos].append(chinese)
    
    # 兜底：如果没有匹配到，直接提取所有中文短语
    if not any(pos_explanations.values()):
        all_chinese = re.findall(r'[\u4e00-\u9fa5]{2,}', entry)
        if all_chinese:
            pos_explanations['other'].extend(all_chinese)
    
    return pos_explanations

# 格式化输出结果
def format_entry_result(word, pos_explanations):
    result_lines = [word]
    for pos in ['n', 'v', 'adj', 'adv', 'prep', 'conj', 'pron', 'other']:
        if pos_explanations[pos]:
            explanations = '；'.join(pos_explanations[pos])
            result_lines.append(f"- {pos}  {explanations}；")
    
    if len(result_lines) > 1:
        return '\n'.join(result_lines)
    return None

# 处理词典文本，提取单词和释义
def process_dictionary(text):
    entries = re.split(r'\n(?=[a-zA-Z-]+\s)', text.strip())
    results = []

    for entry in entries:
        if not entry.strip():
            continue

        # 提取单词
        word = extract_word(entry)
        if not word:
            continue
        
        # 提取释义
        pos_explanations = extract_explanations(entry, pos_patterns)
        
        # 构建输出
        formatted_result = format_entry_result(word, pos_explanations)
        if formatted_result:
            results.append(formatted_result)

    return '\n\n'.join(results)

# 将内容保存到文件
def save_to_file(content, filename):
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)


if __name__ == "__main__":
    with open(dictTxt, 'r', encoding='utf-8') as f:
        dictionary_text = f.read()

    processed_content = process_dictionary(dictionary_text)
    
    save_to_file(processed_content, outputTxt)
    print(f"处理完成，结果已保存到{outputTxt}")