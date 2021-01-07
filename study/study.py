# # # from selenium import webdriver
# # # d=webdriver.Chrome()
# # # d.get('http://www.baidu.com')
# # #'字符串'.format()方法
# # # '字符串{}'.format()用法
# # # from selenium import webdriver
# # # d=webdriver.Chrome()
# # # d.get('https://www.baidu.com/s?wd={}'.format(input('请输入')))
# #
# # # def san(a,b):
# # #     c=a**2+b**2
# # #     d=c**(1/2)
# # #     return('第三边长为'+str(d))
# # #
# # # print(san(6,4))
# #
# #
# # #含参函数
# # # def panduan(a,b,c):
# # #
# # #     if a+b>c and a+c>b and b+c>a:
# # #         print('可以组成三角形')
# # #     else:
# # #         print('不能组成三角形')
# # #
# # # panduan(1,2,3)
# # # # 不含参函数
# # # def uu():
# # #     a=input('请输入')
# # #     b=input('请输入')
# # #     c=int(a)+int(b)
# # #     return c
# # #
# # # print(uu())
# # # 时间转换函数
# # # def timechange(a):
# # #     b=60*a
# # #     c=a*1/600
# # #     return(str(b)+'毫秒等于'+str(a)+'秒'+'等于'+str(c)+'分钟')
# # #
# # # print(timechange(1000000))
# #
# #  # 梯形面积公式
# # # 位置参数与关键词参数
# #
# # # def mianji(base_up,base_down,height):
# # #     return 1/2*(base_up+base_down)*height
# # #
# # # print(mianji(1,2,3)) #位置参数
# # # print(mianji(height=3,base_down=2,base_up=1)) #关键词参数
# # #
# # # height=3
# # # base_up=2
# # # height=1
# # #
# # # print(mianji(height,base_up,height)) #位置参数
# # #
# # #
# # # 圣诞树
# # # print('   *','  * *',' * * *','* * * *','  -|-  ','   |',sep='\n') #sep=''插入，在打印的每个字符串间插入(\n)换行
# #
# # # 给参数设置默认值
# # # def  mianji(base_up, base_down, height=3):
# # #     return 1/2 * (base_up + base_down) * height
# # # print(mianji(1,2)) #默认参数height=3
# # # print(mianji(1,5,6)) #此时参数height=6
# #
# # # 用python写入数据到本地文件 open()方法及write()方法
# # # file=open(r'C:\Users\Tyler Tang\Desktop\text02.txt','w') #路径最后手打，复制的路径容易出错
# # # file.write('welcome,tyler01') #写入内容
# #
# # #设计一个创建文本并写入内容的函数
# # # def text_crert(name='hello',msg='hello'): #给参数默认值
# # #     fist_path='C:\\Users\\Tyler Tang\\Desktop\\'  #此处最好用\\符号代表路径，在路径前面加r和用\会报错
# # #     full_path=fist_path+name+'.txt'
# # #     file=open(full_path,'w')
# # #     file.write(msg)
# # #     file.close()
# # #     print('已创建')
# # #
# # # text_crert('tyler','你好，tyler，欢迎你回来')
# #
# # # def text(word,a_word='lame',b_word='awesome'):
# # #     return word.replace(a_word,b_word)
# # #
# # # print(text('python is lame'))
# # #
# # # #replace()方法
# # # str='anni is a girl,and her father is a enginner,her mather is a teacher,thier house is in city'
# # # print(str.replace('is','was',3)) #将is替换成was，替换次数不超过3次
# # # print(str.replace('is','was'))  #将所有的is替换成was
# #
# #
# # #设计一个创建文本且能过滤掉敏感信息的函数：需用到replace(),open()等方法
# # #先设计一个创建文本并写入内容的函数
# # # def creat_text(name,msg):
# # #     fist_path='C:\\Users\\Tyler Tang\\Desktop\\'
# # #     full_path=fist_path+name+'.txt' #创建文本
# # #     file=open(full_path,'w')
# # #     file.write(msg) #写入内容
# # #     print('done') #提示
# #
# # #再设计一能过滤敏感信息的函数
# # # def filter_msg(msg,a_msg='台湾',b_msg='中国台湾'):
# # #     return msg.replace(a_msg,b_msg)#过滤敏感信息，对输入的内容进行return
# # #     #return msg #这里仅仅是对输入的内容进行return
# # #
# # # #设计一个函数，调用上面的两个函数
# # # def lvy(name,msg):
# # #     msg2=filter_msg(msg,'台湾','台湾01') #调用替换字符串的函数
# # #     creat_text(name,msg2) #调用第一个函数，创建文本
# # #     print('done')
# # # lvy('台湾','台湾，简称台，是中华人民共和国省级行政厅，省会台北，位于中国大陆东南海域，东临太平洋，西隔台湾海峡与福建省相望，台湾省由中国第一大岛台湾岛和周围属岛以及澎湖列岛两大岛群，共80余个岛屿所组成，总面积3.6万平方公里。')
# #
# # # filter_msg('台湾')
# # #
# # # a=4**1/2
# # # print(a)
# #
# # # def strp(msg,a_msg='台湾',b_msg='中国台湾'):
# # #     file=msg.replace(a_msg,b_msg)
# # #     print(file)
# # # strp('武汉','武汉','中国武汉')
# # # from time import *
# # # t=str(time())
# # # t1=list(t)
# # # p=[]
# # # p=t1[0:10]
# # # phone=str(p)
# # # print(p)
# # #
# # # list=[1,2,3,4,5,6]
# # # from random import *
# # # print(choice(list))
# # # phone=randrange(0,10,)
# # # print(phone)
# # # import random
# # # j = 4
# # # id = []
# # # id = ''.join(str(i) for i in random.sample(range(0,9),j))    # sample(seq, n) 从序列seq中选择n个随机且独立的元素；
# # # print(id)
# # # from time import *
# # # def ph():
# # #     t=list(str(time()))[0:10]
# # #     phone='13'+str(t)
# # #     return phone
# # #
# # # print(ph())
# # #split()方法
# # # a='hello wold hi allen'
# # # print(a.split()) #打印列表a
# # # print(a)  #打印原始的变量a
# # #
# # # b='www.baidu.com.cn'
# # # print(b.split('.'))   #以.分割
# # # print(b.split('.',2)) #以.分割2次
# #
# #
# # #split()方法，将字符串转换成列表：
# # # a='hello word,i am tyler,a enngnier,work in guangdong shenzhen nanshan,i love monkey and prity girl'
# # # b=a.split() #默认以空格分隔
# # # print(b)
# # # c=a.split(',')  #以,分隔
# # # print(c)
# # #
# # #join()方法，列表、元祖、字典等进行操作，并且转换成字符串类型的数据
# # # a=['1','2']
# # # b=''.join(a) #将空字符加入a列表中
# # # print(b)
# # # print(''.join(a))
# #
# # # from time import *
# # # from random import *
# # # print(str(time()))
# # # t=str(time()).split('.')
# # # print(t)
# # # ph=t.pop(0)
# # # print(ph)
# # # print(getrandbits(1))
# # # phonenum=ph+str(getrandbits(1))
# # # print(phonenum)
# #
# #
# #
# # # from random import *
# # # while 1>0:
# # #     a=randrange(0,100001)
# # #     print(a)
# # #     if len(str(a))>5:
# # #         break
# #
# #
# #
# # # t2=''.join(t)
# # # print(t2)
# #
# # #创建一个随机生成电话号码的函数，用到random模块，time模块，pop方法，split方法
# # # from random import *
# # # from time import *
# # # def phonenumber():
# # #     t=str(time()).split('.') #用split方法将随机time值转换成列表，并以.分隔
# # #     p=t.pop(0) #截取列表中的第一项
# # #     phnum=p+str(getrandbits(1)) #随机生成1位数以内的整数，拼接到列表中且转换成字符串类型
# # #     return phnum
# # #
# # #
# # # print(phonenumber())
# # #
# # # #join方法
# # # a='helle,word'
# # # b=','.join(a)
# # # print(b)
# # # print(type(b))
# # #
# # #
# # # def han1():
# # #     a=randrange(10)
# # #     return a
# # #
# # # def han2():
# # #     a=5
# # #     return a
# # #
# # # print(han1())
# # # print(han2())
# #
# # #在一个类中使用同变量
# # # class A():
# # #     def test_a(self):
# # #         self.m = "hello"
# # #
# # #     def test_b(self):
# # #         self.test_a()
# # #         n = self.m + "world"
# # #         print(n)
# # #
# # # A().test_b()
# # # # if __name__ == '__main__':
# # # #     A().test_b()
# #
# # # from public import *
# # # from selenium import webdriver
# # # from time import *
# # # from random import *
# # # from selenium.webdriver.common.keys import Keys
# # #
# # # dr=webdriver.Chrome()
# # # dr.maximize_window()
# # # # dr.get('https://apply-gm.atfx.com/')
# # #
# # # sex=dr.find_elements_by_css_selector('.el-radio__label')
# # # choice(sex[0:2]).click()
# # # sleep(2)
# # # p=dr.find_elements_by_css_selector('.el-input__inner')
# # # sleep(2)
# # # while mailad().emailone()==mailad().emailtwo():
# # # p[4].send_keys(email())
# # # sleep(3)
# # # p[4].send_keys(Keys.CONTROL,'a')
# # # sleep(2)
# # # p[4].send_keys(Keys.CONTROL,'c')
# # # sleep(3)
# # # p[5].send_keys(Keys.CONTROL,'v')
# #
# #
# # #随机生成电话号码
# # # from random import *
# # # for i in range(8):
# # #     e=choice('012345678')
# #
# # # from random import *
# # #from random import *
# # # def Create_num():
# # #   list = ['139','138','137','136','135','134','159','158','157','150','151','152','188','187','182','183','184','178','130','131','132','156','155','186','185','176','133','153','189','180','181','177']
# # #   str = '0123456789'
# # #   for i in range(2):
# # #     print(random.choice(list) + "".join(random.choice(str) for i in range(8)))
# # # Create_num()
# #
# # # str='0123456789'
# # # b=(choice(str) for i in range(8))
# #
# #
# # # for i in range(8):
# # #     for i in range(1):
# # #         a1=choice(str)
# # #         a2=choice(str)
# # #         p=a1+a2
# # #         print(p)
# #
# # # print('.'.join(choice(str) for i in range(5)))
# # # print(''.join(for i in range(5)))
# # # b=(choice(str) for i in range(5))
# # # c=(for i in range(5))
# #
# # # def login():
# # #     password=input('Password:')
# # #     if password == '123456':
# # #         print('login success')
# # #     else:
# # #         print('Wrong password')
# # #
# # # login()
# #
# # #创建一个秘密登录程序，可修改密码：
# # #创建一个列表，用于存储用户密码：
# # # pswlist=['*#*#','123456']
# # # def account_login():
# # #     #输入密码
# # #     password=(input('Password:'))
# # #     #添加判断
# # #     if password==pswlist[-1]:
# # #         print('login success')
# # #     #修改密码：
# # #     elif password==(pswlist[0]):
# # #         replacepswd=input('pls input your new password:')
# # #         #将新密码添加到密码列表中储存
# # #         pswlist.append(replacepswd)
# # #         print(pswlist)
# # #     else:
# # #         print('wrong password')
# #
# #
# # # times=3
# # # while times>0:
# # #     account_login()
# # #     times=times-1
# # # for i in 'hello word':
# # #     print(i)
# # #
# # #
# # # class mi():
# # #     def op(self):
# # #         print('nihao')
# # #
# # #
# # # w=mi()
# # # print(w)
# # # list=['hello']
# # #for i in list:#hello是一个整体
# # #     print(i)
# # #for i in list[0]:#hello中每一个元素是一个整体
# # #     print(i)
# # #
# # #
# # # import wmi
# # # import win32con
# # #
# # # w=wmi.WMI()
# # # cpu_list=w.Win32_Processor()
# # # print(cpu_list)
# # # print(list)
# # # for i in cpu_list:
# # #     print(i)
# # #
# # # for i in list:
# # #     print(i)
# # #
# # # print(8/2)
# # # import os
# # # while True:
# # #     fname=input('enter filename>')
# # #     if os.path.exists(fname):
# # #         print("Error:'%s' already exists"%fname)
# # #     else:
# # #         break
# # # fobj=open(fname,'a',encoding='utf-8')
# #
# # # import os
# # # # # f=input('filename')
# # # # # f=open(f,'a',encoding='utf-8')
# # # # print(os.path.isdir('E:\123')
# # # print(os.path.exists('PC基础配置信息.py'))
# #
# # # import socket
# # # name=socket.gethostname()
# # # ip=socket.gethostbyname(name)
# # # print(ip)
# # # print(name)
# #
# # #for循环
# # #简单的递加
# # # for i in range(1,11):
# # #     print(str(i)+'+1='+str(i+1))
# #
# # #小程序
# # # list=['apple','banner','watermaner']
# # # for i in list:
# # #     if i=='apple': #此处用==。表示完全等于
# # #         print('name:苹果')
# # #     elif i=='banner':
# # #         print('name:香蕉')
# # #     else:
# # #         print('name:西瓜')
# #
# # #format方法:string{}.format()将format()括号中的字符串添加到{}中
# # # print('{}是{}'.format(input(),input()))
# #
# # #嵌套循环
# # # for i in range(1,10):
# # #     for y in range(1,10):
# # #         # print('{}*{}={}'.format(i,y,i*y))
# # #         print(str(i)+'*'+str(y)+'='+str(i*y))
# #
# # #while循环
# #
# # # def login():
# # #     password_list = ['**##', '123456']
# # #     times=0
# # #     while times<3:
# # #         ps=input('请输入密码')
# # #         if  ps==password_list[0]:
# # #             print('输入您想设置的密码')
# # #             ps1=input()
# # #             print('添加成功')
# # #             password_list.append(ps1)
# # #         elif ps==password_list[-1]:
# # #             print('输入正确')
# # #             print(password_list)
# # #             break
# # #         else:
# # #             print('密码输入错误')
# # #         times=times+1
# # #     else:
# # #         print('机会用完了')
# # # login()
# #
# # #open(file,mode,encoding='utf-8')mode='w'时打开文件，没有该文件则创建文件
# # #import os
# # #os.path.exists(filepath)判断文件是否存在（其实跟判断是否存在改路径一样）
# #
# #
# # #在桌面创建10个txt文本
# # # import os
# # # def creatfile():
# # #     path='C:\\Users\\Tyler Tang\\Desktop\\test\\'
# # #     if os.path.exists('C:\\Users\\Tyler Tang\\Desktop\\test'): #只要创建了test文件，if后面就返回true
# # #         for i in range(1,11):
# # #             open(path+str(i)+'.txt','w')#文件路径也是字符串，字符串str(i)拼接生成i.txt文件
# # #         print('allredy done')
# # #     else:
# # #         os.mkdir('C:\\Users\\Tyler Tang\\Desktop\\test')
# # #         for i in range(1,11):
# # #             open(path+str(i)+'.txt','w')
# # #         print('done')
# # #
# # # creatfile()
# #
# # #打印1-100内的偶数
# # # for i in range(1,101):
# # #     if i%2==0:
# # #         print(i)
# # #     else:
# # #         pass
# # # print(random.randrange(1,7))
# #
# # #编程小游戏，猜大小：
# # #摇3次骰子，并计算三次骰子的大小，如果18<=和<=11为大，10<=和<=3为小，猜大小
# # # import random
# # # def game():
# # #     times=0
# # #     n_list=[]
# # #     #循环3次，获得3个骰子数
# # #     while times<3:
# # #         n=random.randrange(1,7)
# # #         n_list.append(n)
# # #         times=times+1
# # #
# # #     answer=sum(n_list)#三个骰子数相加
# # #     #定义三个骰子数和的大小
# # #     if 11<=answer<=18:
# # #         result='大'
# # #     elif 3<=answer<=11:
# # #         result='小'
# # #
# # #     money = input('您想压多少钱？注：赔率为1:1')
# # #     while True:
# # #         try:
# # #             money = float(money)  # 程序不出错的情况下的正常操作
# # #             break
# # #         except:  # 程序报错后执行如下代码
# # #             money = input('请输入正确的金额(数字):')
# # #
# # #     print('您此次投注为' + str(money) + '元')#告诉客户投注多少钱
# # #
# # #     while True:#添加while循环判断用户输入的是否为大或者小
# # #         request = input('您押大还是小')
# # #         if request in ['大','小']:
# # #             if request==result:#对比猜的是大还是小，符不符合上面函数定义的大小
# # #                 print('您猜对了,三个数分别是'+str(n_list))
# # #                 print('此次您赢得了'+str(money)+'元')
# # #                 money=2*money
# # #                 print('您的余额为'+str(money)+'元')
# # #             else:
# # #                 print('您猜错了,三个数分别是'+str(n_list))
# # #                 print('很遗憾，此次您输掉了'+str(money)+'元')
# # #             break
# # #         else:
# # #             print('请输入大或者小')
# # # game()
# #
# # #创建一个判断用户手机号输入的程序
# # # def phnum():
# # #     CN_mobile = \
# # #         [134, 135, 136, 137, 138, 139, 150, 151, 152, 157, 158, 159, 182, 183, 184,
# # #          187, 188, 147, 178, 1705]
# # #     CN_union = [130, 131, 132, 155, 156, 185, 186, 145, 176, 1709]
# # #     CN_telecom = [133, 153, 180, 181, 189, 177, 1700]
# # #
# # #     ph = input('请输入您的电话号码1')
# # #     while True:
# # #         try:
# # #             ph=int(ph) #程序未报错下的正常操作
# # #
# # #         except: #程序报错后执行下面的代码
# # #             ph=input('请输入数字')
# # #
# # #             continue #此continue，终止此次循环，继续下次循环
# # #
# # #         #首先判断输入位数是否正确
# # #         ph=str(ph)
# # #
# # #
# # #         if len(ph)==11:
# # #             #判断是那个号段的号码
# # #             if int(ph[0:3])in CN_mobile or int(ph[0:4]) in CN_mobile:
# # #                 print('您输入的是移动号码，验证码稍后发送，请注意查收')
# # #                 break
# # #             elif int(ph[0:3]) in CN_union or int(ph[0:4]) in CN_union:
# # #                 print('您输入的是联通号码，验证码稍后发送，请注意查收')
# # #                 break
# # #             elif int(ph[0:3]) in CN_telecom or int(ph[0:4]) in CN_telecom:
# # #                 print('您输入的是电信号码，验证码稍后发送，请注意查收')
# # #
# # #         elif len(ph)<11:
# # #             #此处输入的数据类型为字符串，后面在判断是哪个好号段的号码时需要进行数据类型的转换
# # #             ph = input('请输入11位有效电话号码2')
# # #         #输入位数正确的情况下：
# # #
# # #         elif len(ph)>11:
# # #             ph = input('请输入11位有效电话号码3')
# # #
# # #
# # # phnum()
# #
# # # list.insert(0,'water') #数字表示新插入的数据在列表中的第几项（下标），如果列表没有那么长，则插入在列表的最后一项
# # # print(list)
# # # list[0:0]=['banner'] #这种方法也可以插入数据，插入在列表的第一项
# # # print(list)
# #
# # # list=['apple','pear','banner']
# # # # # list.remove('apple')#点名删除哪个值
# # # # # print(list)
# # # # # del list[0:1] #关键字声明，删除第一项
# # # # # print(list)
# # #  list.insert(6,'water')
# # # print(list)
# #
# #
# # # dictonery={'bd':'baidu','sn':'sina','dy':'douyu'}
# # # dictonery['yk']='youku'
# # # print(dictonery)
# # # dictonery.update({'hy':'huya','tx':'tencent'})
# # # print(dictonery)
# # # del dictonery['tx']
# # # print(dictonery)
# # # print(len(dictonery))
# #
# # # a=[1,3,2,4,5,9,6]
# # # #sorted()函数，按照长短，大小，英文字母顺序给列表排序
# # # print(sorted(a))
# # # b=sorted(a,reverse=True)
# # # print(b)
# # # print(a)
# #
# # # import time
# # #列表的推导式
# # # t1=time.time()
# # # a=[i for i in range(1,2001)]
# # # print(sorted(a,reverse=True))
# # # b=[]
# # # for i in range(1,20001):
# # #     b.append(i)
# # # t2=time.time()
# # #
# # # print(t2-t1)
# # #例：
# # # a=[i**2 for i in range(1,10)]
# # # print(a)
# # # b=[i for i in range(1,21) if i%2==0]
# # # print(b)
# #
# # #zip()用法
# # # for i,j in zip(range(1,6),'abc'):
# # #     print(i,j)
# #
# # #enumerate()函数用于将一个可遍历的数据对象(如列表、元组或字符串)组合为一个索引序列，同时列出数据和数据下标，一般用在 for 循环当中
# # # a=[i for i in 'abvdefg']
# # # print(a)
# # # #用于for循环中列出列表中的数据及其下标
# # # for i,y in enumerate(a,start=1):
# # #     print(y+'位置：'+str(i))
# #
# # #类，是有一些系列有共同特征和行为事物的抽象概念的总和
# # # class cocacola():
# # #     formula=['caffeine','suga','water','soda'] #类里面赋值的变量，就是类的变量，也叫类的属性
# # #     def __init__(self,logo): #__init__()方法自动执行，除了self参数，类中的参数会传递到这个方法中
# # #         self.local='可口可乐'
# # #         self.local_name=logo
# # #         # for i in self.formula:
# # #         #     print('colo is made by {}'.format(i))
# # #     def drink(self):
# # #         print('energy')
# # #
# # # cocacola('kele')
# #
# #
# #
# # # cocacola().en='cola'
# # # a=cocacola() #类的实例化
# # # a.en='cola' #类的实例属性
# #
# #
# #     # def __init__(self): #__init__()方法可以新增类的实例属性,且自动执行
# #     #     self.local_logo='可口可乐'
# #     #     self.en_logo='cola'
# #     # def drink(self):
# #     #     print('energy')
# #
# # # a=cocacola()  #类的实例化
# # # print(a.local_logo)
# # # print(cocacola().en_logo)
# #
# #
# #     # def drink(self,how_much): #类里面创建的函数，也叫类的方法
# #     #     if how_much=='a sip':
# #     #         print('cool')
# #     #     else:
# #     #         print('headache')
# #
# #
# # # print(cocacola.local2)
# #
# #
# #
# # # cocacola().drink()
# # # print(a.formula)#类属性的引用
# # # print(cocacola.formula)
# #
# # # a.local='可口可乐'  #称为实例的属性
# #
# # # cocacola.local2='百事可乐'
# # # print(a.local)
# #
# # #selenium自动化
# # #导包
# # # from selenium import webdriver
# # # import time
# # #
# # # T1=time.time()
# # # #设置全局变量
# # # dr=webdriver.Chrome()
# # # #最大化窗口
# # # dr.maximize_window()
# # # #访问
# # # #dr.get('https://www.atfx.com/gm/en/')
# # # dr.get('https://www.chinese-atfx.com/')
# # # #休眠2s
# # # #time.sleep(2)
# # # #刷新页面
# # # #dr.refresh()
# # # #time.sleep(2)
# # # #返回上一页
# # # #dr.back()
# # # #sleep(1)
# # # #切换下一页
# # # #dr.forward()
# # # #设置窗口大小
# # # #dr.set_window_size(540,960)
# # # #time.sleep(1)
# # # #截屏
# # # #dr.get_screenshot_as_file('E:\\test\\p1.png')
# # # #定位到开户按钮，点击
# # # dr.find_element_by_css_selector('#menu-item-15').click()
# # # time.sleep(10)
# # #
# # #
# # # #关闭当前窗口
# # # # dr.close()
# # # #退出浏览器进程
# # # # dr.quit()
# # # #
# # # # T2=time.time()
# # # # T=int(T2-T1)
# # # # #打印用时
# # # # print('用时'+str(T)+'秒')
# #
# # # #导包
# # # from selenium import webdriver
# # # import time
# # #
# # #
# # # #设置全局变量
# # # dr=webdriver.Chrome()
# # # #最大化窗口
# # # dr.maximize_window()
# # # dr.get('https://www.chinese-atfx.com/')
# # # time.sleep(2)
# # # dr.find_element_by_css_selector('#menu-item-15').click()
# # # sleep(2)
# # # dr.find_element_by_css_selector('div.el-input>input[type="text"]')
# #
# # #导包
# # from selenium import webdriver
# # import time
# # import os
# # import random
# # #导入键盘模块
# # from selenium.webdriver.common.keys import Keys
# # #鼠标悬停事件模块
# # from selenium.webdriver.common.action_chains import ActionChains
# # #导入select模块
# # from selenium.webdriver.support.select import Select
# # import re
# # from selenium.webdriver.support.wait import WebDriverWait
# # from public import is_elememt_exist
# # from selenium.webdriver.support import expected_conditions as EC
# # import unittest
# #
# # # #设置全局变量
# # # dr=webdriver.Chrome()
# # # #最大化窗口
# # # dr.maximize_window()
# # # #设置隐式等待时间
# # # dr.implicitly_wait(10)
# #
# # #访问百度首页
# # # dr.get('https://www.baidu.com/')
# # # time.sleep(1)
# # # #输入关键字，查询
# # # dr.find_element_by_css_selector('span.s_ipt_wr>input[name="wd"]').send_keys('测试部落')
# # # time.sleep(2)
# # # #点击查询
# # # # dr.find_element_by_css_selector('span.s_btn_wr>input[type="submit"]').click()
# # # #模拟回车键
# # # dr.find_element_by_css_selector('span.s_btn_wr>input[type="submit"]').submit()
# # # sleep(2)
# # # #定位一组元素
# # # s=dr.find_elements_by_css_selector('h3.t>a')
# # # #获取这组元素中的href值
# # # # for i in s:
# # # #     a=i.get_attribute('href')
# # # #     print(a)
# # #
# # # #获取这组元素中的一个随机href值：
# # # a=s[random.randint(0,9)].get_attribute('href')
# # # print(a)
# # # #随机访问url。相当于接口测试
# # # #dr.get(a)
# # # #随机点击一个地址，模拟用户的点击操作
# # # s[random.randint(0,9)].click()
# #
# # # h=dr.window_handles
# # # time.sleep(2)
# # # dr.find_element_by_css_selector('form.navbar-form>div>input[name="q"]').send_keys('selenium')
# # # time.sleep(2)
# # # #模拟回车键操作
# # # #dr.find_element_by_css_selector('form.navbar-form>div>input[name="q"]').submit()
# # # dr.find_element_by_css_selector('form.navbar-form>div>input[name="q"]').send_keys(Keys.ENTER)
# # #定位到设置按钮
# # # ele=dr.find_element_by_css_selector('div#u1>span[name="tj_settingicon"]')
# # # #鼠标悬停在设置按钮上
# # # ActionChains(dr).move_to_element(ele).perform()
# # # #然后随机点击其中一项
# # # a=dr.find_elements_by_css_selector('div.s-top-userset-menu>div.s-user-setting-pfmenu>a')
# # # a[random.randint(0,3)].click()
# # # dr.find_element_by_link_text('房产').click()
# # # #获取当前窗口句柄
# # # h1=dr.current_window_handle
# # # print(h1)
# # # all_h=dr.window_handles
# # # print(all_h)
# # # time.sleep(3)
# # #切换窗口，方法一
# # #dr.switch_to.window(all_h[0])
# # #切换窗口，方法二,循环判断当前句柄是否为首页，不等于就切换
# # # for i in all_h:
# # #     if i!=all_h[0]:
# # #         dr.switch_to.window(all_h[0])
# # #         print(dr.title) #打印当前页面title
# # #     else:
# # #         pass
# # # dr.close()
# # # dr.switch_to.window(h)
# #
# # # dr.get('http://bj.ganji.com/')
# # # h=dr.current_window_handle
# # # print(dr.title)
# # # print(h)
# # # time.sleep(3)
# # # dr.find_element_by_link_text('房产').click()
# # #
# # # h1=dr.window_handles
# # # time.sleep(3)
# # # # dr.switch_to.window(h1[1])
# # # print(dr.title)
# #
# # # dr.get('http://bj.ganji.com/')
# # # dr.find_element_by_link_text('房产').click()#点击房产
# # # time.sleep(3)
# # # dr.find_element_by_link_text('二手物品').click()#点击二手物品
# # # time.sleep(3)
# # # h=dr.current_window_handle #获取当前页面（url为http://bj.ganji.com/）的句柄及title
# # # print(h)
# # # print(dr.title)
# # # h2=dr.window_handles #获取所有句柄
# # # print(h2)
# # # dr.switch_to.window(h2[2]) #将脚本切换到第三个页面，此时浏览器展示的为第三个页面，获取当前页面的title
# # # print(dr.title)
# # # time.sleep(1)
# # # dr.close()#关闭当前页
# # # #回到第一个页面，首页
# # # # dr.switch_to.window(h[0])
# # # # print(h)
# # # #判断此时页面句柄是否为首页句柄，如是，则不切换，如不是，则切换到首页，并展示首页
# # # for i in h2:
# # #     if i!=h2[0]:
# # #         dr.switch_to.window(h2[0])
# # #         print(dr.title)
# # #     else:
# # #         pass
# #
# # # dr.get('https://mail.163.com/')
# # # time.sleep(2)
# # # #定位到iframe表单页
# # # a=dr.find_element_by_css_selector('div#loginDiv>iframe')
# # # #切换到iframe表单
# # # dr.switch_to.frame(a)
# # # #输入邮箱
# # # dr.find_element_by_css_selector('div.u-input>input[name="email"]').send_keys('bmj268')
# # # time.sleep(2)
# # # #输入密码
# # # dr.find_element_by_css_selector('div.u-input>input[name="password"]').send_keys('TL0440934335..')
# # # time.sleep(2)
# # # #点击十天内免登陆
# # # dr.find_element_by_css_selector('div.b-unlogn>label[for="un-login"]').click()
# # # #点击登录
# # # dr.find_element_by_css_selector('div.f-cb>a.u-loginbtn').click()
# # # #释放iframe，回到主页面
# # # dr.switch_to.default_content()
# #
# # # #鼠标悬浮到设置
# # # el=dr.find_element_by_css_selector('div#u1>span.s-top-right-text')
# # # ActionChains(dr).move_to_element(el).perform()
# # # time.sleep(2)
# # # #点击高级搜索
# # # dr.find_element_by_link_text('高级搜索').click()
# # # time.sleep(2)
# # # #定位页面两个select框
# # # se=dr.find_elements_by_css_selector('div.c-select-selection>i.c-select-arrow')
# # # #点击时间框
# # # se[0].click()
# # # time.sleep(2)
# # # tm=dr.find_elements_by_css_selector('div.c-select-dropdown-list>p[data-for="gpc"]')
# # # #随机点击一个时间框中的一个选项,randint函数包括上限
# # # tm[random.randint(0,4)].click()
# # # time.sleep(2)
# # # #点击文档格式框
# # # se[1].click()
# # # time.sleep(2)
# # # sty=dr.find_element_by_css_selector('div.c-select-dropdown-list>p[data-for="ft"]')
# # # Select(sty).select_by_index(2)
# #
# # # dr.get('file:///C:/Users/Tyler%20Tang/Desktop/tyler.html')
# # # # time.sleep(2)
# # # # #点击alert弹窗
# # # # dr.find_element_by_css_selector('button[onclick="myFunctionAlert()"]').click()
# # # # t=dr.switch_to.alert
# # # # #打印警告框文本
# # # # print(t.text)
# # # # #点击警告框确认按钮
# # # # t.accept()
# # # # #点击取消按钮,相当于点击X按钮
# # # # #t.dismiss()
# # # # #点击confirm弹窗
# # # # dr.find_element_by_css_selector('button[onclick="myFunctionConfirm()"]').click()
# # # # time.sleep(2)
# # # # c=dr.switch_to.alert
# # # # #打印弹窗文本
# # # # print(c.text)
# # # # #点击取消按钮
# # # # c.dismiss()
# # # # #点击确认按钮
# # # # #c.accept()
# # #
# # # #点击prompt弹窗
# # # dr.find_element_by_css_selector('button[onclick="myFunctionPrompt()"]').click()
# # # p=dr.switch_to.alert
# # # #向弹窗中输入内容
# # # p.send_keys('hello')
# # # time.sleep(2)
# # # #打印弹窗文本
# # # print(p.text)
# # # #点击确认按钮
# # # p.accept()
# # # #点击取消按钮
# # # #p.dismiss()
# #
# # # dr.get('file:///C:/Users/Tyler%20Tang/Desktop/chekc.html')
# # # #滚动条拉到底部
# # # js='var q=document.documentElement.scrollTop=10000'
# # # dr.execute_script(js)
# # # time.sleep(2)
# # # #滚动条拉到顶部
# # # js1='var q=document.documentElement.scrollTop=0'
# # # dr.execute_script(js1)
# # # time.sleep(2)
# # # #拉动滚动条
# # # js2='var q=document.documentElement.scrollTop=3500'
# # # dr.execute_script(js2)
# # # time.sleep(2)
# # # #横向滚动，x为横向距离，y为纵向距离
# # # js3='window.scrollTo(1000,4500)'
# # # dr.execute_script(js3)
# # # #获取网页可视区高,即滚动条的高度
# # # js4= "var q=document.body.clientHeight;return(q)"
# # # h=dr.execute_script(js4)
# # # print(h)
# # # #获取网页可视区宽，即横向滚动条的宽度
# # # js5 = "var q=document.body.clientWidth;return(q)"
# # # w=dr.execute_script(js5)
# # # print(w)
# # #元素聚焦
# # # a=dr.find_element_by_css_selector('div.elementor-element-d889c47 .elementor-button-text')
# # # dr.execute_script("arguments[0].scrollIntoView();", a)
# # # time.sleep(2)
# # # dr.find_element_by_css_selector('#boy').click()
# # # time.sleep(3)
# # # dr.find_element_by_css_selector('#girl').click()
# # # time.sleep(3)
# # # c=dr.find_elements_by_css_selector('input[type="checkbox"]')
# # # #点击选中复选框
# # # for i in c:
# # #     if i in (c[0],c[2]):
# # #         i.click()
# # #         time.sleep(2)
# # #     else:
# # #         pass
# # # #判断所有复选框是否选中
# # # for y in c:
# # #     n=y.is_selected()
# # #     print(n)
# #
# # #打开jira登录页
# # # dr.get('https://id.atlassian.com/login')
# # # time.sleep(2)
# # # #输入用户名
# # # dr.find_element_by_css_selector('#username').send_keys('tyler.tang@newtype.io')
# # # time.sleep(1)
# # # #点击继续
# # # dr.find_element_by_css_selector('button#login-submit>span.css-1vqao0l>span.css-t5emrf').click()
# # # time.sleep(1)
# # # #输入密码
# # # dr.find_element_by_css_selector('.Input__InputElement-sc-1o6bj35-0').send_keys('TL961013..')
# # # time.sleep(1)
# # # #点击登录
# # # dr.find_element_by_css_selector('span.css-1vqao0l>span.css-t5emrf').click()
# # # time.sleep(6)
# # # #点击jira项目
# # # dr.find_element_by_css_selector('div.sc-EHOje>span.sc-bdVaJa').click()
# # # time.sleep(2)
# # # #点击创建
# # # dr.find_element_by_css_selector('#createGlobalItem').click()
# # # time.sleep(1)
# # # #描述文本框中输入内容
# # # dr.find_element_by_css_selector('.mentionable').send_keys('hello')
# # # time.sleep(2)
# # # #点击取消,页面出现弹窗警告
# # # dr.find_element_by_css_selector('div.buttons>a.cancel').click()
# # # #切换至警告框
# # # a=dr.switch_to.alert
# # # time.sleep(3)
# # # #点击警告框确定按钮
# # # a.accept()
# # # time.sleep(2)
# # # #点击个人资料
# # # dr.find_element_by_css_selector('.sc-giadOv').click()
# # # p=dr.find_elements_by_css_selector('.ItemParts__Content-sc-14xek3m-5')
# # # p[4].click()
# # # time.sleep(5)
# # # #截取当前屏幕
# # # dr.get_screenshot_as_file('E:\\test\\p1.png')
# #
# # # dr.get('https://www.12306.cn/index/')
# # # #去掉readonly属性
# # # js='document.getElementById("train_date").removeAttribute("readonly")'
# # # dr.execute_script(js)
# # # #定位日期
# # # # e=dr.find_element_by_css_selector('#train_date')
# # # # #全选
# # # # e.send_keys(Keys.CONTROL,'a')
# # # # time.sleep(3)
# # # # #输入新的值
# # # # e.send_keys('123')
# # # #通过js清空输入框
# # # js = 'document.querySelector("#train_date").value=""'
# # # dr.execute_script(js1)
# # #
# # # # ActionChains(dr).double_click(e).perform()
# # #
# # # # e.clear()
# # # # time.sleep(2)
# # # # #输入
# # # # dr.find_element_by_css_selector('#train_date').send_keys('2020-05-28')
# #
# # # dr.get('file:///C:/Users/Tyler%20Tang/Desktop/neiqian.html')
# # # time.sleep(2)
# # #竖向滚动到底部
# # # js = "var q=document.getElementById('yoyoketang').scrollTop=10000"
# # # dr.execute_script(js)
# # # time.sleep(3)
# # # #竖向滚动到顶部
# # # js1 = "var q=document.getElementById('yoyoketang').scrollTop=0"
# # # dr.execute_script(js1)
# # # time.sleep(2)
# # # #横向滚动到最右侧
# # # js2 = "var q=document.getElementById('yoyoketang').scrollLeft=10000"
# # # dr.execute_script(js2)
# # # time.sleep(2)
# # # #横向滚动到最左侧
# # # js3 = "var q=document.getElementById('yoyoketang').scrollLeft=0"
# # # dr.execute_script(js3)
# # #横竖滚动
# # # js3 = "var q=document.getElementById('yoyoketang').scrollLeft=(100,10000)"
# # # dr.execute_script(js3)
# #
# # # dr.get('https://www.atfx.com/gm/ko/expected-dividends-cfd-shares/')
# # # time.sleep(2)
# # # #打印页面列表内容
# # # t=dr.find_elements_by_css_selector('tr.row-2>td')
# # # #for循环打印列表中这一行的内容
# # # for i in t:
# # #     print(i.text,end=' ') #不换行显示
# # #     time.sleep(1)
# #
# # # dr.get('https://www.baidu.com/')
# # # time.sleep(2)
# # # #删除target属性
# # # js='document.getElementsByClassName("mnav")[0].removeAttribute("target")'
# # # #修改target属性的值为空
# # # # js='document.getElementsByClassName("mnav")[0].target=""'
# # # dr.execute_script(js)
# # # e=dr.find_elements_by_css_selector('.mnav')
# # # e[0].click()
# #
# # # from selenium import webdriver
# # # from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
# # # import time, os.path
# # # import grid_module
# # #
# # # for host, browser in grid_module.grid().items():
# # #     driver = webdriver.Remote(
# # #         command_executor=host,
# # #         desired_capabilities={
# # #             'platform': 'ANY',
# # #             'browserName': browser,
# # #             'version': '',
# # #             'javascriptEnabled': True
# # #         }
# # #     )
# # #     driver.get("http://www.baidu.com")
# # #     driver.find_element_by_id("kw").send_keys(u"中国")
# # #     driver.find_element_by_id("su").click()
# # #     time.sleep(3)
# # #     if driver.title == u"中国_百度搜索":
# # #         print("title匹配！")
# # #     else:
# # #         print("title不匹配！")
# # #     driver.close()
# #
# # # dr.get('https://www.baidu.com/')
# # # #点击‘相机’按钮
# # # dr.find_element_by_css_selector('span.quickdelete-wrap>span.soutu-btn').click()
# # # time.sleep(2)
# # # #send_keys()方法上传本地文件
# # # dr.find_element_by_css_selector('.upload-pic').click()
# # # time.sleep(2)
# # #dr.find_element_by_css_selector('.upload-pic').click()
# # # os.system(r'‪E:\test\test.exe')
# #
# # # dr.get('https://apply-gm.atfx.com/')
# # # time.sleep(2)
# # # a=dr.find_elements_by_css_selector('.el-input__inner')
# # # a[0].send_keys('test')
# # # time.sleep(2)
# # # a[3].send_keys('123456')
# # # time.sleep(2)
# # # a[4].send_keys('990687322@qq.com')
# # # time.sleep(2)
# # # a[5].send_keys('990687322@qq.com')
# # # time.sleep(2)
# # # b=dr.find_elements_by_css_selector('.el-radio__inner')
# # # time.sleep(2)
# # # b[1].click()
# # # dr.find_element_by_css_selector('.btn-default').click()
# # # time.sleep(2)
# # # dr.find_element_by_css_selector('.upload-btn').click()
# # # time.sleep(2)
# # # #上传图片
# # # os.system(r'E:\test\test.exe')
# #
# # # dr.get('https://www.baidu.com/')
# # # dr.find_element_by_css_selector('input#kw').send_keys('selenium')
# # # time.sleep(2)
# # # #定位联想词
# # # b=dr.find_elements_by_css_selector('div.bdsug-new>ul>li.bdsug-overflow')
# # # #打印联想词
# # # for i in b:
# # #     print(i.get_attribute('data-key'))
# # #     time.sleep(1)
# # #
# # # #随机点击联想词访问，并做判断
# # # if len(b)>1:
# # #     b[random.randint(1,4)].click()
# # #     time.sleep(2)
# # #     print(dr.title)
# # # else:
# # #     print('未获取到联想词')
# #
# # # dr.get('http://www.keedu.cn/school?schid=624')
# # # #改变display属性，使页面元素不显示，应用于页面的自定义弹窗
# # # js='document.getElementById("edu-nav-bottom-r-more").style.display="online";'
# # # dr.execute_script(js)
# #
# # # dr.get('https://www.baidu.com/')
# # # #获取页面title
# # # t=dr.title
# # # print(t)
# # # #获取元素文本
# # # w=dr.find_elements_by_css_selector('.title-content-title')
# # # for i in w:
# # #     print(i.text)
# # #     time.sleep(1)
# # # #获取标签名
# # # s=dr.find_element_by_css_selector('.s_ipt').tag_name
# # # print(s)
# # # #获取元素的其他属性
# # # y=dr.find_element_by_css_selector('.s_ipt').get_attribute('autocomplete')
# # # print(y)
# #
# # # #判断元素是否存在(css定位方法)
# # # def is_elememt_exist(css):
# # #     e=dr.find_elements_by_css_selector(css)
# # #     #唯一，'%s'%s2的用法相当于str{}.format()
# # #     if len(e)==1:
# # #         print('%s元素存在且唯一'%css)
# # #         return True
# # #     #不存在
# # #     elif len(e)==0:
# # #         print('不存在%s元素'%css)
# # #         return False
# # #     #存在多个
# # #     elif len(e)>1:
# # #         print('找到%s元素'%css+str(len(e))+'个')
# # #         return False
# # #
# # # #调用函数，如果存在且唯一，则填写数据
# # # if is_elememt_exist('form.el-form > .row > div:nth-of-type(1) .el-input__inner'):
# # #     dr.find_element_by_css_selector('form.el-form > .row > div:nth-of-type(1) .el-input__inner').send_keys('tyler')
# # # #判断input标签是否存在
# # # is_elememt_exist('input')
# #
# # # def exist(css):
# # #     try:
# # #         dr.find_element_by_css_selector(css)
# # #         return True
# # #         print(1)
# # #     except:
# # #         return False
# # #
# # # exist('xxx')
# #
# # # try:
# # #     a=float(input('输入数字'))
# # #     print(1)
# # # except:
# # #     print(2)
# # # page=dr.page_source
# # # print(page)
# #
# # #匿名函数lambda，相当于def，比def简单
# # # a=lambda x,y:x+y
# # # print(a(1,2))
# # #
# # # def a(x,y):
# # #     return x+y
# #
# # # dr.get('https://www.baidu.com/')
# # # WebDriverWait(dr,10).until(lambda x:x.find_element_by_id('kw')).send_keys('dd')
# # #
# # # a=lambda x:x.find_element_by_id('kw')
# #
# # # a=dr.find_element_by_css_selector('#kw').is_displayed()
# # # print(a)
# #
# # # dr.get('https://www.baidu.com/')
# # # time.sleep(1)
# # # #点击登录
# # # dr.find_element_by_css_selector('.s-top-login-btn').click()
# # # time.sleep(1)
# # # #点击qq登录
# # # dr.find_element_by_css_selector('.phoenix-btn-item').click()
# # # #获取所有句柄
# # # h=dr.window_handles
# # # print(h)
# # # #获取当前窗口句柄
# # # h2=dr.current_window_handle
# # # print(h2)
# # # print(dr.title)
# # # #判断当前页面的句柄，是否为百度页句柄，如是，则跳转
# # # for i in h:
# # #     if i==h2:
# # #         dr.switch_to.window(h[1])
# # #         print(dr.title)
# # #     else:
# # #         pass
# # # time.sleep(1)
# # # #切换iframe
# # # a=dr.find_element_by_css_selector('div.lay_login_form>iframe')
# # # dr.switch_to.frame(a)
# # # time.sleep(2)
# # # #点击十六
# # # dr.find_element_by_css_selector('#img_out_990687322').click()
# # # #返回原先的句柄页面，即百度页面
# # # for i in h:
# # #     if i==h2:
# # #         dr.switch_to.window(h[0])
# # #         print(dr.title)
# # #     else:
# # #         pass
# # # time.sleep(2)
# # # #获取页面cookie
# # # print(dr.get_cookies())
# # # time.sleep(2)
# # # e=EC.alert_is_present()
# # # print(e(dr))
# #
# #
# # #绕过验证码登录
# # # dr.get('https://account.cnblogs.com/signin')
# # # #将登录成功后的cookie值写成字典的类型，name,value
# # # c1={'name':'_gat','value':'1'}
# # # c2={'name':'.CNBlogsCookie','value':'4DC37B9C35B693B4E8241D4EE0716DC69976A02511AF28D6C2AAAA744BCD05EFAA033EF7CFC677A2C4A6192FD11CBAAE6B6F38AF445624250982131A84FA4BA0B8AEAC02B22C3BC69E73E2BBDBD88138FEC47FE1'}
# # # c3={'name':'__gads','value':'ID=c58770ae796f489d:T=1590559453:S=ALNI_MYAA4OMa5p_0-QveIEkEfnvc8Tn3g'}
# # # c4={'name':'.Cnblogs.AspNetCore.Cookies','value':'CfDJ8B9DwO68dQFBg9xIizKsC6Tib5hfr48Mr65rw7zO8pleLkXulEQ9kKB3cVyprv5xpnLElyWKxDO9PDMtanOKhU_wba7GP1jpxM_FONxd_-5PbQUCTAHdz76H30R_X7E4Feg4NYzOR4cVKLBKeEDBGPNrka9ozTmyDOl_hAQ87T5lBTAHYPcjqeUoouC-PzQ7oAvJw2g5LoTaf0NYZva-mBx81JXEaipzKV62EM3BCh6xSr8BhZAuYXXm1DYnLws96C-IxiNQJuNJoHRpvPtu8cX-a7faJtzPRZ6vGT2Ti5uJqXiP9M7QYOP_6GNqLB26D80OrHVA_A0j3J96B2Ql0woqHz2BZn8x5vb8p3KyBZDmyWZi7aCq7yWyC4mggTqpSRw1JmHQClumD8U4N_yLCppcKuLvKRryi-9-DhlNAM98uVRFIWJGb8M8TeC3oxhMAeAjjF3v08bveBOY-H8MT5tyKqFyYAxisQQbEiVhVOqb_--K11NPFpsnGy2GD7fMCxhtqIItqpFjlhubr-P-wSIhP_0pyvFzAs2-zN4aRDgV8GZA5fe9r9GjmYOr7W4Fmw'}
# # # c5={'name':'_gid','value':'GA1.2.15798645.1590559445'}
# # # c6={'name':'_ga','value':'GA1.2.1413485520.1590559445'}
# # # #添加cookie值
# # # dr.add_cookie(c1)
# # # dr.add_cookie(c2)
# # # dr.add_cookie(c3)
# # # dr.add_cookie(c4)
# # # dr.add_cookie(c5)
# # # dr.add_cookie(c6)
# # # time.sleep(3)
# # # #刷新页面
# # # dr.refresh()
# # # dr.find_element_by_css_selector('.btn-primary').click()
# #
# # # dr.get('https://www.baidu.com/')
# # # from selenium.webdriver.support import expected_conditions as EC
# # # time.sleep(2)
# # # #点击登录
# # # dr.find_element_by_css_selector('.s-top-login-btn').click()
# # # time.sleep(1)
# # # #点击qq登录，模拟用户操作
# # # dr.find_element_by_css_selector('.phoenix-btn-item').click()
# # # time.sleep(1)
# # # #清除原有cookie
# # # dr.delete_cookie('pplogid')
# # # dr.delete_cookie('mkey')
# # # dr.delete_cookie('H_PS_PSSID')
# # # dr.delete_cookie('PSTM')
# # # dr.delete_cookie('BIDUPSID')
# # # dr.delete_cookie('BAIDUID')
# # # #将登录后的cookie写成字典类型
# # # c={'name':'pplogid','value':'357IHy4ezlvZ1U0dPVBbK9EnKLsaZDGfCEnI2qPD%2BHhKfRW6tMIeWWiipnZwGZNHl6rQAeS4upIbw8SnqbNC7bIFw%3D%3D'}
# # # c1={'name':'PTOKEN','value':'e4d04f87665d7d642e8380ccb0706f8a'}
# # # c2={'name':'mkey','value':'d16cf27180fbf95c6d59b3f16004613cbc06993a0a45b0ddf2'}
# # # c3={'name':'H_PS_PSSID','value':'31728_1446_21081_31590_30825_31606_31463_30823'}
# # # c4={'name':'BDUSS','value':'GpKc0ZadzdIVkFBUFJYaTZ0LWMyOWlsNWQzdlgwcUxxS1ZTdk5WYWY4Z35yUFplSUFBQUFBJCQAAAAAAAAAAAEAAABTdNF-wM~Lvrv6tPi0-M7SxMcAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAD8fz14~H89eO'}
# # # c5={'name':'STOKEN','value':'b847ad0f6607faff08b019946b3d0c78fbc29561dc56c43b0dfbb3e3c0f482c3'}
# # # c6={'name':'PSTM','value':'1590632249'}
# # # c7={'name':'BIDUPSID','value':'D3590D91F1302898784A2BC3F6F79B12'}
# # # c8={'name':'BAIDUID','value':'F70857EFC45FC89F7C060EFA543B1192:FG=1'}
# # # #插入cookie
# # # dr.add_cookie(c)
# # # dr.add_cookie(c1)
# # # dr.add_cookie(c2)
# # # dr.add_cookie(c3)
# # # dr.add_cookie(c4)
# # # dr.add_cookie(c5)
# # # dr.add_cookie(c6)
# # # dr.add_cookie(c7)
# # # dr.add_cookie(c8)
# # # time.sleep(3)
# # # # #刷新
# # # # dr.refresh()
# #
# # # #判断title
# # # from selenium.webdriver.support import expected_conditions as EC
# # # # dr.get('https://www.baidu.com/')
# # # # a=EC.title_is('百度一下，你就知道')
# # # # print(a(dr))
# # # # b=EC.title_contains('百度')
# # # # print(b(dr))
# # # #判断弹窗
# # # dr.get('https://www.baidu.com/')
# # # #定位设置按钮
# # # e=dr.find_element_by_css_selector('div#u1>span.s-top-right-text')
# # # #鼠标悬浮到设置按钮
# # # ActionChains(dr).move_to_element(e).perform()
# # # time.sleep(2)
# # # #定位悬浮后的搜索设置
# # # d=dr.find_elements_by_css_selector('div.s-user-setting-pfmenu>a')
# # # d[0].click()
# # # time.sleep(1)
# # # #点击恢复默认
# # # dr.find_element_by_css_selector('div#se-setting-7>a.prefpanelrestore').click()
# # # #判断弹窗是否出现
# # # r=EC.alert_is_present()
# # # print(r(dr)) #此处不是放true，而是返回alart这个对象
# # # if r(dr):
# # #     #如果弹窗出现
# # #     p=dr.switch_to.alert
# # #     print(p.text) #打印弹窗文本
# # #     p.accept() #点击弹窗上的接受按钮
# # # else:
# # #     print('alart未弹出')
# #
# # # from selenium.webdriver.common.by import By
# # #
# # # class blog(unittest.TestCase):
# # #     #进入登录页面
# # #     def setUp(self):
# # #         url='https://www.baidu.com/'
# # #         dr.get(url)
# # #         time.sleep(2)
# # #         #点击登录
# # #         dr.find_element_by_css_selector('.s-top-login-btn').click()
# # #         time.sleep(1)
# # #         #点击账户密码登录
# # #         dr.find_element_by_css_selector('.tang-pass-footerBarULogin').click()
# # #         time.sleep(1)
# # #
# # #     #创建登录方法
# # #     def login(self,username,psword):
# # #         #输入用户名
# # #         dr.find_element_by_css_selector('#TANGRAM__PSP_11__userName').send_keys(username)
# # #         time.sleep(2)
# # #         #输入密码
# # #         dr.find_element_by_css_selector('#TANGRAM__PSP_11__password').send_keys(psword)
# # #         time.sleep(2)
# # #         #点击登录
# # #         dr.find_element_by_css_selector('#TANGRAM__PSP_11__submit').click()
# # #      #调用登录方法，编写测试用例，用例必须用test开头
# # #     def test_logsuccess(self):
# # #         self.login('18696194961','TL123456..')
# # #         #获取登录后的文本
# # #         self.text=dr.find_element_by_css_selector('.user-name').text
# # #         print(self.text)
# # #         #断言实际结果,此时是登录成功后的断言
# # #         self.assertEqual(self.text,'老司机带带我那')
# # #     #优化断言方法
# # #     def is_login_sucess(self):
# # #         try:#登录不成功的话是定位不到这个元素的
# # #             self.text = dr.find_element_by_css_selector('.user-name').text
# # #             return True
# # #         except:
# # #             return False
# # #
# # #     def test_log_fail01(self):
# # #         self.login('18696194961','tildjdjijg')
# # #         time.sleep(2)
# # #         result=self.is_login_sucess()
# # #         print(result)
# #
# # # if __name__ == '__main__':
# # #     unittest.main()
# #
# # #登录方法参数化
# # # dr.get('https://www.baidu.com/')
# # # dr.find_element('css selector','#kw').send_keys(123)
# #
# # import unittest
# # # print(help(unittest))
# # # class IntegerArithmeticTestCase(unittest.TestCase):
# # #     def testAdd(self):  # test method names begin with 'test'
# # #         self.assertEqual((1 + 2), 3)
# # #         self.assertEqual(0 + 1, 1)
# # #
# # #     def testMultiply(self):
# # #         self.assertEqual((0 * 10), 0)
# # #         self.assertEqual((5 * 8), 40)
# # # if __name__ == '__main__':
# # #     unittest.main()
# # # class Test(unittest.TestCase):
# # #     def setUp(self): #前置条件
# # #         pass
# # #     def tearDown(self): #后置条件
# # #         pass
# # #
# # #     def test_jianfa(self):
# # #         '''测试减法'''
# # #         result=6-5
# # #         hope=1
# # #         self.assertEqual(result,hope)
# # #     def test_chufa(self):
# # #         '''测试除法'''
# # #         result=7/2
# # #         hope=3.5
# # #         self.assertEqual(result,hope)
# # #
# # # if __name__ == '__main__':
# # #     unittest.main()
# #
# # #一个简单的测试用例
# # # class blog(unittest.TestCase):
# # #     #预置条件，访问博客园主页
# # #     def setUp(self):
# # #         dr.get('https://home.cnblogs.com/u/testyler')
# # #         time.sleep(1)
# # #     #后置条件
# # #     def tearDown(self):
# # #         time.sleep(3)
# # #         dr.close()
# # #         dr.quit()
# # #
# # #     def test_blog(self):
# # #         r=EC.title_contains('我想要程序媛的主页')
# # #         print(r(dr))
# # #         self.assertTrue(r(dr)) #断言用例是否通过
# # #
# # # if __name__ == '__main__':
# # #     unittest.main()
# # #import HTMLTestRunner
# #
# # #unittest用例执行顺序
# # # class Test(unittest.TestCase):
# # #     def setUp(self): #在每个用例之前执行
# # #         print('预置条件')
# # #         pass
# # #     def tearDown(self): #在每个用例之后执行
# # #         print('环境恢复')
# # #         pass
# # #     def test3(self):
# # #         time.sleep(1)
# # #         print('用例3')
# # #     def test1(self):
# # #         time.sleep(1)
# # #         print('用例1')
# # #     def testB(self):
# # #         time.sleep(1)
# # #         print('用例B')
# # #     def testa(self):
# # #         time.sleep(1)
# # #         print('用例a')
# # #     def testA(self):
# # #         time.sleep(1)
# # #         print('用例A')
# # #     def testA01(self):
# # #         time.sleep(1)
# # #         print('用例A01')
# # #
# # # if __name__ == '__main__':
# # #     #unittest.main() #检验测试用例是否能执行
# # #     test=unittest.TestSuite()
# # #     test.addTest(Test('testA01'))
# # #     file_path=r'C:\Users\Tyler Tang\PycharmProjects\tyler\study\result.html'
# # #     fp=open(file_path,'wb')
# # #     runner=HTMLTestRunne.HTMLTestRunner(stream=file_path,title='test',description='yongli')
# # #     runner.run(test)
# # #     fp.close()
# #
# # # #运行单个测试脚本并生成测试报告
# # # from selenium import webdriver
# # # import unittest
# # # import HTMLTestRunner
# # # import os
# # # import time
# # #
# # # #创建一个类，继承unittest模块中的TestCaseL类
# # # class Test(unittest.TestCase):
# # #     #预置条件
# # #     def setUp(self):
# # #         self.dr=webdriver.Chrome()
# # #         self.dr.maximize_window() #最大化窗口
# # #         self.dr.implicitly_wait(10) #隐式等待10s
# # #         self.dr.get('https://www.baidu.com/')
# # #         time.sleep(3)
# # #     #环境恢复
# # #     def tearDown(self):
# # #         time.sleep(2)
# # #         self.dr.close()
# # #         self.dr.quit()
# # #     #封装输入点击搜索方法
# # #     def serch(self,keywrod):
# # #         self.dr.find_element_by_css_selector('#kw').send_keys(keywrod)
# # #         time.sleep(2)
# # #         self.dr.find_element_by_css_selector('#su').click()
# # #     def test_01(self):
# # #         #调用函数
# # #         self.serch('selenium')
# # #         time.sleep(2)
# # #     def test_02(self):
# # #         self.serch('python')
# # #         time.sleep(2)
# # #
# # # if __name__=='__main__':
# # #     # unittest.main() 执行所有测试用例
# # #     testsuit=unittest.TestSuite() #构造测试套件
# # #     #testsuit.addTests(map(Test,['test_01','test_02'])) #添加多个测试用例
# # #     testsuit.addTest(Test('test_01')) #添加单个测试用例
# # #
# # #     report_path=os.path.join(os.getcwd(),'report.html') #定义测试报告路径 os.getcwd()获取文件所在路径
# # #     fp=open(report_path,'wb') #以二进制模式打开当前当前路径下的html报告，如果没有，则创建
# # #     runner=HTMLTestRunner.HTMLTestRunner(stream=fp,title='自动化测试报告',description='用例执行情况')
# # #     runner.run(testsuit)
# # #     fp.close() #关闭报告文件
# #
# # #查找所有未done掉的ticket
# # # from selenium import webdriver
# # # import time
# # # from selenium.webdriver.common.keys import Keys
# # #
# # # class search():
# # #     '''查找所有未done掉的ticket'''
# # #     dr=webdriver.Chrome()
# # #     dr.maximize_window()
# # #     dr.implicitly_wait(60)
# # #     #登录
# # #     def login(self,username,password):
# # #         self.dr.get('https://id.atlassian.com/login')
# # #         time.sleep(2)
# # #         #输入用户名
# # #         self.dr.find_element_by_css_selector('.Input__InputElement-sc-1o6bj35-0').send_keys(username)
# # #         time.sleep(2)
# # #         #点击继续
# # #         self.dr.find_element_by_css_selector('span.css-1vqao0l>span.css-t5emrf').click()
# # #         time.sleep(1)
# # #         #输入密码
# # #         self.dr.find_element_by_css_selector('#password').send_keys(password)
# # #         time.sleep(2)
# # #         #回车登录
# # #         self.dr.find_element_by_css_selector('#password').send_keys(Keys.ENTER)
# # #
# # #     #点击自己的项目
# # #     def project(self,method,keyword):
# # #         #参数化登录方法
# # #         self.dr.find_element(method,keyword).click()
# # #         time.sleep(1)
# # #         #点击事物和过滤器
# # #         self.dr.find_element_by_link_text('事务和过滤器').click()
# # #         time.sleep(2)
# # #         #点击由我报告
# # #         self.dr.find_element_by_link_text('由我报告').click()
# # #         time.sleep(2)
# # #     #点击高级搜索，
# # #     def notdone(self):
# # #         self.dr.find_element_by_link_text('高级搜索').click()
# # #         time.sleep(2)
# # #         e=self.dr.find_elements_by_css_selector('.criteria-wrap')
# # #         time.sleep(1)
# # #         #点击状态
# # #         e[2].click()
# # #         time.sleep(2)
# # #         #点击待办
# # #         a=self.dr.find_elements_by_css_selector('.check-list-item')
# # #         a[-1].click()
# # #         time.sleep(2)
# # #     #打印代办的bug
# # #     def done(self):
# # #         #定位到未处理的ticket列表
# # #         t=self.dr.find_elements_by_css_selector('ol.issue-list>li')
# # #         time.sleep(1)
# # #         for i in t:
# # #             #打印title元素
# # #             print(i.get_attribute('title'+''),end='')
# # #             time.sleep(1)
# # #             #打印ticket
# # #             print(i.get_attribute('data-key'),end='\n')
# # #
# # #
# # # search().login('tyler.tang@newtype.io','TL961013..')
# # # search().project('css selector','.sc-bRBYWo')
# # # search().notdone()
# # # search().done()
# #
# # # import unittest
# # # import time
# # #
# # # class Test(unittest.TestCase):
# # #     # def setUp(self): #在每个用例之前执行
# # #     #     print('预置条件')
# # #     #     pass
# # #     # def tearDown(self): #在每个用例之后执行
# # #     #     print('环境恢复')
# # #     #     pass
# # #     @classmethod
# # #     def setUpClass(cls) :
# # #         print('预置条件')
# # #     @classmethod
# # #     def tearDownClass(cls):
# # #         print('环境恢复')
# # #     def test3(self):
# # #         time.sleep(1)
# # #         print('用例3')
# # #     def test1(self):
# # #         time.sleep(1)
# # #         print('用例1')
# # #     def testB(self):
# # #         time.sleep(1)
# # #         print('用例B')
# # #     def testA(self):
# # #         time.sleep(1)
# # #         print('用例A')
# # #     def testA01(self):
# # #         time.sleep(1)
# # #         print('用例A01')
# # #
# # # if __name__ == '__main__':
# # #     unittest.main()
# #
# # #断言
# #
# import unittest
# import time
#
# class test(unittest.TestSuite):
#     @classmethod
#     def setUpClass(cls):
#         print('start')
#     @classmethod
#     def tearDownClass(cls):
#         print('end')
#     def test01(self):
#         a=1
#         b=2
#         self.assertEqual(a, b)
#     def test02(self):
#         a='123'
#         b='123456'
#         assertIn(a,b)
#
#
# if __name__ == '__main__':
#     unittest.main()

