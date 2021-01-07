print(1)


from selenium import webdriver
import time
from selenium.webdriver.support.wait import WebDriverWait
from country_list import exceldata
import ddt
import unittest
from openpyxl import load_workbook
from BeautifulReport import BeautifulReport

e=exceldata()
rows=e.openexcel(r'E:\test\account_number.xlsx','Sheet1') #测试文档的路径，sheet名,并获取总行数
testdata=e.dict_data()

@ddt.ddt #数据驱动
class creat_trade_account(unittest.TestCase):
    """会员中心创建交易账户"""

    def setUp(self):#预置条件,注册销售/代理，更改链接即可
        self.dr = webdriver.Chrome()
        self.dr.maximize_window()  # 最大化窗口
        self.dr.implicitly_wait(20)  # 隐式等待20s
        self.dr.get('https://at-client-portal-uat.atfxdev.com/login')
        time.sleep(1)

    def tearDown(self):#环境恢复
        time.sleep(3)
        self.dr.close()
        self.dr.quit()

    # 封装css定位方法
    def css(self,element):
        self.el=self.dr.find_element_by_css_selector(element)
        return self.el

    #封装显示等待定位方法,等待10s，每1s询问一次
    def wcss(self,name):
        self.wel = WebDriverWait(self.dr,10,1).until(lambda x: x.find_element_by_css_selector(name))
        return self.wel

    #创建存储注册数据的函数，写入已存在的本地文档中
    def saveaccount(self,val,lin, han):
        workbook = load_workbook(filename=r'E:\test\account_number.xlsx')
        sheet = workbook.active
        cel = sheet['{}{}'.format(lin, han)]
        cel.value = val
        workbook.save(filename=r'E:\test\account_number.xlsx')

    @ddt.data(*testdata)
    def test_login(self,data):
        print('当前测试数据{}'.format(data['主账户']))
        # 获取每组测试数据的下标
        subp = testdata.index(data)
        #去除弹窗
        try:
            self.wcss('.blk-sure-btn').click()
            time.sleep(1)
        except:
            pass
        #选择语言为简中
        self.css('.la-globe').click()
        time.sleep(1)
        self.css('ul.el-dropdown-menu > li:nth-of-type(2)').click()
        #输入邮箱，密码,登录
        self.css('[placeholder="请输入您的电子信箱"]').clear()
        time.sleep(1)
        self.css('[placeholder="请输入您的电子信箱"]').send_keys(data['邮箱'])
        time.sleep(1)
        self.css('div.formBlock > .el-form > .el-col [placeholder="请输入您的密码"]').send_keys('Tl123456')
        time.sleep(1)
        self.css('div.formBlock > .el-form > .el-col .el-button > span').click()
        time.sleep(2)
        try:
            self.wcss('div.text-center .el-checkbox__inner').click()
            time.sleep(2)
            self.css('.confirm-btn').click()
            time.sleep(1)
        except:
            pass
        #创建交易账户
        self.wcss('button.apply-account-btn > span > span').click()
        time.sleep(2)
        #输入交易账户密码
        self.css('[placeholder="真实交易账户密码"]').send_keys('Tl123456')
        time.sleep(1)
        self.css('button.el-button > span > span').click()
        time.sleep(2)
        #回到首页获取交易账户
        self.css('.side-nav-cell').click()
        time.sleep(3)
        t=self.css('.account-number-cla').text+' '
        time.sleep(2)
        tradeid=t[12:-1]
        self.saveaccount(tradeid, 'D', subp + 2)
        print('第{}个测试数据开户成功，交易账户：{}'.format(subp + 1,tradeid))

if __name__=='__main__':
    print(1)
    # 生成测试报告
    suit=unittest.defaultTestLoader.discover('./',pattern='creat_trade_account.py',top_level_dir=None)
    BeautifulReport(suit).report(filename='创建真实交易账户',description='不同证件签发国KYC验证通过',report_dir='all_case_report')