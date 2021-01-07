from selenium.webdriver.support.wait import WebDriverWait
from openpyxl import load_workbook
import time
import re
import os
from selenium.webdriver.common.action_chains import ActionChains
import random
from selenium.webdriver.common.keys import Keys


class basepage():
    """封装基本类，定义所有脚本都能继承的类，页面定位尽量放在此类中"""

    # 初始化函数
    def __init__(self, driver):
        self.dr = driver
        self.dr.maximize_window()
        self.dr.implicitly_wait(20)  # 隐式等待20s

    # 封装css定位
    def css(self, css):
        return self.dr.find_element_by_css_selector(css)

    # 封装显示等待定位
    def wcss(self, name):
        return WebDriverWait(self.dr, 10, 1).until(lambda x: x.find_element_by_css_selector(name))

    # 去除登录页面的弹窗
    def register_top(self):
        # 如果有警告框，则点击，否则pass
        try:
            self.wcss('.blk-sure-btn').click()
        except:
            pass

    # 根据链接/邀请码/直客注册
    def get_url(self, link, code, l, n):  # link:专属链接；code:邀请码；l&n:文档中第几行第几列
        """判断是通过专属链接还是邀请码注册"""
        # 去除弹窗
        self.register_top()
        if len(link) != 0:
            # 通过ib专属链接注册
            self.dr.get(link)
            self.saveaccount(r'E:\test\account_number.xlsx', '专属链接', l, n)
            print(1)
        elif len(code) != 0:
            # 通过邀请码
            self.dr.get('https://at-client-portal-uat-proxy.ntdevops.com/register')
            time.sleep(1)
            self.css('div.el-form-item__content>div.invitationCode-input>textarea').send_keys(code)
            self.saveaccount(r'E:\test\account_number.xlsx', '邀请码', l, n)
            print(2)
        else:
            # 直客注册
            self.dr.get('https://at-client-portal-uat-proxy.ntdevops.com/register')
            self.saveaccount(r'E:\test\account_number.xlsx', '直客', l, n)
            print(3)

    # 创建存储注册数据的函数，写入已存在的本地文档中
    def saveaccount(self, excelpath, val, col, row):
        """注：调用此函数时，不能打开需要写入数据的文档"""
        workbook = load_workbook(filename=excelpath)
        sheet = workbook.active
        cel = sheet['{}{}'.format(col, row)]
        cel.value = val
        workbook.save(filename=excelpath)

    # 判断国家是否为可注册国家
    def is_uk(self, country):
        self.uk_list = ['阿尔巴尼亚', '安道尔', '奥地利', '波斯尼亚和黑塞哥维那', '保加利亚', '克罗地亚', '塞浦路斯', '捷克共和国',
                        '丹麦', '爱沙尼亚', '芬兰', '佐治亚州', '德国', '直布罗陀', '希腊', '匈牙利', '冰岛', '爱尔兰', '意大利',
                        '拉脱维亚', '列支敦士登', '立陶宛', '卢森堡', '马其顿', '马耳他', '摩纳哥', '黑山共和国', '荷兰', '挪威',
                        '葡萄牙', '塞尔维亚共和国', '罗马尼亚', '圣马力诺', '斯洛伐克', '斯洛文尼亚', '西班牙', '瑞典', '瑞士', '英国']
        if country in self.uk_list:
            print('AT Global Markets Limited 不接受居住在这个国家的个人申请。')
            return True
        else:
            return False