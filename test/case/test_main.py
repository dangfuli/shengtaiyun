# coding=utf-8
from selenium import webdriver
from lib.skip_login import *
import unittest,os
from lib.utils import getConfig
from lib.feed import *

uri = getConfig.getElement(os.path.join(os.path.dirname(os.path.dirname(__file__)),'configs/login.json'))['uri']
url = uri + 'auth/goLogin'

def main():
    driver = webdriver.Chrome()
    ## 添加cookie暂时有点问题
    ##driver = Driver()
    ## 先临时手动登录
    __login(driver)
    time.sleep(10)
    ## 点击侧边案件管理
    click_anjianguanli(driver)
    ## 点击发起案件
    click_faqianjian(driver)
    ## 填写基本信息
    choose_dangshiren(driver)
    time.sleep(10)

def __login(driver):
    ## 登录
    driver.get(url)
    driver.implicitly_wait(20)
    driver.find_element_by_id('username').send_keys('admin')
    driver.find_element_by_id('password').send_keys('chan12369')
    time.sleep(10)
    driver.find_element_by_id('loginbutton').click()

main()