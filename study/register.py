from selenium import webdriver
from basepage import basepage
import time
import unittest
import ddt
from country_list import exceldata

# 读取测试文档数据
e = exceldata()
rows = e.openexcel(r'E:\test\country.xlsx', 'Sheet1')  # 测试文档的路径，sheet名,并获取总行数
testdata = e.dict_data()


# 创建类，继承unittest和basepage
@ddt.ddt  # 数据驱动
class cp_register(unittest.TestCase,basepage):

    # 预置条件
    def setUp(self):
        self.dr = webdriver.Chrome()
        # 调用父类
        self.base = basepage(self.dr)

    # 环境恢复
    def tearDown(self):
        self.dr.quit()

    @ddt.data(*testdata)
    def test_register_from(self, data):
        # 获取每组测试数据的下标
        self.subp = testdata.index(data)
        print('当前测试数据:上级销售国家：{}；三字码：{}；邮箱：{}；专属链接：{}；邀请码：{}；点差类型：{}'.
              format(data['上级销售国家'], data['三字码'], data['邮箱'], data['专属链接'], data['邀请码'], data['点差类型']))
        self.get_url(data['专属链接'], data['邀请码'], 'F', self.subp + 2)


if __name__ == '__main__':
    unittest.main()

