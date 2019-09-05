# -*- coding:utf-8 -*-
from appium import webdriver
import os

#定义全局driver变量
# driver=None

#返回需要安装的文件，非路径
PATH = lambda p:os.path.abspath(
        os.path.join(os.path.dirname(__file__),p))
# devicesName='9TONONEUH6N7WSDU,a325dad0,a1a78230'

#打开微信
class BasicSetting():

    #打开真机
    def open_WeChat(self):
        desired_caps={ }
        desired_caps['platformName']='Android'
        desired_caps['platformVersion']='5.0.2'#设备版本号
        desired_caps['deviceName']='9TONONEUH6N7WSDU' #设备名
        desired_caps['noReset']=False
        desired_caps['noSign']=False
        desired_caps['unicodeKeyboard']=True
        desired_caps['resetKeyboard']=True
        desired_caps['appPackage'] ='com.tencent.mm' #微信包名
        desired_caps['appActivity'] = 'com.tencent.mm.ui.LauncherUI' #微信起始页面
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',
                              desired_caps)
        self.driver.implicitly_wait(30)
        return self.driver

    def close(self):
        try:
            self.driver.quit()
        except Exception,e:
            raise e