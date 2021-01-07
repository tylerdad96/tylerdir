# from time import *
# from random import *
# from copy import *
#
# #创建一个类，已便调用创建的变量
#
# #创建生成随机电话号码函数
# def phonenumber():
#     # 用split方法将随机time值转换成列表，并以.分隔
#     t=str(time()).split('.')
#     # 截取列表中的第一项
#     p=t.pop(0)
#     # 随机生成1位数以内的整数，拼接到列表中且转换成字符串类型
#     phnum=p+str(getrandbits(1))
#     return phnum
#
# #创建随机生成邮箱函数
#
# #调用上面的方法生成随机email不可用，应为两次输入的时间总有不一致的
# # def email():
# #     #创建一个列表，符合邮箱格式
# #     a=['@qq.com','@163.com','@sina.com','@io.com']
# #     #调用上面的生成电话号码的函数
# #     mailaddress=phonenumber()+str(choice(a))
# #     return mailaddress
#
# # #创建随机email
# # def emai():
# #     e=randrange(10)
#
#
# # #判断元素是否存在(css定位方法)
# def is_elememt_exist(css):
#     e=dr.find_elements_by_css_selector(css)
#     #唯一，'%s'%s2的用法相当于str{}.format()
#     if len(e)==1:
#         print('%s元素存在且唯一'%css)
#         return True
#     #不存在
#     elif len(e)==0:
#         print('不存在%s元素'%css)
#         return False
#     #存在多个
#     elif len(e)>1:
#         print('找到%s元素'%css+str(len(e))+'个')
#         return False



# def css(dr,element):
#     el=(dr).find_element_by_css_selector(element)
#     return el
#
# #封装显示等待定位方法,等待10s，每1s询问一次
# def wcss(self,name):
#     return WebDriverWait(self.dr,10,1).until(lambda x: x.find_element_by_css_selector(name))

from study import BasePage
from .worktable_to_do_page import WorkToDo


class LoginPage(BasePage):
    '''
    第二层：
    - 页面元素进行分离，每个元素只定位一次，
    隔离定位，如果页面改变，只需要改变相应的元素定位；
    每当页面发生变化的时候，只需要在用例中寻找变动的部分进行修改
    - 业务逻辑分离 或 操作元素动作分离
    注意：
    - 不要在page页面对象外做元素定位 ,
    - 不在page页面对象里面写断言，除非是页面是否成功加载断言
    - 需要多少个元素就定位多少个，不需要对整个页面的元素进行定位
    - 当你的用例设计页面跳转时，例如登陆操作，登陆完成后跳转首页，
    当页面发生“跳转”，封装的业务逻辑需要返回（return）对应的页面对象的实例
    '''

    # 登陆输入框定位（定位分离）
    def form_username(self):
        return self.by_xpath('//input[@id="username"]')

    # 密码输入框定位（定位分离）
    def form_password(self):
        return self.by_xpath('//input[@id="password_input"]')

    # 登陆按钮定位  （定位分离）
    def login_button(self):
        return self.by_xpath('//input[@id="tcloud_login_button"]')

    # 登陆错误信息定位
    def login_error_msg(self):
        return self.by_xpath('//span[@id="error-tips"]')

    # 登陆操作（业务逻辑分离）
    def login(self, username, password):
        # 输入账号
        self.form_username().send_keys(username)
        # 输入密码
        self.form_password().send_keys(password)
        # 点击登陆按钮
        self.login_button().click()
        # 当你的用例设计页面跳转时，例如登陆操作，登陆完成后跳转首页，
        # 当页面发生“跳转”，封装的业务逻辑需要返回（return）对应的页面对象的实例
        # 返回页面对象实例 （实现页面跳转）
        return WorkToDo(self.driver)


















