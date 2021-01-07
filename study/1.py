# # # # # CN_mobile = [134, 135, 136, 137, 138, 139, 150, 151, 152, 157, 158, 159, 182, 183, 184,187, 188, 147, 178, 1705]
# # # # #
# # # # # p=input('请输入电话号码')
# # # # # # print(type(p[0:3]))
# # # # # # print(int(p[0:3]) in CN_mobile)
# # # # # # print(type(CN_mobile[2]))
# # # # # p=str(p)
# # # # # print(p)
# # # # # if len(p)==11:
# # # # #     print(1)
# # # # #导包
# # # # # from selenium import webdriver
# # # # # import time
# # # # #
# # # # #
# # # # # #设置全局变量
# # # # # dr=webdriver.Chrome()
# # # # # #最大化窗口
# # # # # dr.maximize_window()
# # # # # dr.get('https://www.chinese-atfx.com/')
# # # # # time.sleep(2)
# # # # # dr.find_element_by_css_selector('#menu-item-15').click()
# # # # # sleep(2)
# # # # # dr.find_element_by_css_selector('div.el-input>input[type="text"]')
# # # #
# # # # # import random
# # # # #
# # # # # while True:
# # # # #     a = random.randint(1, 10)
# # # # #
# # # # #     if a==10:
# # # # #         print(a)
# # # # #         break
# # # # #     else:
# # # # #         print(a)
# # # # #         pass
# # # #
# # # # from selenium import webdriver
# # # # import time
# # # # from selenium.webdriver.support.select import Select
# # # # dr=webdriver.Chrome()
# # # # dr.get('https://www.atfx.com/gm/en/forex-demo-account/')
# # # # time.sleep(2)
# # # # # dr.find_element_by_css_selector('#sbToggle_50212175').click()
# # # # # time.sleep(2)
# # # # # a=dr.find_elements_by_css_selector('u1#sbOptions_50212175>li.option-item')
# # # # # a[2].click()
# # # # # dr.find_element_by_css_selector('div.combo-select>div.combo-arrow').click()
# # # # # time.sleep(2)
# # # # # a=dr.find_elements_by_css_selector('ul.combo-dropdown>li.option-item')
# # # # # time.sleep(2)
# # # # # a[170].click()
# # # # dr.get('https://apply-gm.atfxid.com/')
# # # # a=dr.find_element_by_css_selector('.btn-default').text
# # # # print(a)
# # #
# # # # dr.get('https://www.cnblogs.com/yoyoketang/p/6426799.html')
# # # # js='document.getElementById("yoyoketang").scrollLeft=10000'
# # # #
# # # # dr.execute_script(js)
# # #
# # # # #判断元素是否存在(css定位方法)
# # # # def is_elememt_exist(css):
# # # #     e=dr.find_elements_by_css_selector(css)
# # # #     #唯一，'%s'%s2的用法相当于str{}.format()
# # # #     if len(e)==1:
# # # #         print('%s元素存在且唯一'%css)
# # # #         return True
# # # #     #不存在
# # # #     elif len(e)==0:
# # # #         print('不存在%s元素'%css)
# # # #         return False
# # # #     #存在多个
# # # #     elif len(e)>1:
# # # #         print('找到%s元素'%css+str(len(e))+'个')
# # # #         return False
# # # #
# # # # from selenium.webdriver.common.by import By
# # #
# # # # dr.maximize_window()
# # # # url = 'https://home.cnblogs.com/u/testyler'
# # # # dr.get(url)
# # # # time.sleep(2)
# # # # # 点击登录
# # # # dr.find_element_by_css_selector('.s-top-login-btn').click()
# # # # time.sleep(2)
# # # # # 点击账户密码登录
# # # # dr.find_element_by_css_selector('.tang-pass-footerBarULogin').click()
# # # # time.sleep(1)
# # # # dr.find_element_by_css_selector('#TANGRAM__PSP_11__userName').send_keys(18696194961)
# # # # dr.find_element_by_css_selector('#TANGRAM__PSP_11__password').send_keys('TL123456..')
# # # # time.sleep(2)
# # # # # 点击登录
# # # # dr.find_element_by_css_selector('#TANGRAM__PSP_11__submit').click()
# # # from selenium import webdriver
# # # import unittest
# # # import time
# # # import HTMLTestRunner
# # # import os
# # #
# # #
# # # # 创建一个类，继承unittest模块中的TestCaseL类
# # # class Test(unittest.TestCase):
# # #     # 预置条件
# # #     def setUp(self):
# # #         self.dr=webdriver.Chrome()
# # #         self.dr.get('https://www.baidu.com/')
# # #         time.sleep(3)
# # #
# # #     # 环境恢复
# # #     def tearDown(self):
# # #         time.sleep(2)
# # #         self.dr.close()
# # #         self.dr.quit()
# # #
# # #     # 封装输入点击搜索方法
# # #     # def serch(self,keywrod):
# # #     #     dr.find_element('css_selector','#kw').send_keys(keywrod)
# # #     #     time.sleep(2)
# # #     #     dr.find_element_by_css_selector('#su').click()
# # #     def test_01(self):
# # #         self.dr.find_element_by_css_selector('#kw').send_keys('selenium')
# # #         time.sleep(2)
# # #         self.dr.find_element_by_css_selector('#su').click()
# # #         time.sleep(2)
# # #
# # #     def test_02(self):
# # #         self.dr.find_element_by_css_selector('#kw').send_keys('python')
# # #         time.sleep(2)
# # #         self.dr.find_element_by_css_selector('#su').click()
# # #         time.sleep(2)
# # #
# # #
# # # if __name__ == '__main__':
# # #     unittest.main()
# #
# # # from selenium import webdriver
# # # dr=webdriver.Chrome()
# # # dr.get('https://www.chinese-atfx.com/20200608/')
# # # js='document.documentElement.scrollTop=10000'
# # # dr.execute_script(js)
# #
# # import ddt
# # import unittest
# #
# # tdata=[{'username': 'tyler', 'password': '123456', '级别': '超级管理员'},
# #           {'username': 'admin', 'password': '67894', '级别': '管理员'},
# #           {'username': 'tang', 'password': 'tl123', '级别': '普通用户'},
# #           {'username': '李四', 'password': '12356', '级别': '普通用户'}]
# # @ddt.ddt
# # class test(unittest.TestCase):
# #     def setUp(self):
# #         print('start')
# #     def tearDown(self):
# #         print('end')
# #     @ddt.data(*tdata)
# #     def test_ddt(self,data): #注意这里的data
# #         print(data)
# #
# # if __name__ == '__main__':
# #     unittest.mai
#
# import xlrd
# from selenium import webdriver
# import time
# import unittest
# import ddt
#
# #获取excel表格的内容，并封装成多个字典的list类型，供测试用例使用
# class exceldata():
#     def openexcel(self,excelpath,sheetnaem):
#         #打开excel表格
#         self.data=xlrd.open_workbook(excelpath)
#         self.table=self.data.sheet_by_name(sheetnaem)
#         #获取第一行数据作为key
#         self.key=self.table.row_values(0)
#         #获取总行数
#         self.rows=self.table.nrows
#         #获取总列数
#         self.clos=self.table.ncols
#
#     def dict_data(self):
#         if self.rows<=1:
#             print('该sheet表无数据')
#         else:
#             r=[]
#             j=1
#             for i in range(self.rows-1):#除去首行
#                 s={}
#                 #获取第二列的值
#                 valus=self.table.row_values(j)
#                 for x in range(self.clos):
#                     s[self.key[x]]=valus[x] #每个循环的字典中，key列表中的第x项=valus列表中的第x项
#                 r.append(s)
#                 j=j+1
#             return r
#
# if __name__=='__main__':
#     e=exceldata()
#     e.openexcel(r'E:\dir\test.xlsx','en')
#     print(e.dict_data())

