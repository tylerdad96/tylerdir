import pytest
import os
from selenium import webdriver

@pytest.fixture()
def testele():
    dr=webdriver.Chrome()
    return dr

def test1():
    url='https://www.cnblogs.com/gaidy/p/13176695.html'
    return url

def test2(testele,test1):
    dr.get(url)

if __name__=='__main__':
    pytest.main(['-q',os.path.abspath(__file__)])