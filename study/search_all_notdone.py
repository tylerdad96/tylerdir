from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

class search():
    '''查找所有未done掉的ticket'''
    dr=webdriver.Chrome()
    dr.maximize_window()
    dr.implicitly_wait(60)
    #登录
    def login(self,username='tyler.tang@newtype.io',password='TL961013..'):
        self.dr.get('https://id.atlassian.com/login')
        time.sleep(2)
        #输入用户名
        self.dr.find_element_by_css_selector('.Input__InputElement-sc-1o6bj35-0').send_keys(username)
        time.sleep(2)
        #点击继续
        self.dr.find_element_by_css_selector('span.css-1vqao0l>span.css-t5emrf').click()
        time.sleep(1)
        #输入密码
        self.dr.find_element_by_css_selector('#password').send_keys(password)
        time.sleep(2)
        #回车登录
        self.dr.find_element_by_css_selector('#password').send_keys(Keys.ENTER)

    #点击自己的项目
    def project(self):
        #参数化登录方法
        self.dr.find_element_by_css_selector('a.sc-jDwBTQ>span.sc-iRbamj').click()
        time.sleep(1)
        #点击事物和过滤器
        s=self.dr.find_elements_by_css_selector('a[data-testid="NavigationItem"]>div.css-t44v0r>div')
        time.sleep(2)
        s[4].click()
        time.sleep(2)
        #点击由我报告
        self.dr.find_element_by_link_text('由我报告').click()
        time.sleep(2)
    #点击高级搜索，
    def notdone(self):
        self.dr.find_element_by_link_text('高级搜索').click()
        time.sleep(2)
        e=self.dr.find_elements_by_css_selector('.criteria-wrap')
        time.sleep(1)
        #点击状态
        e[2].click()
        time.sleep(5)
        #点击待办
        self.dr.find_element_by_css_selector('ul.aui-last>li.check-list-item>label[data-descriptor-title="待办"]').click()
        time.sleep(5)
    #打印代办的bug
    def done(self):
        #定位到未处理的ticket列表
        t=self.dr.find_elements_by_css_selector('ol.issue-list>li')
        time.sleep(1)
        for i in t:
            #打印title元素
            print(i.get_attribute('title'),end=' ')
            time.sleep(1)
            #打印ticket
            print(i.get_attribute('data-key'),end='\n')
            time.sleep(1)
        #统计共有多少未处理ticket
        print('共有未处理ticket{}条'.format(len(t)))
if __name__=='__main__':
    s=search()
    s.login()
    s.project()
    s.notdone()
    s.done()