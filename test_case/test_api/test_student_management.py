from automation_frame.test_business.api_business import Member
from automation_frame.test_parse_config.parse_config import Config
from automation_frame.test_parse_data.prase_data import DataParse
import unittest,warnings
from parameterized import parameterized


class TestStuManageApi(unittest.TestCase):
    @classmethod
    def setUp(self):
        warnings.simplefilter("ignore", ResourceWarning)
        print("开始".center(40, "*"))

    #基本信息搜索接口
    mylist1 = DataParse('../../test_data/data.xlsx').parse_excel_datas("基本信息搜索")
    @parameterized.parameterized.expand(mylist1)
    def test_basic_search(self,tittle,data,expected):
        print('期望',expected)
        self._testMethodDoc = tittle
        url = Config('../../test_config_data/config.ini').parse_config("count", "url") + Config('../../test_config_data/config.ini').parse_config("student-url","basic-search")
        result_text = Member().post_text(url=url,data=data)
        print("响应222",result_text)
        assert expected in result_text

    #基本信息查看接口
    mylist1 = DataParse('../../test_data/data.xlsx').parse_excel_datas("基本信息查看")
    @parameterized.parameterized.expand(mylist1)
    def test_basic_query(self,tittle,data,expected):
        self._testMethodDoc = tittle
        url = Config('../../test_config_data/config.ini').parse_config("count", "url") + Config('../../test_config_data/config.ini').parse_config("student-url","basic-query")
        result_text = Member().post_text(url=url,data=data)
        assert expected in result_text
    #
    #基本信息修改接口
    mylist1 = DataParse('../../test_data/data.xlsx').parse_excel_datas("基本信息修改")
    @parameterized.parameterized.expand(mylist1)
    def test_basic_alter(self,tittle,data,expected):
        self._testMethodDoc = tittle
        url = Config('../../test_config_data/config.ini').parse_config("count", "url") + Config('../../test_config_data/config.ini').parse_config("student-url","basic-alter")
        result_text = Member().post_upfile(url,data)
        print("响应结果",result_text)
        assert expected in result_text
    #
    #今日考勤搜索接口
    mylist1 = DataParse('../../test_data/data.xlsx').parse_excel_datas("今日考勤搜索")
    @parameterized.parameterized.expand(mylist1)
    def test_todaycheckon_search(self,tittle,data,expected):
        self._testMethodDoc = tittle
        url = Config('../../test_config_data/config.ini').parse_config("count", "url") + Config('../../test_config_data/config.ini').parse_config("student-url","todaycheckon-search")
        result_text = Member().post_text(url=url,data=data)
        assert expected in result_text
    # # #
    #今日晨考搜索接口
    mylist1 = DataParse('../../test_data/data.xlsx').parse_excel_datas("今日晨考搜索")
    @parameterized.parameterized.expand(mylist1)
    def test_todaymorning_search(self,tittle,data,expected):
        self._testMethodDoc = tittle
        url = Config('../../test_config_data/config.ini').parse_config("count", "url") + Config('../../test_config_data/config.ini').parse_config("student-url","todaymorning-search")
        result_text = Member().post_text(url=url,data=data)
        assert expected in result_text
    #
    #学员请假查询接口接口
    mylist1 = DataParse('../../test_data/data.xlsx').parse_excel_datas("学员请假查询")
    @parameterized.parameterized.expand(mylist1)
    def test_holiday_query(self,tittle,data,expected):
        self._testMethodDoc = tittle
        url = Config('../../test_config_data/config.ini').parse_config("count", "url") + Config('../../test_config_data/config.ini').parse_config("student-url","holiday-query")
        result_text = Member().post_text(url=url,data=data)
        assert expected in result_text
    #
    #学员请假新增请假接口
    mylist1 = DataParse('../../test_data/data.xlsx').parse_excel_datas("学员请假新增请假")
    @parameterized.parameterized.expand(mylist1)
    def test_holiday_add(self,tittle,data,expected):
        self._testMethodDoc = tittle
        url = Config('../../test_config_data/config.ini').parse_config("count", "url") + Config('../../test_config_data/config.ini').parse_config("student-url","holiday-add")
        result_text = Member().post_text(url=url,data=data)
        print('响应666',result_text)
        assert expected in result_text
    #
    #晨考记录查询接口
    mylist1 = DataParse('../../test_data/data.xlsx').parse_excel_datas("晨考记录查询")
    @parameterized.parameterized.expand(mylist1)
    def test_morn_record_query(self,tittle,data,expected):
        self._testMethodDoc = tittle
        url = Config('../../test_config_data/config.ini').parse_config("count", "url") + Config('../../test_config_data/config.ini').parse_config("student-url","morning-record-query")
        result_text = Member().post_text(url=url,data=data)
        assert expected in result_text

    #阶段测评查询接口
    mylist1 = DataParse('../../test_data/data.xlsx').parse_excel_datas("阶段测评查询")
    @parameterized.parameterized.expand(mylist1)
    def test_stage_query(self,tittle,data,expected):
        self._testMethodDoc = tittle
        url = Config('../../test_config_data/config.ini').parse_config("count", "url") + Config('../../test_config_data/config.ini').parse_config("student-url","stage-query")
        result_text = Member().post_text(url=url,data=data)
        assert expected in result_text

    #阶段测评测评接口
    mylist1 = DataParse('../../test_data/data.xlsx').parse_excel_datas("阶段测评测评")
    @parameterized.parameterized.expand(mylist1)
    def test_stage_appraisal(self,tittle,data,expected):
        self._testMethodDoc = tittle
        url = Config('../../test_config_data/config.ini').parse_config("count", "url") + Config('../../test_config_data/config.ini').parse_config("student-url","stage-appraisal")
        result_text = Member().post_text(url=url,data=data)
        assert expected in result_text

    #阶段测评降级接口
    mylist1 = DataParse('../../test_data/data.xlsx').parse_excel_datas("阶段测评降级")
    @parameterized.parameterized.expand(mylist1)
    def test_stage_lower(self, tittle, data, expected):
        self._testMethodDoc = tittle
        url = Config('../../test_config_data/config.ini').parse_config("count", "url") + Config('../../test_config_data/config.ini').parse_config("student-url", "stage-lower")
        result_text = Member().post_text(url=url, data=data)
        assert expected in result_text
    #
    #测评记录查询接口
    mylist1 = DataParse('../../test_data/data.xlsx').parse_excel_datas("测评记录查询")
    @parameterized.parameterized.expand(mylist1)
    def test_appraisallog_query(self, tittle, data, expected):
        self._testMethodDoc = tittle
        url = Config('../../test_config_data/config.ini').parse_config("count", "url") + Config('../../test_config_data/config.ini').parse_config("student-url", "appraisallog-query")
        result_text = Member().post_text(url=url, data=data)
        assert expected in result_text
    #
    # 班级管理查询接口
    mylist1 = DataParse('../../test_data/data.xlsx').parse_excel_datas("班级管理查询")
    @parameterized.parameterized.expand(mylist1)
    def test_classmanage_query(self, tittle, data, expected):
        self._testMethodDoc = tittle
        url = Config('../../test_config_data/config.ini').parse_config("count", "url") + Config('../../test_config_data/config.ini').parse_config("student-url", "classmanage-query")
        result_text = Member().post_text(url=url, data=data)
        assert expected in result_text

    # 班级管理分班确认接口
    mylist1 = DataParse('../../test_data/data.xlsx').parse_excel_datas("班级管理确认")
    @parameterized.parameterized.expand(mylist1)
    def test_classmanage_affirm(self, tittle, data, expected):
        self._testMethodDoc = tittle
        url = Config('../../test_config_data/config.ini').parse_config("count", "url") + Config('../../test_config_data/config.ini').parse_config("student-url", "classmanage-affirm")
        result_text = Member().post_text(url=url, data=data)
        print("最后",result_text)
        assert expected in result_text
    #
    # 课程安排新增排课接口
    mylist1 = DataParse('../../test_data/data.xlsx').parse_excel_datas("课程安排新增排课")
    @parameterized.parameterized.expand(mylist1)
    def test_course_addcourse(self, tittle, data, expected):
        self._testMethodDoc = tittle
        url = Config('../../test_config_data/config.ini').parse_config("count", "url") + Config('../../test_config_data/config.ini').parse_config("student-url", "course-addcourse")
        result_text = Member().post_text(url=url, data=data)
        assert expected in result_text

    # 课程安排修改课程接口
    mylist1 = DataParse('../../test_data/data.xlsx').parse_excel_datas("课程安排修改课程")
    @parameterized.parameterized.expand(mylist1)
    def test_course_updatecourse(self, tittle, data, expected):
        self._testMethodDoc = tittle
        url = Config('../../test_config_data/config.ini').parse_config("count", "url") + Config('../../test_config_data/config.ini').parse_config("student-url", "course-updatecourse")
        result_text = Member().post_text(url=url, data=data)
        print("最后的",result_text)
        assert expected in result_text

    @classmethod
    def tearDown(self):
        print("结束".center(40, "*"))


if __name__ == '__main__':
    unittest.main()





