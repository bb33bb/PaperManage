#-*- encoding: utf-8 -*-
# Author: haofly
# Data: 2014/6/2
# Fun: 使用MySQLdb进行数据库的各种操作

import MySQLdb
import admin
import MySQLdb.cursors
 
STORE_RESULT_MODE = 0
USE_RESULT_MODE = 1
 
CURSOR_MODE = 0
DICTCURSOR_MODE = 1
SSCURSOR_MODE = 2
SSDICTCURSOR_MODE = 3
 
FETCH_ONE = 0
FETCH_MANY = 1
FETCH_ALL = 2
 
class ConnectSQL():
    def __init__(self,  host = '192.168.175.128', user = None,  passwd = None,  db = 'PaperManage'):
        """
        建立一个新连接，指定host、用户名、密码、默认数据库
        """
        self.conn = MySQLdb.Connect(host = host, user = user, passwd = passwd,  db = db,  charset='utf8')
        self.result = None
    
    def close(self):
        """
        关闭当前连接
        """
        self.conn.close()
     
    def query(self, command,mode=STORE_RESULT_MODE):
        """
        作用：使用connection对象的query方法，当没有游标的时候就用自带的query
        参数：command：sql语句
        返回：元组(影响行数(int),结果集(result)
        """
        self.conn.query(command)
        self.result = self.conn.store_result() 
        return (self.conn.affected_rows(), self.result)
     
    def fetch_queryresult(self, maxrows=1,  how = 0):
        """
        参数:  maxrows: 需要获得的行数
                how： 以何种方式存储结果，0表示tuple，1表示dict，2表示包含字段名的dict
        返回：查询的结果组成的tuple
        """
        dataset =  self.result.fetch_row(maxrows,how)
        return dataset
         
    def execute(self,command,args=None, many=False):
        """
        作用：使用游标（cursor）的execute 执行query
        参数：command： 表示sql语句
                args： command的参数列表
                Many：是否执行多行操作（executemany）
        返回：元组（影响行数（int），游标（Cursor））
        """
        self.cur = self.conn.cursor()
        line = 0
        if many == False :
            if args == None : 
                line = self.cur.execute(command)
            else :
                line = self.cur.execute(command,args)
        else :
            if args == None :
                line = self.cur.executemany(command)
            else :
                line = self.cur.executemany(command,args)
        return (line , self.cur)
    
    def fetch_executeresult(self, mode=FETCH_ONE,rows=1):
        """
        作用：提取cursor获取的数据集
        参数：mode：执行提取模式
                FETCH_ONE: 提取一个； MANY :提取rows个 ；FETCH_ALL : 提取所有
                rows：提取行数
        返回：fetch数据集
        """
        if mode == FETCH_ONE :
            return self.cur.fetchone()
        elif mode == FETCH_MANY :
            return self.cur.fetchmany(rows)
        elif mode == FETCH_ALL :
            return self.cur.fetchall()
            
    def commit(self):
        """
        提交更改
        """
        self.conn.commit()
         
if __name__=="__main__" :
    Login = ConnectSQL(admin.sql['host'], admin.sql['user'], admin.sql['passwd'], admin.sql['db'])
    user = 'aaaaaa'
    command = "select Username, Userpasswd, Mail from User where Username='aaaaaa'"
    Login.query(command)
    print '不会吧'
    print Login.fetch_queryresult()
