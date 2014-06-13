# -*- coding: utf-8 -*-
# Author: haofly
# Date: 2014/6/1
# Fun: 使用正则表达式检验字符串是否符合标准

import re

def isStd(str):
    """检验一般字符串是否包含不正确的特殊字符，正确就返回地址，否则返回None"""
    pattern = re.compile(u'^[a-zA-Z\u4e00-\u9fa5][0-9a-zA-Z\u4e00-\u9fa5]{2,19}$')
    return pattern.match(str)
    
def isName(str):
    """检验是否是合法的姓名"""
    pattern = re.compile(u'^[a-zA-Z\u4e00-\u9fa5][0-9a-zA-Z\u4e00-\u9fa5]{1,19}$')
    return pattern.match(str)

def isZhiwu(str):
    """检验是否是合法的职务信息"""
    pattern = re.compile(u'^[a-zA-Z\u4e00-\u9fa5][0-9a-zA-Z\u4e00-\u9fa5]{1,20}$')
    return pattern.match(str)
    
def isTel(str):
    """检验是否是正确的国内的电话号码，正确返回True，否则返回None"""
    pattern = re.compile("^\d{11}$|^\d{8}$")
    return pattern.match(str)
    
def isEmail(str):
    """检验是否是合法的邮箱地址"""
    pattern = re.compile("\w+([-+.]\w+)*@\w+([-.]\w+)*\.\w+([-.]\w+)*")
    return pattern.match(str)

def isPass(str):
    pattern = re.compile('^[\@A-Za-z0-9\!\#\$\%\^\&\*\.\~]{6,20}$')
    return pattern.match(str)
    
if __name__ == "__main__":
    print isTel('18883287412')
