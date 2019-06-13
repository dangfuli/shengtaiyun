# coding=utf-8
from lib.utils.getConfig import *
import os,random
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
import time

elements = getElement(os.path.join(os.path.dirname(os.path.dirname(__file__)),'elements/jibenanjian.json'))
def click_anjianguanli(driver):
    '''点击侧边栏案件管理'''
    ## 点击进入案件办理
    try:
        driver.find_element_by_css_selector(elements['css_anjianguanli']).click()
        driver.find_element_by_css_selector(elements['css_anjianbanli']).click()
    except:
        print('点击进入案件办理出错')

def click_faqianjian(driver):
    '''发起案件按钮点击'''
    ## 点击发起案件
    try:
        driver.find_element_by_css_selector(elements['css_faqianjian']).click()
    except:
        print('发起案件出错')

def to_base_info(driver):
    '''案件基本信息填写'''
    ## 点击选择当事人名称
    try:
        driver.find_element_by_css_selector(elements['css_dangshiren']).click()
        time.sleep(1)
        ## 输入名称
        driver.find_element_by_id(elements['id_mingcheng']).send_keys('测试')
        time.sleep(1)
        ## 选择类型为个人
        Select(driver.find_element_by_id(elements['id_leixing'])).select_by_value('2')
        ## 点击查询按钮
        driver.find_element_by_id(elements['id_search']).click()
        time.sleep(2)
        driver.find_element_by_css_selector(elements['css_gerendata']).click()
        time.sleep(1)
        driver.find_element_by_id(elements["id_okbutton"]).click()
        time.sleep(1)
    except:
        print('查询添加当事人出错')
    try:
        ## 添加当事人信息
        driver.find_element_by_id(elements['id_idnum']).send_keys('1')
        time.sleep(1)
        driver.find_element_by_id(elements['id_address']).send_keys('1')
        time.sleep(1)
        driver.find_element_by_id(elements['id_phone']).send_keys('1')
        time.sleep(1)
    except:
        print('添加当事人信息出错')
    try:
        ## 填写单位信息
        # 选择案由
        driver.find_element_by_css_selector(elements['css_anyouButton']).click()
        time.sleep(1)
        ## 随机取一个案由
        elements['css_choose_anyou'] = elements['css_choose_anyou'].replace('24',str(random.choice([i for i in range(25) if i!=0])))
        print(elements['css_choose_anyou'])
        driver.find_element_by_css_selector(elements['css_choose_anyou']).click()
        time.sleep(1)
        driver.find_element_by_css_selector(elements['css_anyou_ok_button']).click()
        time.sleep(1)
        # 选择案件发生日期
        # 添加时间
        js_value = 'document.getElementById("illegalDate").value="{0}"'.format(time.strftime('%Y-%m-%d',time.localtime()))
        driver.execute_script(js_value)
        time.sleep(2)
        js = "window.scrollTo(0,document.body.scrollHeight)"
        driver.execute_script(js)
    except:
        print("填报单位信息出错")
    try:
        # 点击保存
        driver.find_element_by_id(elements['id_save']).click()
        time.sleep(1)
        # 点击否，继续
        driver.find_element_by_class_name(elements['class_no_continue']).click()
        time.sleep(1)
        # 点击成功之后的确认
        driver.find_element_by_class_name(elements['class_faqianjian_ok_button']).click()
    except:
        print('进入下一步出错')

