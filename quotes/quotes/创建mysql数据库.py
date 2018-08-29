import pymysql

# 连接MySQL数据库
connection = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='zh12345', db='quotes',)

# 通过cursor创建游标
cursor = connection.cursor()


def create_table():
    cursor.execute('create table famous (wisdom varchar(1024), celebrity varchar(20), tags VARCHAR(64))')
    connection.commit()
    cursor.close()
    print('数据表创建成功!')


def insert():
    # 创建sql 语句，并执行
    sql = "INSERT INTO `users` (`email`, `password`) VALUES ('huzhiheng@itest.info', '123456')"

    # 插入一行记录，注意MySQL的占位符是%s:
    # cursor.execute('insert into user (id, name) values (%s, %s)', ['1', 'Michael'])
    cursor.execute(sql)

    # 提交SQL
    connection.commit()


def search():
    # 执行数据查询
    sql = "SELECT `id`, `password` FROM `users` WHERE `email`='huzhiheng@itest.info'"
    cursor.execute(sql)

    # 查询数据库单条数据
    result = cursor.fetchone()
    print(result)

    print("-----------华丽分割线------------")

    # 执行数据查询
    sql = "SELECT `id`, `password` FROM `users`"
    cursor.execute(sql)

    # 查询数据库多条数据
    result = cursor.fetchall()
    for data in result:
        print(data)

    # 关闭数据连接
    connection.close()


if __name__ == '__main__':
    create_table()
    # insert()
    # search()
