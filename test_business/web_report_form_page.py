from automation_frame.test_business.web_base_page import BasePage
from automation_frame.test_parse_config.parse_config import Config#读取配置
from selenium.common.exceptions import NoSuchElementException
import time
#报表中心页面
class ReportFormPage(BasePage):

    def __init__(self):
        super(ReportFormPage, self).__init__()
        self.config = Config('../../test_config_data/config_web.ini')
    #报表中心
    def report_button(self):
        locator = self.config.parse_config('report', 'report_locator')
        self.click(*locator)
    #解密按钮
    def decode_button(self):
        locator = self.config.parse_config('report','decode_locator')
        self.click(*locator)

    #解密输入框
    def decode_input_text(self,text):
        locator = self.config.parse_config('report', 'decode_input_text_locator')
        self.input_text(*locator,value=text)

    #解密确认按钮
    def decode_affirm(self):
        locator = self.config.parse_config('report', 'decode_affirm_locator')
        self.click(*locator)

    #解密失败确认按钮
    def decode_faile_affirm(self):
        locator = self.config.parse_config('report','decode_faile_locator')
        self.click(*locator)

    #解密取消按钮
    def decode_cancel_button(self):
        locator = self.config.parse_config('report','cancel_locator')
        self.click(*locator)

###解密断言###
    def look_decode(self,*locator):
        error_locator = self.config.parse_config('report','look_decode_locator')
        time.sleep(1)
        try:
            result = self.get_ele_text(*error_locator)
        except Exception as ex:
            print('没有定位到提示解密失败信息',ex)
            # 点击取消
            self.decode_cancel_button()
            return '解密密码success,但解密失败'
        else:
            #点击确定
            self.decode_faile_affirm()
            #点击取消
            self.decode_cancel_button()
            return result

    #咨询部按钮
    def consult_button(self):
        locator = self.config.parse_config('report', 'consult_locator')
        self.click(*locator)

    #咨询部开始时间输入框
    def consult_start_time_input(self,text):
        locator = self.config.parse_config('report', 'consult_start_time_locator')
        self.input_text(*locator,value=text)

    #咨询部结束时间输入框
    def consult_end_time_input(self,text):
        locator = self.config.parse_config('report', 'consult_end_time_locator')
        self.input_text(*locator,value=text)

    #咨询部搜索按钮
    def consult_search_button(self):
        locator = self.config.parse_config('report', 'consult_search_locator')
        self.click(*locator)
###咨询部时间搜索断言###
    def look_consult_time_search(self):
        #获得成都元素
        locator = self.config.parse_config('report', 'consult_CD_locator')
        try:
            result = self.get_ele_text(*locator)
        except NoSuchElementException:
            print("搜索失败",ex)
            return '搜索失败啦'
        else:
            return result

    #咨询部当期按钮
    def consult_date_button(self):
        locator = self.config.parse_config('report', 'consult_date_locator')
        self.click(*locator)
###当期功能断言###
    def look_consult_date(self):
        #获取西安元素
        locator = self.config.parse_config('report','consult_XA_locator')
        try:
            result = self.get_ele_text(*locator)
        except NoSuchElementException:
            print("没有定位到西安元素")
            return '当期功能失败啦'
        else:
            return result

    #电销部按钮
    def phone_sell_button(self):
        locator = self.config.parse_config('report', 'phone_sell_locator')
        self.click(*locator)

    #电销部时间开始
    def phone_sell_starttime(self,text):
        locator = self.config.parse_config('report', 'phone_start_time_locator')
        self.input_text(*locator,value=text)

    #电销部时间结束
    def phone_sell_endtime(self,text):
        locator = self.config.parse_config('report', 'phone_end_time_locator')
        self.input_text(*locator,value=text)

    #电销部搜索按钮
    def phone_sell_search_button(self):
        locator = self.config.parse_config('report', 'phone_search_locator')
        self.click(*locator)

###电销部搜索断言###
    def look_phone_time_search(self):
        locator = self.config.parse_config('report','phone_sell_CQ_locator')
        try:
            result = self.get_ele_text(*locator)
        except NoSuchElementException:
            print("没有定位到重庆元素")
            return '时间搜索失败'
        else:
            return result



    #电销部当期按钮
    def phone_sell_date(self):
        locator = self.config.parse_config('report', 'phone_date_locator')
        self.click(*locator)

    ###电销部当期功能断言###
    def look_phone_date(self):
        # 获取报名转换率元素
        locator = self.config.parse_config('report', 'phone_sell_BM_locator')
        try:
            result = self.get_ele_text(*locator)
        except NoSuchElementException:
            print("没有定位到报名转换率元素")
            return '搜索功能失败啦'
        else:
            return result

    #市场部按钮
    def market_button(self):
        locator = self.config.parse_config('report', 'market_locator')
        self.click(*locator)

    #市场部开始时间
    def market_starttime(self,text):
        locator = self.config.parse_config('report', 'market_start_time_locator')
        self.input_text(*locator,value=text)

    # 市场部结束时间
    def market_endtime(self,text):
        locator = self.config.parse_config('report', 'market_end_time_locator')
        self.input_text(*locator,value=text)

    #市场部搜索按钮
    def market_search(self):
        locator = self.config.parse_config('report', 'market_search_locator')
        self.click(*locator)

    #市场部当期按钮
    def market_date(self):
        locator = self.config.parse_config('report', 'market_date_locator')
        self.click(*locator)

###市场部时间搜索断言###
    def look_market_time_search(self):
        locator = self.config.parse_config('report', 'market_search_all_locator')
        try:
            result = self.get_attribute_outer(*locator)
        except NoSuchElementException:
            print("没有定位到重庆元素")
            return '时间搜索失败'
        else:
            return result

