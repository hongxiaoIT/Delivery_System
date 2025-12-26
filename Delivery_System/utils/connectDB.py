import pymysql
class DBConnection:
    def __init__(self, ip='', port=3306,user='root', passwd='sq', db=''):
        self.ip = ip
        self.port=port
        self.user = user
        self.passwd = passwd
        self.db = db
    def getCon(self):
        try:
            conn = pymysql.connect(host=self.ip, port=self.port, user=self.user, passwd=self.passwd,
                                        database=self.db)
            return conn
        except pymysql.Error as e:
            print(f'mysqldb error :{e}')

    def select(self,sql):
        try:
            con=self.getCon()
            cur=con.cursor()
            cur.execute(sql)
            result=cur.fetchall()
            return result
        except pymysql.Error as e:
            print(f'mysqldb error :{e}')
        finally:
            cur.close()
            con.close()
    def update(self,sql):
        try:
            con = self.getCon()
            cur = con.cursor()
            cur.execute(sql)
            con.commit()
        except pymysql.Error as e:
            con.rollback()
            print(f'mysqldb error :{e}')
        finally:
            cur.close()
            con.close()
    def insert(self,sql):
        try:
            con = self.getCon()
            cur = con.cursor()
            cur.execute(sql)
            con.commit()
        except pymysql.Error as e:
            con.rollback()
            print(f'mysqldb error :{e}')
        finally:
            cur.close()
            con.close()
    def delete(self,sql):
        try:
            con = self.getCon()
            cur = con.cursor()
            cur.execute(sql)
            con.commit()
        except pymysql.Error as e:
            con.rollback()
            print(f'mysqldb error :{e}')
        finally:
            cur.close()
            con.close()







if __name__ == '__main__':
    # db=DBConnection(ip='192.168.19.144',db="sq-waimai")
    # print(db.select("select * from `t_sys_dept` WHERE `id` = 3278"))
    # db.update("UPDATE `sq-waimai`.`t_sys_dept` SET `fullname` = '巴奴火锅桐110' WHERE `id` = 3278")
    # print(db.select("select * from `t_sys_dept` WHERE `id` = 3278"))
    db=DBConnection(ip='192.168.32.128',db="sq-waimai")#连接mysql数据库---外卖数据库
    res1=db.select('select * from t_sys_dept where id=1;')#查询店铺全称
    print(res1)
    db.update("UPDATE t_sys_dept SET fullname = 'sq淘汰郎小火锅桐乡店总部' WHERE id = 1;")#修改店铺全称
    res2=db.select('select * from t_sys_dept where id=1;')
    print(res2)