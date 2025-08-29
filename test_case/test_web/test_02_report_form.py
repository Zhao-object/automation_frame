from automation_frame.test_business.web_report_form_page import ReportFormPage
from automation_frame.test_parse_data.prase_data import DataParse
from parameterized import parameterized
import unittest
import time
class TestReport(unittest.TestCase):

    def setUp(self):
        print("-" * 20 + "开始测试一条用例(API)" + "-" * 20)
        # 先获得一个类属性
        self.reportpage = ReportFormPage()  # 实例化报表中心页面对象

    #点击报表中心
    def test_1_report(self):
        self.reportpage.report_button()
        time.sleep(10)

    #验证解密功能
    mydata = DataParse('../../test_data/data_web.xlsx').parse_excel_datas('report_decode')
    @parameterized.parameterized.expand(mydata)
    def test_a1_decode(self,tittle,mylist,expected):
        self._testMethodDoc = tittle
        # self.reportpage.report_button()
        self.reportpage.decode_button()#点击解密
        self.reportpage.decode_input_text(mylist[0])#输入密码
        self.reportpage.decode_affirm()#点击确认
        result = self.reportpage.look_decode()
        assert expected in result
    #验证咨询部输入时间,搜索功能
    mydata = DataParse('../../test_data/data_web.xlsx').parse_excel_datas('consult_time_search')
    @parameterized.parameterized.expand(mydata)
    def test_a2_consult_search(self,tittle,mylist,expected):
        self._testMethodDoc = tittle
        self.reportpage.consult_button()#点击咨询部
        time.sleep(1)
        self.reportpage.consult_start_time_input(mylist[0])#输入开始时间
        self.reportpage.consult_end_time_input(mylist[1])#输入结束时间
        self.reportpage.consult_search_button()#搜索
        time.sleep(1)
        result = self.reportpage.look_consult_time_search()#断言
        assert expected in result

    #验证咨询部当期按钮功能
    mydata = DataParse('../../test_data/data_web.xlsx').parse_excel_datas('consult_date')
    @parameterized.parameterized.expand(mydata)
    def test_a3_consult_date(self,tittle,mylist,expected):
        self._testMethodDoc = tittle
        self.reportpage.consult_date_button()#当期
        # self.reportpage.move_driver_until_down()#到最底
        result = self.reportpage.look_consult_date()#断言,返回结果
        # self.reportpage.move_driver_until_up()#到顶部
        assert expected in result
    #
    # 验证电销部输入时间,搜索功能
    mydata = DataParse('../../test_data/data_web.xlsx').parse_excel_datas('phone_sell_time_search')
    @parameterized.parameterized.expand(mydata)
    def test_a4_phone_search(self, tittle, mylist, expected):
        self._testMethodDoc = tittle
        self.reportpage.phone_sell_button()  #点击电销部
        time.sleep(1)
        self.reportpage.phone_sell_starttime(mylist[0])  # 输入开始时间
        self.reportpage.phone_sell_endtime(mylist[1])  # 输入结束时间
        self.reportpage.phone_sell_search_button()  # 搜索
        time.sleep(1)
        result = self.reportpage.look_phone_time_search()#获取结果
        assert expected in result

    #验证电销部当期按钮功能
    mydata = DataParse('../../test_data/data_web.xlsx').parse_excel_datas('phone_date')
    @parameterized.parameterized.expand(mydata)
    def test_a5_phone_date(self,tittle,mylist,expected):
        self._testMethodDoc = tittle
        self.reportpage.phone_sell_date()#当期
        time.sleep(1)
        # self.reportpage.move_driver_until_down()#到最底
        result = self.reportpage.look_phone_date()#断言,返回结果
        # self.reportpage.move_driver_until_up()#到顶部
        assert expected in result

    # 验证市场部输入时间,搜索功能
    mydata = DataParse('../../test_data/data_web.xlsx').parse_excel_datas('market_sell_time_search')
    @parameterized.parameterized.expand(mydata)
    def test_a6_phone_search(self, tittle, mylist, expected):
        self._testMethodDoc = tittle
        self.reportpage.market_button()  # 点击市场部
        time.sleep(1)
        self.reportpage.market_starttime(mylist[0])  # 输入开始时间
        self.reportpage.market_endtime(mylist[1])  # 输入结束时间
        self.reportpage.market_search()  # 搜索
        time.sleep(1)
        result = self.reportpage.look_market_time_search()  # 获取结果
        assert expected in result

    #验证市场部当期按钮功能
    mydata = DataParse('../../test_data/data_web.xlsx').parse_excel_datas('market_date')
    @parameterized.parameterized.expand(mydata)
    def test_a7_market_date(self,tittle,mylist,expected):
        self._testMethodDoc = tittle
        self.reportpage.market_date()#市场部当期
        time.sleep(1)
        result = self.reportpage.look_market_date()#断言
        assert expected in result

