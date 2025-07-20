import configparser
import os
import pymysql

def load_db_config(config_file="config.ini"):
    config = configparser.ConfigParser()

    if not os.path.exists(config_file):
        # 自动创建默认配置文件
        config["mysql"] = {
            "host": "127.0.0.1",
            "user": "root",
            "password": "your_password",
            "port": 3306,
            "database": 'my_database',
            "charset": "utf8mb4"
        }
        with open(config_file, "w") as f:
            config.write(f)
        print(f"配置文件 {config_file} 已生成，请根据实际情况填写数据库信息后重新运行程序。")
        exit(0) # 停止程序运行

    config.read(config_file)

    try:
        mysql_conf = config["mysql"]
        return {
            "host": mysql_conf.get("host"),
            "user": mysql_conf.get("user"),
            "password": mysql_conf.get("password"),
            "port": int(mysql_conf.get("port")),
            "database": mysql_conf.get("database"),
            "charset": mysql_conf.get("charset","utf8mb4"),
            "cursorclass": pymysql.cursors.DictCursor
        }
    except KeyError as e:
        raise RuntimeError(f"配置文件缺少字段：{e}")