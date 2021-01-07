from basepage import basepage
from selenium import webdriver
import time
import random

class formfill(basepage):
    """会员中心注册页面表单，正常注册流程逻辑封装在此类中"""
    #定义初始化方法，实例化父类并传参浏览器驱动
    def __init__(self):
        self.dr=webdriver.Chrome()
        self.base=basepage(self.dr)
    
    #ib返佣申请表格
    def ib_table(self):
        time.sleep(1)
        ib_list=self.dr.find_elements_by_css_selector('.el-checkbox__inner')
        time.sleep(1)
        if len(ib_list)<=2:
            self.clickweb('div.ps-agree-bot .el-checkbox__inner')
            time.sleep(1)
        else:
            for i in ib_list[0:random.randint(1,len(ib_list)-2)]:
                i.click()
                time.sleep(1)
            self.clickweb('div.ps-agree-bot .el-checkbox__inner')
        time.sleep(1)
        #点击提交
        self.clickweb('div.ibRebateCon > div:nth-of-type(4) > .el-button')   
        
    #根据链接/邀请码/直客注册
    def get_url(self,link,code,l,n): #link:专属链接；code:邀请码；l&n:文档中第几行第几列
        """判断是通过专属链接还是邀请码注册"""
        #去除弹窗
        if len(link)!=0:
            #通过ib专属链接注册
            self.dr.get(link)
            self.saveaccount(r'E:\test\account_number.xlsx', '专属链接', l, n)
            print('专属链接注册')
            self.register_top()
        elif len(code)!=0:
            #通过邀请码
            self.dr.get('https://at-client-portal-sit-proxy.ntdevops.com/register')
            time.sleep(1)
            self.css('div.el-form-item__content>div.invitationCode-input>textarea').send_keys(code)
            self.saveaccount(r'E:\test\account_number.xlsx', '邀请码', l, n)
            print('邀请码注册')
            self.register_top()
        else:
            #直客注册
            self.dr.get('https://at-client-portal-uat-proxy.ntdevops.com/register')
            self.saveaccount(r'E:\test\account_number.xlsx', '直客', l, n)
            print('直客注册')
            self.register_top()
        
    #判断国家是否为可注册国家
    def is_uk(self,country):
        self.uk_list=['阿尔巴尼亚','安道尔','奥地利','波斯尼亚和黑塞哥维那','保加利亚','克罗地亚','塞浦路斯','捷克共和国',
                      '丹麦','爱沙尼亚','芬兰','佐治亚州','德国','直布罗陀','希腊','匈牙利','冰岛','爱尔兰','意大利',
                      '拉脱维亚','列支敦士登','立陶宛','卢森堡','马其顿','马耳他','摩纳哥','黑山共和国','荷兰','挪威','中国香港'
                      '葡萄牙','塞尔维亚共和国','罗马尼亚','圣马力诺','斯洛伐克','斯洛文尼亚','西班牙','瑞典','瑞士','英国']
        if country in self.uk_list:
            print('当前所选国家无法注册，请重新选择')
            return True
        else:
            return False

    #选择页面语言为中文
    def choose_lg(self):
        self.clickweb('.el-icon-arrow-down')
        time.sleep(1)
        #选择简体中文
        self.clickweb('ul.el-dropdown-menu > li:nth-of-type(2)')

    #填写注册页表单
    """会员中心注册页表单"""
    def register_form(self,firstnam,lastname,contury,email,psword):
        #选择语言
        self.choose_lg()
        time.sleep(1)
        #填写名字
        self.inputform('[placeholder="名字"]',firstnam)
        time.sleep(1)
        #填写姓氏
        self.inputform('[placeholder="姓氏"]',lastname)
        time.sleep(1)
        #选择居住国家
        self.clickweb('[placeholder="选择居住国家"]')  #点击下拉框
        time.sleep(1)
        self.dr.find_element_by_xpath('//span[.="{}"]'.format(contury)).click()
        time.sleep(1)
        #输入手机号码
        self.inputform('[placeholder="手机号码"]',self.randomint(8))
        time.sleep(1)
        #输入电子信箱
        self.inputform('[placeholder="电子信箱"]',email)
        time.sleep(1)
        #输入密码
        self.inputform('[placeholder="会员账户密码"]',psword)
        time.sleep(1)
        #输入验证码
        self.inputform('[placeholder="验证码"]','R0sLRl/E2wOcQ/lrejVuabwi9zOnoWCoLrV7yTduyEI=')
        time.sleep(1)
        #点击下一步
        self.clickweb('button.el-button > span')
        time.sleep(1)
        #点击首次登录的弹窗
        self.login_top()