from selenium import webdriver
import time
from basepage import basepage
import re
import random
from selenium.webdriver.common.action_chains import ActionChains
import os

class kycdata(basepage):
    """此类中封装获取邮件/手机验证码，及kyc表单填写的基本操作"""

    #定义初始化函数，实例化基本类传参
    def __init__(self):
        self.dr=webdriver.Chrome()
        self.base=basepage(self.dr)

    #点击验证联系方式
    def contact(self):
        self.clickweb('button.el-button--primary > span')

    #进入邮箱短信页面（初级函数）
    def emailpage(self):
        self.dr.find_element_by_css_selector('div[width="200"] li:nth-of-type(5) > .ivu-menu-submenu-title > span').click()
        time.sleep(1)
        self.dr.find_element_by_css_selector('div[width="200"] [href="/report/emailrecord"]').click()
        time.sleep(1)

    #获取邮箱验证码
    def get_emailcode(self,idnum):
        #切换窗口
        self.windsw(1)
        time.sleep(1)
        #输入主账户进行筛选
        self.css('div.ivu-input-wrapper-default>input').clear()
        time.sleep(1)
        self.inputform('div.ivu-input-wrapper-default>input',idnum)
        time.sleep(1)
        self.clickweb('div.ivu-input-wrapper-default>div.ivu-input-group-append>button>i.ivu-icon-ios-search')
        time.sleep(1)
        #排序
        self.clickweb('div.ivu-tabs-content > div:nth-of-type(1) th:nth-of-type(5) i:nth-of-type(2)')
        #获取最新的验证码
        self.dr.find_element_by_xpath('//div[@class="ivu-tabs-content"]//tr[1]/td[3]').click()
        time.sleep(1)
        self.e = self.dr.find_elements_by_xpath('//div[@class="ivu-drawer-wrap"]//tr[2]//tr[4]/td[1]/span')
        self.t = self.e[0].text
        # 输出验证码
        self.emailcode=re.sub(r'\D','',self.t) #提取数字
        print('当前测试数据邮箱验证码:{}'.format(self.emailcode))
        #关闭弹窗
        self.tpo=self.dr.find_elements_by_css_selector('a.ivu-drawer-close>i.ivu-icon-ios-close')
        time.sleep(1)
        self.tpo[1].click()
        return self.emailcode

    #填写邮箱验证码
    def code_pr(self,idnumber):
        #点击验证联系方式
        self.contact()
        # 发送邮箱验证码
        self.css('div.el-col-24>button.dialog-sendCode').click()
        time.sleep(1)
        # 调用函数，获取邮箱验证码
        self.get_emailcode(idnumber)
        self.windsw(0)
        time.sleep(1)
        # 输入验证码
        time.sleep(1)
        self.inputform('[placeholder="验证码"]',self.emailcode)
        time.sleep(1)
        #点击下一步
        self.clickweb('button.dialog-submit > span')
        #点击以后再做
        self.clickweb('.doItLeTer-css')
        #点击完成
        self.clickweb('button.dialog-submit > span')

     #上传图片
    def upload_img(self):
        self.css('div.upload-box>div.upload-text>div.icon').click()
        time.sleep(1)
        os.system(r'E:\test\client_kyc.exe')
        time.sleep(1)

    #填写kyc表单
    def kyc_form(self):
        # 上传图片
        self.upload_img()
        time.sleep(1)
        # 随机选择性别
        sex = self.dr.find_elements_by_css_selector('label.el-radio>span>span.el-radio__inner')
        sex[random.choice([0, 1])].click()
        time.sleep(1)
        self.css('[placeholder="请选择出生日期为DD-MM-YYYY的格式"]').click()
        time.sleep(1)
        self.css('div.el-date-picker__header > span:nth-of-type(1)').click()
        # 年份
        selty = self.dr.find_element_by_css_selector('.el-icon-d-arrow-left')
        ActionChains(self.dr).double_click(selty).perform()  # 双击
        selty.click()
        time.sleep(1)
        by = self.dr.find_elements_by_css_selector('table.el-year-table>tbody>tr>td')
        by[random.randint(0, 9)].click()
        time.sleep(1)
        # 月份
        bm = self.dr.find_elements_by_css_selector('table.el-month-table>tbody>tr>td')
        bm[random.randint(0, 11)].click()
        time.sleep(1)
        # 日期
        bd = self.dr.find_elements_by_css_selector('table.el-date-table>tbody>tr>td')
        bd[random.randint(0, 41)].click()
        time.sleep(1)
        # 随机输入证件号码
        self.inputform('[placeholder="请输入证件号码"]',self.randomint(8))
        time.sleep(1)
        #输入随机地址
        self.inputform('[placeholder="请输入地址"]',self.randomstr(8))
        #接受条款
        self.clickweb('label.agree-checkbox>span.el-checkbox__input>span.el-checkbox__inner')
        time.sleep(1)
        #提交
        self.clickweb('button.submit-btn > span')
        time.sleep(1)

    #kyc认证
    def kycfulfill(self,idnum):
        #手机邮箱验证
        self.code_pr(idnum)
        time.sleep(2)
        #KYC表格填写
        self.kyc_form()
        time.sleep(1)
        self.clickweb('button.side-nav-cell .menu-font') #回到首页
        time.sleep(1)