# coding:utf-8

# import unittest
# class Test(unittest.TestCase):
#     @classmethod
#     def setUpClass(cls):
#         print('start')
#     @classmethod
#     def tearDownClass(cls):
#         print('end')
#
#     def test01(self):
#         a=1
#         b=1
#         self.assertEqual(a,b)
#     def test02(self):
#         a='你好'
#         b='你好，tyler'
#         self.assertIn(a,b)
#     def test03(self):
#         a=1<2
#         self.assertTrue(a)
#     def test04(self):
#         a='tyler'
#         b='hello'
#         #自定义异常
#         self.assertEqual(a,b,msg='%s!=%s'%(a,b))
#
#
# if __name__=='__main__':
#     unittest.main()

# from selenium import webdriver
# from selenium.common.exceptions import NoSuchElementException
# dr=webdriver.Chrome()
# dr.maximize_window()
# dr.get('https://www.baidu.com/')
# try:#正常操作
#     dr.find_element_by_css_selector('.s-top-right**').click()
# except NoSuchElementException as msg: #异常后的操作
#     print('程序异常%s'%msg)
# # else:#若无异常下的操作
# #     e.click()

#读取exlce表格内容

# import xlrd #导入xlrd模块
#
# #打开表格
# data=xlrd.open_workbook(r'E:\dir\test.xlsx')
#
# table=data.sheets()[0] #通过索引打开对应的sheet表,此时为en表
# table2=data.sheet_by_index(1) #通过索引打开对应的sheet表，此时为cn表
# table3=data.sheet_by_name('en+cn') #通过sheet名来打开对应的表
#
# rows=table.nrows #获取总行数
# cols=table.ncols #获取总列数
#
# print(table.row_values(2)) #获取en表第二行的值
# print(table2.col_values(1)) #获取cn表第二列的数据