# from selenium import webdriver
# import time
# from PIL import Image
#
# dr=webdriver.Chrome()
# dr.get('https://at-client-portal-uat.atfxdev.com/register')
# time.sleep(1)
# def css(name):
#     el=dr.find_element_by_css_selector(name)
#     return el
# import random
# rs =''.join(random.sample('0123456789', 4))
# print(rs)
# rs1 =random.sample('0123456789', 4)
# print(rs1)
#
# list=['6', '8', '2', '1']
# a=''.join(list)
# print(a)
#
# import json
# import requests
# import base64
# from io import BytesIO
# from PIL import Image
# from sys import version_info
#
#
# def base64_api(uname,pwd,img):
#     img = img.convert('RGB')
#     buffered = BytesIO()
#     img.save(buffered, format="JPEG")
#     if version_info.major >= 3:
#         b64 = str(base64.b64encode(buffered.getvalue()), encoding='utf-8')
#     else:
#         b64 = str(base64.b64encode(buffered.getvalue()))
#     data = {"username": uname, "password": pwd, "image": b64}
#     result = json.loads(requests.post("http://api.ttshitu.com/base64", json=data).text)
#     if result['success']:
#         return result["data"]["result"]
#     else:
#         return result["message"]
#     return ""
#
#
# if __name__ == "__main__":
#     img_path = r"E:\test\001.png"
#     img = Image.open(img_path)
#     result = base64_api(uname='tyler', pwd='123456', img=img)
#     print(result)
# def a():
#     print('1')
#
# def b():
#     a()
#     print(2)
# b()