def to_jianyi_info(driver):
    '''简易案件'''
    # 滑到顶部
    driver.execute_script("window.scrollTo(0,0)")

    elements = getElement(os.path.join(os.path.dirname(os.path.dirname(__file__)), 'elements/jianyianjian.json'))
    try:
        ## 点击简易案件标题
        driver.find_element_by_css_selector(elements['css_jianyi_title']).click()
    except:
        print('进入简易案件失败')
    time.sleep(5)
    try:
        #点击关联的专项选择按钮
        driver.find_element_by_css_selector(elements['css_guanlian_button']).click()
        time.sleep(1)
        #点击第一个
        driver.find_element_by_css_selector(elements['css_guanlian_value']).click()
        time.sleep(1)
        #点击确定按钮
        driver.find_element_by_css_selector(elements['css_guanlian_okbutton']).click()
        time.sleep(1)
    except:
        print('选择关联专项出错')

    try:
        #点击违法类型选择按钮
        driver.find_element_by_css_selector(elements['css_weifaleixing_button']).click()
        time.sleep(2)
        #选择第一个内容
        driver.find_element_by_css_selector(elements['css_weifaleixing_value']).click()
        time.sleep(1)
        #点击确定按钮
        driver.find_element_by_css_selector(elements['css_weifaleixing_okbutton']).click()
        time.sleep(1)
    except:
        print('选择违法类型出错')

    try:
        ##选择决定书文号为已有
        Select(driver.find_element_by_id(elements['id_isJuedingshuwenhao'])).select_by_visible_text("已有文号")
        driver.find_element_by_id(elements['id_input_wenhao']).send_keys('222')
    except:
        print('输入决定书文号错误')

    try:
        ## 输入立案号，选择处罚类型
        driver.find_element_by_id(elements['id_lianhao']).send_keys('111') #输立案号
        driver.find_element_by_css_selector(elements['css_choose_chufaleixing']).click() #点选择处罚种类
        time.sleep(1)
        driver.find_element_by_css_selector(elements['css_chufaleixing_value']).click()  #选择处罚种类
        time.sleep(1)
        driver.find_element_by_css_selector(elements['css_chufa_okbutton']).click()  #点击处罚种类确定按钮
        time.sleep(1)
    except:
        print('输入立案号，选择处罚种类出错')
    try:
        ## 环保部对应违法行为
        driver.find_element_by_css_selector(elements['css_huanbaobu_choose_button']).click()  #点击环保部对应违法行为选择按钮
        time.sleep(1)
        driver.find_element_by_css_selector(elements['css_huanbaobu_choose_value']).click()  #选择违反建设项目“三同时”及验收制度
        time.sleep(1)
        driver.find_element_by_css_selector(elements['css_huanbaobu_choose_okbutton']).click()  #点击确定
        time.sleep(1)
    except:
        print('选择环保部对应违法行为出错')
    try:
        ## 处罚依据选择
        driver.find_element_by_css_selector(elements['css_choose_chufayiju_button']).click()  #点击选择处罚依据按钮
        time.sleep(1)
        driver.find_element_by_css_selector(elements['css_choose_chufayiju_value']).click()  #点击处罚依据弹窗的第一个内容
        time.sleep(1)
        driver.find_element_by_css_selector(elements['css_choose_chufayiju_okbutton']).click() #点击处罚依据的确定按钮
        time.sleep(1)
    except:
        print('选择处罚依据出错')
    try:
        ## 违法案件类型选择
        driver.find_element_by_css_selector(elements['css_choose_weifaanjianleixing_button']).click()  #点击违法案件类型选择按钮
        time.sleep(1)
        driver.find_element_by_css_selector(elements['css_choose_weifaanjianleixing_value']).click()  #选择第一个
        time.sleep(1)
        driver.find_element_by_css_selector(elements['css_choose_weifaanjianleixing_okbutton']).click() #点击确定
        time.sleep(1)
    except:
        print('选择违法案件类型错误')
    try:
        ##选择命令种类，选择是否听证
        Select(driver.find_element_by_id(elements['id_xzminglingzhonglei'])).select_by_visible_text('无')
        Select(driver.find_element_by_css_selector(elements['css_isTingzheng'])).select_by_visible_text('否')
        time.sleep(1)
    except:
        print('选择命令种类，选择是否听证出错')

    try:
        ## 添加主要执法人员
        driver.find_element_by_css_selector(elements['css_zhifarenyuan_button']).click()  #点击选择主要执法人员按钮
        time.sleep(1)
        driver.find_element_by_css_selector(elements['css_zhifarenyuan_value1']).click()  #点击选择一个执法人员
        driver.find_element_by_css_selector(elements['css_zhifarenyuan_value2']).click()  #点击选择第二个执法人员
        time.sleep(1)
        driver.find_element_by_id(elements['id_zhifarenyuan_okbutton']).click()  #点击确定按钮
        time.sleep(1)
        ## 添加执法日期
        driver.execute_script('document.getElementById("{1}").value="{0}"'.format(time.strftime('%Y-%m-%d', time.localtime()),elements['id_zhifarenyuan_date1']))
        time.sleep(1)
        driver.execute_script('document.getElementById("{1}").value="{0}"'.format(time.strftime('%Y-%m-%d', time.localtime()),elements['id_zhifarenyuan_date2']))
        time.sleep(1)

    except:
        print('添加执法人员错误')
    try:
        ##点击保存
        driver.find_element_by_css_selector(elements['css_save_button']).click() #点击保存按钮
        time.sleep(2)
        driver.find_element_by_class_name(elements['class_choose_yes']).click()  #选择是的进行保存
        time.sleep(2)
        driver.find_element_by_css_selector(elements['css_end_okbutton']).click()  #保存成功后确定
        time.sleep(2)
    except:
        print('保存失败')