from country_list import exceldata
from openpyxl import load_workbook
import random


countrydata=exceldata()
countrydata.openexcel(r'E:\test\all_country.xlsx','Sheet1')
countrytest=countrydata.dict_data()


class creat_datatest():
    """国家，三字码，邮箱自动写入测试文档，无需手动注册"""
       
     #创建存储注册数据的函数，写入已存在的本地文档中
    def saveaccount(self,excelpath,val,col,row):
        """注：调用此函数时，不能打开需要写入数据的文档"""
        workbook = load_workbook(filename=excelpath)
        sheet = workbook.active
        cel = sheet['{}{}'.format(col, row)]
        cel.value = val
        workbook.save(filename=excelpath)

    #创建是否需要执行此类的函数
    def iscreat(self):
        self.n=input('输入数字表示需要几条测试用例，非数字表示不需要制造测试数据')
        try:
            int(self.n)
            return self.n,True
        except:
            return False

    #生成n位数的随机数（联通号码开头）
    def randomint(self,e):
        self.email_list = ['@qq.com','@163.com','@gmail.com',]
        self.email = ''.join(random.sample('0123456789',e))+str(random.choice(self.email_list)) # 随机生成联通号码
        return self.email

    #存入测试文档
    def savatestdata(self):
        if self.iscreat():
            for i in range(2,int(self.n)+2):
                rows=random.randint(2,239)
                self.randomint(9)
                self.saveaccount(r'E:\test\country.xlsx',countrytest[rows]['国家'],'B',i)
                self.saveaccount(r'E:\test\country.xlsx',countrytest[rows]['ISO'],'A',i)
                self.saveaccount(r'E:\test\country.xlsx',self.email,'D',i)
        else:
            print('无需制造测试数据')
