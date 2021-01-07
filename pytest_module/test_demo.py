import pytest

#函数式
def setup_function():
    print('每个用例前执行')

def teardown_function():
    print('每个测试用例后执行')

#模块级
def setup_module():
    print('整个.py文件只执行一次')
    print('例如打开浏览器')

def teardown_module():
    print('整个.py文件只执行一次')
    print('例如关闭浏览器')

def test_one():
    print('用例一')
    x='yhie'
    assert 'i' in x,'断言'

def test_two():
    print('用例二')
    x='hello'
    assert hasattr(x,'hello')

def test_three():
    print('用例三')
    assert 1<2

if __name__=='__main__':
    pytest.main(['-s','./pytest_module/test_demo.py'])