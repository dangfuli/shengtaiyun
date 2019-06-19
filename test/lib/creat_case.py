from lib.flow import *
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