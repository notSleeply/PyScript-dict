import os
import json
import re
from tools.unique import get_unique_dir

def split_dictionary_by_initial(txt_path, output_dir):

    output_dir = get_unique_dir(output_dir)
    # 读取处理后的词典内容
    with open(txt_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 按空行分割每个单词块
    entries = re.split(r'\n{2,}', content.strip())
    initial_dict = {}

    for entry in entries:
        lines = entry.strip().split('\n')
        if not lines:
            continue
        word = lines[0].strip()
        if not word:
            continue
        initial = word[0].lower()
        if not initial.isalpha():
            initial = '#'
        if initial not in initial_dict:
            initial_dict[initial] = []
        explanations = [line.lstrip('- ').strip() for line in lines[1:]]
        # 组装为字典结构，便于 json 存储
        initial_dict[initial].append({
            "word": word,
            "explanations": explanations
        })
    
    # 输出目录
    os.makedirs(output_dir, exist_ok=True)
    for initial, items in initial_dict.items():
        json_path = os.path.join(output_dir, f"{initial}.json")
        with open(json_path, 'w', encoding='utf-8') as f:
            json.dump(items, f, ensure_ascii=False, indent=2)
    print(f"已按首字母拆分并保存到 {output_dir}")