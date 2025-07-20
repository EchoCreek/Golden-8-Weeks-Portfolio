# 📋 CSV 数据迁移工具（CSV-To-MySQL）

一个基于 Python 的轻量级命令行工具，可将 CSV 文件中的学生数据批量导入至 MySQL 数据库中，适合数据初始化、信息录入等使用场景。

---

## ✨ 功能特性

- ✅ **CSV 文件读取**：支持带表头的 UTF-8 CSV 文件。
- ✅ **数据校验**：跳过空字段、格式错误行，并给出提示。
- ✅ **批量插入**：使用 `executemany()` 实现高效写入数据库。
- ✅ **错误处理**：自动捕捉文件错误、主键冲突等常见异常。
- ✅ **首次配置自动生成**：自动生成 `config.ini` 文件，无需手动创建。

---

## 🔧 安装与配置

### 1. 克隆仓库

```bash
git clone https://github.com/your_username/csv-to-mysql.git
cd csv-to-mysql
```

### 2. 创建并激活虚拟环境（推荐）

```bash
# Windows
python -m venv .venv
.venv\Scripts\activate

# macOS / Linux
python3 -m venv .venv
source .venv/bin/activate
```

### 3. 安装依赖

```bash
pip install -r requirements.txt
```

### 4. 配置数据库信息

首次运行时，程序将自动生成 `config.ini` 配置文件：

```ini
[mysql]
host = 127.0.0.1
user = root
password = yourpassword
port = 3306
database = myschool
charset = utf8mb4
```

请根据自己的数据库信息编辑并保存 `config.ini` 文件。

---

## 🚀 使用方法

将你要导入的学生数据准备为 CSV 文件（例如 `students.csv`），格式如下：

```csv
id,name,age
1,Alice,20
2,Bob,21
3,Charlie,22
```

然后运行程序：

```bash
python Main.py
```

程序将自动读取 `students.csv` 文件中的数据，并写入到数据库中的 `students` 表中。

---

## ⚙️ 数据库要求

- 数据表结构需与 CSV 字段对应，例如：

```sql
CREATE TABLE students (
  id INT PRIMARY KEY,
  name VARCHAR(50),
  age INT
);
```

---

## 🛡️ 错误处理机制

| 异常类型              | 系统行为                         |
|-----------------------|----------------------------------|
| `config.ini` 缺失     | 自动生成模板                     |
| CSV 缺失或格式错误    | 报错并终止                       |
| 主键冲突              | 自动提示冲突行并终止             |
| 数据格式错误          | 自动跳过错误行并提示             |
| 数据库连接失败        | 给出友好报错                     |

---

## 📦 打包为 EXE（可选）

你可以使用 PyInstaller 打包为独立的可执行文件：

```bash
pip install pyinstaller
pyinstaller --onefile Main.py
```

可执行文件将出现在 `dist/` 目录中。

---

## ❤️ 致谢

- **数据库驱动**：[PyMySQL](https://github.com/PyMySQL/PyMySQL)
- **CSV 支持**：Python 标准库 `csv`
- **配置文件管理**：`configparser`

---

## ⚠️ 免责声明

本项目仅用于教学与学习目的，若将其用于生产环境，请自行加强数据验证和权限控制。

作者不对以下情况承担责任：

- 数据导入失败或格式异常；
- 因误操作导致的数据库损坏；
- 第三方库的接口变动带来的兼容性问题。

请谨慎使用，并备份重要数据。
