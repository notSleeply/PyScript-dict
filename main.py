import re

def process_dictionary(text):
    entries = re.split(r'\n(?=[a-zA-Z-]+\s)', text.strip())
    results = []

    for entry in entries:
        if not entry.strip():
            continue

        # 提取单词
        word_match = re.match(r'^([a-zA-Z-]+)', entry)
        if not word_match:
            continue
        word = word_match.group(1)

        # 词性与中文释义
        pos_explanations = {
            'n': [],
            'v': [],
            'adj': [],
            'adv': [],
            'prep': [],
            'conj': [],
            'pron': [],
            'other': []
        }

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

        # 构建输出
        result_lines = [word]
        for pos in ['n', 'v', 'adj', 'adv', 'prep', 'conj', 'pron', 'other']:
            if pos_explanations[pos]:
                explanations = '；'.join(pos_explanations[pos])
                result_lines.append(f"- {pos}  {explanations}；")
        if len(result_lines) > 1:
            results.append('\n'.join(result_lines))

    return '\n\n'.join(results)

if __name__ == "__main__":
    with open('dictionary.txt', 'r', encoding='utf-8') as f:
        dictionary_text = f.read()
    processed_content = process_dictionary(dictionary_text)
    with open('processed_dictionary.txt', 'w', encoding='utf-8') as f:
        f.write(processed_content)
    print("处理完成，结果已保存到processed_dictionary.txt")