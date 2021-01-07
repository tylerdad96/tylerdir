from selenium import webdriver
from basepage import basepage
import time
import unittest
import ddt
from country_list import exceldata
from cp_register_form import formfill
from creat_testdata import creat_datatest

#读取测试文档数据
e=exceldata()
rows=e.openexcel(r'E:\test\country.xlsx','Sheet1') #测试文档的路径，sheet名,并获取总行数
testdata=e.dict_data()
#测试数据自动化
c=creat_datatest()
c.savatestdata()

#创建类，继承unittest和basepage
@ddt.ddt #数据驱动
class cp_register(unittest.TestCase,formfill):
    """注：自定义类formfill已继承basepage基本类，所以cp_register类也继承基本类"""

    #预置条件，实例化基本类
    def setUp(self):
        self.dr=webdriver.Chrome()
        self.base=basepage(self.dr)

    #环境恢复
    def tearDown(self):
        self.dr.quit()
    
    @ddt.data(*testdata)
    def test_register_from(self,data):
        #判断当前国家是否可注册
        if self.is_uk(data['国家']):
            self.dr.close()
        else:
            # 获取每组测试数据的下标
            self.subp = testdata.index(data)
            print('当前测试数据:国家：{}；三字码：{}；邮箱：{}；专属链接：{}；邀请码：{}；点差类型：{}'.
                format(data['国家'],data['三字码'],data['邮箱'],data['专属链接'],data['邀请码'],data['点差类型']))
            self.get_url(data['专属链接'],data['邀请码'],'F',self.subp+2)
            time.sleep(1)
            #调用封装方法，姓名，密码可在此设置
            self.register_form('test','tyler',data['国家'],data['邮箱'],'Tl123456')
            # 保存测试数据到本地文档
            self.saveaccount(r'E:\test\account_number.xlsx',data['国家'], 'A', self.subp + 2)
            self.saveaccount(r'E:\test\account_number.xlsx',data['邮箱'], 'B', self.subp + 2)
            self.saveaccount(r'E:\test\account_number.xlsx',data['三字码'], 'D', self.subp + 2)
            self.saveaccount(r'E:\test\account_number.xlsx',data['点差类型'], 'E', self.subp + 2)
            # 获取主账号,并保存至本地文档
            try:
                textid = self.page_text('.user-name-font') + ' '
                self.id = textid[4:-1]
                self.saveaccount(r'E:\test\account_number.xlsx',self.id, 'C', self.subp + 2)
                #ib账户点击ib返佣表格
                if self.id[0:2]=='10':
                    self.ib_table()
                else:
                    pass
                print('第{}个测试数据注册成功，主账户：{}'.format(self.subp + 1, self.id))
            except:
                print('注册失败')

if __name__=='__main__':
    unittest.main()