import os,time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium import webdriver
from time import sleep
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from lib.utils import Log

log = Log.Log()
#浏览器选择方法
class BasePage(object):
    def __init__(self, driver):

        "一个构造函数，param参数driver"

        self.driver = driver
    # def Browser(self, driver):
    #     self.driver = driver
    #
    # def get_browser(self):
    #     """
    #     通过if语句，来控制初始化不同浏览器的启动，默认是启动Chrome
    #     :return: driver
    #     """
    #     if self.driver == 'Firefox':
    #         driver = webdriver.Firefox()
    #     elif self.driver == 'Chrome':
    #         driver = webdriver.Chrome()
    #     elif self.driver == 'IE':
    #         driver = webdriver.Ie()
    #     else:
    #         driver = webdriver.Chrome()
    #     driver.maximize_window()
    #     driver.implicitly_wait(10)
    #     return driver
    @staticmethod
#Toast方法判断耗时3秒最大化，寻找页面存在元素 XPATH
    def Toast(self,driver,text,timeout=2,poll_frequency=0.1,waitTimes=3):
        try:
            toast_loc = ("xpath", ".//*[contains(text(),'%s')]" % text)
            for t in range(waitTimes-1):
                t1 = WebDriverWait(driver, timeout, poll_frequency).until(expected_conditions.presence_of_element_located(toast_loc))
                if t1.is_displayed():
                    return True
                else:
                    sleep(0.2)
        except:
            return False
    @staticmethod
#Toast方法判断耗时3秒最大化，寻找页面存在元素 ID
    def ToastId(self,driver,text,timeout=2,poll_frequency=0.1,waitTimes=3):
        try:
            toast_loc = ("id", "id" % text)
            for t in range(waitTimes-1):
                t1 = WebDriverWait(driver, timeout, poll_frequency).until(expected_conditions.presence_of_element_located(toast_loc))
                if t1.is_displayed():
                    return True
                else:
                    sleep(0.2)
        except:
            return False
    @staticmethod
#Toast方法判断耗时3秒最大化，寻找页面存在元素 classname
    def ToastClassname(self,driver,text,timeout=2,poll_frequency=0.1,waitTimes=3):
        try:
            toast_loc = ("class_name", "class_name" % text)
            for t in range(waitTimes-1):
                t1 = WebDriverWait(driver, timeout, poll_frequency).until(expected_conditions.presence_of_element_located(toast_loc))
                if t1.is_displayed():
                    return True
                else:
                    sleep(0.2)
        except:
            return False
    @staticmethod
#Toast方法判断耗时3秒最大化，寻找页面存在元素 name
    def ToastName(self,driver,text,timeout=2,poll_frequency=0.1,waitTimes=3):
        try:
            toast_loc = ("name", "name" % text)
            for t in range(waitTimes-1):
                t1 = WebDriverWait(driver, timeout, poll_frequency).until(expected_conditions.presence_of_element_located(toast_loc))
                if t1.is_displayed():
                    return True
                else:
                    sleep(0.2)
        except:
            return False
    @staticmethod
#Toast方法判断耗时3秒最大化，寻找页面存在元素 Css
    def ToastCss(self,driver,text,timeout=2,poll_frequency=0.1,waitTimes=3):
        try:
            toast_loc = ("css_selector", "css_selector" % text)
            for t in range(waitTimes-1):
                t1 = WebDriverWait(driver, timeout, poll_frequency).until(expected_conditions.presence_of_element_located(toast_loc))
                if t1.is_displayed():
                    return True
                else:
                    sleep(0.2)
        except:
            return False
    @staticmethod
    def Toastxpath(driver,text,timeout=2,poll_frequency=0.1,waitTimes=3):
        try:
            toast_loc = ("xpath", ".//*[contains(text(),'%s')]" % text)
            for t in range(waitTimes-1):
                t1 = WebDriverWait(driver, timeout, poll_frequency).until(expected_conditions.presence_of_element_located(toast_loc))
                if t1.is_displayed():
                    return True
                else:
                    sleep(0.2)
        except:
            return False
#判断try中内容是否存在，true或false
    @staticmethod#静态方法
    #css
    def isElementExistcss(driver, element):
        flag = True
        try:
            driver.find_element_by_css_selector(element)
            return flag
        except:
            flag = False
            return flag
    @staticmethod
    #id
    def isElementExistid(driver, element):
        flag = True
        try:
            driver.find_element_by_id(element)
            return flag
        except:
            flag = False
            return flag
    @staticmethod
    #name
    def isElementExistname(driver, element):
        flag = True
        try:
            driver.find_element_by_name(element)
            return flag
        except:
            flag = False
            return flag
    @staticmethod
    #class_name
    def isElementExistclassname(driver, element):
        flag = True
        try:
            driver.find_element_by_class_name(element)
            return flag
        except:
            flag = False
            return flag
    #link_text
    @staticmethod
    def isElementExistlinktext(driver, element):
        flag = True
        try:
            driver.find_element_by_link_text(element)
            return flag
        except:
            flag = False
            return flag
    #创建文件夹用于图片存储
    @staticmethod
    def Cjwenjian():
        directory_time = time.strftime("%Y-%m-%d", time.localtime(time.time()))
        try:
            File_Path = os.getcwd() + '\\' + directory_time + '\\'
            if not os.path.exists(File_Path):
                os.makedirs(File_Path)
                print("目录新建成功：%s" % File_Path)
            else:
                print("目录已存在！！！")
        except BaseException as msg:
            print("新建目录失败：%s" % msg)

    #截图函数
    #寻找页面id是否存在
    # def isECid(driver, element):
    #     flag = True
    #     try:
    #         EC.presence_of_element_located((By.ID, element))
    #         logger.info("本次页面元素ID已展示: %s" % flag)
    #         return flag
    #
    #     except:
    #         flag = False
    #         logbug.debug("本次页面元素ID未展示: %s" % flag)
    #         return flag
