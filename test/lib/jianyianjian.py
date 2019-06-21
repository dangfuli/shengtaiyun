# coding=utf-8
from lib.utils.getConfig import *
import os,random,time
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from lib.creat_case import *
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
        #随便选一个
        elements['css_weifaleixing_value'] = elements['css_weifaleixing_value'].replace('1', str(
            random.choice([i for i in range(8) if i != 0])))
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
        driver.find_element_by_id(elements['id_input_wenhao']).send_keys(random.randrange(100,10000))
    except:
        print('输入决定书文号错误')

    try:
        ## 输入立案号，选择处罚类型
        driver.find_element_by_id(elements['id_lianhao']).send_keys('111') #输立案号
        driver.find_element_by_css_selector(elements['css_choose_chufaleixing']).click() #点选择处罚种类
        time.sleep(1)
        elements['css_chufaleixing_value'] = elements['css_chufaleixing_value'].replace('1', str(
            random.choice(['3','4','5','6'])))
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
        elements['css_huanbaobu_choose_value'] = elements['css_huanbaobu_choose_value'].replace('1', str(
            random.choice([i for i in range(23) if i != 0])))
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
    try:
        ##生成案卷
        time.sleep(1)
        driver.find_element_by_css_selector(elements['css_shengcheng_button']).click()  # 点击一键生成案卷
        time.sleep(2)
        driver.find_element_by_class_name(elements['class_choose_shengcheng_button']).click()  # 点击是的，我要生成！
        time.sleep(2)
        driver.find_element_by_class_name(elements['class_success_button']).click()  # 点击成功后的确认
        time.sleep(2)
    except:
        print('点击生成案卷按钮错误')

    generate_anjuan(driver)
    try:
        ## 提交基本案件信息
        driver.find_element_by_css_selector(elements['css_tijiao_button']).click()  #点击提交按钮
        time.sleep(1)
        driver.find_element_by_class_name(elements['class_reconfirm_button']).click()  # 点击确认，不在修改
        time.sleep(1)
        driver.find_element_by_class_name(elements['class_reconfirm_button']).click()  #点击确认
        time.sleep(5)
    except:
        print('提交简易案件信息')
    try:
        ## 简易案件结案
        driver.execute_script('document.getElementById("{1}").value="{0}"'.format(time.strftime('%Y-%m-%d', time.localtime()),elements['id_zhixing_date']))     # 填写执行完毕日期
        time.sleep(1)
        driver.execute_script('document.getElementById("{1}").value="{0}"'.format(time.strftime('%Y-%m-%d', time.localtime()),elements['id_close_date']))       # 填写结案日期
        time.sleep(1)
        driver.find_element_by_id(elements['id_anjian_num']).send_keys(random.randrange(1000,100000))  # 填写案卷号
        time.sleep(1)
        driver.find_element_by_id(elements['id_remark']).send_keys('test')      # 填写备注
        time.sleep(1)
        driver.find_element_by_css_selector(elements['css_jiean_button']).click()   #点击保存结案
        time.sleep(1)
        driver.find_element_by_class_name(elements['class_jiean_save_suc']).click()  #点击保存成功ok按钮
        time.sleep(5)

    except:
        print('结案信息填写错误')
    try:
        ## 生成结案案卷
        driver.find_element_by_css_selector(elements['css_to_shengcheng_anjuan']).click()  # 点击一键生成案卷按钮
        time.sleep(2)
        driver.find_element_by_css_selector(elements['css_shengcheng_anjuan_button']).click()  #点击案卷生成
        time.sleep(1)
        driver.find_element_by_class_name(elements['class_continue_button']).click()  #点击是的，继续生成
        time.sleep(5)
        driver.find_element_by_class_name(elements['class_toyulan_button']).click()   #预览弹窗，点击是的
        time.sleep(1)
        driver.find_element_by_css_selector(elements['css_yulan_okbutton']).click()   #点击预览界面的确认生成
        time.sleep(1)
        driver.find_element_by_class_name(elements['class_fujian_okbutton']).click()   #确认附件ok按钮
        time.sleep(1)
        driver.find_element_by_css_selector(elements['css_back2_button']).click()    #点击返回按钮，返回倒上一级
        time.sleep(5)
        driver.find_element_by_css_selector(elements['css_jiean_tijiao_button']).click()  #结案提交按钮
        time.sleep(1)
        driver.find_element_by_class_name(elements['class_yes_confirm']).click()    #点击是的，我要提价
        time.sleep(1)
        driver.find_element_by_class_name(elements['class_chenggong_confirm']).click()   #点击成功提交按钮
    except:
        print('生成结案案卷错误')
    ## 结案
    jiean(driver)
