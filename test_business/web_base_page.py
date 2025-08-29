from automation_frame.test_commen.webdriver import WebDriverDriven
from selenium.webdriver.support.select import Select

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from selenium.common.exceptions import NoSuchElementException
import uiautomation

#被继承的基础类(不传入元素配置的元素及其操作们)
class BasePage:

    #打开网页
    def __init__(self):
        self.driver = WebDriverDriven.get_driver()

    #定位元素,返回元素对象!
    def find_element(self,*locator):
        return self.driver.find_element(*locator)

    #定位元素,输入text文本!
    def input_text(self,*locator,value):
        self.find_element(*locator).send_keys(value)

    #定位元素,点击该元素!
    def click(self,*locator):
        self.find_element(*locator).click()

    #定位元素,返回get_attribute('innerHTML')结果!
    def get_attribute_inner(self,*locator):
        return self.find_element(*locator).get_attribute('innerHTML')#获取元素内所有HTML

    #位元素,返回get_attribute('outerHTML')结果1
    def get_attribute_outer(self, *locator):
        return self.find_element(*locator).get_attribute('outerHTML')#获取包含元素的所有HTML


    # 定位元素,返回get_attribute('textContent')结果!
    def get_attribute_textContent(self, *locator):
        return self.find_element(*locator).get_attribute('textContent')#获取元素内的文本内容(一层)

    # 定位元素,返回get_attribute('value')结果!
    def get_attribute_value(self, *locator):
        return self.find_element(*locator).get_attribute('value')  #获取元素的value属性的值

    # #定位元素
    # def get_pro(self,*locator):
    #     return self.find_element(*locator).get_property()

    #定位元素,返回元素文本值!
    def get_ele_text(self,*locator):
        return self.find_element(*locator).text

    #定位元素,清空该元素输入框!
    def ele_text_clear(self,*locator):
        self.find_element(*locator).clear()

    #返回WebDriverWait.until
    def get_WebDriverWait(self):
        return WebDriverWait(self.driver,10,1).until

    #返回等待到的弹窗
    def wait_now_alert(self):
        return self.get_WebDriverWait()(EC.alert_is_present())

    #取消等待到的弹窗
    def dismiss_wait_alert(self):
        self.wait_now_alert().dismiss()

    #定位弹窗,返回弹窗对象!
    def get_alert_object(self):
        alert = self.driver.switch_to.alert
        return alert


    #弹窗点击确定!
    def alert_confirm(self):
        self.get_alert_object().accept()

    #弹窗点击取消!
    def alert_cancel(self):
        self.get_alert_object().dismiss()

    #获取弹窗文本!
    def get_alert_text(self):
        alert_text = self.get_alert_object().text
        return alert_text

    #定位下拉框,返回下拉框对象!
    def find_select_object(self,*locator):
        sele_object = Select(self.find_element(*locator))
        return sele_object

    #根据option文本值选择下拉框选项!
    def select_text_option(self,*locator,text):
        self.find_select_object(*locator).select_by_visible_text(text)


    #根据value属性值选择下拉框选项!
    def select_value_option(self,*locator,value):
        self.find_select_object(*locator).select_by_value(value)

    #根据索引值选择下拉框选项!
    def select_index_option(self,*locator,index):
        self.find_select_object(*locator).select_by_index(index)

    #显性等待(直到出现)!
    def overt_wait_until(self,*locator):
        WebDriverWait(self.driver,10,0.5).until(EC.presence_of_element_located(*locator))

    # 显性等待(直到不出现)!
    def overt_wait_untilnot(self,*locator):
        WebDriverWait(self.driver, 10, 0.5).until_not(EC.presence_of_element_located(*locator), message='显性等待超时')

    #刷新页面!
    def refresh(self):
        self.driver.refresh()



    # #页面向下滑动10000像素
    # def move_driver_until_down(self):
    #     self.driver.execute_script('window.scrollTo(0,10000)')

    # #页面滑到最上面
    # def move_driver_until_up(self):
    #     self.driver.execute_script('window.scrollTo(0,0)')

    # # 页面向上滑动1000像素
    # def drag_until_pix_up(self):
    #     self.driver.execute_script('document.querySelector("html").scrollTo(0,-1000)')



    #返回选择文集windows系统弹框对象
    def window_locate(self,name):  #name= "文件上传"
        try:
            window = uiautomation.WindowControl(Name=name)
            print('文件上传窗口定位成功')
        except Exception as e:
            print('文件上传窗口定位失败,抛出异常:%s' % e)
        else:
            return window

    #windows系统弹框输入文件
    def window_inout(self,name,AutomationId,file):  #AutomationId="1148"
        window = self.window_locate(name)
        try:
            window.EditControl(AutomationId).SendKeys(file)
            print('输入文件名成功，文件名为：%s' % file)
        except Exception as e:
            print('文件名输入失败,抛出异常：%s' % e)
            # self.get_window_img()


    #windows系统弹框点击打开
    def window_button(self,name):   # name="打开(O)"
        window = self.window_locate(name)
        try:
            window.ButtonControl(Name="打开(O)").Click()
            print('打开按钮点击成功')
        except Exception as e:
            print('打开按钮点击失败，抛出异常：%s' % e)
            # self.get_window_img()

    #执行js语句
    def execute_js(self,js):
        self.driver.execute_script(js)

    #执行js语句,返回js的结果
    def return_execute_js(self,js):
        result_js = "return " + js
        return self.execute_js(result_js)

    #frame指定(id,name)切换
    def frame_switch_id(self,id):
        self.driver.switch_to.frame(id)

    #frame指定(frame对象)切换
    def frame_switch_ele(self,*locator):
        ele = self.find_element(*locator)
        self.driver.switch_to.frame(ele)

    #frame切换到上层
    def frame_switch_parent(self):
        self.driver.switch_to.parent_frame()

    #frame切换到默认最外层
    def frame_switch_default(self):
        self.driver.switch_to.default_content()


    #切换窗口
    def switch_window(self):
        windows = self.driver.window_handles
        self.driver.switch_to.window(windows[-1])

    #切换回要操作的窗口
    def switch_current_window(self):
        windows = self.driver.window_handles
        self.driver.switch_to.window(windows[0])

    #切换句柄(浏览器对象的属性)不能用??????????
    def switch_to_window(self):
        for window in self.driver.window_handles:#所有句柄列表
            if window != self.driver.current_window_handle:#当前操作的句柄
                self.driver.switch_to.window(window)


    #若元素出现,返回对象元素的文本,不出现,返回失败
    def try_return_ele_textORfaile(self,*locator):
        try:
            result = self.get_ele_text(*locator)
        except NoSuchElementException:
            print("目标元素没有出现")
            return '失败'
        else:
            return result

    #若元素出现,返回成功,不出现,返回失败
    def try_return_ele_passORfaile(self,*locator):
        try:
            self.get_ele_text(*locator)
        except NoSuchElementException:
            print("目标元素没有出现")
            return '失败了'
        else:
            return '成功了'

    #关闭句柄
    def close_handle(self):
        self.driver.close()

    #关闭浏览器
    def quit_driver(self):
        self.driver.quit()






