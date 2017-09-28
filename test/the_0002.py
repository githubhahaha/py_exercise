import random
import pymysql

#数据库地址，用户名，密码，数据库名
db = pymysql.Connect("localhost", "root", "111999333", "py_test")

#创建一个游标对象cursor
cursor = db.cursor()


def make_random():
    seed = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    length = len(seed)-1
    string = ''
    for x in range(4):
        for j in range(4):
            string += random.choice(seed)
        if x != 3:
            string += '-'
    return string


if __name__ == '__main__':
    for i in range(200):
        s = make_random()
        sql = "INSERT INTO the_0003 (the_key) VALUES ('%s') "
        try:
            cursor.execute(sql % s)
            db.commit()
        except:
            db.rollback()
        print(s)
    db.close()

#参考资料
#http://www.cnblogs.com/woider/p/5926744.html
#http://www.cnblogs.com/lhuan/p/6160023.html
