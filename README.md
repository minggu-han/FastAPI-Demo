# FastAPI-Demo





# pip

|                 命令                 |                 说明                 |
| :----------------------------------: | :----------------------------------: |
|           pip install 包名           |             安装指定的包             |
|     pip install -i 镜像地址 包名     |      临时使用镜像地址安装指定包      |
| pip config set global.index-url 地址 |       设置pip所使用的镜像地址        |
|           pip config list            |        查看当前环境的pip配置         |
|  pip config unset global.index-url   |     让pip恢复使用官方默认的地址      |
|               pip list               | 列出当前环境中，已安装的所有第三方包 |
|          pip uninstall 包名          |    从当前环境中卸载指定的第三方包    |



# PyPI

```mark
清华大学 https://pypi.tuna.tsinghua.edu.cn/simple
阿里云 https://mirrors.aliyun.com/pypi/simple
中国科技大学 https://pypi.mirrors.ustc.edu.cn/simple
```





# uv

```mark
windows环境
# 创建项目文件夹
mkdir my-fastmcp-project
cd my-fastmcp-project

# 初始化项目，指定 Python 版本（推荐 3.10+）
uv init --python 3.10

# 这会创建以下文件：
# - pyproject.toml (项目配置)
# - README.md
# - .gitignore (如果使用 git)
# - src/my_fastmcp_project/__init__.py (包结构)

# 创建虚拟环境
uv venv

# 激活虚拟环境
# macOS/Linux:
source .venv/bin/activate

# Windows:
.venv\Scripts\activate

# 添加指定版本的 fastmcp
uv add "fastmcp==2.11.0"

# 或者使用 pip 风格
uv pip install fastmcp==2.11.0

# 查看已安装的包
uv pip list

# 应该能看到类似输出：
# fastmcp         2.11.0
# ...

# 测试导入
python -c "import fastmcp; print(fastmcp.__version__)"
```



# FastAPI

## 虚拟环境

创建项目

```mark
mkdir fastAPI-Project
cd fastAPI-Project
```



创建虚拟环境

```mark
uv venv
```



激活虚拟环境

```mark
#Windows Bash

source .venv/Scripts/activate

```



安装软件包

1、直接安装

```mark
uv add "fastmcp==2.11.0"

或

uv pip install "fastmcp==2.11.0"
```



2、从requirements.txt安装

```mark
uv pip install -r requirements.txt
```

