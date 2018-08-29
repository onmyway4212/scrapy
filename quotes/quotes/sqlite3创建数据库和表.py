import sqlite3

# 连接数据库,得到Connection对象
conn = sqlite3.connect('quotes.db')

# 创建curosr游标对象对象
cur = conn.cursor()


def create_table():
    # 创建表格
    cur.execute("CREATE TABLE famous(wisdom VARCHAR(256),celebrity VARCHAR(32),tags VARCHAR(64))")
    # 保存更改,提交数据
    conn.commit()
    # 关闭连接
    conn.close()


def serch_teable():
    cur.execute("select * from famous")
    result = cur.fetchall()
    for each in result:
        print(each)


if __name__ == '__main__':
    serch_teable()
    # create_table()