###市场部当期按钮断言###
    def look_market_date(self):
        locator = self.config.parse_config('report', 'market_date_locator')
        try:
            result = self.get_attribute_outer(*locator)
        except NoSuchElementException:
            print("没有定位到重庆元素")
            return '时间搜索失败'
        else:
            return result

    #市场部今日按钮
    def market_today_button(self):
        locator = self.config.parse_config('report', 'market_today_locator')
        self.click(*locator)

###市场部今日按钮断言###
    def look_market_today(self):
        locator = self.config.parse_config('report', 'market_look_today_locator')
        try:
            result = self.get_attribute_outer(*locator)
        except NoSuchElementException:
            print("没有定位到重庆元素")
            return '时间搜索失败'
        else:
            return result

    #市场部本周按钮
    def market_this_week(self):
        locator = self.config.parse_config('report', 'market_this_week_locator')
        self.click(*locator)

###市场部本周按钮断言###
    def look_market_this_week(self):
        locator = self.config.parse_config('report', 'market_look_today_locator')
        try:
            result = self.get_attribute_outer(*locator)
        except NoSuchElementException:
            print("没有定位到重庆元素")
            return '时间搜索失败'
        else:
            return result

    # 市场部本月按钮
    def market_this_month(self):
        locator = self.config.parse_config('report', 'market_this_month_locator')
        self.click(*locator)

###市场部本月按钮断言###
    def look_market_this_month(self):
        locator = self.config.parse_config('report', 'market_look_today_locator')
        try:
            result = self.get_attribute_outer(*locator)
        except NoSuchElementException:
            print("没有定位到重庆元素")
            return '时间搜索失败'
        else:
            return result

    # 市场部上周按钮
    def market_last_week(self):
        locator = self.config.parse_config('report', 'market_last_week_locator')
        self.click(*locator)

###市场部上周按钮断言###
    def look_market_last_week(self):
        locator = self.config.parse_config('report', 'market_look_today_locator')
        try:
            result = self.get_attribute_outer(*locator)
        except NoSuchElementException:
            print("没有定位到重庆元素")
            return '时间搜索失败'
        else:
            return result

    # 市场部上月按钮
    def market_last_month(self):
        locator = self.config.parse_config('report', 'market_last_month_locator')
        self.click(*locator)

###市场部上月按钮断言###
    def look_market_last_month(self):
        locator = self.config.parse_config('report', 'market_look_today_locator')
        try:
            result = self.get_attribute_outer(*locator)
        except NoSuchElementException:
            print("没有定位到重庆元素")
            return '时间搜索失败'
        else:
            return result

    # 市场部本年按钮
    def market_this_year(self):
        locator = self.config.parse_config('report', 'market_this_year_locator')
        self.click(*locator)

###市场部本年按钮断言###
    def look_market_this_year(self):
        locator = self.config.parse_config('report', 'market_look_today_locator')
        try:
            result = self.get_attribute_outer(*locator)
        except NoSuchElementException:
            print("没有定位到重庆元素")
            return '时间搜索失败'
        else:
            return result

    #教学部按钮
    def teach_button(self):
        locator = self.config.parse_config('report', 'teach_locator')
        self.click(*locator)

###教学部按钮断言###
    def look_teach_function(self):
        locator = self.config.parse_config('report', 'area_locator')
        try:
            result = self.get_ele_text(*locator)
        except NoSuchElementException:
            print("没有定位到分区域显示元素")
            return '功能失败'
        else:
            return result

    #成都按钮
    def teach_CD_button(self):
        locator = self.config.parse_config('report', 'chengdu_locator')
        self.click(*locator)

###成都按钮断言###
    def look_teach_CD(self):
        locator = self.config.parse_config('report', 'class_locator')
        try:
            result = self.get_ele_text(*locator)
        except NoSuchElementException:
            print("没有定位到班级元素")
            return '功能失败'
        else:
            return result

    #成都下的第一个班级按钮
    def class_button(self):
        locator = self.config.parse_config('report', 'class_locator')
        self.click(*locator)

###成都下第一个班级按钮断言###
    def look_CD_class(self):
        locator = self.config.parse_config('report', 'class_decide_locator')
        try:
            result = self.get_ele_text(*locator)
        except NoSuchElementException:
            print("没有定位到canvas元素")
            return '功能失败'
        else:
            return result

    #重庆按钮
    def teach_CQ_button(self):
        locator = self.config.parse_config('report', 'chongqing_locator')
        self.click(*locator)

    #西安按钮
    def teach_CQ_button(self):
        locator = self.config.parse_config('report', 'xian_locator')
        self.click(*locator)

    #就业部按钮
    def employ_button(self):
        locator = self.config.parse_config('report', 'employ_locator')
        self.click(*locator)

    #就业部开始时间
    def employ_starttime(self,text):
        locator = self.config.parse_config('report', 'employ_start_time_locator')
        self.input_text(*locator,value=text)

    #就业部结束时间
    def employ_endtime(self,text):
        locator = self.config.parse_config('report', 'employ_end_time_locator')
        self.input_text(*locator,value=text)

    #就业部搜索按钮
    def empploy_search(self):
        locator = self.config.parse_config('report', 'employ_search_locator')
        self.click(*locator)

###就业部时间搜索功能断言###
    def look_employ_search(self):
        locator = self.config.parse_config('report', 'employ_search_decide_locator')
        try:
            result = self.get_ele_text(*locator)
        except NoSuchElementException:
            print("没有定位到元素")
            return '功能失败'
        else:
            return result

###断言部分###

