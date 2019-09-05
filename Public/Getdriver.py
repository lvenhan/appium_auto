#coding=utf-8
from appium import webdriver
import os

#定义全局driver变量
driver=None

#返回需要安装的文件，非路径
PATH = lambda p:os.path.abspath(
        os.path.join(os.path.dirname(__file__),p))
# devicesName='9TONONEUH6N7WSDU,a325dad0,a1a78230'
def openWeChat():
    global driver
    desired_caps={}
    desired_caps['platformName']='Android'
    desired_caps['platformVersion']='5.0.2'#备版本号
    desired_caps['deviceName']='9TONONEUH6N7WSDU' #设备名
    # desired_caps['noReset']=True
    # desired_caps['fullReset']=False
    desired_caps['noSign']=True
    desired_caps['unicodeKeyboard']=True
    desired_caps['resetKeyboard']=True
    desired_caps['appPackage'] ='com.tencent.mm' #微信包名
    desired_caps['appActivity'] = 'com.tencent.mm.ui.LauncherUI' #微信起始页面
    driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',
                              desired_caps)
    driver.implicitly_wait(30)

