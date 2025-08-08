# PyScript-dict Makefile
# 可自定义的配置项
PYTHON = .venv\Scripts\python.exe

# 创建虚拟环境
venv:
		python -m venv .venv

# 安装依赖
install:
		$(PYTHON) -m pip install --upgrade pip
		$(PYTHON) -m pip install -r requirements.txt

# 运行主程序处理词典
run:
		$(PYTHON) src/main.py