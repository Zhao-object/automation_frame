from automation_frame.test_business.web_login_page import LogInPage
from automation_frame.test_parse_data.prase_data import DataParse
from automation_frame.test_business.web_marketing_management_page import MarketPage
import unittest
import time
from parameterized import parameterized

class Marketing(unittest.TestCase):
    @classmethod
    def setUp(self):
        self.marketpage = MarketPage()

    def test_01markting(self):

        time.sleep(3)
        self.marketpage.marketing()
        assert '新增资源' in self.marketpage.assert_click_marketing()

    loginfo=DataParse('../../test_data/data_web.xlsx').parse_excel_datas('市场营销区域下拉框')
    @parameterized.parameterized.expand(loginfo)
    def test_02_Market_region_drop_down_box (self,arg1,arg2,arg3):
        self._testMethodDoc = arg1
        self.marketpage.region_Dropdownbox(arg2[0])

    loginfo=DataParse('../../test_data/data_web.xlsx').parse_excel_datas('市场营销状态下拉框')
    @parameterized.parameterized.expand(loginfo)
    def test_03_Market_status_drop_down_box(self,arg1,arg2,arg3):
        self._testMethodDoc=arg1
        self.marketpage.state_Dropdownbox(arg2[0])

    def test_04_search(self):
        self._testMethodDoc='搜索'
        self.marketpage.search()
        assert '新入库' in self.marketpage.assert_search()

    # def test_05_Upload_exclusive(self):
    #     self._testMethodDoc='上传专属按钮'
    #     self.marketpage.Upload_exclusive()
    #     assert '上传专属简历' in self.marketpage.assert_Upload_exclusive()
    #
    # loginfo=DataParse('../../test_data/data_web.xlsx').parse_excel_datas("市场营销上传文件")
    # @parameterized.parameterized.expand(loginfo)
    # def test_06_Upload_resume(self,arg1,arg2,arg3):
    #     self._testMethodDoc=arg1
    #     self.marketpage.Upload_resume(arg2[0],arg2[1])

    def test_07_new_network(self):
        self._testMethodDoc='新增网络'
        self.marketpage.new_network()
        assert '新增网络资源' in self.marketpage.assert_new_network()

    loginfo=DataParse('../../test_data/data_web.xlsx').parse_excel_datas('新增网络资源')
    @parameterized.parameterized.expand(loginfo)
    def test_8_New_network_resources(self,arg1,arg2,arg3):
        self._testMethodDoc=arg1
        self.marketpage.new_network_resources(arg2[0],arg2[1],arg2[2])

