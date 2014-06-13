# -*- coding: utf-8 -*- 
 
import os
import admin
from ftplib import FTP 
from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class MyFtp():
    def __init__(self,  userID,  ip,  port,  timeout,  admin,  passwd):
        """
        连接ftp服务器并直接进入user用户的根目录，这里其实只需要提供use的ID即可，其它都可以为默认
        """
        self.ftp = FTP()
        try:
            self.ftp.connect(ip,  port,  timeout)
            self.ftp.login(admin,  passwd)
            print '登入成功'
        except:
            print '远程连接失败'
        else:
            if ip == '192.168.175.128': #如果是本地测试，打开的目录不一样
                self.cd('/root/' + str(userID))
            else:
                self.cd('/myfolder/' + str(userID))
            
    def ls(self,  direction = ""):
        """
        列出当前目录的文件信息，返回值是文件名和目录名组成的一个tuple，其中文件名和目录名是列表
        direction：表示要获取的那个目录
        """
        dir_res = []
        if direction != "":
            self.ftp.dir(direction,  dir_res.append)
        else:
            self.ftp.dir(dir_res.append)

        a = [f for f in dir_res if f.startswith('-')]
        files = [f.split(None,  8)[-1] for f in dir_res if f.startswith('-')]
        dirs = [f.split(None,  8)[-1] for f in dir_res if f.startswith('d')]
        return (files,  dirs)
    
    def pwd(self):
        """获取当前目录"""
        return self.ftp.pwd()
    def cd(self,  dir):
        """
        切换目录
        
        """
        self.ftp.cwd(dir)
    
    def upfile(self, localpath,  ID):
        """上传文件，因为我不是单独上传某一个文件，所以使用的是直接上传用户空间那个目录"""
        # 先切换到那个目录
        os.chdir(localpath)
        # 首先获取本地的文件列表
        Dir = self.localls(localpath)
        for i in Dir[0]:
            print i
            s = i#.encode('gbk')
            file_handler = open(s,'rb')#以读模式在本地打开文件 
            self.ftp.storbinary('STOR %s' % os.path.basename(s.encode('utf8')),file_handler, 1024)

        # 目录又要用递推
        for i in Dir[1]:
            s = i
            try:
                self.mkdir(s.encode('utf8'))
            except:
                print '目录已经存在'
            # 接下来是进入目录进行递推
            self.cd(s.encode('utf8'))   # 远程进入目录
            os.chdir(s)
            self.upfile(os.path.join(localpath,  s),   ID)#.encode('utf8')),  100)
            # 现在又要把目录切换回去
            self.cd('..')
            os.chdir(localpath)
        
    def localls(self,  localpath):
        """
        获取本地的文件列表
        返回值是[[文件名][文件夹名]]
        """
        list = os.listdir(localpath)  #列出目录下的所有文件和目录
        file = []
        folder = []
        for i in list:
            filepath = os.path.join(localpath, i)
            if os.path.isdir(filepath):
                folder.append(i)
            else:
                file.append(i)
        return [file,  folder]
            
    def updir(self):
        pass
        
    def downfile(self,  filename,  localpath):
        """下载文件"""
        currentPath = os.getcwd()
        os.chdir(localpath.decode('utf8'))
        bufsize = 1024  # 设置缓冲区大小
        file_handle=open(filename,"wb").write #以写模式在本地打开文件
        self.ftp.retrbinary("RETR " + filename, file_handle, bufsize) #接收服务器上文件并写入本地文件
        os.chdir(currentPath.decode('utf8')) # 要把当前工作路径切换回去
        
    def downdir(self,  dirname,  localpath):
        """下载目录"""
        currentPath = os.getcwd()  # 保存当前的本地目录以便恢复
        currentRemote = self.pwd()  # 保存当前的远程目录以便恢复
        remote = self.pwd() + '/' + dirname
        
        os.chdir(localpath.decode('utf8'))  # 进入工作目录，以后就不需要输入绝对路径了
        try:
            os.mkdir(dirname.decode('utf8'))  # 先建立目录再进入
        except:
            print '该目录已经存在该文件'
        self.cd(remote)
        Dir = self.ls()
        bufsize = 1024
        
        def ditui(remote):  # 我的策略是先创建文件夹再进入，所以不用提供文件夹名了
            """递推方法下载文件夹"""
            Dir = self.ls()
            
            # 肯定是要先下载文件撒
            for i in Dir[0]:
                # 操蛋，下载文件还是单独写吧
                file_handle=open(i.decode('utf8'),"wb").write #以写模式在本地打开文件
                self.ftp.retrbinary("RETR " + i, file_handle, bufsize) #接收服务器上文件并写入本地文件
                
            # 然后就该下载文件夹了
            for i in Dir[1]:
                print '正在新建目录'  + i
                os.mkdir(i)   # 新建目录
                current = os.getcwd()  # 保存当前工作目录
                remo = self.pwd()      # 保存当前远程目录
                os.chdir(i)   # 进入该目录
                self.cd(i)    # 远程也要进入该目录
                
                ditui(remote + '/' + i)
                os.chdir(current)
                self.cd(remo)
        
        os.chdir(dirname.decode('utf8'))
        ditui(remote)
        
        os.chdir(currentPath.decode('utf8'))
        self.cd(currentRemote)
        
    def mkdir(self,  dir):
        """
        创建远程目录
        其中dir为绝对路径
        """
        self.ftp.mkd(dir)

    def rmdir(self, name,  ID):
        """
        删除远程目录，可能为空也可能不为空，无需用递归，直接一层一层的删就行了
        在第一次进入的时候，直接新建远程目录，之后进入之后才进行递推
        name：要删除的文件夹名（当前目录）
        ID：当前的用户ID
        """
        trash = '/root/' + str(ID) + '/.trash'
        local = self.pwd() + '/' + name
        def ditui(local,  trash):
            """
            用递推的方法删除目录，并新建回收站目录
            """
            self.cd(local)  # 传递进来的name是一个目录，所以要先进入该目录，之后的目录就是local= /100/mulu1
            Dir = self.ls()   # 获取该目录的文件夹名Dir[1]以及文件名Dir[0]
            trash = trash + '/' + local.split('/',  10)[-1]  # 先在回收站建立一个根目录，其中rash = /100/.trash/mulu1
            try:  # 先建立该目录
                self.mkdir(trash)
                print '建立目录   ' + trash + '   成功！'
            except:
                print '目录已经存在'
                
            # 先删除文件
            for i in Dir[0]:
                # 先进入回收站的那个目录看看是否有那个文件了，此时不用担心目录的切换问题，因为当前目录是保存在name里面的
                index = -1  # 和直接删除文件一样，还是要定义一个index以作为序号用
                for j in self.ls(trash)[0]:
                    found = j.rsplit('.',  2)
                    if found[0] == i and int(found[1]) > index:
                        index = int(found[1])
                self.rename(i,  trash + '/' + i  + '.' + str(index + 1))
       
            # 再递推删除目录的内容
            for i in Dir[1]:
                # 这就不用先进入回收站了
                ditui(local + '/' + i,  trash)
        
            self.cd(local)
            for i in Dir[1]:
                self.ftp.rmd(i)
            
        # 执行递推函数
        ditui(local,  trash)
        
        # 把里面的清空后就删除最外面这个
        self.cd('..')
        self.ftp.rmd(name)
    
    def rm(self,  name, ID):
        """
        删除远程文件
        name：要删除的文件名（当前目录）
        ID：当前的用户ID
        """
        current = self.pwd()  # 先要保存当前目录
        self.cd('/root/' + str(ID) + '/.trash/')
        Dir = self.ls()
        self.cd(current)
        index = -1  # index 为负表示为找到，否则index的值就为最大的序号
        for i in Dir[0]:
            found = i.rsplit('.',  2)
            if found[0] == name:
                if int(found[1]) > index:
                    index = int(found[1])
        self.rename(name,  '/root/' + str(ID) + '/.trash/' + name + '.' + str(index + 1))
        
    def rename(self,  old,  new):
        """
        把远程文件old改名为new，移动也用它
        如果在同一目录内，文件被重命名，如果目标是另外一个目录下的名字，文件被移动
        """
        self.ftp.rename(old,  new)
        
    def size(self,  filename):
        """获取文件大小"""
        return self.ftp.size(filename)
        
    def quit(sel):
        """退出连接"""
        self.ftp.quit()

    def welcome(self):
        """打印欢迎信息"""
        print self.ftp.getwelcome()

if __name__ == "__main__":
    a = MyFtp(100,  admin.ftp['ip'],  admin.ftp['port'],  admin.ftp['timeout'],  admin.ftp['admin'], admin.ftp['passwd'])
    print a.pwd()
    a.cd('/root/100')
    print a.ls()
    print a.size('start.py')
