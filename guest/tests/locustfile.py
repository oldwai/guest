# -*- coding:utf-8 -*-
'''
@author:oldwai
'''
# email: frankandrew@163.com


from locust import HttpLocust,TaskSet,task


#定义用户行为
class UserBehavior(TaskSet):
    @task
    def baidu_page(self):
        self.client.get("/")


class WebsiteUser(HttpLocust):
    task_set = UserBehavior
    min_wait = 3000
    max_wait = 6000


#在cmd执行 locust -f D:\guest\guest\tests\locustfile.py --host=https://172.16.3.251:9443/#/login