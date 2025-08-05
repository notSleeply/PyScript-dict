# py-cambridge-dict-script

这是一款专门用于处理剑桥词典相关数据的 Python 脚本，旨在为用户提供便捷、高效的词典数据处理体验，无论是进行语言研究、开发学习工具还是整理个人词汇库，都能发挥重要作用。

## 核心功能

- **数据提取**：能够精准从剑桥词典的网页或者本地存储的文件中，提取出单词、音标、词性、详尽释义以及实用例句等关键信息，不放过任何一个重要内容。

- **格式转换**：支持将提取到的词典数据转换为 JSON、TXT、Excel 等多种常见格式，满足不同场景下的数据使用需求。

- **内容筛选**：允许用户根据自身需求，按照单词字母范围、词性、释义关键词等条件进行筛选，快速获取目标数据。

- **数据清洗**：自动去除数据中的冗余信息、错误格式，确保输出数据的准确性和规范性。

## 快速安装

在使用本脚本之前，请确保你的电脑已安装 Python 3.7 及以上版本。

1. 首先克隆本仓库到本地：

```
git clone https://github.com/yourusername/py-cambridge-dict-script.git
```

1. 进入项目目录：

```
cd py-cambridge-dict-script
```

1. 安装所需依赖：

```
pip install -r requirements.txt
```

## 使用教程

### 示例 1：提取并导出网页数据

```
from cambridge_handler import CambridgeHandler

# 初始化处理器，传入剑桥词典网页URL
handler = CambridgeHandler(url="https://dictionary.cambridge.org/dictionary/english/example")
# 提取数据
handler.extract_data()
# 将数据导出为JSON格式
handler.export_data("output.json", format="json")
```

### 示例 2：处理本地文件并筛选数据

```
from cambridge_handler import CambridgeHandler

# 初始化处理器，传入本地文件路径
handler = CambridgeHandler(file_path="local_cambridge_data.html")
# 提取数据
handler.extract_data()
# 筛选出词性为名词的单词
noun_data = handler.filter_data(pos="noun")
# 将筛选后的数据导出为Excel格式
handler.export_data("noun_words.xlsx", format="excel", data=noun_data)
```

## 依赖列表

- requests：用于获取网页数据

- beautifulsoup4：用于解析 HTML 内容

- pandas：用于数据处理和格式转换

- openpyxl：用于 Excel 文件的读写

## 许可证

本项目采用 MIT 许可证，详情请查看 LICENSE 文件。

## 反馈与贡献

如果在使用过程中遇到任何问题，或者有好的建议，欢迎通过 Issue 向我们反馈。同时，也非常欢迎各位开发者提交 Pull Request，一起完善这个脚本。