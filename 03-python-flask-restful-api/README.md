# 📝 Flask RESTful API 项目 (Flask-RESTful-API-Demo)

一个基于 Flask 和 Blueprint 构建的轻量级 RESTful API，用于管理博客文章。项目完整实现了文章的增、删、改、查（CRUD）功能，并展示了模块化、配置分离等最佳实践。

---

## ✨ 功能特性

- **RESTful 架构**：提供标准的 HTTP 方法（`GET`, `POST`, `PUT`, `DELETE`）来操作文章资源。
  
- **模块化设计**：使用 Flask Blueprint 将文章相关的路由（`posts`）独立管理，使项目结构清晰、易于扩展。
  
- **配置与代码分离**：通过 `config.ini` 文件管理数据库连接信息，无需硬编码，方便在不同环境中部署。
  
- **首次配置自动生成**：当 `config.ini` 文件不存在时，程序会自动创建模板文件，引导用户完成配置。
  
- **分层设计**：将数据库操作封装在独立的 `Database` 类中，实现了业务逻辑（路由处理）与数据访问（数据库交互）的分离。
  
- **应用上下文**：通过 `current_app` 在蓝图中安全地访问在主应用中初始化的数据库实例（`db`）。
  
- **统一错误处理**：对数据库异常、请求参数错误、资源未找到等情况进行了捕获，并返回规范的 JSON 错误信息。

---

## 🔧 安装与配置

1. **克隆仓库**
   
    ```bash
    git clone https://github.com/your_username/your_reponame.git
    cd your_reponame
    ```
2. **创建并激活虚拟环境** (推荐)
   
    ```bash
    # Windows
    python -m venv .venv
    .venv\Scripts\activate
    
    # macOS / Linux
    python3 -m venv .venv
    source .venv/bin/activate
    ```
3. **安装依赖** 项目依赖已记录在 `requirements.txt` 文件中。
   
    ```bash
    # 如果没有 requirements.txt，请手动安装
    pip install Flask PyMySQL
    ```
4. **配置数据库信息** 首次运行 `main.py` 时，程序会自动在根目录生成 `config.ini` 配置文件：
   
    ```toml
    [mysql]
    host = 127.0.0.1
    user = root
    password = your_password
    port = 3306
    database = my_database
    charset = utf8mb4
    ```
    
    请根据您自己的数据库信息，**编辑并保存** `config.ini` 文件，然后重新运行程序。

---

## 🚀 使用方法

1. **启动服务** 确保虚拟环境已激活，并已正确配置 `config.ini` 文件。
   
    ```bash
    python main.py
    ```
    
    服务将在 `http://127.0.0.1:5000` 上运行。所有 API 接口均以 `/api` 为前缀。
    
2. **API 端点说明**
   
    - **获取所有文章**
      
        - **URL**: `/api/posts`
          
        - **方法**: `GET`
          
        - **成功响应 (200 OK)**:
          
            ```json
            [
                {
                    "id": 1,
                    "title": "我的第一篇文章",
                    "content": "这是内容...",
                    "created_at": "Sat, 20 Jul 2025 10:30:00 GMT"
                }
            ]
            ```
    - **创建新文章**
      
        - **URL**: `/api/posts`
          
        - **方法**: `POST`
          
        - **请求体 (JSON)**:
          
            ```json
            {
                "title": "一篇新文章的标题",
                "content": "这是新文章的具体内容。"
            }
            ```
        - **成功响应 (201 Created)**:
          
            ```json
            {
                "message": "Post created successfully",
                "id": 2
            }
            ```
    - **更新指定文章**
      
        - **URL**: `/api/posts/<post_id>`
          
        - **方法**: `PUT`
          
        - **请求体 (JSON)**:
          
            ```JSON
            {
                "title": "更新后的标题",
                "content": "更新后的内容。"
            }
            ```
        - **成功响应 (200 OK)**:
          
            ```JSON
            {
                "message": "Post 2 updated successfully"
            }
            ```
    - **删除指定文章**
      
        - **URL**: `/api/posts/<post_id>`
          
        - **方法**: `DELETE`
          
        - **成功响应 (200 OK)**:
          
            ```json
            {
                "message": "Post 2 deleted successfully"
            }
            ```

---

## ⚙️ 数据库要求

项目需要一个名为 `posts` 的数据表。请在您的数据库中执行以下 SQL 语句来创建该表：

```sql
CREATE TABLE posts (
  id INT AUTO_INCREMENT PRIMARY KEY,
  title VARCHAR(255) NOT NULL,
  content TEXT NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

---

## 🛡️ 错误处理机制

| 异常类型                     | 系统行为                                       | 返回状态码 |
| ---------------------------- | ---------------------------------------------- | ---------- |
| `config.ini` 缺失            | 自动生成模板文件，并提示用户填写后退出程序     | \-         |
| 数据库连接/执行失败          | 捕获异常，回滚事务，并返回详细错误信息         | `500`      |
| 请求体非 JSON 或缺少字段     | 校验请求数据，返回 "Missing title or content"  | `400`      |
| 更新/删除的 `post_id` 不存在 | 判断 SQL 操作影响的行数，返回 "Post not found" | `404`      |

---

## ❤️ 致谢

本项目基于以下优秀的开源库构建：

- **Web 框架**: [Flask](https://flask.palletsprojects.com/)
  
- **数据库驱动**: [PyMySQL](https://github.com/PyMySQL/PyMySQL)
  
- **配置文件解析**: `configparser` (Python 标准库)
  

---

## ⚠️ 免责声明

本项目主要用于教学和学习目的，展示 Flask 应用的基本结构和开发实践。若计划将其用于生产环境，请务必自行在以下方面进行增强：

- **安全**：增加用户认证、授权机制，并对所有输入进行严格的清理和验证。
  
- **部署**：使用 Gunicorn、uWSGI 等生产级 WSGI 服务器替代 Flask 内置的开发服务器。
  
- **性能**：优化数据库查询，添加缓存策略等。
  

作者不对因使用、修改或分发此项目而导致的任何数据丢失、服务中断或潜在安全问题承担责任。请谨慎使用，并始终备份重要数据。