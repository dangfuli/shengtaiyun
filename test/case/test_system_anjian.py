# coding=utf-8
from selenium import webdriver
import unittest,os
from lib.flow import *
login_data = getElement(os.path.join(os.path.dirname(os.path.dirname(__file__)),'configs/login.json'))
url = login_data['uri'] + 'auth/goLogin'

def main():
    driver = webdriver.Chrome()
    ## 登录
    cookieLogin(driver)
    ## 先临时手动登录
    #__login(driver)
    time.sleep(10)
    ## 发起案件
    # base_case(driver)
    # time.sleep(10)
    ############## 简易案件
    #to_jianyi_info(driver)
    # time.sleep(10)
    ############## 一般案件
    base_case(driver)
    time.sleep(10)
    to_yiban_info(driver)

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
    driver.implicitly_wait(10)
    driver.add_cookie(login_data['cookie'])
    driver.add_cookie(login_data['cookie2'])
    time.sleep(2)
    driver.get(login_data['uri']+'/auth/goHome')

def _temp_debug():
    driver = webdriver.Chrome()
    ## 添加cookie暂时有点问题
    ##driver = Driver()
    ## 先临时手动登录
    cookieLogin(driver)
    time.sleep(10)
    click_anjianguanli(driver)
    driver.find_element_by_css_selector('#caseDataTable > tbody > tr:nth-child(1) > td:nth-child(4) > a > i').click()
    time.sleep(3)
    to_yiban_info(driver)


#_temp_debug()
main()