# from selenium import webdriver
# from selenium.webdriver.support.wait import WebDriverWait
# dr=webdriver.Chrome()

# dr = webdriver.Chrome()
# dr.maximize_window()
# dr.get('https://at-client-portal-uat.atfxdev.com/register')
# def login(element):
#     el=WebDriverWait(dr,10).until(lambda x:x.find_element_by_css_selector(element))
#     return el
#
# login('.blk-sure-btn').click()
# a=lambda x,y:x*y
# print(a(3,6))
#
# def a(x,y):
#     print(x*y)
#
# a(3,6)
# def A(x):
#     x.get('www.baidu.com')

# from selenium import webdriver
#
# class creat_account():
#     """2.0会员中心注册流程,根据国家列表注册对应的证件签发国账户"""
#     #进入注册页面
#     def __init__(self):
#         self.dr=webdriver.Chrome()
#         self.dr.maximize_window() #最大化窗口
#         self.dr.implicitly_wait(20) #隐式等待20s
#     def login(self):
#         self.dr.get('https://www.baidu.com/')
#
# if __name__=='__mian__':
#     c=creat_account()
#     c.login()
# class A():
#     def __init__(self):
#         print(123)
#     def a(self):
#         print(456)
#
# A()
# b=A().a()

# from selenium import webdriver
# import time
# import random
#
# dr = webdriver.Chrome()
# dr.get('https://at-client-portal-uat.atfxdev.com/register')
# time.sleep(5)
# try:
#     dr.find_element_by_css_selector('.blk-sure-btn').click()
# except:
#     pass
#
# # dr.find_element_by_css_selector('.blk-sure-btn').click()
# time.sleep(1)
# dr.find_element_by_css_selector('.la-globe').click()
# time.sleep(1)
# dr.find_element_by_css_selector('ul.el-dropdown-menu > li:nth-of-type(2)').click()
# time.sleep(2)
# dr.find_element_by_css_selector('[placeholder="名字"]').send_keys('tyler')
# time.sleep(1)
# dr.find_element_by_css_selector('[placeholder="姓氏"]').send_keys('test')
#
# time.sleep(1)
# dr.find_element_by_css_selector('[placeholder="选择居住国家"]').click()
# time.sleep(2)
# text01='毛里求斯'
# dr.find_element_by_xpath('//span[.="{}"]'.format(text01)).click()


