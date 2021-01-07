import unittest
from BeautifulReport import BeautifulReport

if __name__=='__main__':
    #生成测试报告
    #注册
    suit=unittest.defaultTestLoader.discover(r'C:\Users\Tyler Tang\PycharmProjects\tylerdir\creat_accout\git_register_account',pattern='client_portal_register.py',top_level_dir=None)
    BeautifulReport(suit).report(filename='SL开IB',description='不同证件签发国注册账户',report_dir='all_case_report')
    #KYC认证
    suit=unittest.defaultTestLoader.discover(r'C:\Users\Tyler Tang\PycharmProjects\tylerdir\creat_accout\git_register_account',pattern='KYC_vfcation.py',top_level_dir=None)
    BeautifulReport(suit).report(filename='KYC验证测试报告',description='不同证件签发国KYC验证通过',report_dir='all_case_report')
    # # 初审通过
    suit=unittest.defaultTestLoader.discover(r'C:\Users\Tyler Tang\PycharmProjects\tylerdir\creat_accout\git_register_account',pattern='Preliminary_view.py',top_level_dir=None)
    BeautifulReport(suit).report(filename='ib_code修改等操作',description='用例执行情况',report_dir='all_case_report')
