from selenium import webdriver

class WebDriverDriven(object):
    '''我们在使用class创建类的时候, 只会创建一个类对象, 但是, 当我们实例化这个类对象的时候, 一个类对象,
    可以实例化出很多不同的对象, 而我们每次实例化出来一个对象, 就会在内存中重新分配一块空间,
    而单例模式, 就是为了解决上述问题, 使得由一个类对象所实例化出来的全部对象都指向同一块内存空间.'''

    driver = 'none' #定义一个类属性

    @classmethod #定义一个类方法 类方法只有类可以调用
    def get_driver(cls,type='Chrome'): #类方法
        if cls.driver == 'none': #判断类属性
            if type == 'Chrome':# 如果类型是Chrome
                cls.driver = webdriver.Chrome() #则打开谷歌浏览器
            else:
                cls.driver = webdriver.Firefox() #如果不是则打开火狐浏览器
            cls.driver.maximize_window() #最大化窗口
            cls.driver.implicitly_wait(10)#隐性等待
        return cls.driver #返回这个类属性



if __name__ == '__main__':
    a=SetUp.get_driver()
    b=SetUp.get_driver()
    print(a)
    print(b)