# dr.find_element_by_css_selector('[placeholder="选择居住国家"]').send_keys('阿尔及利亚')
# time.sleep(1)
# dr.find_element_by_css_selector('div[x-placement="bottom-start"] li:nth-of-type(2) > span').click()
# time.sleep(1)
# phone_list=[130,131,132,155,156,185,186,145,146,166,167,175,176]
# phone_num=str(random.choice(phone_list))+''.join(random.sample('0123456789',8))
# dr.find_element_by_css_selector('[placeholder="手机号码"]').send_keys(phone_num)
# time.sleep(1)
# # email=phone_num+'@wo.cn'
# dr.find_element_by_css_selector('[placeholder="电子信箱"]').send_keys(phone_num+'@wo.cn')
# time.sleep(1)
# dr.find_element_by_css_selector('[placeholder="会员帐户密码"]').send_keys('Tl123456')
# dr.find_element_by_css_selector('[placeholder="验证码"]').send_keys('1234')
# dr.find_element_by_css_selector('button.el-button > span').click()
# time.sleep(5)
# a=dr.find_element_by_css_selector('form.el-form > div:nth-of-type(7) .el-form-item__error').text
# print(a)
# a=dr.find_element_by_css_selector('form.el-form > div:nth-of-type(7) .el-form-item__error').is_displayed()
# print(a)
# def is_code_true():
#     try:
#         dr.find_element_by_css_selector('form.el-form > div:nth-of-type(7) .el-form-item__error')
#         return True
#     except:
#         return False
#
# while True:
#     if is_code_true():
#         dr.find_element_by_css_selector('[placeholder="验证码"]').clear()
#         time.sleep(2)
#         dr.find_element_by_css_selector('[placeholder="验证码"]').send_keys('4569')
#         time.sleep(2)
#         dr.find_element_by_css_selector('.login-wrap').click()
#         continue
#     else:
#         break







# # 获取当前时间并格式化，用当前时间命名截图，保存至本地test文件下
# img_name = time.strftime('%Y-%m-%d%H%M%S', time.localtime(time.time()))
# dr.get_screenshot_as_file(r'E:\test\{}.png'.format(img_name))
# # 获取图片元素定位
# img_ele = dr.find_element_by_css_selector('div.code-cell>svg')
# # 得到该元素左上角的 x，y 坐标和右下角的 x，y 坐标
# left = img_ele.location.get('x')
# lefty = img_ele.location.get('y')
# right = left + img_ele.size.get('width')
# righty = lefty + img_ele.size.get('height')
# # 打开之前的截图
# image = Image.open(r'E:\test\{}.png'.format(img_name))
# # 对图片进行裁剪，裁剪范围为之前验证的左上角至右下角范围
# new_image = image.crop((left, lefty, right, righty))
# new_image.save(r'E:\test\{}.png'.format(img_name + 'new'))
# # 调用第三方接口，识别验证码图片
# img_path = r'E:\test\{}.png'.format(img_name + 'new')
# img = Image.open(img_path)
# result = base64_api('tyler', '123456', img)


