# -*- coding:utf-8 -*-
'''
@author:oldwai
'''
# email: frankandrew@163.com


from selenium import webdriver
from selenium.common.exceptions import UnexpectedAlertPresentException
from selenium.webdriver.common.action_chains import ActionChains
import time
#使用谷歌浏览器，方便查看效果，如果追求速度可以用phantomJS
driver=webdriver.Chrome()
#调整最大窗口，否则某些元素无法显示
driver.maximize_window()
#J_AgreementBtn  统一协议按钮
#使用淘宝找回密码界面做测试
driver.get('https://reg.taobao.com/member/reg/fill_mobile.htm')
time.sleep(5)#等待滑动模块和其他JS文件加载完毕！
agree_pro = 'J_AgreementBtn'
driver.find_element_by_id(agree_pro).click()

action = ActionChains(driver)
action1 = ActionChains(driver)
action.move_by_offset()
source=driver.find_element_by_xpath("//*[@id='nc_1_n1z']")
#action.click_and_hold(source)  #鼠标左键按下不放
action.drag_and_drop(source,120,0).perform()#在本地拖到验证码成功之后，按F12查看


time.sleep(2)
action1.move_by_offset(138,0)#在本地拖到验证码成功之后，按F12查看
action.drag_and_drop()
action1.release().perform()

#driver.quit()