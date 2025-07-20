# 命令行工具箱 🧰 (CommandLine Toolbox)

一个基于 Python 的多功能命令行工具，集合了天气查询、IP地址获取和趣味知识等实用功能。

## ✨ 功能特性

- **天气查询**: 输入城市名，获取实时的天气状况和温度。
- **IP 查询**: 快速获取您当前的公网 IP 地址。
- **猫咪趣闻**: 随机获取一条有趣的猫咪冷知识，并提供中文翻译。

## 🔧 安装与配置

1.  **克隆仓库**
    ```bash
    git clone [https://github.com/your_username/your_reponame.git](https://github.com/your_username/your_reponame.git)
    cd your_reponame
    ```

2.  **创建并激活虚拟环境** (推荐)
    ```bash
    # Windows
    python -m venv .venv
    .venv\Scripts\activate
    
    # macOS / Linux
    python3 -m venv .venv
    source .venv/bin/activate
    ```

3.  **安装依赖**
    项目依赖已记录在 `requirements.txt` 文件中，执行以下命令安装：
    ```bash
    pip install -r requirements.txt
    ```

4.  **配置 API Key**
    本项目的天气查询功能需要使用[心知天气](https://www.seniverse.com/)的 API Key。
    程序采用首次使用时自动配置的机制：
    - 第一次执行 `weather` 命令时，程序会提示您输入 API Key。
    - 输入后，Key 将被自动保存在项目根目录下的 `config.ini` 文件中，供后续使用。
    - **请注意**：`config.ini` 已被添加到 `.gitignore`，不会上传至 GitHub。

## 🚀 使用方法

确保您在项目的根目录，并已激活虚拟环境。

- **查询天气**:
  ```bash
  python main.py weather [城市名称]
  ```
  
- **获取公网 IP**:
  ```bash
  python main.py ip
  ```
  
- **获取猫咪趣闻**:
  ```bash
  python main.py cat
  ```
  
## 📦 打包成 EXE (可选)
如果您想将此工具打包成单个可执行文件，可以使用 PyInstaller：

1. 安装 PyInstaller:
    ```Bash
    pip install pyinstaller
    ```

2. 执行打包命令:
    ```Bash
    pyinstaller --onefile main.py
    ```
    打包完成后，可执行文件将出现在 `dist` 文件夹中。

## ❤️ 致谢
本项目使用了以下优秀的第三方服务和资源，特此感谢：

- **天气数据**: [心知天气](https://www.seniverse.com/)

- **IP 地址查询**: [httpbin.org](https://httpbin.org/)

- **猫咪趣闻**: [catfact.ninja](https://catfact.ninja/)

详细的第三方许可信息，请查阅 `NOTICE.md` 文件。

## ⚠️ 免责声明

本项目仅用于个人学习与技术交流，所有接口调用均来自第三方平台，可能随时间变动而失效。
 项目作者不对以下情况承担责任：

- 第三方服务变更、终止或产生费用；
- 程序运行过程中出现的任何数据丢失、错误或异常；
- 用户将该项目用于非法用途或超出学习范围的行为。

请确保在遵守相关法律法规及第三方平台使用条款的前提下使用本项目。