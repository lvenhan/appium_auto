# -*- coding:utf-8 -*-
import time
from selenium.webdriver.support.ui import WebDriverWait,Select
from appium.common.exceptions import NoSuchContextException
from  Public import BasicSetting
import os
from  selenium.webdriver.common.by import By

#获取根文件夹路径
p_file=os.path.dirname(os.getcwd())
filepath=os.path.join(p_file,'screenshot')
basicS=BasicSetting.BasicSetting()

class BaseAction():
    #获取时间戳
    def getTime(self):
        tf=time.strftime("%Y-%m-%d_%H_%M_%S",time.localtime(time.time()))
        return tf

    """
    根据不同的定位方法，获取返回的元素
    lacateType:定位方法
    str：元素定位
    value:判断是否是accessibility_id方法
    """
    def get_element(self,driver,lacateType,str):
        try:
            if (lacateType == "desc"):
                element=WebDriverWait(driver,30).until\
                (lambda x:x.find_element_by_accessibility_id(str))
            else:
                element=WebDriverWait(driver,30).until\
                    (lambda x:x.find_element(by=lacateType,value=str))
            return element
        except Exception as e:
            print(e)

    """
    根据获取的元素，点击内容
    type：定位元素的方法
    str：输入的内容
    value:用来判断是否是accessibility_id方法定位
    """
    def ele_click(self,driver,type,str):
        try:
            ele=self.get_element(driver,type,str)
            ele.click()
        except Exception as e:
            print(e)

    #查找元素，输入内容
    def element_input(self,driver,type,str,value):
        try:
            self.get_element(driver,type,str).send_keys(value)
        except Exception ,e:
            print(e)

    #根据字典list，读取内容，执行操作
    def click_dict (self,driver,type,list):
        try:
            for param in list:
                self.ele_click(driver,type,param)
        except NoSuchContextException as e:
            print(u"元素异常",e )

    #报错之后截图，保存到文件中
    def screenshot(self,driver,filename):
        type='.png'
        time=self.getTime()
        driver.get_screenshot_as_file(filepath+"\\"+filename+time+type)

    #断言页面源码是否存在某关键字或关键字字符串
    def assert_string_in_pagesource(self,driver,assertString):
        try:
            assert assertString in driver.page_source,\
            u"%s not found in page source!" % assertString
        except AssertionError as e:
            raise  e
        except Exception as e:
            raise e

    #断言页面标题是否攒在给定的关键字
    def assert_title(self,driver,titleString):
        try:
            assert  titleString in driver.title,\
                u"% not fount in title!" %titleString
        except AssertionError as e:
            raise e
        except Exception as e:
            raise e

    #获取手机屏幕大小
    def getsize(self,driver):
        x = driver.get_window_size()['width']
        y = driver.get_window_size()['height']
        return (x, y)

    #手机屏幕上滑
    def swipeUp(self,driver,time):
        size=self.getsize(driver)
        x1 = int(size[0] /2)    #x坐标
        y1 = int(size[1]/4*3)   #起始y坐标
        y2 = int(size[1]/4)   #终点y坐标
        driver.swipe(x1, y1, x1, y2,time)

    #按住A点后快速滑动至B点
    def flick(self,driver):
        size=self.getsize(driver)
        x1 = int(size[0] /2)    #x坐标
        y1 = int(size[1]/4*3)   #起始y坐标
        y2 = int(size[1]/4)   #终点y坐标
        driver.swipe(x1, y1, x1, y2)



    #元素从A元素滚动到B元素
    def ele_scroll(self,driver,type1,str1,type2,str2):
        try:
            ele1=self.get_element(driver,type,str1)
            ele2=self.get_element(driver,type ,str2)
            driver.scroll(ele1,ele2)
        except Exception as e:
            raise e


    #下拉框选择值
    def selected(self,driver,type,param,str,text):
        try:
            if type is "index":
                ele=Select(self.get_element(driver,param,str))
                ele.select_by_index(text)
            elif type is "value":
                ele=Select(WebDriverWait(self.driver,10).until(lambda driver: driver.find_element_by_id(str)))
                ele.select_by_value(text)
            elif type is "visibletext":
                ele=Select(WebDriverWait(self.driver,10).until(lambda driver: driver.find_element_by_id(str)))
                ele.select_by_visible_text(text)
            else:
                print(u"该元素不存在",+str)
        except NoSuchContextException as e:
            print(u"元素异常",e )








