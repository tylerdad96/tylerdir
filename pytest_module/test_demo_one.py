import pytest
import selenium


@pytest.fixture()
def yuzhi():
    print('先登录')


#TODO Tree hello world
def test_one(yuzhi):
    print('登录后操作')






if __name__=='__main__':
    pytest.main(['-s','./pytest_module/test_demo_one.py'])

