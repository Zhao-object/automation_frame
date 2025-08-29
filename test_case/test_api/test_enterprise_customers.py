from automation_frame.test_business.api_business import Member
from automation_frame.test_parse_config.parse_config import Config
from automation_frame.test_parse_data.prase_data import DataParse
from parameterized import parameterized
import requests,unittest,warnings


class API_enterprise(unittest.TestCase):
    @classmethod
    def setUp(cls):
        warnings.simplefilter("ignore", ResourceWarning)
        print("开始".center(40, "*"))

    loginfo=DataParse('../../test_data/data.xlsx').parse_excel_datas('新增企业')
    @parameterized.parameterized.expand(loginfo)
    def test_add_enterprise(self,arg1,arg2,arg3):  #新增企业
        url=Config('../../test_config_data/config.ini').parse_config('url','add_enterprise')
        self._testMethodDoc = arg1
        response = Member().get_resource_data(url,arg2)
        print('用例标题:', arg1, '响应结果:', response)
        self.assertEqual(response.text, arg3, '失败')


    loginfo=DataParse('../../test_data/data.xlsx').parse_excel_datas('企业客户搜索')
    @parameterized.parameterized.expand(loginfo)
    def test_search(self,arg1,arg2,arg3,arg4):  #搜索
        url=Config('../../test_config_data/config.ini').parse_config('url','Enterprise_search')
        self._testMethodDoc = arg1
        response=Member().post_resource_data_params(url,arg2,arg3)
        print('用例标题:', arg1, '响应结果:', response)
        self.assertIn(arg4,response.text,'失败')

    loginfo=DataParse('../../test_data/data.xlsx').parse_excel_datas('企业修改')
    @parameterized.parameterized.expand(loginfo)
    def test_modify(self,arg1,arg2,arg3):  #企业修改
        url=Config('../../test_config_data/config.ini').parse_config('url','Modify_enterprise')
        self._testMethodDoc = arg1
        response=Member().get_resource_data(url,arg2)
        print('用例标题:', arg1, '响应结果:', response)
        self.assertEqual(response.text,arg3,'失败')



    @classmethod
    def tearDown(cls):
        print("结束".center(40, "*"))


if __name__ == '__main__':
    unittest.main()

