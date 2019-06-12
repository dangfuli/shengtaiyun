# coding=utf-8
from lib.utils.getConfig import *
import os
elements = getElement(os.path.join(os.path.dirname(os.path.dirname(__file__)),'elements/jibenanjian.json'))
print(elements)
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
import time
def click_anjianguanli(driver):
    ## 点击进入案件办理
    try:
        driver.find_element_by_css_selector(elements['css_anjianguanli']).click()
        driver.find_element_by_css_selector(elements['css_anjianbanli']).click()
    except:
        print('点击进入案件办理出错')

def click_faqianjian(driver):
    ## 点击发起案件
    try:
        driver.find_element_by_css_selector(elements['css_faqianjian']).click()
    except:
        print('发起案件出错')

def choose_dangshiren(driver):
    ## 点击选择当事人名称
    try:
        driver.find_element_by_css_selector(elements['css_dangshiren']).click()
        ## 输入名称
        driver.find_element_by_id(elements['id_mingcheng']).send_keys('测试')
        ## 选择类型为个人
        Select(driver.find_element_by_id(elements['id_leixing'])).select_by_value('2')
        ## 点击查询按钮
        driver.find_element_by_id(elements['id_search']).click()
        time.sleep(2)
        driver.find_element_by_css_selector(elements['css_gerendata']).click()
        driver.find_element_by_id(elements["id_okbutton"]).click()
    except:
        print('查询添加当事人出错')
    try:
        ## 添加当事人信息
        time.sleep(2)
        driver.find_element_by_id(elements['id_idnum']).send_keys('1')
        driver.find_element_by_id(elements['id_address']).send_keys('1')
        driver.find_element_by_id(elements['id_phone']).send_keys('1')
    except:
        print('添加当事人信息出错')
    try:
        ## 填写单位信息
        # 选择案由
        driver.find_element_by_css_selector(elements['css_anyouButton']).click()
        time.sleep(1)
        driver.find_element_by_css_selector(elements['css_choose_anyou']).click()
        driver.find_element_by_css_selector(elements['css_anyou_ok_button']).click()
        # 选择案件发生日期
        # 去除时间控件readonly
        js_value = 'document.getElementById("illegalDate").value="2019-06-10"'
        driver.execute_script(js_value)
        print('123')
        driver.find_element_by_id(elements['id_anjian_date']).send_keys('{0}'.format(time.strftime('%Y-%m-%d',time.localtime())))

    except:
        print("填报单位信息出错")

    ## 点击保存
    driver.find_element_by_id(elements['id_save']).click()
