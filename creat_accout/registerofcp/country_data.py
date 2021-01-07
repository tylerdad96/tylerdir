"""此模块用于获取BOS国家列表中的ISO码与国家，制造测试数据"""
from selenium import webdriver
from basepage import basepage
import time

class data_for_register():
    #登录bos
    def login(self,url):
        self.dr=webdriver.Chrome()
        #实例化基本类，并传入参数
        self.base=basepage(self.dr)
        #访问bos登录页
        self.dr.get(url)
        #登录bos
        self.base.login_bos('tyler.tang','Tl123456')

    #打开国家列表页面
    def to_country(self):
        self.melu=self.dr.find_elements_by_css_selector('ul.ivu-menu-vertical>li.ivu-menu-submenu')
        #点击系统设置
        self.melu[5].click()
        time.sleep(1)
        #点击国家列表
        self.melu2=self.dr.find_elements_by_css_selector('li.ivu-menu-opened>ul.ivu-menu>a.ivu-menu-item')
        self.melu2[1].click()
        time.sleep(1)
        #选择每页显示条数
        self.base.clickweb('div.ivu-page-options-sizer span')
        time.sleep(1)
        # #显示100条
        self.article=self.dr.find_elements_by_css_selector('ul.ivu-select-dropdown-list>li.ivu-select-item')
        self.article[7].click()
        time.sleep(1)

    #获取系统中所有的国家，保存至本地
    def getcountry(self):
        #内嵌滚动条滚动到底部
        js='document.getElementsByClassName("ivu-table-overflowY")[0].scrollTop = 10000'
        self.dr.execute_script(js)
        country_list=[]
        time.sleep(1)
        #获取当前页列表长度
        self.page=0
        while self.page<3:
            self.listlong=len(self.dr.find_elements_by_css_selector('tbody.ivu-table-tbody>tr'))-3
            #轮询获取国家名和ISO码
            print(self.listlong)
            for i in range(1,self.listlong+1):
                self.cname=self.dr.find_element_by_xpath('//*[@id="app"]/div/div/div[4]/div/div[2]/\
                    div/div[1]/div[2]/table/tbody/tr[{}]/td[4]'.format(i)).text   
                self.isoname=self.dr.find_element_by_xpath('//*[@id="app"]/div/div/div[4]/div/div[2]\
                    /div/div[1]/div[2]/table/tbody/tr[{}]/td[12]'.format(i)).text
                self.phonecode=self.dr.find_element_by_xpath('//*[@id="app"]/div/div/div[4]/div/div[2]\
                    /div/div[1]/div[2]/table/tbody/tr[{}]/td[13]'.format(i)).text
                if self.page==0:
                    self.base.saveaccount(r'E:\test\all_country.xlsx',self.cname,'A',i+1)
                    self.base.saveaccount(r'E:\test\all_country.xlsx',self.isoname,'B',i+1)
                    self.base.saveaccount(r'E:\test\all_country.xlsx',self.phonecode,'C',i+1)
                elif self.page==1:
                    self.base.saveaccount(r'E:\test\all_country.xlsx',self.cname,'A',i+101)
                    self.base.saveaccount(r'E:\test\all_country.xlsx',self.isoname,'B',i+101)
                    self.base.saveaccount(r'E:\test\all_country.xlsx',self.phonecode,'C',i+101)
                else:
                    self.base.saveaccount(r'E:\test\all_country.xlsx',self.cname,'A',i+201)
                    self.base.saveaccount(r'E:\test\all_country.xlsx',self.isoname,'B',i+201)
                    self.base.saveaccount(r'E:\test\all_country.xlsx',self.phonecode,'C',i+201)    

                dic_country={}
                dic_country[self.cname]=self.isoname
                country_list.append(dic_country)
                # print('国家：{}，ISO：{}'.format(self.cname,self.isoname),end='\n')
                #当获取当前列表中的最后一组数据后，翻页
                if i==self.listlong:
                    self.base.clickweb('.ivu-icon-ios-arrow-forward')
                    time.sleep(1)
                    self.page=self.page+1
                    continue
        return country_list

if __name__=='__main__':
    b=data_for_register()
    b.login('https://at-bos-frontend-uat.atfxdev.com/login')
    b.to_country()
    b.getcountry()