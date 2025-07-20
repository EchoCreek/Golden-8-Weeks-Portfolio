from DataMigrator import DataMigrator
from Config_loader import load_db_config

if __name__ == '__main__':

    try:
        db_config = load_db_config()

        migrator = DataMigrator(db_config)
        migrator.connect()

        data = migrator.read_csv("students.csv")
        if data:
            migrator.write_to_db(data)
        else:
            print("未读取到任何有效数据，终止写入。")

    except Exception as e:
        print(f"出现异常：{e}")

    finally:
        if "migrator" in locals() and hasattr(migrator, "connection") and migrator.connection:
            migrator.connection.close()
            print("🔒 数据库连接已关闭")
