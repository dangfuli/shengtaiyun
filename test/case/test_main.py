# coding=utf-8
from selenium import webdriver
import unittest,os
from lib.utils import getConfig
from lib.anjian import *
login_data = getConfig.getElement(os.path.join(os.path.dirname(os.path.dirname(__file__)),'configs/login.json'))

url = login_data['uri'] + 'auth/goLogin'

def main():
    driver = webdriver.Chrome()
    ## 添加cookie暂时有点问题
    cookieLogin(driver)
    ## 先临时手动登录
    #__login(driver)
    time.sleep(10)
    print(driver.get_cookies())
    ## 点击侧边案件管理
    click_anjianguanli(driver)
    ## 点击发起案件
    click_faqianjian(driver)
    ## 填写基本信息
    to_base_info(driver)
    time.sleep(10)
    ############## 简易案件
    to_jianyi_info(driver)
    driver.quit()

def __login(driver):
    ## 登录
    driver.get(url)
    driver.implicitly_wait(20)
    driver.find_element_by_id('username').send_keys('admin')
    driver.find_element_by_id('password').send_keys('chan12369')
    print(driver.get_cookies())
    time.sleep(10)
    driver.find_element_by_id('loginbutton').click()

def cookieLogin(driver):
    driver.get(url)
    driver.implicitly_wait(20)
    driver.add_cookie(login_data['cookie'])
    driver.add_cookie(login_data['cookie2'])
    time.sleep(2)
    driver.get(login_data['uri']+'/auth/goHome')

# jianyianjian()
# yibanxingzheng()
def _temp_debug():
    driver = webdriver.Chrome()
    ## 添加cookie暂时有点问题
    ##driver = Driver()
    ## 先临时手动登录
    __login(driver)
    time.sleep(10)
    click_anjianguanli(driver)
    driver.find_element_by_css_selector('#caseDataTable > tbody > tr:nth-child(1) > td:nth-child(4) > a > i').click()
    time.sleep(3)
    to_jianyi_info(driver)

# _temp_debug()

main()
