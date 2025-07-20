import pymysql
from pymysql import connect

from config_loader import load_db_config

class Database:
    """
    数据库操作的专属管家类。
    所有与数据库的交互都通过这个类的实例进行。
    """
    def __init__(self):
        """
        初始化时，加载数据库配置。
        """
        self.db_config = load_db_config()

    def _get_connection(self):
        """
        一个内部方法，用于获取一个新的数据库连接
        :return:
        """
        return pymysql.connect(**self.db_config)

    def get_all_posts(self):
        """
        获取所有文章。
        :return:
        """
        connection = self._get_connection()
        try:
            with connection.cursor() as cursor:
                cursor.execute("SELECT * FROM posts ORDER BY created_at DESC")
                posts = cursor.fetchall()
            return posts, None # 返回数据和None（表示没有错误）
        except Exception as e:
            return None, e # 返回None（表示没有数据）和错误信息
        finally:
            if connection:
                connection.close()
    def create_post(self, title, content):
        """
        创建一篇新文章。
        :param title:
        :param content:
        :return:
        """
        connection = self._get_connection()
        try:
            with connection.cursor() as cursor:
                sql = "INSERT INTO `posts` (`title`, `content`) VALUES (%s, %s)"
                cursor.execute(sql, (title, content))
                new_post_id = cursor.lastrowid
            connection.commit()
            return new_post_id, None
        except Exception as e:
            if connection:
                connection.rollback()
            return None, e
        finally:
            if connection:
                connection.close()

    def update_post(self, post_id, title, content):
        """
        更新指定 ID 的文章
        :param post_id:
        :param title:
        :param content:
        :return:
        """
        connection = self._get_connection()
        try:
            with connection.cursor() as cursor:
                sql = "UPDATE `posts` SET `title` = %s, `content` = %s WHERE `id` = %s"
                result = cursor.execute(sql, (title, content, post_id))
            connection.commit()
            return result, None # result 是受影响的行数
        except Exception as e:
            if connection:
                connection.rollback()
            return None, e
        finally:
            if connection:
                connection.close()

    def delete_post(self, post_id):
        """
        删除指定 ID 的文章
        :param post_id:
        :return:
        """
        connection = self._get_connection()
        try:
            with connection.cursor() as cursor:
                sql = "DELETE FROM `posts` WHERE `id` = %s"
                result = cursor.execute(sql, (post_id))
            connection.commit()
            return result, None # result 是受影响的行数
        except Exception as e:
            if connection:
                connection.rollback()
            return None, e
        finally:
            if connection:
                connection.close()