# from selenium import webdriver
# import time
# import random
#
# dr=webdriver.Chrome()
# dr.get('https://www.douban.com/')
# a=dr.find_element_by_css_selector('.app-title>span').text
# print(a)
# from selenium import webdriver
# import time
# from selenium.webdriver.support.wait import WebDriverWait
#
# dr=webdriver.Chrome()
# dr.maximize_window()
# dr.get('https://at-bos-frontend-uat.atfxdev.com/login')
# dr.find_element_by_css_selector('.ivu-icon-ios-arrow-down').click()
# time.sleep(1)
# #选择语言为中文
# dr.find_element_by_css_selector('ul.ivu'
#                                 '-select-dropdown-list > li:nth-of-type(1)').click()
# time.sleep(1)
# dr.find_element_by_css_selector('[placeholder="账号"]').send_keys('tyler')
# dr.find_element_by_css_selector('[placeholder="密码"]').send_keys('Tl123456')
# dr.find_element_by_css_selector('button.ivu-btn-large > span').click()
# time.sleep(1)
# WebDriverWait(dr,10,1).until(lambda x: x.find_element_by_css_selector('div[width="200"] li:nth-of-type(5) > .ivu-menu-submenu-title > span')).click()
# #点击邮件/短信记录
# time.sleep(1)
# dr.find_element_by_css_selector('div[width="200"] [href="/report/emailrecord"]').click()
# time.sleep(2)
# #简讯sms
# dr.find_element_by_css_selector('div.ivu-tabs-nav > div:nth-of-type(3)').click()
# dr.find_element_by_css_selector('div.ivu-tabs-content > div:nth-of-type(2) > div:nth-of-type(1) > '
#          'div:nth-of-type(1) > div:nth-of-type(1) > '
#          'div:nth-of-type(2) span:nth-of-type(1)').click()
# time.sleep(1)
# dr.find_element_by_css_selector('div.ivu-select-visible .ivu-select-dropdown-list > li:nth-of-type(1)').click()
# time.sleep(1)
# dr.find_element_by_css_selector('div.ivu-tabs-content > \
# div:nth-of-type(2) div:nth-of-type(2) > \
# div:nth-of-type(1) > input:nth-of-type(1)').send_keys('1200006169')  # 输入主账户
# dr.find_element_by_css_selector('div.ivu-tabs-content >div:nth-of-type(2) > \
# div:nth-of-type(1) > div:nth-of-type(1) > div:nth-of-type(1) > \
# div:nth-of-type(2) div:nth-of-type(2) \
# i:nth-of-type(1)').click()
# time.sleep(1)
# dr.find_element_by_css_selector('div.ivu-tabs-content > div:nth-of-type(2) th:nth-of-type(5) i:nth-of-type(2)').click()
# time.sleep(1)
# dr.find_element_by_css_selector('div.ivu-tabs-content > div:nth-of-type(2) > \
#            div:nth-of-type(1) > div:nth-of-type(1) \
#            div:nth-of-type(1) > div:nth-of-type(2) a:nth-of-type(1)').click()
# pe=dr.find_elements_by_css_selector('div.ivu-drawer-no-header>\
#         div.ivu-drawer-content>div.ivu-drawer-body>div')
# time.sleep(1)
# print(pe[1].is_displayed())
# print(pe[1].text)
# a=1
#
# print('zhengj{}'.format(a))
# from selenium import webdriver
# import time
# import random
# from selenium.webdriver.common.action_chains import ActionChains
#
# from selenium.webdriver.support.wait import WebDriverWait
# from bs4 import BeautifulSoup
# import os
#
#
# # soup=BeautifulSoup(html,'lxml')
# dr=webdriver.Chrome()
# dr.maximize_window()
# dr.implicitly_wait(20)
# dr.get('https://at-client-portal-uat.atfxdev.com/home')
# time.sleep(2)
# # 如果有警告框，则点击，否则pass
# try:
#     dr.find_element_by_css_selector('.blk-sure-btn').click()
# except:
#     pass
# dr.find_element_by_css_selector('b').click()
# time.sleep(2)
# dr.find_element_by_css_selector('ul.el-dropdown-menu > li:nth-of-type(2)').click()
# time.sleep(2)
# dr.find_element_by_css_selector('[placeholder="请输入您的电子信箱"]').send_keys('2515756303@qq.com')
# time.sleep(1)
# dr.find_element_by_css_selector('div.formBlock > .el-form > .el-col [placeholder="请输入您的密码"]').send_keys('Tl123456')
# time.sleep(1)
# dr.find_element_by_css_selector('div.formBlock > .el-form > .el-col .el-button').click()
# time.sleep(3)
# dr.find_element_by_css_selector('div.nav > div:nth-of-type(4) .progress-text').click()
# time.sleep(1)
# #输入证件签发国国家
# dr.find_element_by_css_selector('[placeholder="请选择您的证件签发国"]').click()
# time.sleep(1)
# f=dr.find_elements_by_xpath('//span[.="百慕大"]')
# time.sleep(1)
# f[1].click()
# time.sleep(1)
# dr.find_element_by_css_selector('div.imgCard > div:nth-of-type(1) .upload-text > [data-v-167e3d93]').click()
# time.sleep(1)
# os.system(r'E:\test\client_kyc.exe')
# time.sleep(1)
# sex=dr.find_elements_by_css_selector('label.el-radio>span>span.el-radio__inner')
# #随机选择性别
# sex[random.choice([0,1])].click()
# #选择出生日期
# dr.find_element_by_css_selector('[placeholder="请选择出生日期为DD-MM-YYYY的格式"]').click()
# time.sleep(1)
# dr.find_element_by_css_selector('div.el-date-picker__header > span:nth-of-type(1)').click()
# #选择年份
# y=dr.find_element_by_css_selector('.el-icon-d-arrow-left')
# ActionChains(dr).double_click(y).perform()
# dr.find_element_by_css_selector('.el-icon-d-arrow-left').click()
# #随机选择年份
# ye=dr.find_elements_by_css_selector('table.el-year-table>tbody>tr>td')
# ye[random.randint(0,9)].click()
# time.sleep(1)
# mu=dr.find_elements_by_css_selector('table.el-month-table>tbody>tr>td')
# mu[random.randint(0,11)].click()
# time.sleep(1)
# da=dr.find_elements_by_css_selector('table.el-date-table>tbody>tr>td')
# da[random.randint(0,41)].click()
# time.sleep(1)
# #输入随机电话号码
# dr.find_element_by_css_selector('[placeholder="请输入证件号码"]').send_keys(''.join(random.sample('0123456789', 8)))
# #选择证件到期日
# # dr.find_element_by_css_selector('[placeholder="请选择证件到期日为DD-MM-YYYY的格式"]').click()
# # time.sleep(1)
# # dr.find_element_by_css_selector('div[x-placement="bottom-start"] .el-date-picker__header > span:nth-of-type(1)').click()
# # time.sleep(1)
# # dy=dr.find_elements_by_css_selector('table.el-year-table>tbody>tr>td')
# # dy[random.randint(13,21)].click()
# # time.sleep(1)
# # dm=dr.find_elements_by_css_selector('table.el-month-table>tbody>tr>td')
# # dm[random.randint(12,23)].click()
# # time.sleep(1)
# # dd=dr.find_elements_by_css_selector('table.el-date-table>tbody>tr>td')
# # dd[random.randint(42,83)].click()
# # time.sleep(1)
# dr.find_element_by_css_selector('[placeholder="请选择现居地"]').click()
# time.sleep(1)
# ju=dr.find_elements_by_xpath('//span[.="{}"]'.format('马里'))
# ju[1].click()
# time.sleep(1)
# dr.find_element_by_css_selector('[placeholder="请输入地址"]').send_keys(''.join(random.sample('ABCDEFGHIJKLMN', 8)))
# time.sleep(1)
# dr.find_element_by_css_selector('label.agree-rules-box .el-checkbox__inner').click()
# time.sleep(1)
# # dr.find_element_by_css_selector('button.submit-btn > span').click()

