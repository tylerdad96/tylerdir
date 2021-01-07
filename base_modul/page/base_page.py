from selenium.webdriver.support.wait import WebDriverWait

class basepage():
    """对selenium二次封装，定义一个所有脚本都继承的类，封装基本方法"""
    def __init__(self,driver,path=None):
        self.dr=driver
        self.dr.implicitly_wait(20)
        self.dr.maximize_window()
        #访问url
        self.log_page(path)

    #封装css定位
    def css(self,css):
        return self.dr.find_element_by_css_selector(css)

    #封装显示等待定位
    def wcss(self, name):
        return WebDriverWait(self.dr, 10, 1).until(lambda x: x.find_element_by_css_selector(name))

    def log_page(self,path1=None):
        if path1==None:
            pass
        else:
            self.dr.get(path1)