from selenium import webdriver
import ddt
import unittest
from register import fill_form
from excel_data import  exceldata
from BeautifulReport import BeautifulReport
import time

#读取excel中的测试用例
e = exceldata()
e.openexcel(r'E:\bos_cp_example\register_ex.xlsx', 'data')
testdata = e.dict_data()

#unittest单元测试框架，执行测试用例
@ddt.ddt
class registercase(unittest.TestCase,fill_form):
    #预置条件
    def setUp(self):
        self.dr=webdriver.Chrome()

    #环境恢复
    def tearDown(self):
        time.sleep(2)
        self.dr.quit()

    #判断表单字段填写是否正确
    def form_erro(self):
        if self.is_error():
            self.erro_list = self.dr.find_elements_by_css_selector('.el-form-item__error')
            for i in self.erro_list:
                self.errotext=i.text
                #保存提示语至本地文档：实际结果
                self.saveaccount(r'E:\bos_cp_example\register_ex.xlsx',self.errotext,'I',self.subp+2)
                print('实际结果：{}'.format(self.errotext))
            return True
        else:
            return False

    #登录后返回title
    def welcome_text(self):
        return self.welcome().text

    #写入测试结果
    def result(self,ele1,ele2):
        if ele1 in ele2:
            self.saveaccount(r'E:\bos_cp_example\register_ex.xlsx', 'PASS', 'K', self.subp + 2)
            print('用例PASS')
        else:
            self.saveaccount(r'E:\bos_cp_example\register_ex.xlsx', 'FAILD', 'K', self.subp + 2)
            print('用例FAILD')

    #判断是否为uk国家
    def is_uk(self,country):
        uk_list=['阿尔巴尼亚','安道尔','奥地利','保加利亚','塞浦路斯','捷克共和国','丹麦']
        if country in uk_list:
            self.uk_tips=self.css('div.el-dialog__body>div.tips_body>div>p').text
            return True
        else:
            return False

    #判断邀请码是否正确
    def code_erro(self):
        try:
            self.submitform().click()
            time.sleep(1)
            self.code_erroalert=self.css('.el-message__content')
            if self.code_erroalert.is_displayed():
                print('实际结果:{}'.format(self.code_erroalert.text))
                return True
        except:
            return False

    #数据驱动，读取测试用例
    @ddt.data(*testdata)
    def test_register(self,data):
        # 获取测试用例的下标
        self.subp = testdata.index(data)
        print('第{}条测试用例：名字：{}，姓氏：{}，居中国家：{}，手机号码：{}，电子邮箱：{}，密码：{}，邀请码：{}'
              .format(self.subp+1,data['名字'],data['姓氏'],data['居住国家'],data['手机号码'],data['电子信箱'],data['会员账户密码'],data['邀请码']))

        # #调用已封装的注册方法
        register_form=fill_form(self.dr,'https://at-client-portal-uat.atfxdev.com/register')
        self.submit(data['名字'],data['姓氏'],data['居住国家'])

        #判断国家是否为uk
        if self.is_uk(data['居住国家']):
            self.saveaccount(r'E:\bos_cp_example\register_ex.xlsx', self.uk_tips, 'I', self.subp + 2)
            time.sleep(1)
            print('实际结果：{}'.format(self.uk_tips))
            print('预期结果：{}'.format(data['预期结果']))
            self.dr.close()
            self.assertIn(data['预期结果'],self.uk_tips)
            #运行结果写入本地文档
            self.result(data['预期结果'],self.uk_tips)
        else:
            #输入手机号等字段
            self.submitatlast(data['手机号码'],data['电子信箱'],data['会员账户密码'])
            self.need_code(data['邀请码'])

            # 点击提交
            self.submitform().click()
            #判断各字段是否填写正确
            #邀请码是否正确
            if self.form_erro():#如不正确，退出
                print('预期结果：{}'.format(data['预期结果']))
                #执行结果写入本地文档
                self.result(data['预期结果'], self.errotext)
                # 断言
                self.assertIn(data['预期结果'],self.errotext)
                self.dr.close()
            elif self.code_erro():
                self.saveaccount(r'E:\bos_cp_example\register_ex.xlsx', self.code_erroalert.text, 'I', self.subp + 2)
                print('预期结果：{}'.format(data['预期结果']))
                # 运行结果写入本地文档
                self.result(data['预期结果'], self.code_erroalert.text)
                time.sleep(1)
                self.assertIn(data['预期结果'], self.code_erroalert.text)
                # 运行结果写入本地文档
                self.dr.close()
            # 填写无误
            else:
                # 去除登录后弹窗
                self.cl_pop_up().click()
                self.clikok().click()
                print('预期结果：{}'.format(data['预期结果']))
                print('实际结果：{}'.format(self.welcome_text()))
                self.saveaccount(r'E:\bos_cp_example\register_ex.xlsx', self.welcome_text(), 'I', self.subp + 2)
                #断言-相等
                time.sleep(1)
                self.assertIn(data['预期结果'], self.welcome_text())
                # 运行结果写入本地文档
                self.result(data['预期结果'], self.welcome_text())

if __name__=='__main__':
    #生成测试报告
    suit=unittest.defaultTestLoader.discover('./',pattern='test_register.py',top_level_dir=None)
    BeautifulReport(suit).report(filename='会员中心测试用例报告',description='测试用例执行情况',report_dir=r'E:\bos_cp_example\会员中心注册页测试用例报告')