#验证市场部今日按钮功能
    mydata = DataParse('../../test_data/data_web.xlsx').parse_excel_datas('market_today')
    @parameterized.parameterized.expand(mydata)
    def test_a8_market_date(self,tittle,mylist,expected):
        self._testMethodDoc = tittle
        self.reportpage.market_today_button()#市场部今日
        time.sleep(1)
        result = self.reportpage.look_market_today()#断言
        assert expected in result

#验证市场部本周按钮功能
    mydata = DataParse('../../test_data/data_web.xlsx').parse_excel_datas('market_this_week')
    @parameterized.parameterized.expand(mydata)
    def test_a9_market_date(self,tittle,mylist,expected):
        self._testMethodDoc = tittle
        self.reportpage.market_this_week()#市场部本周
        time.sleep(1)
        result = self.reportpage.look_market_this_week()#断言
        assert expected in result

#验证市场部本月按钮功能
    mydata = DataParse('../../test_data/data_web.xlsx').parse_excel_datas('market_this_month')
    @parameterized.parameterized.expand(mydata)
    def test_b1_market_date(self,tittle,mylist,expected):
        self._testMethodDoc = tittle
        self.reportpage.market_this_month()#市场部本月
        time.sleep(1)
        result = self.reportpage.look_market_this_month()#断言
        assert expected in result

#验证市场部上周按钮功能
    mydata = DataParse('../../test_data/data_web.xlsx').parse_excel_datas('market_last_week')
    @parameterized.parameterized.expand(mydata)
    def test_b2_market_date(self,tittle,mylist,expected):
        self._testMethodDoc = tittle
        self.reportpage.market_last_week()#上周
        time.sleep(1)
        result = self.reportpage.look_market_last_week()#断言
        assert expected in result


#验证市场部上月按钮功能
    mydata = DataParse('../../test_data/data_web.xlsx').parse_excel_datas('market_last_month')
    @parameterized.parameterized.expand(mydata)
    def test_b3_market_date(self,tittle,mylist,expected):
        self._testMethodDoc = tittle
        self.reportpage.market_last_month()#上月
        time.sleep(1)
        result = self.reportpage.look_market_last_month()#断言
        assert expected in result

#验证市场部本年按钮功能
    mydata = DataParse('../../test_data/data_web.xlsx').parse_excel_datas('market_this_year')
    @parameterized.parameterized.expand(mydata)
    def test_b4_market_date(self,tittle,mylist,expected):
        self._testMethodDoc = tittle
        self.reportpage.market_this_year()#本年按钮
        time.sleep(1)
        result = self.reportpage.look_market_this_year()#断言
        assert expected in result


#验证教学部按钮功能
    mydata = DataParse('../../test_data/data_web.xlsx').parse_excel_datas('teach_function')
    @parameterized.parameterized.expand(mydata)
    def test_b5_teach(self,tittle,mylist,expected):
        self._testMethodDoc = tittle
        self.reportpage.teach_button()
        time.sleep(1)
        result = self.reportpage.look_teach_function()#断言
        assert expected in result



#验证教学部成都按钮功能
    mydata = DataParse('../../test_data/data_web.xlsx').parse_excel_datas('teach_CD')
    @parameterized.parameterized.expand(mydata)
    def test_b6_teach_date(self,tittle,mylist,expected):
        self._testMethodDoc = tittle
        self.reportpage.teach_CD_button()
        time.sleep(1)
        result = self.reportpage.look_teach_CD()#断言
        assert expected in result

# #验证教学部成都班级按钮功能
#     mydata = DataParse('../../test_data/data_web.xlsx').parse_excel_datas('teach_CD_class')
#     @parameterized.parameterized.expand(mydata)
#     def test_b7_teach_date(self,tittle,mylist,expected):
#         self._testMethodDoc = tittle
#         self.reportpage.class_button()#班级
#         time.sleep(1)
#         result = self.reportpage.look_CD_class()#断言
#         assert expected in result

#验证就业部时间搜索功能
    mydata = DataParse('../../test_data/data_web.xlsx').parse_excel_datas('employ_time_search')
    @parameterized.parameterized.expand(mydata)
    def test_b8_employ_date(self,tittle,mylist,expected):
        self._testMethodDoc = tittle
        self.reportpage.employ_button()#就业部
        time.sleep(0.5)
        self.reportpage.employ_starttime(mylist[0])
        self.reportpage.employ_endtime(mylist[1])
        self.reportpage.empploy_search()
        time.sleep(0.5)
        result = self.reportpage.look_employ_search()#断言
        assert expected in result








if __name__ == '__main__':
   unittest.main()
#



