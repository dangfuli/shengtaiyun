# coding=utf-8
from lib.creat_case import *
elements = getElement(os.path.join(os.path.dirname(os.path.dirname(__file__)),'elements/yibananjian.json'))

def to_yiban_info(driver):
    ## 一般案件
    try:
        driver.execute_script("window.scrollTo(0,0)")   #滑到顶部
        driver.find_element_by_css_selector(elements['css_yiban_title']).click()  # 点击一般案件标题
        time.sleep(5)
    except:
        print('点击一般案件标题错误')
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
        ## 填写基本信息
        driver.execute_script('document.getElementById("{1}").value="{0}"'.format(time.strftime('%Y-%m-%d', time.localtime()),elements['id_do_time']))          #添加立案时间
        time.sleep(1)
        driver.find_element_by_id(elements['id_lian_num']).send_keys(random.randrange(2000,200000))     #输入立案号码
        time.sleep(1)
        driver.find_element_by_css_selector(elements['css_info_save_button']).click()   #点击保存按钮
        time.sleep(2)
        driver.find_element_by_class_name(elements['class_save_succ_button']).click()   #点击保存成功按钮
        time.sleep(1)
    except:
        print('填写立案基本信息错误')
    try:
        driver.find_element_by_css_selector(elements['css_chufa_button']).click()   #点击处罚决定按钮
        time.sleep(5)
    except:
        print('点击处罚决定错误')
    try:
        ##环保部违法行为
        driver.execute_script('document.getElementById("{1}").value="{0}"'.format(time.strftime('%Y-%m-%d', time.localtime()),elements['id_chufa_do_date']))    #处罚决定开始办理时间
        time.sleep(1)
        driver.find_element_by_css_selector(elements['css_hbbwfxw_action']).click()     #点击环保部违法行为选择按钮
        time.sleep(1)
        elements['css_hbbwfxw_value'] = elements['css_hbbwfxw_value'].replace('1', str(
            random.choice([i for i in range(23) if i != 0])))
        driver.find_element_by_css_selector(elements['css_hbbwfxw_value']).click()      #选择一个环保部违法行为的值
        time.sleep(1)
        driver.find_element_by_css_selector(elements['css_hbbwfxw_okbutton']).click()   #点击确定
        time.sleep(1)
    except:
        print('选择环保部违法行为错误')
    try:
        ##选择处罚依据
        driver.find_element_by_css_selector(elements['css_cfyj_choose_button']).click() #点击选择处罚依据
        time.sleep(2)
        driver.find_element_by_css_selector(elements['css_cfyj_value']).click() #选择第一个依据
        time.sleep(1)
        driver.find_element_by_css_selector(elements['css_cfyj_okbutton']).click()  #点击确定按钮
        time.sleep(1)
    except:
        print("选择处罚依据错误")
    try:
        #选择违法案件类型
        driver.find_element_by_css_selector(elements['css_wfajlx_button']).click()      #点击选择违法案件类型
        time.sleep(1)
        driver.find_element_by_css_selector(elements['css_wfajlx_value']).click()       #点击违法案件类型第一个数据
        time.sleep(1)
        driver.find_element_by_css_selector(elements['css_wfajlx_okbutton']).click()    #点击违法案件类型确定按钮
        time.sleep(1)
    except:
        print('选择违法案件类型错误')
    try:
        ##选择处罚种类
        driver.find_element_by_css_selector(elements['css_cfzl_button']).click()        #点击选择处罚种类按钮
        time.sleep(1)
        elements['css_cfzl_value'] = elements['css_cfzl_value'].replace('1', str(
            random.choice(['3','4','5','6'])))
        driver.find_element_by_css_selector(elements['css_cfzl_value']).click()         #点击处罚种类值
        time.sleep(1)
        driver.find_element_by_css_selector(elements['css_cfzl_okbutton']).click()      #点击处罚种类确定按钮
        time.sleep(1)
        Select(driver.find_element_by_id(elements['id_is_have_juedingshu'])).select_by_visible_text('已有文号') #选择决定书为已有文号
        time.sleep(1)
        driver.find_element_by_id(elements['id_juedingshu_num']).send_keys(random.randrange(100,20000))
    except:
        print('填写处罚决定书错误')
    try:
        ##is听证，is建设项目
        Select(driver.find_element_by_id(elements['id_is_hearing'])).select_by_visible_text('否')    #是否听证选择否
        time.sleep(1)
        Select(driver.find_element_by_id(elements['id_is_project'])).select_by_visible_text('否')    #是否建设项目，选择否
        time.sleep(1)
    except:
        print('选择是否听证，是否建设性项目错误')
    try:
        ##添加执法人员
        driver.find_element_by_css_selector(elements['css_zhifa_man_button']).click()      #点击编辑执法人员按钮
        time.sleep(1)
        driver.find_element_by_css_selector(elements['css_zhifa_man_value1']).click()   #点击第一个执法人员
        driver.find_element_by_css_selector(elements['css_zhifa_man_value2']).click()   #点击第二个执法人员
        time.sleep(1)
        driver.find_element_by_id(elements['id_zhifa_okbutton']).click()     #点击确定
        time.sleep(1)
        driver.execute_script('document.getElementById("{1}").value="{0}"'.format(time.strftime('%Y-%m-%d', time.localtime()),elements['id_zhifa_man_date1']))  #第一个执法人员的日期
        driver.execute_script('document.getElementById("{1}").value="{0}"'.format(time.strftime('%Y-%m-%d', time.localtime()),elements['id_zhifa_man_date2']))  # 第二个执法人员的日期
        time.sleep(2)
    except:
        print('添加执法人员错误')
    try:
        ##保存一般案件
        driver.find_element_by_css_selector(elements['css_save_button']).click()        #点击保存
        time.sleep(1)
        driver.find_element_by_class_name(elements['class_save_conti_button']).click()  #点击继续，不修改
        time.sleep(1)
        driver.find_element_by_class_name(elements['class_save_end_button']).click()    #点击确定，ok结束
        time.sleep(5)
    except:
        print('保存一般案件处罚规定失败')
    try:
        ## 点击进入生成案卷
        driver.find_element_by_css_selector(elements['css_get_anjuan_button']).click()  #点击一键生成案卷按钮
        time.sleep(1)
        driver.find_element_by_class_name(elements['class_yes_do_button']).click()      #是的，继续
        time.sleep(2)
        driver.find_element_by_class_name(elements['class_yes_do_button']).click()      #确定按钮
        time.sleep(1)
    except:
        print('点击进入生成案卷错误')

    ## 一键生成案卷
    generate_anjuan(driver)

    try:
        #提交一般案件信息
        driver.find_element_by_css_selector(elements['css_yiban_tj_button']).click()    #点击提交
        time.sleep(1)
        driver.find_element_by_class_name(elements['class_yiban_tijiao_button']).click()  #点击是的，我要提交
        time.sleep(1)
        driver.find_element_by_class_name(elements['class_yiban_tijiao_button']).click()    #提交完成后点击确定
        time.sleep(5)
    except:
        print('点击提交一般案件按钮错误')
    try:
        driver.execute_script("var q=document.documentElement.scrollTop=400")
        ##结案，执行情况
        driver.find_element_by_css_selector(elements['css_tree_jiean_button']).click()     #点击树图中结案按钮
        time.sleep(5)
        driver.execute_script('document.getElementById("{1}").value="{0}"'.format(time.strftime('%Y-%m-%d', time.localtime()),elements['id_start_jiean_date']))     #输入执行情况的执行时间
        time.sleep(1)
        driver.execute_script('document.getElementById("{1}").value="{0}"'.format(time.strftime('%Y-%m-%d', time.localtime()),elements['id_end_jiean_date']))       #输入执行情况结束时间
        time.sleep(1)
    except:
        print('输入执行情况错误')
    try:
        ##结案信息
        Select(driver.find_element_by_id(elements['id_fuyi'])).select_by_visible_text('否')      ##选择复议情况为否
        time.sleep(1)
        Select(driver.find_element_by_id(elements['id_susong'])).select_by_visible_text('否')    ##选择诉讼情况为否
        time.sleep(1)
        driver.find_element_by_css_selector(elements['css_ysqk_button']).click()    #点击移送情况按钮
        time.sleep(1)
        driver.find_element_by_css_selector(elements['css_ysqk_value']).click()     #选择移送按钮
        time.sleep(1)
        driver.find_element_by_css_selector(elements['css_ysqk_okbutton']).click()  #点击确定按钮
        time.sleep(1)
        Select(driver.find_element_by_css_selector(elements['css_isbank'])).select_by_visible_text('否') #选择是否纳入银行征信系统为否
        time.sleep(1)
        driver.execute_script('document.getElementById("{1}").value="{0}"'.format(time.strftime('%Y-%m-%d', time.localtime()),elements['id_close_date']))   #填写结案日期
        time.sleep(1)
        driver.find_element_by_id(elements['id_anjuan_num']).send_keys(random.randrange(10000,1000000000))
        time.sleep(1)
        Select(driver.find_element_by_id(elements['id_isopen'])).select_by_visible_text('否')    #选择是否公开为否
        time.sleep(1)
        driver.find_element_by_id(elements['id_remark']).send_keys('test')      #输入备注
        time.sleep(1)
        driver.find_element_by_css_selector(elements['css_yiban_save_button']).click()      #点击保存按钮
        time.sleep(1)
        driver.find_element_by_class_name(elements['class_save_okbutton']).click()      #点击保存之后点击确定
        time.sleep(1)
    except:
        print('填写结案信息不正确')
    try:
        ##点击一键生成案卷
        driver.find_element_by_css_selector(elements['css_shengcheng_case']).click()    #点击一键生成案卷
        time.sleep(5)

        driver.find_element_by_css_selector("css_scaj_button").click()
        time.sleep(1)
        driver.find_element_by_class_name("class_okbutton").click()
        time.sleep(5)
        driver.find_element_by_class_name("class_okbutton").click()
        time.sleep(2)
        driver.find_element_by_css_selector("css_confirm_sc_button").click()
        time.sleep(2)
        driver.find_element_by_class_name('class_okbutton').click()
        time.sleep(1)

        driver.find_element_by_css_selector(elements['css_back_case']).click()      #点击返回按钮
        time.sleep(5)
        driver.find_element_by_css_selector(elements['css_tijiao_button']).click()  #点击提交按钮
        time.sleep(1)
        driver.find_element_by_class_name(elements['class_tijiao_button']).click()  #点击继续提交
        time.sleep(1)
        driver.find_element_by_class_name(elements['class_tijiao_button']).click()  #点击确定
        time.sleep(1)
    except:
        print('一键生成案卷出错')
    jiean(driver)