#
# class WorkToDo(BasePage):
#     '''
#     第二层：
#     - 页面元素进行分离，每个元素只定位一次，隔离定位，
#     如果页面改变，只需要改变相应的元素定位；
#     - 业务逻辑分离 或 操作元素动作分离
#     '''
#
#     # 我的待办定位 （定位分离）
#     def worktable_undo(self):
#         return self.by_xpath('//*[@id="new_worktable_nav"] //li[1]/a')
#
#     # 获取我的待办文本信息 （操作元素动作分离）
#     def worktable_undo_text(self):
#         return self.worktable_undo().text
#
# from openpyxl import load_workbook
#
# #
# def saveaccount(val, lin, han):
#     workbook = load_workbook(filename=r'E:\bos_cp_example\register_ex.xlsx')
#     data = workbook.active
#     cel = data['{}{}'.format(lin, han)]
# #     cel.value = val
# #     workbook.save(filename=r'E:\bos_cp_example\register_ex.xlsx')
#
# # def saveaccount01(val, lin, han):
# #     workbook = load_workbook(filename=r'E:\test\account_number.xlsx')
# #     sheet = workbook.active
# #     cel = sheet['{}{}'.format(lin, han)]
# #     cel.value = val
# #     workbook.save(filename=r'E:\test\account_number.xlsx')
# #
# # saveaccount01('5465','B',3)
#
# import random
# from selenium import webdriver
# import time
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.action_chains import ActionChains
# import random
#
# dr = webdriver.Chrome()
# dr.maximize_window()
# dr.implicitly_wait(20)
# dr.get('https://at-bos-frontend-uat.atfxdev.com/login')
#
# dr.find_element_by_css_selector('.ivu-icon-ios-arrow-down').click()
# time.sleep(1)
# dr.find_element_by_css_selector('ul.ivu-select-dropdown-list > li:nth-of-type(2)').click()
# time.sleep(1)
# dr.find_element_by_css_selector('[placeholder="账号"]').send_keys('tyler')
# dr.find_element_by_css_selector('[placeholder="密码"]').send_keys('Tl123456')
# dr.find_element_by_css_selector('button.ivu-btn-large > span').click()
# time.sleep(1)
# dr.find_element_by_css_selector('div[width="200"] li:nth-of-type(1) .ivu-badge > [data-v-8f6464e2]').click()
# time.sleep(1)
# dr.find_element_by_css_selector('div[width="200"] [href="/client/clientListNew/:type*"] > [data-v-5c5d5a98]').click()
# time.sleep(1)
# dr.find_element_by_css_selector('div.ivu-input-group-with-append > [placeholder]').send_keys(1000003863)
# time.sleep(1)
# dr.find_element_by_css_selector('button.ivu-btn-icon-only > .ivu-icon').click()
# time.sleep(1)
# dr.find_element_by_xpath('//a[.="1000003863"]').click()
# hadl = dr.window_handles
# # 切换窗口
# dr.switch_to.window(hadl[1])
# time.sleep(1)
# js_dowm = "var q=document.documentElement.scrollTop=10000"
# dr.execute_script(js_dowm)
# time.sleep(1)
# ib_code = dr.find_element_by_css_selector('.ivu-row-flex[data-v-70802fca] > div:nth-of-type(4) .item-text')
# ActionChains(dr).double_click(ib_code).perform()  # 双击
# time.sleep(1)
# ib_code.click()
# time.sleep(1)
# id_iuput=dr.find_element_by_css_selector('.ivu-input-small')
# id_iuput.send_keys(Keys.CONTROL,'a')
# time.sleep(1)
# id_iuput.clear()  # 清空
# id_iuput.send_keys(''.join(random.sample('ABCDEFGHIJKLMN', 6))+'TYLERIB')
# time.sleep(1)
# dr.find_element_by_css_selector('.ivu-icon-md-checkmark').click()
# ib_link=dr.find_element_by_css_selector('.ivu-row-flex[data-v-70802fca] > div:nth-of-type(5) .item-content')
# time.sleep(1)
# ActionChains(dr).double_click(ib_link).perform()  # 双击
# time.sleep(1)
# dr.find_element_by_css_selector('.ivu-select-multiple.ivu-select [placeholder="请选择"]').click()
# time.sleep(1)
# dr.find_element_by_css_selector('div.ivu-select-dropdown-transfer li:nth-of-type(3)').click()
# time.sleep(1)
# cli=dr.find_element_by_css_selector('.ivu-icon-md-checkmark')
# ActionChains(dr).double_click(cli).perform()
#
# js_top = "var q=document.documentElement.scrollTop=0"
# # 回到顶部
# dr.execute_script(js_top)
#
# # 初审处理中
# dr.find_element_by_css_selector('button.ivu-btn-default>span>span').click()
# time.sleep(1)
# # 成功初审
# dr.find_element_by_css_selector('div.application-wrap .ivu-dropdown-menu > li:nth-of-type(1)').click()
# # 选择组别
# dr.find_element_by_css_selector('form[data-v-04909214] div:nth-of-type(6) > '
#                                 'div:nth-of-type(1) > div:nth-of-type(1) > '
#                                 'div:nth-of-type(1) > div:nth-of-type(1) > '
#                                 'div:nth-of-type(1) > div:nth-of-type(1) > '
#                                 'input:nth-of-type(1)').click()
# time.sleep(1)
# # demoforex-atfx
# dr.find_element_by_css_selector('div.ivu-select-visible li:nth-of-type(7)').click()
# # 输入随机邮编
# dr.find_element_by_css_selector('form[data-v-04909214] div:nth-of-type(8) input:nth-of-type(1)').\
#     send_keys(''.join(random.sample('0123456789', 8)))
# time.sleep(1)
# # 确定
# dr.find_element_by_css_selector('.ivu-btn-primary[data-v-04909214] > span > span:nth-of-type(1)').click()
# time.sleep(2)
# # 获取交易账户
# js_dowmt = "var q=document.documentElement.scrollTop=10000"
# dr.execute_script(js_dowmt)  # 回到底部
# # 真实交易账信息
# dr.find_element_by_css_selector('div#tdAccount > .ivu-collapse-header').click()
# time.sleep(1)
# # 获取交易账户信息并写入本地文档
# for i in [1, 3, 4, 5]:
#     idmsg = dr.find_element_by_xpath('//*[@id="tdAccount"]/div[2]/div/'
#                                           'div/div[3]/div[1]/div[2]/table/tbody/tr/td[{}]/div/div/span'.format(i)).text
#     time.sleep(1)
#     if i == 1:
#         print(idmsg+'D')
#     elif i == 3:
#         print(idmsg+'E')
#     elif i == 4:
#         print(idmsg+'F')
#     else:
#         print(idmsg+'G')


