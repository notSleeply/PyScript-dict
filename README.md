# PyScript-dict

这是一款专门用于处理剑桥词典相关数据的 Python 脚本，旨在为用户提供便捷、高效的词典数据处理体验，无论是进行语言研究、开发学习工具还是整理个人词汇库，都能发挥重要作用。

## 核心功能

- **数据提取**：能够精准从剑桥词典的网页或者本地存储的文件中，提取出单词、音标、词性、详尽释义以及实用例句等关键信息，不放过任何一个重要内容。

- **格式转换**：支持将提取到的词典数据转换为 JSON、TXT、Excel 等多种常见格式，满足不同场景下的数据使用需求。

- **内容筛选**：允许用户根据自身需求，按照单词字母范围、词性、释义关键词等条件进行筛选，快速获取目标数据。

- **数据清洗**：自动去除数据中的冗余信息、错误格式，确保输出数据的准确性和规范性。

## 快速安装

在使用本脚本之前，请确保你的电脑已安装 Python 3.7 及以上版本。

1. 首先克隆本仓库到本地：

```powershell
git clone https://github.com/notSleeply/PyScript-dict.git
```

2. 进入项目目录：

```powershell
cd PyScript-dict
```

3. 安装所需依赖：

```powershell
pip install -r requirements.txt
```

## 目录结构

```shell
├── src/                      # 源代码
│   ├── config.py             # 📌 全局配置变量
│   ├── main.py               # 程序入口
│   ├── parser/               # 各种词典解析器，剑桥、牛津等
│   ├── typer/                # 导出模块，各种文件类型。例：全部json，分类json，txt等。
│   └── tools/                # 工具方法，
├── dict/
│   ├── raw/                  # 📥 原始词典文件
│   └── processed/            # 📤 处理后的词典文件
│   	├── json			  # Json 格式
│   	├── csv			  	  # Csv 格式
│       └── txt               # Txt 格式
```

## 规范

#### 注释规范

- 文件开头

```python
"""
main.py  - **调度中心**
1. 解析`config` 配置的参数（选择输入文件、解析器、导出类型等）
2. 根据参数调用对应的 `parser/` 模块解析词典
3. 把解析结果交给 `typer/` 模块导出到 `dict/processed/` 对应的子文件夹
"""
```

- 函数

```python
    """
    - 函数名: add
    - 作用: 计算两个整数的和
    - 参数:
        a (int): 第一个整数
        b (int): 第二个整数
    - 返回:
        int: 两数之和
    """
```

- 变量与定量

```python

dict_name = 'dictionary'
""" 词典名称，用于生成文件名和路径 """
```

#### Git提交规范

```shell
feat : 新功能
fix : 修复bug
doc : 文档改变
style : 代码格式改变
refactor : 某个已有功能重构
perf : 性能优化
test : 增加测试
build : 改变了build工具 如 grunt换成了 npm
revert : 撤销上一次的 commit
chore : 构建过程或辅助工具的变动
```

#### 模块规范

- 每个模型下都要有`__init.py`，并且要导入模型下的内容。

#### 命名规矩

- 命名样式 : 采用**下滑线**连接方式。 

## 许可证

本项目采用 MIT 许可证，详情请查看 [LICENSE](LICENSE) 文件。

## 反馈与贡献

如果在使用过程中遇到任何问题，或者有好的建议，欢迎通过 Issue 向我们反馈。同时，也非常欢迎各位开发者提交 Pull Request，一起完善这个脚本。