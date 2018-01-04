# -*- coding:utf-8 -*-
'''
@author:oldwai
简单计算器功能
'''
# email: frankandrew@163.com

class Calculator():
    '''
    实现两个数的加、减、乘、除
    '''

    #
    def __init__(self,a,b):
        self.a = int(a)
        self.b = int(b)

    #Addition
    def add(self):
        return self.a + self.b
    #subtraction
    def sub(self):
        return self.a - self.b
    #multiplication
    def mul(self):
        return self.a * self.b

    #division
    def div(self):
        return self.a / self.b
