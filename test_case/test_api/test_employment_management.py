from automation_frame.test_business.api_business import Member
from automation_frame.test_parse_config.parse_config import Config
from automation_frame.test_parse_data.prase_data import DataParse
from parameterized import parameterized
import unittest,warnings

class TestEmployManApi(unittest.TestCase):

    @classmethod
    def setUp(self):
        warnings.simplefilter("ignore", ResourceWarning)
        print("开始".center(40, "*"))

    #就业管理技术面试全部接口
    mylist1 = DataParse('../../test_data/data.xlsx').parse_excel_datas("技术面试全部接口")
    @parameterized.parameterized.expand(mylist1)
    def test_technology_alloption(self,tittle,data,expected):
        self._testMethodDoc = tittle
        url = Config('../../test_config_data/config.ini').parse_config("count", "url") + Config('../../test_config_data/config.ini').parse_config("job-url","technology-alloption")
        result_text = Member().post_text(url,data)
        print("响应结果",result_text)
        assert expected in result_text

    #就业管理技术面试通过接口
    mylist1 = DataParse('../../test_data/data.xlsx').parse_excel_datas("技术面试通过接口")
    @parameterized.parameterized.expand(mylist1)
    def test_technology_passoption(self,tittle,data,expected):
        self._testMethodDoc = tittle
        url = Config('../../test_config_data/config.ini').parse_config("count", "url") + Config('../../test_config_data/config.ini').parse_config("job-url","technology-passoption")
        result_text = Member().post_text(url,data)
        assert expected in result_text
    #
    # 就业管理技术面试未通过接口
    mylist1 = DataParse('../../test_data/data.xlsx').parse_excel_datas("技术面试未通过接口")
    @parameterized.parameterized.expand(mylist1)
    def test_technology_unpassoption(self,tittle,data,expected):
        self._testMethodDoc = tittle
        url = Config('../../test_config_data/config.ini').parse_config("count", "url") + Config('../../test_config_data/config.ini').parse_config("job-url","technology-unpassoption")
        result_text = Member().post_text(url,data)
        assert expected in result_text

    # 就业管理技术面试面试接口
    mylist1 = DataParse('../../test_data/data.xlsx').parse_excel_datas("技术面试面试接口")
    @parameterized.parameterized.expand(mylist1)
    def test_technology_interview(self,tittle,data,expected):
        self._testMethodDoc = tittle
        url = Config('../../test_config_data/config.ini').parse_config("count", "url") + Config('../../test_config_data/config.ini').parse_config("job-url","technology-interview")
        result_text = Member().post_text(url,data)
        print("响应结果",result_text)
        assert expected in result_text

    # 就业管理就业管理搜索接口
    mylist1 = DataParse('../../test_data/data.xlsx').parse_excel_datas("就业管理搜索接口")
    @parameterized.parameterized.expand(mylist1)
    def test_getjob_search(self,tittle,data,expected):
        self._testMethodDoc = tittle
        url = Config('../../test_config_data/config.ini').parse_config("count", "url") + Config('../../test_config_data/config.ini').parse_config("job-url","getjob-search")
        result_text = Member().post_text(url,data)
        print("响应结果",result_text)
        assert expected in result_text
    #
    #就业管理就业管理面试接口(url拼接)返回空
    mylist1 = DataParse('../../test_data/data.xlsx').parse_excel_datas("就业管理面试接口")
    @parameterized.parameterized.expand(mylist1)
    def test_getjob_intersave(self,tittle,data,expected):
        self._testMethodDoc = tittle
        url = Config('../../test_config_data/config.ini').parse_config("count", "url") + Config('../../test_config_data/config.ini').parse_config("job-url","getjob-intersave")
        result_text = Member().get_resource_data(url,data)
        assert expected in result_text.text
    #
    #就业管理就业管理提交接口(url拼接)
    mylist1 = DataParse('../../test_data/data.xlsx').parse_excel_datas("就业管理提交接口")
    @parameterized.parameterized.expand(mylist1)
    def test_getjob_intercommit(self,tittle,data,expected):
        self._testMethodDoc = tittle
        url = Config('../../test_config_data/config.ini').parse_config("count", "url") + Config('../../test_config_data/config.ini').parse_config("job-url","getjob-intercommit")
        result_text = Member().get_resource_data(url,data)
        assert expected in result_text.text

    @classmethod
    def tearDown(self):
        print("结束".center(40, "*"))
if __name__ == '__main__':
    unittest.main()