#封装函数
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
#     #print(e.dict_data())
# #获取测试数据，包含多个字典的list类型数据
# testdata=e.dict_data()
#
# @ddt.ddt
# class blog(unittest.TestCase):
#     def setUp(self):
#         self.dr=webdriver.Chrome()
#         self.dr.maximize_window()
#         self.dr.implicitly_wait(10)
#         #进入注册页面
#         self.dr.get('https://cn.eddidbullion.com/lp/mt4-download/')
#     #注册方法
#     def login(self,name,phonenum,email):
#         #用户名
#         self.dr.find_element_by_css_selector('#sf_last_name').send_keys(name)
#         time.sleep(1)
#         #电话
#         self.dr.find_element_by_css_selector('#sf_phone').send_keys(phonenum)
#         time.sleep(1)
#         #邮箱
#         self.dr.find_element_by_css_selector('#sf_email').send_keys(email)
#         #点击下载
#         self.dr.find_element_by_css_selector('div.w2lsubmit>input[type="submit"]').click()
#         time.sleep(2)
#     #判断注册是否成功
#     def is_login_sucess(self):
#         try: #注册成功后获取文本
#             self.t=self.dr.find_element_by_css_selector('div#mt4_confirmtext>h2').text
#             print(self.t)
#             return True
#         except Exception as msg:#注册失败返回false,并记录异常原因
#             print('登录失败')
#             print('异常原因{}'.format(msg))
#             nowtime=time.strftime('%Y%m%d.%H%M%S')
#             t=self.dr.get_screenshot_as_file(r'E:\test\{}.png'.format(nowtime)) #获取异常后的截图,截图成功，返回True，失败返回False
#             print('截图结果为{}'.format(t))
#             return False
#
#     #测试数据驱动
#     @ddt.data(*testdata)
#     def test_login(self,data):
#         print('当前测试数据{}'.format(data))
#         #列表中的每一个字典依次当做测试用例的数据，调用注册方法
#         self.login(data['name'],data['phonenum'],data['email'])
#         #调用判断
#         result=self.is_login_sucess()
#         self.assertTrue(result)
#
#     def tearDown(self):
#         self.dr.close()
#         self.dr.quit()
#
# if __name__=='__main__':
#     unittest.main()
#
# # if __name__=='__main__':
# #     e=exceldata()
# #     e.openexcel(r'E:\dir\test.xlsx','en')
# #     print(e.dict_data())
#
# # import ddt
# # import unittest
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
#     unittest.main()

