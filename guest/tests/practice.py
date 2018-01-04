# -*- coding:utf-8 -*-
'''
@author:oldwai
'''
# email: frankandrew@163.com


def multipliers():
  return lab1(x)


def lab1(x):
    list1 = []
    for i in range(4):
        sum = x*i
        list1.append(sum)
    return list1

#print ([m(2) for m in multipliers()])
def func1(x):
    list2 = []
    for m in multipliers():
        list2.append(m(x))
    return list2

print(func1(3))