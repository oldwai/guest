# -*- coding:utf-8 -*-
'''
@author:oldwai
'''
# email: frankandrew@163.com

with open('test.txt','a+') as f:
    #f.writelines("\nnihaoa")
    print(f.tell())
    f.seek(0,0)
    content = f.read()
    print(content,type(content))
