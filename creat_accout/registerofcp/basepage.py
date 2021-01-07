from selenium.webdriver.support.wait import WebDriverWait
from openpyxl import load_workbook
import time
import re
import os
from selenium.webdriver.common.action_chains import ActionChains
import random
from selenium.webdriver.common.keys import Keys

class basepage():
    """封装基本类，定义所有脚本都能继承的父类：
    定位方法，点击操作，随机数据等方法封装在此类中"""
    
    #初始化函数
    def __init__(self,driver):
        self.dr=driver
        self.dr.maximize_window()
        self.dr.implicitly_wait(20) #隐式等待20s

    #封装css定位
    def css(self,css):
        return self.dr.find_element_by_css_selector(css)

    #封装显示等待定位
    def wcss(self, name):
        return WebDriverWait(self.dr, 10, 1).until(lambda x: x.find_element_by_css_selector(name))

    #封装输入方法
    def inputform(self,element,values):
        return self.css(element).send_keys(values)

    #封装点击操作
    def clickweb(self,element):
        return self.css(element).click()

    #去除会员中心登录页面的弹窗
    def register_top(self):
        # 如果有警告框，则点击，否则pass
        try:
            self.wcss('.blk-sure-btn').click()
        except:
            pass

    #创建存储注册数据的函数，写入已存在的本地文档中
    def saveaccount(self,excelpath,val,col,row):
        """注：调用此函数时，不能打开需要写入数据的文档"""
        workbook = load_workbook(filename=excelpath)
        sheet = workbook.active
        cel = sheet['{}{}'.format(col, row)]
        cel.value = val
        workbook.save(filename=excelpath)

    #生成n位数的随机数（联通号码开头）
    def randomint(self,n):
        self.phone_list = [130, 131, 132, 155, 156, 185, 186, 145, 146, 166, 167, 175, 176]
        self.phone_num = str(random.choice(self.phone_list)) + ''.join(random.sample('0123456789',n))  # 随机生成联通号码
        return self.phone_num

    #生成n位数的随机字符串
    def randomstr(self,n):
        self.str=''.join(random.sample('ABCDEFGHIJKLMN', n))
        return self.str

    #显示等待获取页面文本
    def page_text(self,element):
        self.t=self.wcss(element).text
        return self.t

    #窗口切换
    def windsw(self,n):
        self.all_handles = self.dr.window_handles
        #n=0切换到会员中心，n=1切换到bos
        return self.dr.switch_to.window(self.all_handles[n])

    #登录bos
    def login_bos(self,username,psword):
        #切换语言
        self.clickweb('.ivu-icon-ios-arrow-down')
        time.sleep(1)
        self.clickweb('ul.ivu-select-dropdown-list > li:nth-of-type(1)')
        #登录bos账户
        self.inputform('[placeholder="账号"]',username)
        time.sleep(1)
        self.inputform('[placeholder="密码"]',psword)
        time.sleep(1)
        self.clickweb('button.ivu-btn-large > span')

    #创建初级函数登录bos  用于修饰器中的调用
    def login_bosin(self):
        self.dr.find_element_by_css_selector('.ivu-icon-ios-arrow-down').click()
        time.sleep(1)
        self.dr.find_element_by_css_selector('ul.ivu-select-dropdown-list > li:nth-of-type(1)').click()
        time.sleep(1)
        self.dr.find_element_by_css_selector('[placeholder="账号"]').send_keys('tyler.tang')
        time.sleep(1)
        self.dr.find_element_by_css_selector('[placeholder="密码"]').send_keys('Tl123456')
        time.sleep(1)
        self.dr.find_element_by_css_selector('button.ivu-btn-large > span').click()

    #登录会员中心
    def login_cl(self,email,pasword):
        # 选择简体中文
        time.sleep(1)
        self.clickweb('.la-globe')
        time.sleep(1)
        self.clickweb('ul.el-dropdown-menu > li:nth-of-type(2)')
        # 输入邮箱
        self.inputform('[placeholder="请输入您的电子信箱"]',email)
        time.sleep(1)
        # 输入密码
        self.inputform('div.formBlock > .el-form > .el-col [placeholder="请输入您的密码"]',pasword)
        time.sleep(1)
        # 点击登录
        self.clickweb('div.formBlock > .el-form > .el-col .el-button')
        time.sleep(2)

    #鼠标悬浮操作
    def chainsaction(self,dr,elenment):
        self.mont=self.css(elenment)
        return ActionChains(dr).move_to_element(self.mont).perform()

    #点击首次登录会员中心的弹窗
    def login_top(self):
        #去除弹窗
        self.wcss('div.text-center .el-checkbox__inner').click()
        time.sleep(1)
        self.clickweb('.confirm-btn')
        time.sleep(2)

    #登出会员中心
    def lgoout_cp(self,dr):
        #鼠标悬浮
        self.chainsaction(dr,'.el-icon--right')
        time.sleep(1)
        #点击登出
        self.clickweb('ul.el-client-menu > li:nth-of-type(3) > .drop-sub-title')
        time.sleep(1)
        #点击确定登出
        self.clickweb('button.logout-btn-confirm > span')
