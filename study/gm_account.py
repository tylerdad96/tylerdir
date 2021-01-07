from public import * #调用创建的函数
from selenium import webdriver
from time import *  #调用time模块
from random import * #调用random模块
#调用keys模块，引用键盘事件
from selenium.webdriver.common.keys import Keys

#创建全局变量
dr=webdriver.Chrome()
#添加隐式等待
dr.implicitly_wait(10)
#创建打开网页的函数，url赋予默认值
def openweb(url='https://www.atfx.com/gm/en/'):
    # 最大化窗口
    dr.maximize_window()
    # 打开uk首页
    dr.get(url)
    sleep(2)
    # 点击创建真实账户
    dr.find_element_by_css_selector('.mobile_menu ').click()

#调用函数
openweb()

sleep(2)

# def stepone():
#填写真实姓名
dr.find_element_by_css_selector('input[type="text"][autocomplete="off"]').send_keys('test_tyler')
sleep(1)
#定位性别
sex=dr.find_elements_by_css_selector('.el-radio__label')
#随机选择性别
choice(sex[0:2]).click()
sleep(1)
#点击居住国家
dr.find_element_by_css_selector('input[placeholder="请选择"]').click()
sleep(2)
#定位class='el-select-dropdown__item'
ele=dr.find_elements_by_css_selector('.el-select-dropdown__item')
#定位到国家下拉列表
ele1=ele[258:458]
#随机选择国家
choice(ele1).click()
sleep(1)
#定位输入框
p=dr.find_elements_by_css_selector('.el-input__inner')
#随机输入电话号码
p[3].send_keys(phonenumber())
sleep(2)
#随机输入电子邮件
if mailad().emailone()==mailad().emailtwo():
    p[4].send_keys(mailad().emailone())
    p[5].send_keys(mailad().emailtwo())
# else:
#     p[4].clear()
#     p[5].clear()