# from selenium import webdriver
#
# import time
#
# dr=webdriver.Firefox()
# dr.implicitly_wait(30)
#
# dr.get('https://www.atfx.com/gm/en/quarterly-market-outlook-thank-you/')
# time.sleep(2)
# while 1>0:
#     send_keys(Keys.TAB)

# d={'username':'tyler','password':'123456'}
# d['skall']='python'
# print(d)
# print(d.items())
# for i,y in d.items():
#     print('key is {}'.format(i))
#     print('valus is {}'.format(y))
# l=[('username','tyler'),('password','123456'),('post','super')]
# for i,y in l:
#     print(i)
#     print(y)

# class A(object):
#     def __init__(self,a,b):
#         try:
#             self.a=int(a)
#             self.b=int(b)
#         except:
#             print('参数错误')
#
#     def add(self):
#         self.c=self.a+self.b
#         return self.c
#
# class B(A):
#     def sub(self):
#         self.d=self.a-self.b
#         return self.d
#
# num=A(6,6)
# print(num.add())
#
# print(B(7,5).add())
# print(B(7,5).sub())
# try:
#     print(1+'l')
# except BaseException as msg:
#     print(msg)
# finally:
#     print('无论有无异常，均执行')

# from selenium import webdriver
# import time
#
# dr=webdriver.Chrome()
# dr.maximize_window()
# dr.get('https://www.chinese-atfx.com/')
# time.sleep(6)
# dr.find_element_by_css_selector('div.close>span').click()
# print(dr.title)
# print(dr.current_url)

