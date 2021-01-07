from selenium import webdriver
import time
from country_list import exceldata
import ddt
import unittest
from BeautifulReport import BeautifulReport
from kyc_formfill import kycdata
from basepage import basepage

#提取前面脚本注册成功后的数据
e=exceldata()
rows=e.openexcel(r'E:\test\account_number.xlsx','Sheet1') #测试文档的路径，sheet名,并获取总行数
testdata=e.dict_data()

@ddt.ddt#数据驱动
class kyc_verification(unittest.TestCase,kycdata):
        
    """2.0会员中心的验证码及KYC验证"""

    #调用修饰器，所有用例中仅执行一次如下操作
    @classmethod
    def setUpClass(cls):  # cls作为毕传默认参数
        cls.dr=webdriver.Chrome()
        cls.pub = basepage(cls.dr) #基本类的实例化
        #登录页
        cls.dr.get('https://at-client-portal-uat-proxy.ntdevops.com/lgoin')
        time.sleep(1)
        #js打开新窗口访问bos登录页
        js = 'window.open("https://at-bos-frontend-uat.atfxdev.com/login")'
        cls.dr.execute_script(js)
        time.sleep(1)
        #切换窗口
        cls.windsw(cls,1) #cls为必传参数
        time.sleep(1)
        #登录bos
        cls.login_bosin(cls)
        #进入邮箱短信页面
        cls.emailpage(cls)

    def tearDown(self):  #环境恢复
        #登出会员中心
        self.lgoout_cp(self.dr)
        time.sleep(1)
        #刷新页面
        self.dr.refresh()
        
    @ddt.data(*testdata)
    def test_verification(self,data):
        # 测试数据下标
        self.subp = testdata.index(data)
        print('当前测试数据：邮箱:{}，主账户:{}，国家:{}'.format(data['邮箱'],data['主账户'],data['国家']))
        self.windsw(0)
        #登录会员中心
        self.register_top() #去除登录页弹窗
        self.login_cl(data['邮箱'],'Tl123456')
        #填写kyc认证表单
        self.kycfulfill(data['主账户'])
        text=self.css('.is-process.el-step__description .curr-status').text
        time.sleep(1)
        if text=='审批中':
            print('第{}个测试用例：主账户{}个人资讯填写完成等待审核'.format(self.subp+1,data['主账户']))
        else:
            print('个人信息填写失败')

if __name__=='__main__':
    unittest.main()