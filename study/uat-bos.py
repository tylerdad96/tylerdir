#导包
from selenium import webdriver
import time
from PIL import Image

#创建类：
class creat_account():
    #进入注册页面
    def __init__(self):
        self.dr=webdriver.Chrome()
        self.dr.maximize_window() #最大化窗口
        self.dr.implicitly_wait(20) #隐式等待20s
        self.dr.get('https://at-client-portal-uat.atfxdev.com/register')
        time.sleep(1)
    #封装css定位方法
    def css(self,element):
        self.el=self.dr.find_element_by_css_selector(element)
        return self.el


# c=creat_account()
# c.css('.login-btn').click()