# from search_all_notdone import search
#
# if __name__=='__main__':
#     s=search()
#     s.login()
#     s.project()
#     s.notdone()
#     s.done()

# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC

# dr=webdriver.Chrome()
# dr.get('https://www.baidu.com/')
#
# e=WebDriverWait(dr,5,0.5).until(EC.invisibility_of_element((By.ID,'kw')))
# e.sned_keys('123')
# from selenium import webdriver
# dr=webdriver.Chrome()
# dr.maximize_window()
# dr.get('https://mail.126.com/')
# e=dr.find_element_by_css_selector('iframe[id^="x-URS-iframe"]')
# dr.switch_to.frame(e)
# dr.find_element_by_css_selector('.j-inputtext').send_keys('123456')
# from selenium import webdriver
# class DriverUtil():
#     def get_driver(self):
#         self.driver = webdriver.Chrome()
#         self.driver.maximize_window()
#         self.driver.get('https://uat.atfx.com/gm/en/quarterly-market-outlook/')
#         # return self.driver

#下载文件，Firefox：
# from selenium import webdriver
# import os,time

# #通过FirefoxProfile()进行下载设置
# fp=webdriver.FirefoxProfile()
# fp.set_preference('browser.download.folderList',0) #设置成0代表下载到浏览器默认的下载路径
# fp.set_preference('browser.download.manager.showhenStarting',False) #是否显示开始，True显示开始，False不显示开始
# fp.set_preference('browser.download.dir',os.getcwd()) #用于指定所下载文件的目录
# fp.set_preference('broser.helperApps.neverAsk.saveToDisk','binary/octet-stream') #下载文件类型
#
# dr=webdriver.Firefox(firefox_profile=fp)
# dr.get('https://pypi.org/project/selenium/#files')
# f=dr.find_elements_by_css_selector('th[scope="row"]>a')
# f[1].click()
# time.sleep(30)
#
# dr=webdriver.Chrome()
# dr.set_window_size(600,800)
# dr.get('https://www.baidu.com/')
#
# js='document.documentElement.scrollTop=10000'
# js1='document.documentElement.scrollLeft=1000'
# dr.execute_script(js1)

