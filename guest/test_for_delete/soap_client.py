# -*- coding:utf-8 -*-
'''
@author:oldwai
'''
# email: frankandrew@163.com

from suds.client import Client

#使用库suds_jurko: https://bitbucket.org/jurko/suds
#Web Sevices查询: http://ws.webxml.com.cn/zh_cn/web_services.aspx

#电话号码归属地查询

url = 'http://ws.webxml.com.cn/WebServices/MobileCodeWS.asmx?wsdl'
client = Client(url)
while True:
    phone_number = input("请输入你的手机号：")
    result = client.service.getMobileCodeInfo(phone_number)
    print(result)
