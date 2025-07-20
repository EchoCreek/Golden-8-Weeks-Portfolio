from flask import Flask
from database import Database

# 1. 先创建核心的 app 和 db 对象
app = Flask(__name__)
db = Database()

# 2. 【关键改动】将 db 实例附加到 app 对象上。
#    这样，在应用的其他地方，我们可以通过 current_app.db 来访问它。
app.db = db

# 3. 在 db 创建并附加到 app 之后，再导入和注册蓝图
from routes.posts import posts_bp
app.register_blueprint(posts_bp, url_prefix='/api')


# --- 主程序入口 ---
if __name__ == '__main__':
    app.run(debug=True)