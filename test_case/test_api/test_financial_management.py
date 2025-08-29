from automation_frame.test_business.api_business import Member
from automation_frame.test_parse_data.prase_data import DataParse
from automation_frame.test_parse_config.parse_config import Config
from parameterized import parameterized
import unittest
import warnings

class Financial(unittest.TestCase):

    @classmethod
    def setUp(cls):
        warnings.simplefilter("ignore", ResourceWarning)
        print('开始'.center(40,'*'))

    loginfo = DataParse('../../test_data/data.xlsx').parse_excel_datas('财务管理财务流水查询接口')
    @parameterized.parameterized.expand(loginfo)
    def test_The_financial_flow_search_api(self,arg1,arg2,arg3):#财务管理财务流水查询接口
        c_search_url=Config().parse_config('url','c_search_url')
        self._testMethodDoc = arg1
        c_search_result = Member().post_text(url=c_search_url, data=arg2)
        print('用例标题:', arg1, '响应结果:', c_search_result)
        self.assertIn(arg3,c_search_result,'fail')

    loginfo = DataParse('../../test_data/data.xlsx').parse_excel_datas('财务管理财务流水上月本月查询接口')
    @parameterized.parameterized.expand(loginfo)
    def test_last_month_api(self,arg1,arg2,arg3):# 财务管理财务流水上月/本月查询接口
        c_last_month_url=Config().parse_config('url','c_last_month_url')
        self._testMethodDoc = arg1
        c_last_month_result = Member().post_text(url=c_last_month_url, data=arg2)
        print('用例标题:', arg1, '响应结果:', c_last_month_result)
        self.assertIn(arg3,c_last_month_result,'fail')

    loginfo = DataParse('../../test_data/data.xlsx').parse_excel_datas('财务管理财务流水新增流水接口')
    @parameterized.parameterized.expand(loginfo)
    def test_add_running_water_api(self,arg1,arg2,arg3):#财务管理财务流水新增流水接口
        c_add_running_water_url=Config().parse_config('url','c_add_running_water_url')
        self._testMethodDoc = arg1
        c_last_month_result = Member().post_text(url=c_add_running_water_url, data=arg2)
        print('用例标题:', arg1, '响应结果:', c_last_month_result)
        self.assertIn(arg3,c_last_month_result,'fail')

    loginfo = DataParse('../../test_data/data.xlsx').parse_excel_datas('修改接口')
    @parameterized.parameterized.expand(loginfo)
    def test_modification_api(self,arg1,arg2,arg3):#修改接口
        c_modification_url=Config().parse_config('url','c_modification_url')
        self._testMethodDoc = arg1
        c_modification_result = Member().post_text(url=c_modification_url, data=arg2)
        print('用例标题:', arg1, '响应结果:', c_modification_result)
        self.assertEqual(arg3,c_modification_result)

    # 公账导入无接口
    # 以下为财务管理学员缴费接口
    loginfo = DataParse('../../test_data/data.xlsx').parse_excel_datas('学员缴费姓名搜索查询接口')
    @parameterized.parameterized.expand(loginfo)
    def test_name_search_api(self,arg1,arg2,arg3):#学员缴费姓名搜索查询接口
        x_name_search_url=Config().parse_config('url','x_name_search_url')
        self._testMethodDoc = arg1
        x_name_search_result = Member().post_text(url=x_name_search_url, data=arg2)
        print('用例标题:', arg1, '响应结果:', x_name_search_result)
        self.assertIn(arg3,x_name_search_result,'fail')

    loginfo = DataParse('../../test_data/data.xlsx').parse_excel_datas('学员缴费缴费接口')
    @parameterized.parameterized.expand(loginfo)
    def test_pay_the_fees_api(self,arg1,arg2,arg3):#缴费
        x_pay_the_fees_url=Config().parse_config('url','x_pay_the_fees_url')
        self._testMethodDoc = arg1
        x_pay_the_fees_result = Member().post_text(url=x_pay_the_fees_url, data=arg2)
        print('用例标题:', arg1, '响应结果:', x_pay_the_fees_result)
        self.assertIn(arg3, x_pay_the_fees_result,'fail')

    loginfo = DataParse('../../test_data/data.xlsx').parse_excel_datas('学员缴费退费接口')
    @parameterized.parameterized.expand(loginfo)
    def test_return_premium_api(self,arg1,arg2,arg3):#退费
        x_return_premium_url=Config().parse_config('url','x_return_premium_url')
        self._testMethodDoc = arg1
        x_return_premium_result = Member().post_text(url=x_return_premium_url, data=arg2)
        print('用例标题:', arg1, '响应结果:', x_return_premium_result)
        self.assertIn(arg3, x_return_premium_result,'fail')

    @classmethod
    def tearDown(cls):
        print("结束".center(40, "*"))

if __name__ == '__main__':
    unittest.main()