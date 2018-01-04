# -*- coding:utf-8 -*-
'''
@author:oldwai
'''
# email: frankandrew@163.com
import HTMLTestRunner
import requests
import unittest
import sys,os
parent_dir = os.path.dirname((os.path.dirname((os.path.abspath(__file__)))))
sys.path.insert(0,parent_dir)
import time
from guest.db_fixture import test_data


class AddEventTest(unittest.TestCase):

    def setUp(self):
        self.base_url = "http://127.0.0.1:8000/api/add_event/"

    def test_add_event_all_null(self):
        ''' 所有参数为空 '''
        payload = {'eid':1,'':'','limit':'','address':"",'start_time':''}
        r = requests.post(self.base_url, data=payload)
        result = r.json()
        self.assertEqual(result['status'], 10021)
        self.assertEqual(result['message'], 'parameter error')

    def test_add_event_eid_exist(self):
        ''' id已经存在 '''
        payload = {'eid':1,'name':'一加4发布会','limit':2000,'address':"深圳宝体",'start_time':'2017'}
        r = requests.post(self.base_url, data=payload)
        result = r.json()
        self.assertEqual(result['status'], 10022)
        self.assertEqual(result['message'], 'event id already exists')

    def test_add_event_name_exist(self):
        ''' 名称已经存在 '''
        payload = {'eid':11,'name':'一加3手机发布会','limit':2000,'address':"深圳宝体",'start_time':'2017'}
        r = requests.post(self.base_url,data=payload)
        result = r.json()
        self.assertEqual(result['status'], 10023)
        self.assertEqual(result['message'], 'event name already exists')

    def test_add_event_data_type_error(self):
        ''' 日期格式错误 '''
        payload = {'eid':11,'name':'一加4手机发布会','limit':2000,'address':"深圳宝体",'start_time':'2017'}
        r = requests.post(self.base_url,data=payload)
        result = r.json()
        self.assertEqual(result['status'], 10024)
        self.assertIn('start_time format error.', result['message'])

    def test_add_event_success(self):
        ''' 添加成功 '''
        payload = {'eid':11,'name':'一加4手机发布会','limit':2000,'address':"深圳宝体",'start_time':'2017-05-10 12:00:00'}
        r = requests.post(self.base_url,data=payload)
        result = r.json()
        self.assertEqual(result['status'], 200)
        self.assertEqual(result['message'], 'add event success')

class GetEventListTest(unittest.TestCase):
    '''查询发布会的接口测试'''

    def setUp(self):
        self.url = "http://127.0.0.1:8000/api/get_event_list/"

    def test_get_event_eid_null(self):
        '''发布会id为空'''

        r = requests.get(self.url,params={'eid':''})
        result = r.json()
        self.assertEqual(result['status'],10021)
        self.assertEqual(result['message'],'parameter error')

    def test_get_event_eid_error(self):
        '''发布会id不存在'''

        r = requests.get(self.url,params={'eid':'901'})
        result = r.json()
        self.assertEqual(result['status'],10022)
        self.assertEqual(result['message'],'query result is empty')

    def test_get_event_eid_success(self):
        '''发布会id为1,查询成功'''

        r = requests.get(self.url,params={'eid':'1'})
        result = r.json()
        self.assertEqual(result['status'],200)
        self.assertEqual(result['message'],'success')

    # def test_get_event_name_null(self):
    #     '''发布会id为空'''
    #
    #     r = requests.get(self.url,params={'eid':''})
    #     result = r.json()
    #     self.assertEqual(result['status'],10021)
    #     self.assertEqual(result['message'],'parameter error')


if __name__ == '__main__':
    test_data.init_data()
    report_time = time.strftime("%Y-%m-%d %H_%M_%S",time.localtime(time.time()))
    report_filename = 'D:\\guest\\guest\\tests\\report'+ report_time + '_result.html'
    test_dir = 'D:\\guest\\guest\\tests'
    #discover=unittest.defaultTestLoader.discover(test_dir,pattern='*_test.py')
    discover = unittest.TestLoader().loadTestsFromTestCase(AddEventTest)
    fp = open(report_filename,'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp,title="接口测试报告",description="用例测试情况")
    runner.run(discover)
    fp.close()

 