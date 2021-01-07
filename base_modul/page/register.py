from base_page import basepage
import time
from openpyxl import load_workbook

class fill_form(basepage):
    """定位与操作分离"""
    #定位表单中的各个字段
    #定位弹窗
    def pop_up(self):
        return self.wcss('.blk-sure-btn')
    #定位名字
    def form_fistname(self):
        return self.css('[placeholder="名字"]')
    #定位姓氏
    def form_lastname(self):
        return self.css('[placeholder="姓氏"]')
    #定位居住国家
    def form_country(self):
        return self.css('[placeholder="选择居住国家"]')
    #定位手机号
    def form_phonenum(self):
        return self.css('[placeholder="手机号码"]')
    #定位邮箱
    def form_email(self):
        return self.css('[placeholder="电子信箱"]')
    #定位用户密码
    def form_psword(self):
        return self.css('[placeholder="会员账户密码"]')
    #定位验证码
    def form_vcode(self):
        return self.css('[placeholder="验证码"]')
    #定位提交按钮
    def form_submit(self):
        return self.css('button.el-button > span')
    #定位首页的'欢迎***'
    def welcome(self):
        return self.css('.nav-title')
    #定位弹窗
    def cl_pop_up(self):
        return self.css('div.text-center .el-checkbox__inner')
    def clikok(self):
        return self.css('.confirm-btn')

    # #输入邀请码
    def need_code(self,code):
        if len(code) != 0:
            self.css('.el-textarea__inner').send_keys(code)
        else:
            pass

    #定位提交按钮
    def submitform(self):
        return self.css('.el-form-item__content>button')

    #判断表单填写后页面有无成功跳转
    def login_popup(self):
        self.css('div.text-center .el-checkbox__inner').click()
        time.sleep(1)
        self.css('div.text-center>button.declar-checked').click()

    #创建存储注册数据的函数，写入已存在的本地文档中
    def saveaccount(self,excelpath,val, lin, han):
        workbook = load_workbook(filename=excelpath)
        data = workbook.active
        cel = data['{}{}'.format(lin, han)]
        cel.value = val
        workbook.save(filename=excelpath)

    def is_error(self):
        try:
            self.css('.el-form-item__error')
            return True
        except:
            return False

    #操作定位元素
    def submit(self,fname,lname,country):
        #点击弹窗
        self.pop_up().click()
        time.sleep(1)
        #切换语言
        self.css('.la-globe').click()
        time.sleep(1)
        self.css('ul.el-dropdown-menu > li:nth-of-type(2)').click()
        time.sleep(1)
        # 输入名
        self.form_fistname().send_keys(fname)
        time.sleep(1)
        #输入姓
        self.form_lastname().send_keys(lname)
        time.sleep(1)
        #选择居住国家
        self.form_country().click()
        time.sleep(1)
        self.dr.find_element_by_xpath('//span[.="{}"]'.format(country)).click()
        time.sleep(1)

    def submitatlast(self,phonenum,email,psword):
        self.form_phonenum().send_keys(phonenum)
        time.sleep(1)
        #输入邮箱
        self.form_email().send_keys(email)
        time.sleep(1)
        #输入密码
        self.form_psword().send_keys(psword)
        time.sleep(1)
        #输入验证码
        self.form_vcode().send_keys('R0sLRl/E2wOcQ/lrejVuabwi9zOnoWCoLrV7yTduyEI=')