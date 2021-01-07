from selenium.webdriver.support.wait import WebDriverWait


class basepage():
    """封装定位方法及操作"""
    def __init__(self,driver):
        self.dr=driver
        self.dr.maximize_window()
        self.dr.implicitly_wait(20)

    #封装css定位
    def css(self,css):
        return self.dr.find_element_by_css_selector(css)

    #封装显示等待定位
    def wcss(self, name):
        return WebDriverWait(self.dr, 10, 1).until(lambda x: x.find_element_by_css_selector(name))