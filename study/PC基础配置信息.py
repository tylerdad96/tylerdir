'''
    Code description：'此程序用以获取用户电脑基础配置信息'；Create time：2020/04/15 Developer：tyler
'''
# -*- coding: utf-8 -*-

import wmi
import win32con
import time
import os

print('###在命令行窗口输入保存的文件名，运行完成后打开生成的txt文本即可查看获取到的计算机基础配置信息')

#开始时间：
start_time=time.time()
while True:
    fname=input('enter filename>')#输入
    # 判断该输入是否存在
    if os.path.exists(fname):
        print("Error:'%s' already exists"%fname)
    else:
        break

#open函数在目录中进行检查，有则打开，无则新建，'a'表示以追加模式打开
fobj=open(fname,'a',encoding='utf-8')


#WMI类的实例化(wmi模块中的WMI类)：定义一个全局变量，用来表示wmi模块中的WMI类：
w=wmi.WMI()

#Win32_OperatingSystem()方法获取sn号、系统版本信息号
def sys_version():
    for i in w.Win32_OperatingSystem():
        print('操作系统版本：%s'% i.Caption)
        #写进文件fname，即你刚刚输入的文件名的文件
        fobj.write('操作系统版本：'+ i.Caption)
        print('操作系统位数：',i.OSArchitecture)
        #写进文件fname
        fobj.write('\n'+'操作系统位数：'+i.OSArchitecture)

#Win32_NetworkAdapterConfiguration(IPEnabled=1)方法获取IP及MAC地址和网卡类型
def get_ip():
    for i in w.Win32_NetworkAdapterConfiguration(IPEnabled=1):
        print('网口型号为：',i.Description)
        #写进文件fname
        fobj.write('\n'+'网口型号为：'+i.Description)
        #获取IP地址及mac地址
        for y in i.IPAddress:
            print(y)
            fobj.write('\n'+'IP地址和MAC地址为：'+y)

#Win32_Processor()方法获取CPU信息，Win32_PhysicalMemory()获取内存大小：
#统计cpu的个数：print(cpu_list,len(cpu_list))
def cpu_and_mem():
    for i in w.Win32_Processor():
        print('CPU:%s'%i.Name.strip())
        #写入文件fname
        fobj.write('\n'+'CPU:'+i.Name.strip())
    for y in w.Win32_PhysicalMemory():
        print("内存大小: %.fGB" % ( (int(y.Capacity) / 1048576) /1024) )
        #写入文件fname
        fobj.write('\n'+("内存大小: %.fGB" % ( (int(y.Capacity) / 1048576)/1024) ))

#Win32_DiskDrive()获取物理磁盘信息
def disk():
    for i in w.Win32_DiskDrive():
        print('硬盘制造商：',i.Manufacturer)
        #写入文件fname
        fobj.write('\n'+'硬盘制造商：'+i.Manufacturer)
        print('硬盘型号：', i.Model)
        # 写入文件fname
        fobj.write('\n'+'硬盘型号：'+i.Model)
        # 写入文件fname
        print('硬盘sn：', i.SerialNumber)
        # 写入文件fname
        fobj.write('磁盘sn:'+i.SerialNumber)
        print('硬盘大小：', int(i.Size) / (1024 * 1024 * 1024))
        # 写入文件fname
        fobj.write('磁盘大小：'+str(int(i.Size) / (1024 * 1024 * 1024)))
        for y in i.associators('Win32_DiskDriveToDiskPartition'):
            for l in y.associators('Win32_LogicalDiskToPartition'):
                print(i.Caption,y.Caption,l.Caption)
                #写入文件fname：
                fobj.write('\n'+'磁盘分区:'+i.Caption+y.Caption+l.Caption)
    #获取各个磁盘分区大小：
    for d in w.Win32_LogicalDisk(DriveType=3):
        print(d.Caption, "磁盘大小: %0.1fGB" % ((int(d.Size) / 1048576) / 1024))
        #写入文件fname
        fobj.write('\n' +d.Caption + "磁盘大小: %0.1fGB" % ((int(d.Size) / 1048576) / 1024))

#Win32_NetworkAdapterConfiguration()方法用于网络接口信息对象，并存以列表形式
#获取所有网卡信息
def net():
    data={}
    count=0
    for nic in w.Win32_NetworkAdapterConfiguration():
        if nic.MACAddress is not None:
            count+=1
            item_data = {}
            item_data['macaddress'] = nic.MACAddress
            item_data['model'] = nic.Caption
            item_data['name'] = nic.Index

            if nic.IPAddress is not None:
                item_data['ipaddress'] = nic.IPAddress[0]
                item_data['netmask'] = nic.IPSubnet
            else:
                item_data['ipaddress'] = ""
                item_data['netmask'] = ""
            data["nic%s" %count] = item_data
    #输出
    print(data)
    #写入文件fname
    fobj.write('\n'+'所有网卡信息为：'+str(data))

#调用以上创建的函数
def to_do():
    sys_version()
    get_ip()
    cpu_and_mem()
    disk()
    net()

if __name__ == '__main__':
    to_do()

over_time=time.time()
pa_time=over_time-start_time
fobj.write('\n'+'查询用时：'+str(pa_time)+'ms')
fobj.close()