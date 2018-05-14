#!/bin/python
# -*- coding: utf-8 -*-  
import os
import json

#test
print("hello world")

#insert new line withtou LFCR settings

print("hahahaha")


#插入一点中文试试呢
print("你好~")
#结论，diff无效和中文无关啊...


#now add LFCT setting
#额...忘记了，我的git早已设置过git config --global core.autocrlf input
#所以，上面的commit都已经被git做了自动换行符转换

#最后，加上utf8注释试试