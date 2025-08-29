
from automation_frame.test_business.api_business import Member
from automation_frame.test_parse_data.prase_data import DataParse
from automation_frame.test_parse_config.parse_config import Config
from parameterized import parameterized
import unittest,warnings

class ReportForms(unittest.TestCase):

    @classmethod
    def setUp(cls):
        warnings.simplefilter("ignore",ResourceWarning)
        print('开始'.center(40,'*'))

    loginfo=DataParse('../../test_data/data.xlsx').parse_excel_datas('报表中心咨询部搜索接口')
    @parameterized.parameterized.expand(loginfo)
    def test01_search_api(self,arg1,arg2,arg3):# 报表中心咨询部搜索接口
        self._testMethodDoc = arg1
        search_url=Config('../../test_config_data/config.ini').parse_config('url','search_url')
        search_result = Member().post_text(url=search_url,data=arg2)
        print('用例标题:', arg1, '响应结果:', search_result)
        self.assertIn(arg3,search_result,'fail')

    loginfo = DataParse('../../test_data/data.xlsx').parse_excel_datas('报表中心咨询部当期接口')
    @parameterized.parameterized.expand(loginfo)
    def test02_current_period_api(self,arg1,arg2,arg3):# 报表中心咨询部当期接口
        self._testMethodDoc = arg1
        current_period_url=Config('../../test_config_data/config.ini').parse_config('url','current_period_url')
        current_period_result=Member().post_text(url=current_period_url,data=arg2)
        print('用例标题:', arg1, '响应结果:', current_period_result)
        self.assertIn(arg3, current_period_result, 'fail')

    loginfo = DataParse('../../test_data/data.xlsx').parse_excel_datas('报表中心咨询部今日接口')
    @parameterized.parameterized.expand(loginfo)
    def test03_today_api(self,arg1,arg2,arg3):# 报表中心咨询部今日接口
        self._testMethodDoc = arg1
        today_url=Config('../../test_config_data/config.ini').parse_config('url','today_url')
        today_result=Member().post_text(url=today_url,data=arg2)
        print('用例标题:', arg1, '响应结果:', today_result)
        self.assertIn(arg3, today_result, 'fail')

    loginfo = DataParse('../../test_data/data.xlsx').parse_excel_datas('报表中心咨询部本周接口')
    @parameterized.parameterized.expand(loginfo)
    def test04_week_api(self,arg1,arg2,arg3):# 报表中心咨询部本周接口
        week_url = Config('../../test_config_data/config.ini').parse_config('url','week_url')
        week_result = Member().post_text(url=week_url, data=arg2)
        self._testMethodDoc = arg1
        print('用例标题:', arg1, '响应结果:', week_result)
        self.assertIn('"employee_name":"倪雪"', week_result, 'fail')

    loginfo = DataParse('../../test_data/data.xlsx').parse_excel_datas('报表中心咨询部本月接口')
    @parameterized.parameterized.expand(loginfo)
    def test05_month_api(self,arg1,arg2,arg3):# 报表中心咨询部本月接口
        month_url = Config('../../test_config_data/config.ini').parse_config('url','month_url')
        month_result = Member().post_text(url=month_url, data=arg2)
        self._testMethodDoc = arg1
        print('用例标题:', arg1, '响应结果:', month_result)
        self.assertIn('"employee_name":"倪雪"', month_result, 'fail')

    loginfo = DataParse('../../test_data/data.xlsx').parse_excel_datas('报表中心咨询部上周接口')
    @parameterized.parameterized.expand(loginfo)
    def test06_lastweek_api(self,arg1,arg2,arg3):# 报表中心咨询部上周接口
        lastweek_url = Config('../../test_config_data/config.ini').parse_config('url','lastweek_url')
        lastweek_result = Member().post_text(url=lastweek_url, data=arg2)
        self._testMethodDoc = arg1
        print('用例标题:', arg1, '响应结果:', lastweek_result)
        self.assertIn('"employee_name":"倪雪"', lastweek_result, 'fail')

    loginfo = DataParse('../../test_data/data.xlsx').parse_excel_datas('报表中心咨询部上月接口')
    @parameterized.parameterized.expand(loginfo)
    def test07_lastmonth_api(self,arg1,arg2,arg3):# 报表中心咨询部上月接口
        lastmonth_url = Config('../../test_config_data/config.ini').parse_config('url','lastmonth_url')
        lastmonth_result = Member().post_text(url=lastmonth_url, data=arg2)
        self._testMethodDoc = arg1
        print('用例标题:', arg1, '响应结果:', lastmonth_result)
        self.assertIn('"employee_name":"倪雪"', lastmonth_result, 'fail')

    loginfo = DataParse('../../test_data/data.xlsx').parse_excel_datas('报表中心咨询部本年接口')
    @parameterized.parameterized.expand(loginfo)
    def test08_year_api(self,arg1,arg2,arg3):# 报表中心咨询部本年接口
        year_url = Config('../../test_config_data/config.ini').parse_config('url','year_url')
        year_result = Member().post_text(url=year_url, data=arg2)
        self._testMethodDoc = arg1
        print('用例标题:', arg1, '响应结果:', year_result)
        self.assertIn('"employee_name":"倪雪"', year_result, 'fail')

    # 报表中心咨询部接口=报表中心电销部接口
    # -------------------------以下为报表中心市场部接口-------------------------

    loginfo = DataParse('../../test_data/data.xlsx').parse_excel_datas('报表中心市场部搜索接口')
    @parameterized.parameterized.expand(loginfo)
    def test09_s_search_api(self,arg1,arg2,arg3):# 报表中心市场部搜索接口
        s_search_url=Config('../../test_config_data/config.ini').parse_config('url','s_search_url')
        s_search_result=Member().post_text(url=s_search_url,data=arg2)
        self._testMethodDoc = arg1
        print('用例标题:', arg1, '响应结果:', s_search_result)
        self.assertIn(arg3,s_search_result,'fail')


    loginfo = DataParse('../../test_data/data.xlsx').parse_excel_datas('报表中心市场部当期接口')
    @parameterized.parameterized.expand(loginfo)
    def test10_s_current_period_api(self,arg1,arg2,arg3):# 报表中心市场部当期接口
        s_current_period_url=Config('../../test_config_data/config.ini').parse_config('url','s_current_period_url')
        s_current_period_result=Member().post_text(url=s_current_period_url,data=arg2)
        self._testMethodDoc = arg1
        print('用例标题:', arg1, '响应结果:', s_current_period_result)
        self.assertIn('', s_current_period_result, 'fail')

    loginfo = DataParse('../../test_data/data.xlsx').parse_excel_datas('报表中心市场部今日接口')
    @parameterized.parameterized.expand(loginfo)
    def test11_s_today_api(self,arg1,arg2,arg3):# 报表中心市场部今日接口
        s_today_url=Config('../../test_config_data/config.ini').parse_config('url','s_today_url')
        s_today_result=Member().post_text(url=s_today_url,data=arg2)
        self._testMethodDoc = arg1
        print('用例标题:', arg1, '响应结果:', s_today_result)
        self.assertIn('',s_today_result,'fail')

    loginfo = DataParse('../../test_data/data.xlsx').parse_excel_datas('报表中心市场部本周接口')
    @parameterized.parameterized.expand(loginfo)
    def test12_s_week_api(self,arg1,arg2,arg3):# 报表中心市场部本周接口
        s_week_url = Config('../../test_config_data/config.ini').parse_config('url','s_week_url')
        s_week_result = Member().post_text(url=s_week_url, data=arg2)
        self._testMethodDoc = arg1
        print('用例标题:', arg1, '响应结果:', s_week_result)
        self.assertIn('', s_week_result, 'fail')


    loginfo = DataParse('../../test_data/data.xlsx').parse_excel_datas('报表中心市场部本月接口')
    @parameterized.parameterized.expand(loginfo)
    def test13_s_month_api(self,arg1,arg2,arg3):# 报表中心市场部本月接口
        s_month_url = Config('../../test_config_data/config.ini').parse_config('url','s_month_url')
        s_month_result = Member().post_text(url=s_month_url, data=arg2)
        self._testMethodDoc = arg1
        print('用例标题:', arg1, '响应结果:', s_month_result)
        self.assertIn('', s_month_result, 'fail')

    loginfo = DataParse('../../test_data/data.xlsx').parse_excel_datas('报表中心市场部上周接口')
    @parameterized.parameterized.expand(loginfo)
    def test14_s_lastweek_api(self,arg1,arg2,arg3):# 报表中心市场部上周接口
        s_lastweek_url = Config('../../test_config_data/config.ini').parse_config('url','s_lastweek_url')
        s_lastweek_result = Member().post_text(url=s_lastweek_url, data=arg2)
        self._testMethodDoc = arg1
        print('用例标题:', arg1, '响应结果:', s_lastweek_result)
        self.assertIn('', s_lastweek_result, 'fail')

    loginfo = DataParse('../../test_data/data.xlsx').parse_excel_datas('报表中心市场部上月接口')
    @parameterized.parameterized.expand(loginfo)
    def test15_s_lastmonth_api(self,arg1,arg2,arg3):# 报表中心市场部上月接口
        s_lastmonth_url = Config('../../test_config_data/config.ini').parse_config('url','s_lastmonth_url')
        s_lastmonth_result = Member().post_text(url=s_lastmonth_url, data=arg2)
        self._testMethodDoc = arg1
        print('用例标题:', arg1, '响应结果:', s_lastmonth_result)
        self.assertIn('', s_lastmonth_result, 'fail')

    loginfo = DataParse('../../test_data/data.xlsx').parse_excel_datas('报表中心市场部本年接口')
    @parameterized.parameterized.expand(loginfo)
    def test16_s_year_api(self,arg1,arg2,arg3):# 报表中心市场部本年接口
        s_year_url = Config('../../test_config_data/config.ini').parse_config('url','s_year_url')
        s_year_result = Member().post_text(url=s_year_url, data=arg2)
        self._testMethodDoc = arg1
        print('用例标题:', arg1, '响应结果:', s_year_result)
        self.assertIn('', s_year_result, 'fail')


    # -----------报表中心教学部无接口-----------
    # -----------以下为报表中心教学部接口-----------

    loginfo = DataParse('../../test_data/data.xlsx').parse_excel_datas('报表中心就业部搜索接口')
    @parameterized.parameterized.expand(loginfo)
    def test17_job_search_api(self,arg1,arg2,arg3):  # 报表中心就业部搜索接口
        j_search_url = Config('../../test_config_data/config.ini').parse_config('url','j_search_url')
        j_search_result = Member().post_text(url=j_search_url, data=arg2)
        self._testMethodDoc = arg1
        print('用例标题:', arg1, '响应结果:', j_search_result)
        self.assertIn('', j_search_result, 'fail')



    loginfo = DataParse('../../test_data/data.xlsx').parse_excel_datas('报表中心就业部今日接口')
    @parameterized.parameterized.expand(loginfo)
    def test18_job_today_api(self,arg1,arg2,arg3):  # 报表中心就业部今日接口
        j_today_url = Config('../../test_config_data/config.ini').parse_config('url','j_today_url')
        j_today_result = Member().post_text(url=j_today_url, data=arg2)
        self._testMethodDoc = arg1
        print('用例标题:', arg1, '响应结果:', j_today_result)
        self.assertIn('', j_today_result, 'fail')

    loginfo = DataParse('../../test_data/data.xlsx').parse_excel_datas('报表中心就业部本周接口')
    @parameterized.parameterized.expand(loginfo)
    def test19_job_week_api(self,arg1,arg2,arg3):  # 报表中心就业部本周接口
        j_week_url = Config('../../test_config_data/config.ini').parse_config('url','j_week_url')
        j_week_result = Member().post_text(url=j_week_url, data=arg2)
        self._testMethodDoc = arg1
        print('用例标题:', arg1, '响应结果:', j_week_result)
        self.assertIn('', j_week_result, 'fail')

    loginfo = DataParse('../../test_data/data.xlsx').parse_excel_datas('报表中心就业部本月接口')
    @parameterized.parameterized.expand(loginfo)
    def test20_job_month_api(self,arg1,arg2,arg3):  # 报表中心就业部本月接口
        j_month_url = Config('../../test_config_data/config.ini').parse_config('url','j_month_url')
        j_month_result = Member().post_text(url=j_month_url, data=arg2)
        print('用例标题:', arg1, '响应结果:', j_month_result)
        self.assertIn('', j_month_result, 'fail')
        self._testMethodDoc = arg1

    loginfo = DataParse('../../test_data/data.xlsx').parse_excel_datas('报表中心就业部上周接口')
    @parameterized.parameterized.expand(loginfo)
    def test21_job_lastweek_api(self,arg1,arg2,arg3):  # 报表中心就业部上周接口
        j_lastweek_url = Config('../../test_config_data/config.ini').parse_config('url','j_lastweek_url')
        j_lastweek_result = Member().post_text(url=j_lastweek_url, data=arg2)
        print('用例标题:', arg1, '响应结果:', j_lastweek_result)
        self.assertIn('', j_lastweek_result, 'fail')
        self._testMethodDoc = arg1

    loginfo = DataParse('../../test_data/data.xlsx').parse_excel_datas('报表中心就业部上月接口')
    @parameterized.parameterized.expand(loginfo)
    def test22_job_lastmonth_api(self,arg1,arg2,arg3):  # 报表中心就业部上月接口
        j_lastmonth_url = Config('../../test_config_data/config.ini').parse_config('url','j_lastmonth_url')
        j_lastmonth_result = Member().post_text(url=j_lastmonth_url, data=arg2)
        print('用例标题:', arg1, '响应结果:', j_lastmonth_result)
        self.assertIn('', j_lastmonth_result, 'fail')
        self._testMethodDoc = arg1

    loginfo = DataParse('../../test_data/data.xlsx').parse_excel_datas('报表中心就业部本年接口')
    @parameterized.parameterized.expand(loginfo)
    def test23_job_year_api(self,arg1,arg2,arg3):  # 报表中心就业部本年接口
        j_year_url = Config('../../test_config_data/config.ini').parse_config('url','j_year_url')
        j_year_result = Member().post_text(url=j_year_url, data=arg2)
        self._testMethodDoc = arg1
        print('用例标题:', arg1, '响应结果:', j_year_result)
        self.assertIn('', j_year_result, 'fail')

    @classmethod
    def tearDown(cls):
        print("结束".center(40, "*"))

if __name__ == '__main__':
    unittest.main()


