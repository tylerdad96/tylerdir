from selenium import webdriver
import time
import random

dr=webdriver.Chrome()
dr.maximize_window()
dr.get(r"http://demo.atdailytrain.com/lp/atfx_one/?utm_content=TYLER&utm_term=TYLER&utm_source=google0%14_deg")

def form_fill (t):
    while True:
        time.sleep(1)
        dr.find_element_by_css_selector('#form-field-name').send_keys('tyler-测试11050{}'.format(t))
        time.sleep(1)
        phone_list = [186, 136, 135]
        phone_num = str(random.choice(phone_list)) + ''.join(random.sample('0123456789', 8))
        dr.find_element_by_css_selector('#form-field-phone').send_keys(phone_num)
        time.sleep(1)
        dr.find_element_by_css_selector('#form-field-email').send_keys(phone_num + '@qq.com')
        time.sleep(1)
        dr.find_element_by_css_selector('button.elementor-button .elementor-button-text').click()
        time.sleep(2)
        if is_rok():
            dr.back()
            break
        else:
            dr.find_element_by_css_selector('#form-field-name').clear()
            time.sleep(1)
            dr.find_element_by_css_selector('#form-field-phone').clear()
            time.sleep(1)
            dr.find_element_by_css_selector('#form-field-email').clear()
            continue

def is_rok():
    try:
        dr.find_element_by_css_selector('div.demoacount_thanku>div>h2')
        return True
    except:
        return False

def much(t):
    a=1
    while a<=t:
        form_fill(a)
        a=a+1
    dr.close()
    dr.quit()

much(10)