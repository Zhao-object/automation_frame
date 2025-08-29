import pymysql
class DataBase(object):
    def __init__(self, host="192.168.137.188", user="root", password="123456",
                 database='woniusales',
                 charset="utf8", port=3306,
                 cursor_type=pymysql.cursors.DictCursor):

        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.charset = charset
        self.port = port
        self.cursor_type = cursor_type

        # 显示连接和游标属性
        self.cnn = None
        self.cursor = None
        #连接数据库
        self.connect()

    def connect(self):
        # 创建连接
        self.cnn = pymysql.connect(host=self.host,
                                   user=self.user,
                                   password=self.password,
                                   database=self.database,
                                   charset=self.charset,
                                   port=self.port
                                   )
        # 创建游标
        self.cursor = self.cnn.cursor(cursor=self.cursor_type)

    def fetchall(self, sql, args=None):
        """默认以字典格式返回查询结果"""
        try:
            # 使用游标发送sql
            self.cursor.execute(sql, args)
            # 获取结果
            return self.cursor.fetchall()
        except Exception as e:
            print("执行出错了，错误信息：", e)

    def execute(self, sql, args=None):
        """执行写，改，删操作

               :param str sql: Query to execute.

               :param args: parameters used with query. (optional)
               :type args: tuple, list or dict

               :return: Number of affected rows
               :rtype: int

               If args is a list or tuple, %s can be used as a placeholder in the query.
               If args is a dict, %(name)s can be used as a placeholder in the query.
        """

        try:
            # 开启事务
            self.cnn.begin()
            # 使用游标发送sql指令
            num = self.cursor.execute(sql, args)  # 获取受影响行数
            if num == 0:
                print("执行受影响的行为0，注意检查sql语句！")

        except Exception as e:
            print("执行出错，错误信息：", e)
            self.cnn.rollback()
        else:
            self.cnn.commit()
            # 返回受影响的行数
            return num

    def __del__(self):  # 对象在内存中销毁的时候调用
        self.cursor.close()
        self.cnn.close()

