# -*- coding:utf-8 -*-
'''
@author:oldwai
'''
# email: frankandrew@163.com


import  requests


#r = requests.post('http://httpbin.org/post', data=payload)
# r = requests.get('https://segmentfault.com/q/1010000008565425/')
# t = r.headers.values()
# s = str(t).split(',')
# print(r.headers, end='\n')
# print(s, end='\n')
# print(r.headers.get('content-type'),end='\n')
#print(r.raise_for_status())
#s = requests.Session()
r = requests.get('http://localhost:8000/event_manage')
name = r.cookies.get('user','')
print(name)

# print(s.cookies._cookies)
# print(r.cookies.__name__.getter)
# print(r.cookies.get_dict(domain='segmentfault.com'))
