# -*- coding: UTF-8 -*-

import MySQLdb

class DBConnet():

    #链接数据库
    def getCon(self):
        try:
            con=MySQLdb.connect(host='116.62.28.180',user='riskeys_yb',passwd='Ja5pe+hYjBc=',db='yunbao',port=3306,charset='utf8')
            return  con
        except MySQLdb.Error,e:
            print(e)

    #查询
    def select(self,sql1,sql2):
        try:
            conn=self.getCon()
            consor=conn.cursor(MySQLdb.cursors.DictCursor)
            consor.execute(sql1)
            fc=consor.fetchone()[0]
            if fc>0:
                self.delete(sql2)
            else:
                print("没有查找到数据")
        except MySQLdb.Error, e:
            print(e)
        finally:
            consor.close()
            conn.close()

    #删除
    def delete(self,sql2):
        try:
            conn=self.getCon()
            cursor=conn.cursor()
            cursor.execute(sql2)
            conn.commit()
        except MySQLdb.Error,e:
            print(e)
        finally:
            cursor.close()
            conn.close()