# dr.add_cookie({'name':'tyler','value':'tyler0111'})
# c=dr.get_cookies()
# print(dr.get_cookies())
# for i in dr.get_cookies():
#     print('$s-->$s'%(c['name'],c['value']))
#
# from selenium import webdriver
# import time
#
# # dr=webdriver.Chrome()
# # dr.set_window_size(600,800)
# # dr.get('https://www.baidu.com/')
# # time.sleep(2)
# # dr.find_element_by_css_selector('#kw').send_keys('selenium')
# # time.sleep(2)
# # dr.find_element_by_css_selector('#kw').submit()
# # time.sleep(3)
# # js='document.documentElement.scrollTop=10000'
# # js1='document.documentElement.scrollLeft=1000'
# #
# # dr.execute_script(js)
# # time.sleep(3)
# # dr.execute_script(js1)
# # time.sleep(3)
# # js3='window.scrollTo(100,500)'
# # dr.execute_script(js3)
# # import time
# # from selenium import webdriver
# #
# # dr=webdriver.Chrome()
# # dr.get('https://videojs.com/')
# #
# # vedio=dr.find_element_by_css_selector('#vjs_video_3_html5_api')
# # url=dr.execute_script('return arguments[0].currentSrc;',vedio)
# # print(url)
#
# from selenium import webdriver
# import time
# from PIL import Image
# import random
#
# dr=webdriver.Chrome()
# dr.maximize_window()
# dr.get('https://at-client-portal-uat.atfxdev.com/register')
# time.sleep(1)
#
# #截屏
# dr.get_screenshot_as_file(r'E:\test\full.png')
# #获取图片元素定位
# img_ele=dr.find_element_by_css_selector('div.code-cell>svg')
# #得到该元素左上角的 x，y 坐标和右下角的 x，y 坐标
# left=img_ele.location.get('x')
# lefty=img_ele.location.get('y')
# right=left+img_ele.size.get('width')
# righty=lefty+img_ele.size.get('height')
#
# #打开之前的截图
# image=Image.open(r'E:\test\full.png')
# #对图片进行裁剪，裁剪范围为之前验证的左上角至右下角范围
# new_image=image.crop((left,lefty,right,righty))
# new_image.save(r'E:\test\cropde02.png')

