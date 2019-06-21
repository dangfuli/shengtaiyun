from lib.utils.getConfig import *
from selenium.webdriver.support.select import Select
import time,random,os
elements = getElement(os.path.join(os.path.dirname(os.path.dirname(__file__)),'elements/jibenxinxi.json'))
def base_case(driver):
    '''案件基本信息填写'''
    ## 点击进入案件办理
    try:
        driver.find_element_by_css_selector(elements['css_anjianguanli']).click()   ##点击侧边栏案件
        time.sleep(2)
        driver.find_element_by_css_selector(elements['css_anjianbanli']).click()    ##点击进入案件管理
        time.sleep(1)
        driver.find_element_by_css_selector(elements['css_faqianjian']).click()    ## 点击发起案件
    except:
        print('点击进入案件办理出错')

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
        driver.find_element_by_css_selector(elements['css_choose_anyou']).click()
        time.sleep(1)
        driver.find_element_by_css_selector(elements['css_anyou_ok_button']).click()
        time.sleep(1)
        ## 案件名称随便加个东西
        driver.find_element_by_id(elements['id_case_name']).send_keys(random.randrange(0,100000))
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

def generate_anjuan(driver):
    elements = getElement(os.path.join(os.path.dirname(os.path.dirname(__file__)), 'elements/jianyianjian.json'))
    try:
        ## 点击添加文书
        time.sleep(1)
        driver.find_element_by_css_selector(elements['css_fujian']).click()  #添加附件
        time.sleep(2)
        driver.find_element_by_id(elements['id_put_pic']).send_keys(
            os.path.join(os.path.dirname(os.path.dirname(__file__)), 'configs/jianyianjian.png'))  ## 上传图片
        time.sleep(2)

        driver.find_element_by_css_selector(elements['css_choose_leixing']).click()
        driver.find_element_by_css_selector("[codealias='勘察笔录']").click()
        # Select(driver.find_element_by_css_selector(elements['css_choose_leixing'])).select_by_visible_text("勘查")  #选择类型
        time.sleep(2)
        driver.find_element_by_css_selector(elements['css_put_button']).click()  #上传图片之后点击上传按钮
        time.sleep(5)
        driver.find_element_by_css_selector(elements['css_put_succ_button']).click()  #点击上传成功按钮
        time.sleep(1)
        driver.find_element_by_css_selector(elements['css_put_ok_button']).click()   #点击确定按钮
        time.sleep(1)
        driver.find_element_by_css_selector(elements['css_put_save_ok_button']).click()  #确定之后保存成功按钮
        time.sleep(1)
    except:
        print('上传图片失败')
    try:
        driver.find_element_by_css_selector(elements['css_shengcheng_anjuan_button']).click()  #点击案卷生成
        time.sleep(2)
        driver.find_element_by_class_name(elements['class_save_continue']).click()  #点击继续保存
        time.sleep(2)
        driver.find_element_by_class_name(elements['class_ok_button']).click()  #点击确定按钮
        time.sleep(2)
        driver.find_element_by_css_selector(elements['css_shengchegn_anjuan_button']).click()  #点击生成案卷按钮
        time.sleep(2)
        driver.find_element_by_class_name(elements['class_shengcheng_suc_okbutton']).click()   #点击生成成功之后的ok按钮
        time.sleep(1)
        driver.find_element_by_css_selector(elements['css_back_button']).click()  # 点击返回，返回到上一级
        time.sleep(2)

    except:
        print('保存案卷失败')
def jiean(driver):
    elements = getElement(os.path.join(os.path.dirname(os.path.dirname(__file__)), 'elements/jianyianjian.json'))
    try:
        ## 办结
        driver.execute_script("var q=document.documentElement.scrollTop=0")
        time.sleep(2)
        driver.find_element_by_css_selector(elements['css_banjie_button']).click()  #点击办结按钮
        time.sleep(1)
        driver.find_element_by_css_selector(elements['css_banjie_confirm_button']).click()  #提交确认办结
        time.sleep(1)
        driver.find_element_by_class_name(elements['class_banjie_end_button']).click()  #点击确认
    except:
        print('办结出错')