from automation_frame.test_business.web_login_page import LogInPage
from automation_frame.test_parse_data.prase_data import DataParse
from automation_frame.test_business.web_financial_management_page import FinancialPage
import unittest
import time
from parameterized import parameterized

class Financial(unittest.TestCase):

    @classmethod
    def setUp(self):
        self.financialpage=FinancialPage()

    def test_01_Enter_the_financial_flow_module(self):
        self._testMethodDoc='进入财务流水模块'
        self.financialpage.Enter_the_financial_flow_module()

    loginfo=DataParse('../../test_data/data_web.xlsx').parse_excel_datas('新增流水资金用途输入框')
    @parameterized.parameterized.expand(loginfo)
    def test_02_New_flow(self,arg1,arg2,arg3):
        self._testMethodDoc=arg1
        self.financialpage.New_flow(arg2[0])

    loginfo=DataParse('../../test_data/data_web.xlsx').parse_excel_datas('流水记录修改')
    @parameterized.parameterized.expand(loginfo)
    def test_03_Revision_of_flow_record(self,arg1,arg2,arg3):
        self._testMethodDoc=arg1
        result=self.financialpage.Revision_of_flow_record(arg2)
        assert result in arg3