# from selenium import webdriver
# import time
# time.sleep(1)
# dr=webdriver.Chrome()
# dr.implicitly_wait(20)
# dr.maximize_window()

# dr.get('https://at-client-portal-uat.atfxdev.com/register')
# dr.find_element_by_css_selector('.blk-sure-btn').click()
# time.sleep(1)
# dr.find_element_by_css_selector('.la-globe').click()
# time.sleep(1)
# dr.find_element_by_css_selector('ul.el-dropdown-menu > li:nth-of-type(2)').click()
# time.sleep(1)
# dr.find_element_by_css_selector('[placeholder="名字"]').send_keys('test')
# time.sleep(1)
# dr.find_element_by_css_selector('[placeholder="姓氏"]').send_keys('test')
# time.sleep(1)
# dr.find_element_by_css_selector('[placeholder="选择居住国家"]').click()
# time.sleep(1)
# dr.find_element_by_xpath('//span[.="智利"]').click()
# time.sleep(1)
# dr.find_element_by_css_selector('[placeholder="手机号码"]').send_keys('556451')
# time.sleep(1)
# dr.find_element_by_css_selector('[placeholder="电子信箱"]').send_keys('5565446451@qq.com')
# time.sleep(1)
# dr.find_element_by_css_selector('[placeholder="会员账户密码"]').send_keys('Tl44123456')
# time.sleep(1)
# dr.find_element_by_css_selector('[placeholder="验证码"]').send_keys('R0sLRl/E2wOcQ/lrejVuabwi9zOnoWCoLrV7yTduyEI=')
# dr.find_element_by_css_selector('.el-textarea__inner').send_keys('12356lkk')
# dr.find_element_by_css_selector('.el-form-item__content>button').click()
# time.sleep(1)

