from automation_frame.test_business.api_business import Member
from automation_frame.test_parse_config.parse_config import Config
from automation_frame.test_parse_data.prase_data import DataParse
from parameterized import parameterized
import requests,unittest,warnings

class API_train(unittest.TestCase):
    @classmethod
    def setUp(self):
        warnings.simplefilter("ignore", ResourceWarning)
        print("开始".center(40, "*"))

    loginfo=DataParse('../../test_data/data.xlsx').parse_excel_datas('培训资源搜索')
    @parameterized.parameterized.expand(loginfo)
    def test_resources_search(self,arg1,arg2,arg3):  #培训资源搜索
        url=Config('../../test_config_data/config.ini').parse_config('url','Training_search')
        self._testMethodDoc = arg1
        response=Member().post_text(url,arg2)
        print('用例标题:', arg1, '响应结果:', response)
        self.assertIn(arg3,response,'失败')

    loginfo=DataParse('../../test_data/data.xlsx').parse_excel_datas('培训资源新增')
    @parameterized.parameterized.expand(loginfo)
    def test_resources_add(self,arg1,arg2,arg3):  #培训资源新增
        url=Config('../../test_config_data/config.ini').parse_config('url','Training_add')
        self._testMethodDoc = arg1
        response=Member().post_text(url,arg2)
        print(response)
        print('用例标题:', arg1, '响应结果:', response)
        self.assertEqual(response,arg3,'失败')

    loginfo=DataParse('../../test_data/data.xlsx').parse_excel_datas('跟踪资源')
    @parameterized.parameterized.expand(loginfo)
    def test_Track_resources(self,arg1,arg2,arg3): #跟踪资源
        url=Config('../../test_config_data/config.ini').parse_config('url','Track_resources')
        self._testMethodDoc = arg1
        response=Member().post_text(url,arg2)
        self.assertIn(arg3,response,'失败')

    loginfo=DataParse('../../test_data/data.xlsx').parse_excel_datas('培训资源修改')
    @parameterized.parameterized.expand(loginfo)
    def test_Training_modify(self,arg1,arg2,arg3): #培训资源修改
        url=Config('../../test_config_data/config.ini').parse_config('url','Training_modify')
        self._testMethodDoc = arg1
        response=Member().post_text(url,arg2)
        self.assertIn(arg3,response,'失败')

    loginfo = DataParse('../../test_data/data.xlsx').parse_excel_datas('培训资源废弃')
    @parameterized.parameterized.expand(loginfo)
    def test_Waste_training(self, arg1, arg2, arg3):  # 培训资源废弃
        url = Config('../../test_config_data/config.ini').parse_config('url', 'Waste_training')
        self._testMethodDoc = arg1
        response = Member().post_text(url, arg2)
        self.assertIn(arg3,response,'失败')

    loginfo = DataParse('../../test_data/data.xlsx').parse_excel_datas('转交责任人查询')
    @parameterized.parameterized.expand(loginfo)
    def test_Transfer_inquiry(self, arg1, arg2, arg3):  # 转交责任人查询
        url = Config('../../test_config_data/config.ini').parse_config('url', 'Transfer_inquiry')
        self._testMethodDoc = arg1
        response = Member().post_text(url, arg2)
        self.assertIn(arg3,response,'失败')

    loginfo = DataParse('../../test_data/data.xlsx').parse_excel_datas('转交责任人查看')
    @parameterized.parameterized.expand(loginfo)
    def test_Transfer_show(self, arg1, arg2, arg3):  # 转交责任人查看
        url = Config('../../test_config_data/config.ini').parse_config('url', 'Transfer_show')
        self._testMethodDoc = arg1
        response = Member().post_text(url, arg2)
        self.assertIn( arg3, response,'失败')

    loginfo = DataParse('../../test_data/data.xlsx').parse_excel_datas('转交责任人提交')
    @parameterized.parameterized.expand(loginfo)
    def test_Transfer_submit(self, arg1, arg2, arg3):  # 转交责任人提交
        url = Config('../../test_config_data/config.ini').parse_config('url', 'Transfer_submit')
        self._testMethodDoc = arg1
        response = Member().post_text(url,arg2)
        self.assertIn( arg3, response,'失败')

    loginfo = DataParse('../../test_data/data.xlsx').parse_excel_datas('分配资源查询')
    @parameterized.parameterized.expand(loginfo)
    def test_Allocate_resource_query(self, arg1, arg2, arg3):  # 分配资源查询
        url = Config('../../test_config_data/config.ini').parse_config('url', 'Allocate_resource_query')
        self._testMethodDoc = arg1
        response = Member().post_text(url, arg2)
        self.assertIn(arg3,response,'失败')

    # loginfo = DataParse('../../test_data/data.xlsx').parse_excel_datas('分配资源提交')
    # @parameterized.parameterized.expand(loginfo)
    # def test_Allocate_resource_submission(self, arg1, arg2, arg3):  # 分配资源提交
    #     url = Config('../../test_config_data/config.ini').parse_config('url', 'Allocate_resource_submission')
    #     self._testMethodDoc = arg1
    #     response = Member().post_status(url,arg2)
    #     self.assertEqual(response,200,'失败')

    loginfo = DataParse('../../test_data/data.xlsx').parse_excel_datas('按比例分配')
    @parameterized.parameterized.expand(loginfo)
    def test_Prorated_distribution(self, arg1, arg2, arg3):  # 按比例分配
        url = Config('../../test_config_data/config.ini').parse_config('url', 'Prorated_distribution')
        self._testMethodDoc = arg1
        response = Member().post_text(url, arg2)
        self.assertIn(arg3,response,'失败')

    loginfo = DataParse('../../test_data/data.xlsx').parse_excel_datas('公共资源查询')
    @parameterized.parameterized.expand(loginfo)
    def test_Public_resource_query(self, arg1, arg2, arg3):  # 公共资源查询
        url = Config('../../test_config_data/config.ini').parse_config('url', 'Public_resource_query')
        self._testMethodDoc = arg1
        response = Member().post_text(url, arg2)
        self.assertIn(arg3,response, '失败')

    loginfo = DataParse('../../test_data/data.xlsx').parse_excel_datas('公共资源认领')
    @parameterized.parameterized.expand(loginfo)
    def test_Public_resource_claim(self, arg1, arg2, arg3):  # 公共资源认领
        url = Config('../../test_config_data/config.ini').parse_config('url', 'Public_resource_claim')
        self._testMethodDoc = arg1
        response = Member().post_text(url, arg2)
        self.assertIn(arg3,response,'失败')




    @classmethod
    def tearDown(cls):
        print("结束".center(40, "*"))

if __name__ == '__main__':
    unittest.main()