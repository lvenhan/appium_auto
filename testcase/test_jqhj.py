# -*-coding:utf-8-*-
import unittest
from selenium.webdriver.common.by import By
from Public import Common
from time import sleep
from Public import ReadCsv
from Public import BasicSetting
from Public import BaseAction
import time

readcsv=ReadCsv.GetCsv()
com=Common.Common()
baseS=BaseAction.BaseAction()
bsetting=BasicSetting.BasicSetting()

class JQHJ(unittest.TestCase):
    u"""
    假期护家
    """
    def test_openjqhj(self):
        u"""假期护家投保"""
        try:
            #获取假期护家链接
            self.driver=com.get_driver()
            product_link=readcsv.getproduct()['jqhj']
            print("开始执行假期护家，链接如下:")
            print(product_link)
            com.com_link(product_link)
            self.driver=com.get_driver()
            # baseS.ele_click(self.driver,"desc","保障责任")
            baseS.swipeUp(self.driver,3000)
            #查看每一项保障责任,包含房屋及其室内附属设施，室内财产，盗抢保险，管道破裂及水泽，第三者责任保险
            # insuredlist=self.driver.find_elements_by_xpath(".//android.widget.ListView[@resource-id='insured-table']/android.view.View[@content-desc='']")
            # regulations=(len(insuredlist))
            # num=1
            # while(num<=regulations):
            #     baseS.ele_click(self.driver,"xpath",".//android.widget.ListView[@resource-id='insured-table']/android.view.View[@content-desc='']["+str(num)+"]")
            #     baseS.ele_click(self.driver,"xpath",".//android.widget.ListView[@resource-id='insured-table']/android.view.View[@content-desc='']["+str(num)+"]")
            #     num=num+1
            #     if(num>regulations):
            #         break

            #查看投保须知，保险条款
            # list_name=["《投保须知》"," 我已了解","《保险条款》"," 我已了解"]
            # baseS.click_dict(self.driver,"desc",list_name)

            #开始投保
            sleep(1)
            print("执行立即投保")
            baseS.ele_click(self.driver,"desc","立即投保")
            #判断是否进入投保信息页面

            # #输入投保人姓名，证件号码，手机号码，电子邮箱，确认投保,
            baseS.element_input(self.driver,"xpath",".//android.widget.EditText[@resource-id='people_info_name']","testhan")
            baseS.element_input(self.driver,"xpath",".//android.widget.EditText[@resource-id='people_info_id']","110101198001010010")
            baseS.element_input(self.driver,"xpath",".//android.widget.EditText[@resource-id='form_insurer_phone']","18207278423")

            #页面往上滑
            #页面向上滑动，填写邮箱，地址等信息
            baseS.flick(self.driver)
            baseS.element_input(self.driver,"xpath",".//android.widget.EditText[@resource-id='form_insurer_email']","xiaoqing.han@riskeys.com")
            #选择省市区
            baseS.ele_click(self.driver,"desc","请选择省市区")
            area=["上海市","市辖区","黄浦区"]
            baseS.click_dict(self.driver,"desc",area)
            baseS.element_input(self.driver,"xpath",".//android.widget.EditText[@resource-id='peopleaddress']",u"亮秀路112号")
            baseS.element_input(self.driver,"xpath",".//android.widget.EditText[@resource-id='peopleaddress']","200000")

            baseS.ele_click(self.driver,"xpath",".//android.view.View[@resource-id='bottom-price']/android.view.View[2]")


        except Exception ,e:
            print(e)


if __name__ == '__main__':
    suite=unittest.TestSuite()
    suite.addTest(JQHJ("test_openjqhj"))
    #执行测试集
    runner=unittest.TextTestRunner()
    runner.run(suite)