#导包
# from selenium import webdriver
# import time
# import random
# #from PIL import Image
# #from analysis_captcha import base64_api
# from selenium.webdriver.support.wait import WebDriverWait
# from country_list import exceldata
# import ddt
# import unittest
#
# #提取测试文档数据
# e=exceldata()
# e.openexcel(r'E:\test\country.xlsx','Sheet1') #测试文档的路径，sheet名
# testdata=e.dict_data()
#
# #创建类，继承unittest.TestCase类：
#
# @ddt.ddt #数据驱动
# class creat_account(unittest.TestCase):
#     """2.0会员中心注册流程,根据国家列表注册对应的证件签发国账户"""
#     #进入注册页面
#     def __init__(self,methodName='runTest'):
#         super(creat_account,self).__init__(methodName) #重写父类的init方法
#
#         self.dr=webdriver.Chrome()
#         self.dr.maximize_window() #最大化窗口
#         self.dr.implicitly_wait(20) #隐式等待20s
#
#     def setUp(self):#预置条件
#         self.dr.get('https://at-client-portal-uat.atfxdev.com/register')
#         time.sleep(1)
#
#     def tearDown(self):#环境恢复
#         time.sleep(3)
#         self.dr.close()
#         self.dr.quit()
#
#     # 封装css定位方法
#     def css(self,element):
#         self.el=self.dr.find_element_by_css_selector(element)
#         return self.el
#
#     #封装显示等待定位方法,等待10s，每1s询问一次
#     def wcss(self,name):
#         self.wel = WebDriverWait(self.dr,10,1).until(lambda x: x.find_element_by_css_selector(name))
#         return self.wel
#
#     #填写表单
#     @ddt.data(*testdata)
#     def test_fill_form(self,data):
#         # 显示等待，去除页面警告框
#         self.wcss('.blk-sure-btn').click()
#         time.sleep(2)
#         #选择语言为简体中文
#         self.css('.la-globe').click()
#         time.sleep(1)
#         self.css('ul.el-dropdown-menu > li:nth-of-type(2)').click()
#         time.sleep(2)
#         #名字字段引用测试文档中的三字码，此处需要用到数据驱动
#         self.css('[placeholder="名字"]').send_keys(data['三字码'])
#         time.sleep(2)
#         #姓氏
#         self.css('[placeholder="姓氏"]').send_keys('tyler')
#         #居住国家选择测试文档中的国家
#         self.css('[placeholder="选择居住国家"]').send_keys(data['国家'])
#         time.sleep(1)
#         self.css('div[x-placement="bottom-start"] li:nth-of-type(2) > span').click()
#
# # c=creat_account()
# # c.test_fill_form()
# #
# if __name__=='__main__':
#     unittest.main()

#creat_account().fill_form()


# phone_list=[130,131,132,155,156,185,186,145,146,166,167,175,176]
# print(random.choice(phone_list))
# print((random.sample('0123456789',8)))
# phone_num=str(random.choice(phone_list))+''.join(random.sample('0123456789',8))
# print(phone_num)
# email=phone_num+'@wo.cn'
# print(email)

# import time
#
# # print(time.localtime(time.time()))
# img_name=time.strftime('%Y-%m-%d%H%M%S',time.localtime(time.time()))


# from selenium import webdriver
#
# from PIL import Image
# import random
#
# dr=webdriver.Chrome()
# dr.maximize_window()
# dr.get('https://at-client-portal-uat.atfxdev.com/register')
# dr.get('https://www.atfx.com/gm/en/ripple-cfd-broker/')
# time.sleep(1)
# dr.find_element_by_css_selector('.blk-sure-btn').click()
# #截屏
# dr.get_screenshot_as_file(r'E:\test\{}.png'.format(img_name))
# #获取图片元素定位
# img_ele=dr.find_element_by_css_selector('div.code-cell>svg')
# #得到该元素左上角的 x，y 坐标和右下角的 x，y 坐标
# left=img_ele.location.get('x')
# lefty=img_ele.location.get('y')
# right=left+img_ele.size.get('width')
# righty=lefty+img_ele.size.get('height')
#
# #打开之前的截图
# image=Image.open(r'E:\test\{}.png'.format(img_name))
# #对图片进行裁剪，裁剪范围为之前验证的左上角至右下角范围
# new_image=image.crop((left,lefty,right,righty))
# new_image.save(r'E:\test\{}.png'.format(img_name+'new'))
#
# from selenium import webdriver
# import time
# import random
#
# dr=webdriver.Chrome()
# dr.maximize_window()
# dr.get('http://demo.atdailytrain.com/lp/atfx_one/')
# t=1
# while t<=40:
#     time.sleep(1)
#     dr.find_element_by_css_selector('#form-field-name').send_keys('tyler-测试测试08040{}'.format(t))
#     time.sleep(1)
#     dr.find_element_by_css_selector('#form-field-phone').send_keys('136'+ ''.join(random.sample('0123456789', 8)))
#     time.sleep(1)
#     dr.find_element_by_css_selector('#form-field-email').send_keys('tyler.tang@newtype.io')
#     time.sleep(2)
#     dr.find_element_by_css_selector('button.elementor-button .elementor-button-text').click()
#     time.sleep(3)
#     dr.back()
#     time.sleep(2)
#     t=t+1
#
# dr.close()
# dr.quit()
#
#
# #类与方法，公共变量的用法
# class A():
#     def a(self):
#         self.ele=input() #当这个变量要在其他的方法中使用时，加self
#         return self.ele
#     def b(self):
#         self.a() #调用同一个类中的方法，加self
#         print('hello，'+self.ele)
#
# from openpyxl import load_workbook
# from country_list import exceldata
#
# e=exceldata()
# rows=e.openexcel(r'E:\test\country.xlsx','Sheet1')
# data=e.dict_data()
# print(rows)
# print(data)
#
# def saveaccount(A,row):
#
#     workbook=load_workbook(filename=r'E:\test\account_number.xlsx')
#     sheet=workbook.active
#     cel=sheet['{}{}'.format(A,row)]
#     cel.value='hhh'
#     workbook.save(filename=r'E:\test\account_number.xlsx')
#
# saveaccount('A',2)

