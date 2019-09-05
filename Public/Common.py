# -*-coding:utf-8-*-
from Public import ReadCsv
from time import sleep
import BasicSetting,BaseAction


readcsv=ReadCsv.GetCsv()
baseS=BaseAction.BaseAction()
bsetting=BasicSetting.BasicSetting()
testname="测试"
class Common():

    def __init__(self):
        self.driver=bsetting.open_WeChat()
        sleep(10)

    def get_driver(self):
        return self.driver

    #把输入链接和发送提出来作为一个方法
    def entry(self,product_link):
        self.driver=self.get_driver()
        baseS.element_input(self.driver,"xpath",".//android.widget.EditText[@index='0']",product_link)
        baseS.ele_click(self.driver,"xpath",'.//android.widget.Button[@text="发送"]')
        ele=self.driver.find_elements_by_id("com.tencent.mm:id/jz")
        num=len(ele)
        baseS.ele_click(self.driver,"xpath","//android.widget.RelativeLayout[@index="+str(num)+"]")

    #进入链接，然后输入链接并发送
    def com_link(self,product_link):
        #获取假期护家链接
        # 1. 进入测试号里，2. 输入链接，发送， 3. 调用方法，进入链接
        # baseS.ele_click(self.driver,"xpath",".//android.view.View[contains(@text,'测试')]")
        self.driver.find_element_by_xpath(".//android.view.View[contains(@text,'测试')]").click()
        #baseS.ele_click(self.driver,'xpath','.//android.view.View[@resource-id="com.tencent.mm:id/apv" and text="测试"]')
        #断言是否进入安逸测试号，否则返回页面，重新进入
        # ele=baseS.get_element(self.driver,'xpath',".//android.widget.TextView[@resource-id='com.tencent.mm:id/hn']")
        # print(ele.text)
        # while (ele.text != u"测试"):
        #     print("返回到前一个页面")
        #     baseS.ele_click(self.driver,"desc","返回")
        #     sleep(1)
        #     baseS.ele_click(self.driver,'xpath','.//android.view.View[contains(@text,"测试")]')
        #     ele=baseS.get_element(self.driver,'xpath',".//android.widget.TextView[@resource-id='com.tencent.mm:id/hn']")
        # else:
        #     print("继续执行")
        #     self.entry(product_link)



