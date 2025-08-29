from automation_frame.test_business.web_login_page import LogInPage
from automation_frame.test_parse_data.prase_data import DataParse
from automation_frame.test_business.web_training_resources_page import StrainingPage
import unittest
import time
from parameterized import parameterized
class Training(unittest.TestCase):

    @classmethod
    def setUp(self):
        self.strainingpage=StrainingPage()

    loginfo=DataParse('../../test_data/data_web.xlsx').parse_excel_datas('培训资源资源库下拉框')
    @parameterized.parameterized.expand(loginfo)
    def test_01_Resource_base_drop_down_box(self,arg1,arg2,arg3):
        self._testMethodDoc=arg1
        self.strainingpage.tarin_button()
        self.strainingpage.Resource_base_drop_down_box(arg2[0])

    loginfo = DataParse('../../test_data/data_web.xlsx').parse_excel_datas('培训资源咨询师下拉框')
    @parameterized.parameterized.expand(loginfo)
    def test_02_Consultant_drop_down_box(self, arg1, arg2, arg3):
        self._testMethodDoc = arg1
        self.strainingpage.Consultant_base_drop_down_box(arg2[0])

    loginfo = DataParse('../../test_data/data_web.xlsx').parse_excel_datas('培训资源状态下拉框')
    @parameterized.parameterized.expand(loginfo)
    def test_03_state_drop_down_box(self, arg1, arg2, arg3):
        self._testMethodDoc = arg1
        self.strainingpage.state_base_drop_down_box(arg2[0])

    loginfo = DataParse('../../test_data/data_web.xlsx').parse_excel_datas('培训资源来源下拉框')
    @parameterized.parameterized.expand(loginfo)
    def test_04_source_state_drop_down_box(self, arg1, arg2, arg3):
        self._testMethodDoc = arg1
        self.strainingpage.source_base_drop_down_box(arg2[0])

    loginfo = DataParse('../../test_data/data_web.xlsx').parse_excel_datas('培训资源分配时间输入框')
    @parameterized.parameterized.expand(loginfo)
    def test_05_Assign_time_input_box(self, arg1, arg2, arg3):
        self._testMethodDoc = arg1
        self.strainingpage.Assign_time_input_box(arg2[0])

    loginfo=DataParse('../../test_data/data_web.xlsx').parse_excel_datas('培训资源搜索输入框')
    @parameterized.parameterized.expand(loginfo)
    def test_06_Training_resource_search_input_box(self,arg1,arg2,arg3):
        self._testMethodDoc=arg1
        self.strainingpage.Training_resource_search_input_box(arg2[0])

    def test_07_Training_resource_search_button(self):
        self._testMethodDoc = '培训资源搜索按钮'
        self.strainingpage.Training_resource_search_button()

    def test_08_Training_resource_tracking(self):
        self._testMethodDoc = '培训资源跟踪按钮'
        self.strainingpage.Training_resource_tracking()

    def test_09_Tracking_resources(self):
        self._testMethodDoc = '培训资源跟踪资源'
        self.strainingpage.Tracking_resources()

    loginfo=DataParse('../../test_data/data_web.xlsx').parse_excel_datas('跟踪资源本次状态下拉框')
    @parameterized.parameterized.expand(loginfo)
    def test_10_Tracking_resource_current_status_drop_down_box(self,arg1,arg2,arg3):
        self._testMethodDoc=arg1
        self.strainingpage.Tracking_resource_current_status_drop_down_box(arg2[0])

    loginfo = DataParse('../../test_data/data_web.xlsx').parse_excel_datas('跟踪资源优先级别下拉框')
    @parameterized.parameterized.expand(loginfo)
    def test_11_Tracking_resource_priority_drop_down_box(self, arg1, arg2, arg3):
        self._testMethodDoc = arg1
        self.strainingpage.Tracking_resource_priority_drop_down_box(arg2[0])

    loginfo=DataParse('../../test_data/data_web.xlsx').parse_excel_datas('跟踪资源下次跟踪输入框')
    @parameterized.parameterized.expand(loginfo)
    def test_12_Tracking_resource_next_tracking_input_box(self,arg1,arg2,arg3):
        self._testMethodDoc=arg1
        self.strainingpage.Tracking_resource_next_tracking_input_box(arg2[0])

    loginfo = DataParse('../../test_data/data_web.xlsx').parse_excel_datas('跟踪资源跟踪内容输入框')
    @parameterized.parameterized.expand(loginfo)
    def test_13_Tracking_resource_tracking_content_input_box(self, arg1, arg2, arg3):
        self._testMethodDoc = arg1
        self.strainingpage.Tracking_resource_tracking_content_input_box(arg2[0])

    def test_14_Tracking_resource_saving(self):
        self._testMethodDoc='跟踪资源保存'
        self.strainingpage.Tracking_resource_saving()

    def test_15_Transfer_to_responsible_person(self):
        self._testMethodDoc='进入转交责任人模块'
        self.strainingpage.Transfer_to_responsible_person()

    def test_16_Transfer_to_responsible_person_for_inquiry(self):
        self._testMethodDoc = '转交责任人查询按钮'
        self.strainingpage.Transfer_to_responsible_person_for_inquiry()

    def test_17_Transfer_to_responsible_person_for_check(self):
        self._testMethodDoc = '转交责任人查看按钮'
        self.strainingpage.Transfer_to_responsible_person_for_check()

    loginfo=DataParse('../../test_data/data_web.xlsx').parse_excel_datas('转交责任人提交区域下拉框')
    @parameterized.parameterized.expand(loginfo)
    def test_18_To_be_submitted_by_the_responsible_person(self,arg1,arg2,arg3):
        self._testMethodDoc=arg1
        self.strainingpage.To_be_submitted_by_the_responsible_person(arg2[0])

    def test_19_Allocate_resources(self):
        self._testMethodDoc='进入分配资源'
        self.strainingpage.Allocate_resources()

    loginfo=DataParse('../../test_data/data_web.xlsx').parse_excel_datas('分配资源按比例分配')
    @parameterized.parameterized.expand(loginfo)
    def test_20_Pro_rata_distribution(self,arg1,arg2,arg3):
        self._testMethodDoc=arg1
        self.strainingpage.Pro_rata_distribution(arg2[0],arg2[1],arg2[2],arg2[3],arg2[4])
        assert arg3 in self.strainingpage.assert_Pro_rata_distribution()

    def test_21_Common_resource_pool(self):
        self._testMethodDoc='进入公共资源池'
        self.strainingpage.Common_resource_pool()

    def test_22_Public_resource_claim(self):
        self._testMethodDoc='公共资源认领'
        self.strainingpage.Public_resource_claim()
        assert '认领完成' in self.strainingpage.assert_Public_resource_claim()