#
# from selenium import webdriver
# import time
# from selenium.webdriver.support.wait import WebDriverWait
# from bs4 import BeautifulSoup
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
# dr.find_element_by_css_selector('[placeholder="请输入您的电子信箱"]').send_keys('17645566@qq.com')
# time.sleep(1)
# dr.find_element_by_css_selector('div.formBlock > .el-form > .el-col [placeholder="请输入您的密码"]').send_keys('Tl123456')
# time.sleep(1)
# dr.find_element_by_css_selector('div.formBlock > .el-form > .el-col .el-button').click()
# time.sleep(3)
# # id=dr.find_element_by_css_selector('.user-name-font').text
# id=WebDriverWait(dr,10,1).until(lambda x: x.find_element_by_css_selector('.user-name-font')).text
# print(id)
# #点击验证您的联系方式
# dr.find_element_by_css_selector('.box.progress-content > .progress-text').click()
# time.sleep(1)
# #发送验证码
# dr.find_element_by_css_selector('div.el-col-24>button.dialog-sendCode').click()
# #js新开窗口
# js='window.open("https://at-bos-frontend-uat.atfxdev.com/login")'
# dr.execute_script(js)
# time.sleep(3)
# #获取所有句柄
# all_handles=dr.window_handles
# client_handle=all_handles[0]
# print(dr.title)
# bos_handle=all_handles[1]
# #切换到bos窗口
# dr.switch_to.window(bos_handle)
# print(dr.title)
#
# dr.find_element_by_css_selector('.ivu-icon-ios-arrow-down').click()
# time.sleep(1)
# #选择语言为中文
# dr.find_element_by_css_selector('ul.ivu'
#                                 '-select-dropdown-list > li:nth-of-type(1)').click()
# dr.find_element_by_css_selector('[placeholder="账号"]').send_keys('tyler')
# dr.find_element_by_css_selector('[placeholder="密码"]').send_keys('Tl123456')
# dr.find_element_by_css_selector('button.ivu-btn-large > span').click()
# time.sleep(1)
# WebDriverWait(dr,10,1).until(lambda x: x.find_element_by_css_selector('div[width="200"] li:nth-of-type(5) > .ivu-menu-submenu-title > span')).click()
# #点击邮件/短信记录
# dr.find_element_by_css_selector('div[width="200"] [href="/report/emailrecord"]').click()
# time.sleep(2)
# # dr.find_element_by_css_selector('div.ivu-tabs-content > div:nth-of-type(1) div:nth-of-type(2) > div:nth-of-type(1) > input:nth-of-type(1)').send_keys('1200001561')
# # time.sleep(1)
# # dr.find_element_by_css_selector('div.ivu-tabs-content > \
# # div:nth-of-type(1) > \
# # div:nth-of-type(1) > \
# # div:nth-of-type(1) > \
# # div:nth-of-type(1) > \
# # div:nth-of-type(2) \
# # div:nth-of-type(2) \
# # i:nth-of-type(1)').click()
# time.sleep(1)
# #按时间排序
# dr.find_element_by_css_selector('div.ivu-tabs-content > '
#                                 'div:nth-of-type(1) th:nth-of-type(5) i:nth-of-type(2)').click()
#
# try:
#     dr.find_element_by_xpath('//div[@class="ivu-tabs-content"]//tr[1]/td[3]').click()
# except:
#     time.sleep(2)
#     dr.refresh()
#
# e=dr.find_elements_by_xpath('//div[@class="ivu-drawer-wrap"]//tr[2]//tr[4]/td[1]/span')
# target=e[0]
# time.sleep(2)
# t=target.text+' '
# #输出验证码
# code=t[6:-1]
# print(code)
# dr.switch_to.window(client_handle)
# dr.find_element_by_css_selector('[placeholder="验证码"]').send_keys(code)
# time.sleep(1)
# #点击下一步
# dr.find_element_by_css_selector('button.dialog-submit > span').click()

# from selenium import webdriver
# import time
# dr = webdriver.Chrome()
# dr.get('https://at-client-portal-uat.atfxdev.com/register')
# time.sleep(1)
# import requests
# import json
# data = {
#     'name': 'germey', 'age': '22'
# }
# response = requests.post("http://httpbin.org/post", data=data)
# print(response.text)
# print(response.json())
# print(response.headers)

# from public import *
# from selenium import webdriver
# class login():
#     dr = webdriver.Chrome()
#     def a(self):
#         self.dr.get('https://www.baidu.com/')
#         css(self.dr,'#kw').send_keys('123')
#
# login().a()
# while True:
#     print(1)
#     a=input()
#     if a=='a':
#         print(2)
#         continue
#     else:
# #         break
# from country_list import exceldata
# e=exceldata()
# rows=e.openexcel(r'E:\test\account_number.xlsx','Sheet1') #测试文档的路径，sheet名,并获取总行数
# testdata=e.dict_data()
# print(testdata)
#
# class BasePage():
#     '''
#     第一层：对Selenium 进行二次封装，定义一个所有页面都继承的 BasePage ，
#     封装 Selenium 基本方法 例如：元素定位，元素等待，导航页面 ，
#     不需要全部封装，用到多少方法就封装多少方法。
#     '''
#
#     def __init__(self, driver, path=None):
#         '''
#         :param driver: Webdriver实例对象
#         :param path:   传入URI
#         '''
#         self.driver = driver
#         self.url = 'https://www.tapd.cn'
#
#         # 设置全局元素定位等待时间 10 秒
#         self.driver.implicitly_wait(10)
#
#         # 打开页面
#         self.load_page(path)
#
#     def by_xpath(self, xpath):
#         return self.driver.find_element_by_xpath(xpath)
#
#     def load_page(self, path=None):
#         # 如果不传入path,则不打开浏览器
#         if path == None:
#             url = None
#         else:
#             url = self.url + path
#         if url != None:
#             self.driver.get(url)
#
# from selenium import webdriver
# import time
# time.sleep(1)
# dr=webdriver.Chrome()
# dr.get('https://at-client-portal-uat.atfxdev.com/register')
# dr.find_element_by_css_selector('.blk-sure-btn').click()
# time.sleep(1)
# dr.find_element_by_css_selector('.la-globe').click()
# time.sleep(1)
# dr.find_element_by_css_selector('ul.el-dropdown-menu > li:nth-of-type(2)').click()
#
# dr.find_element_by_css_selector('[placeholder="选择居住国家"]').click()
# dr.find_element_by_xpath('//span[.="英国"]').click()
# def is_uk():
#     uk_text=dr.find_element_by_css_selector('div.el-dialog__body>div.tips_body>div.p_10_0>p')
#     print(uk_text)
#     if uk_text=='AT Global Markets Limited 不接受居住在这个国家的个人申请。您可以在ATFX UK申请交易账户。':
#         return True
#     else:
#         return False
#
# is_uk()

# class A():
#     def fangfaone(self):
#         self.a='nihao'
#         return self.a
#
# class B(A):
#     def fangfatwo(self):
#         self.fangfaone()
#         print(self.a)


# b=B()
# b.fangfatwo()
#
# from cp_register.page.excel_data import  exceldata
#
# e = exceldata()
# e.openexcel(r'E:\bos_cp_example\register_ex.xlsx', 'uk_list')
# testdata = e.dict_data()
# print(testdata)
#
# con='阿尔巴尼亚'
# print(con in testdata)

# from selenium import webdriver
#
# dr=webdriver.Chrome()
# dr.maximize_window()
# dr.get('https://www.baidu.com/')
# def is_ok():
#     try:
#         el=dr.find_element_by_css_selector('kdlk').text
#         return True
#     except:
#         return False
#
# print(is_ok())

# def china(contury, ivcode):
#     if contury == '中国':
#         # 输入邀请码
#         print('zhonggg')
#     else:
#         ivcode = None
#         print(ivcode)
#
# china('中国','123')
# china('suizhou','123')
# from selenium import webdriver
# import time
# import random

# dr=webdriver.Chrome()
# dr.maximize_window()
# dr.get('https://at-client-portal-uat.atfxdev.com/login')
# time.sleep(1)
# dr.find_element_by_css_selector('.blk-sure-btn').click()
# time.sleep(1)
# dr.find_element_by_css_selector('.la-globe').click()
# time.sleep(1)
# dr.find_element_by_css_selector('ul.el-dropdown-menu > li:nth-of-type(2)').click()
# time.sleep(1)
# dr.find_element_by_css_selector('[placeholder="请输入您的电子信箱"]').send_keys('153125555@QQ.COM')
# time.sleep(1)
# dr.find_element_by_css_selector('div.formBlock > .el-form > .el-col [placeholder="请输入您的密码"]').send_keys('Tl123456')
# time.sleep(1)
# dr.find_element_by_css_selector('div.formBlock > .el-form > .el-col .el-button').click()
# time.sleep(6)
# dr.find_element_by_css_selector('div.el-dialog__footer>div>button.el-button--primary').click()
# time.sleep(1)
# ib_list=dr.find_elements_by_css_selector('.el-checkbox__inner')
# time.sleep(1)

# print(len(ib_list))
# for i in ib_list[0:random.randint(1, len(ib_list) - 1)]:
#     i.click()
#     time.sleep(1)
# time.sleep(1)
# ib_list[-1].click()

# from selenium import webdriver

# dr=webdriver.Chrome()
# dr.maximize_window()
# dr.get('file:///C:/Users/Tyler%20Tang/PycharmProjects/tylerdir/study/scroll_bar.html')

# #js='document.getElementById("yoyoketang").scrollTop = 10000'
# js='document.getElementsByClassName("scroll")[0].scrollTop = 10000'
# dr.execute_script(js)

# import json
# list_city=[{'神仙帝国': 'SXD'}, {'爱沙尼亚': 'EE'}, {'美属维尔京群岛': 'VIR'}, {'巴巴多斯': 'BRB'}]
# data=json.dumps(list_city)
# print(data,type(data))

# from selenium import webdriver
# import time
# from selenium.webdriver.common.action_chains import ActionChains

# dr=webdriver.Chrome()
# dr.maximize_window()
# dr.implicitly_wait(20)
# dr.get('https://at-client-portal-uat-proxy.ntdevops.com/login')
# time.sleep(1)

# dr.find_element_by_css_selector('.blk-sure-btn').click()

# dr.find_element_by_css_selector('.la-globe').click()
# time.sleep(1)
# dr.find_element_by_css_selector('ul.el-dropdown-menu > li:nth-of-type(2)').click()
# time.sleep(1)
# dr.find_element_by_css_selector('[placeholder="请输入您的电子信箱"]').send_keys('0031414538@qq.com')
# time.sleep(1)
# ps=dr.find_elements_by_css_selector('[placeholder="请输入您的密码"]')
# ps[-1].send_keys('Tl123456')
# time.sleep(1)
# dr.find_element_by_css_selector('div.formBlock > .el-form > .el-col .el-button').click()
# time.sleep(1)
# dr.find_element_by_css_selector('.btn-cancel').click()
# ele=dr.find_element_by_css_selector('.el-icon--right')
# time.sleep(1)
# print(124544)
# ActionChains(dr).move_to_element(ele).perform()
# print(1111)
# time.sleep(1)
# dr.find_element_by_css_selector('ul.el-client-menu > li:nth-of-type(3) > .drop-sub-title').click()
# time.sleep(1)
# dr.find_element_by_css_selector('button.logout-btn-confirm > span').click()

# def iscretd(answer='是'):
#     answer=input('是否创建测试数据')
#     if answer == '是':
#         print('默认创建')
#     else:
#         print('不创建')

# n=input('shuru')

# def a():
#     try:
#         int(n)
#         return n,True
#     except:
#         print(2565)
#         return False

# if a():
#     print(123)
# else:
#     print(456)

# import random
# # for i in range(1,5):
# #     print(random.randint(1,12))

# def randomint(n):
#     email_list = ['@qq.com','@163.com','@gmail.com',]
#     email = ''.join(random.sample('0123456789',n))+str(random.choice(email_list)) # 随机生成联通号码
#     return email

# print(randomint(9))







































































































































