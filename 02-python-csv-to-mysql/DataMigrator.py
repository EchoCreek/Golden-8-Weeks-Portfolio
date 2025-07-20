import csv
import pymysql
import pymysql.err

class DataMigrator:
    def __init__(self, db_config):
        self.db_config = db_config
        self.connection = None

    def connect(self):
        try:
            self.connection = pymysql.connect(**self.db_config)
            print("数据库连接成功")
        except pymysql.MySQLError as e:
            raise RuntimeError(f"数据库连接失败：{e}")

    def read_csv(self, filepath):
        student_data = []

        try:
            with open(filepath, "r", encoding="utf-8-sig") as file:
                reader = csv.DictReader(file)
                for row in reader:
                    if not row.get("id") or not row.get("name") or not row.get("age"):
                        print(f"跳过无效行：{row}")
                        continue
                    try:
                        student_data.append((int(row["id"]), row["name"], int(row["age"])))
                    except ValueError:
                        print(f"数据格式错误，跳过此行：{row}")
            print(f"成功读取CSV文件，共{len(student_data)}条记录")

            return student_data
        except Exception as e:
            raise RuntimeError(f"读取CSV失败：{e}")


    def write_to_db(self, student_data):
        if not self.connection:
            print("数据库未连接")
            return

        try:
            with self.connection.cursor() as cursor:
                sql = "INSERT INTO students (id, name, age) VALUES (%s, %s, %s)"
                cursor.executemany(sql, student_data)
                self.connection.commit()
                print(f"成功写入数据库，共{len(student_data)}条记录")
        except pymysql.err.InternalError as e:
            raise RuntimeError("写入数据库失败：主键冲突，可能有重复 ID")
        except Exception as e:
            raise RuntimeError(f"写入数据库失败：{e}")
