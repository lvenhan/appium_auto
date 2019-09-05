# -*-coding:utf-8-*-
import csv,os,sys

class GetCsv():
    def getproduct(self):
        try:
            csvpath=os.path.join(sys.path[1],'testdata','productCsv.csv')
            datum={}
            with open(csvpath,'rb')as csvfile:
                account_list=csv.reader(csvfile)
                for data in account_list:
                    datum[data[0]]=data[1]
                return datum

        except:
            print(u"读取csv出错")


    def readEle(self,csvpath):
        try:
            data=[]
            with open(csvpath,'rb')as csvfile:
                account_list=csv.reader(csvfile)
                for list in account_list:
                    data.append(list)
                return data
        except:
            print(u"读取csv出错")

if __name__ == '__main__':
    data=GetCsv().getproduct()
    print(data)