#
# def code_erro():
#     try:
#         code_erro = dr.find_element_by_css_selector('.el-message__content')
#         code_errotext = code_erro.text
#         print(code_errotext)
#         return True
#     except:
#         return False
# try:
#     t=dr.find_element_by_css_selector('div.el-message--error>p')
#     if t.is_displayed():
#         print(t.is_displayed())
#         print(t.text)
#         # text=dr.find_element_by_css_selector('div.el-message--error>p').text
#         print(12345)
#         # print(text)
#     else:
#         print(555)
# except:
#     print(2222)


# if code_erro():
#     print(222)
# else:
#     print(111)
# def form_erro():
#     try:
#         error=dr.find_element_by_css_selector('.el-form-item__error')
#         if error.is_displayed():
#             try:
#                 erro_list=dr.find_elements_by_css_selector('.el-form-item__error')
#                 for i in erro_list:
#                     print(i.text)
#             except:
#                 print(error.text)
#             return True
#         else:
#             print('字段填写无误')
#     except:
#         dr.find_element_by_css_selector('.el-form-item__content>button').click()
#         return False
#
# if form_erro():
#     dr.close()
# else:
#     time.sleep(1)
#     dr.find_element_by_css_selector('div.text-center .el-checkbox__inner').click()
#     time.sleep(1)
#     dr.find_element_by_css_selector('div.text-center>button.declar-checked').click()

# def is_error():
#     try:
#         dr.find_element_by_css_selector('.el-form-item__error')
#         return True
#     except:
#         return False
#
# def form_erro():
#     if is_error():
#         erro_list = dr.find_elements_by_css_selector('.el-form-item__error')
#         time.sleep(1)
#         print(1111222)
#         for i in erro_list:
#             print(i.text)
#         return True
#     else:
#         print('字段填写无误')#点击下一步
#         return False
#
# form_erro()
# print(is_error())







# def is_uk():
#     try:
#         uk_text = dr.find_element_by_css_selector('div.el-dialog__body>div.tips_body>div.p_10_0>p').text
#         if '不接受居住在这个国家的个人申请' in uk_text:
#             print('注册失败：{}'.format(uk_text))
#             return True
#         else:
#             pass
#     except:
#         return False
#
# if is_uk():
#     dr.close()
# else:
#     pass
import pytest

def test_a():
    print('-----test_a')
    assert 1
def test_b():
    print('-----test_b')
    assert 0

if __name__=='__main__':
    pytest.main()